# foxplug launch v2 — "Patch bay": one matte-black synth panel, patch cables that draw on, metal jacks with lamps,
# brand marks on white chips, Barlow Condensed + Barlow + JetBrains Mono. Copy frame: PAS.
# Metaphor: foxplug is a patch cable. The agent plugs straight into GitHub, Notion, Slack; no box in the middle.
# Every claim: ~/Documents/Personal/foxplug/README.md (foxplug-agent 0.1.0). No footage, no screenshots.
# Storyboard: fox-media/foxplug/STORYBOARD.md. v1 (no music, black first frame) lives at /tmp/foxmate-work/video.
import re
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "_groupd"))
from common import Comp, Safe, build, icon, draw, orb, cursor  # noqa: E402

HERE = Path(__file__).parent
ROOT = HERE / "project"
safe = Safe(HERE / "SAFE.json")
GROUND, CREAM, DIM, ORANGE, GOLD, GREEN, RED, STEEL, BOX = "#16171b", "#f2ead8", "#9a958a", "#ff7a1a", "#ffc23d", "#3ddc84", "#ff5a4f", "#3a3d45", "#2a2c33"
BEAT, PH = 0.5357, 0.032                     # 112 BPM bed, grid fitted with `hyperframes beats` + grid.py
B = lambda n: round(PH + BEAT * n, 3)
D = 27.0
ORB_G = f"radial-gradient(circle at 34% 30%, #ffffff 0%, #ffe0c2 14%, {ORANGE} 48%, #b8360f 92%)"
ORB_GLOW = f"0 0 60px rgba(255,122,26,0.45), inset -14px -18px 30px rgba(60,10,0,0.35), inset 12px 14px 26px rgba(255,255,255,0.45)"

# Brand marks: Simple Icons (CC0), unmodified paths, in each brand's own colour, on a white chip. They only name the
# service foxplug works with. Slack's entry is no longer in the Simple Icons data file; its colour is Slack aubergine.
HEX = {"github": "181717", "notion": "000000", "slack": "4A154B", "linear": "5E6AD2", "todoist": "E44332",
       "airtable": "18BFFF", "stripe": "635BFF", "asana": "F06A6A"}
PATHS = {k: re.findall(r'<path d="([^"]+)"', (HERE / "logos" / f"{k}.svg").read_text())[0] for k in HEX}

base_css = f"""
.t {{ position: absolute; font-family: "Barlow Condensed", sans-serif; font-weight: 700; color: {CREAM}; line-height: 1.0; white-space: nowrap; }}
.lab {{ position: absolute; font-family: "Barlow", sans-serif; font-weight: 600; color: {CREAM}; white-space: nowrap; letter-spacing: 0.01em; }}
.or {{ color: {ORANGE}; }}
.mono {{ font-family: "JetBrains Mono", monospace; font-weight: 500; }}
.chip {{ position: absolute; background: #ffffff; border-radius: 22%; box-shadow: 0 10px 26px rgba(0,0,0,0.45); display: flex; align-items: center; justify-content: center; }}
.jack {{ position: absolute; border-radius: 50%; background: radial-gradient(circle at 35% 30%, #f4f4f4 0%, #b9bcc2 38%, #6c7078 72%, #3c3f46 100%);
  box-shadow: 0 6px 14px rgba(0,0,0,0.6); }}
.jack i {{ position: absolute; inset: 26%; border-radius: 50%; background: #050506; box-shadow: inset 0 3px 6px rgba(0,0,0,0.9); }}
.lamp {{ position: absolute; border-radius: 50%; background: #3b2a24; box-shadow: inset 0 2px 3px rgba(0,0,0,0.6); }}
.cab {{ fill: none; stroke-linecap: round; stroke-dasharray: 1; }}
.sig {{ fill: none; stroke: #fff6e6; stroke-linecap: round; stroke-width: 6; stroke-dasharray: 0.015 0.085; opacity: 0.85; }}
.ic {{ fill: none; stroke: {CREAM}; stroke-width: 6; stroke-linecap: round; stroke-linejoin: round; stroke-dasharray: 1; }}
.ic.g {{ stroke: {GOLD}; }}
.ic.r {{ stroke: {RED}; stroke-width: 9; }}
.ic.gr {{ stroke: {GREEN}; stroke-width: 9; }}
.knob {{ position: absolute; border-radius: 50%; background: radial-gradient(circle at 38% 32%, #4a4d55 0%, #26282e 70%, #18191d 100%);
  border: 4px solid #55585f; box-shadow: 0 12px 24px rgba(0,0,0,0.55); }}
.knob b {{ position: absolute; left: calc(50% - 5px); top: 10%; width: 10px; height: 34%; border-radius: 5px; background: {CREAM}; }}
"""
fonts = [("Barlow Condensed", "barlowcondensed-600.woff2", 600, "normal"), ("Barlow Condensed", "barlowcondensed-700.woff2", 700, "normal"),
         ("Barlow", "barlow-600.woff2", 600, "normal"), ("JetBrains Mono", "jetbrains-mono-normal-500.woff2", 500, "normal")]
comps, sched = {}, []


def shot(cid, t0, t1):
    c = Comp(cid, round(t1 - t0, 3))
    comps[cid] = c
    sched.append((cid, t0))
    return c


def chip(c, eid, brand, x, y, s):
    c.add(f'<div class="chip" id="{c.id(eid)}" style="left:{x}px;top:{y}px;width:{s}px;height:{s}px">'
          f'<svg viewBox="0 0 24 24" width="{int(s * 0.6)}" height="{int(s * 0.6)}"><path d="{PATHS[brand]}" fill="#{HEX[brand]}"/></svg></div>')


def jack(c, eid, cx, cy, r=44, lamp=True):
    c.add(f'<div class="jack" id="{c.id(eid)}" style="left:{cx - r}px;top:{cy - r}px;width:{2 * r}px;height:{2 * r}px"><i></i></div>')
    if lamp:
        c.add(f'<div class="lamp" id="{c.id(eid)}-l" style="left:{cx - 13}px;top:{cy - r - 40}px;width:26px;height:26px"></div>')


def lamp_on(c, eid, t, color=GREEN):
    c.js.append(f'tl.to("#{c.id(eid)}-l", {{ backgroundColor: "{color}", boxShadow: "0 0 22px {color}", duration: 0.08 }}, {t:.2f});')


def curve(x1, y1, x2, y2, sag=120):
    dx = (x2 - x1) * 0.35
    return f"M{x1} {y1} C{x1 + dx:.0f} {y1 + sag} {x2 - dx:.0f} {y2 + sag} {x2} {y2}"


def svg(inner):
    return f'<svg viewBox="0 0 1920 1080" width="1920" height="1080" data-layout-ignore style="position:absolute;left:0;top:0;overflow:visible">{inner}</svg>'


def cable(c, eid, d, color, w=16, t=None, dur=0.5, signal=None):
    """A patch cable. t=None: already drawn (poster). signal=(t0, loops): light dots run along it."""
    e = c.id(eid)
    inner = f'<path id="{e}" class="cab" pathLength="1" d="{d}" style="stroke:{color};stroke-width:{w}px;filter:drop-shadow(0 8px 8px rgba(0,0,0,0.5))"/>'
    if signal:
        inner += f'<path id="{e}-s" class="sig" pathLength="1" d="{d}"/>'
    c.add(svg(inner))
    if t is not None:
        c.js.append(f'tl.fromTo("#{e}", {{ strokeDashoffset: 1 }}, {{ strokeDashoffset: 0, duration: {dur}, ease: "power2.inOut" }}, {t:.2f});')
        if signal:
            c.js.append(f'tl.set("#{e}-s", {{ opacity: 0 }}, 0); tl.set("#{e}-s", {{ opacity: 0.85 }}, {t + dur:.2f});')
    if signal:
        t0, loops = signal
        c.js.append(f'tl.fromTo("#{e}-s", {{ strokeDashoffset: 0 }}, {{ strokeDashoffset: -0.2, duration: 0.6, ease: "none", repeat: {loops} }}, {t0:.2f});')


def label(c, eid, text, y, t, size=68, how="rise", x=None):
    e = c.id(eid)
    pos = f"left:{x}px" if x is not None else "left:0;width:1920px;text-align:center"
    c.add(f'<div class="lab" id="{e}" style="{pos};top:{y}px;font-size:{size}px">{text}</div>')
    if how == "rise":
        c.js.append(f'tl.fromTo("#{e}", {{ opacity: 0, y: 30 }}, {{ opacity: 1, y: 0, duration: 0.4, ease: "power3.out" }}, {t:.2f});')
    elif how == "wipe":
        c.js.append(f'tl.fromTo("#{e}", {{ clipPath: "inset(0 100% 0 0)" }}, {{ clipPath: "inset(0 0% 0 0)", duration: 0.45, ease: "power3.out" }}, {t:.2f});')
    elif how == "stamp":
        c.js.append(f'tl.fromTo("#{e}", {{ opacity: 0, scale: 1.5 }}, {{ opacity: 1, scale: 1, duration: 0.25, ease: "back.out(2)" }}, {t:.2f});')
    elif how == "type":
        c.js.append(f'tl.fromTo("#{e}", {{ clipPath: "inset(0 100% 0 0)" }}, {{ clipPath: "inset(0 0% 0 0)", duration: 0.6, ease: "steps(18)" }}, {t:.2f});')


# ---------- S1 HOOK + POSTER (finished at frame 0): the orb, three live cables into GitHub, Notion, Slack.
c = shot("s1", 0, B(7))
c.add('<div class="t" style="left:140px;top:110px;font-size:120px">Plug your local AI</div>')
c.add('<div class="t or" style="left:140px;top:240px;font-size:120px">into your apps.</div>')
orb(c, "orb", 250, 560, 240, ORB_G, ORB_GLOW, spark=CREAM)
jy = [520, 700, 880]
for i, (b, col) in enumerate(zip(["github", "notion", "slack"], [ORANGE, GOLD, "#34d1bf"])):
    cable(c, f"c{i}", curve(470, 680, 1426, jy[i], 90 - i * 30), col, signal=(0.2 + i * 0.1, 5))
    jack(c, f"j{i}", 1470, jy[i], 44, lamp=False)
    chip(c, f"k{i}", b, 1560, jy[i] - 62, 124)
    c.add(f'<div class="lamp" style="left:1712px;top:{jy[i] - 13}px;width:26px;height:26px;background:{GREEN};box-shadow:0 0 22px {GREEN}"></div>')
c.js.append('tl.fromTo("#s1-orb", { scale: 1 }, { scale: 1.05, duration: 0.53, ease: "sine.inOut", yoyo: true, repeat: 5 }, 0.3);')

# ---------- S2 PROBLEM: the usual way puts a server box in the middle, and the key goes into it.
c = shot("s2", B(7), B(11))
orb(c, "orb", 240, 420, 220, ORB_G, ORB_GLOW, spark=CREAM)
c.add(f'<div id="s2-box" style="position:absolute;left:820px;top:390px;width:280px;height:280px;border-radius:20px;background:{STEEL};box-shadow:0 18px 40px rgba(0,0,0,0.55)">'
      + "".join(f'<div style="position:absolute;left:36px;top:{40 + k * 52}px;width:208px;height:30px;border-radius:8px;background:#23252b"></div>' for k in range(3))
      + f'<div class="lab" style="left:0;top:208px;width:280px;text-align:center;font-size:44px;color:{DIM}">server</div></div>')
cable(c, "a", curve(450, 530, 820, 530, 70), ORANGE, t=0.0, dur=0.35)
cable(c, "b", curve(1100, 530, 1486, 530, 70), ORANGE, t=0.3, dur=0.35)
jack(c, "j", 1530, 530, 44)
chip(c, "k", "slack", 1620, 470, 124)
c.add(icon(c.id("key"), "key", 0, 0, 120, "ic g"))
c.js += ['tl.fromTo("#s2-key", { x: 420, y: 330, opacity: 0 }, { x: 420, y: 330, opacity: 1, duration: 0.15 }, 0.55);',
         'tl.to("#s2-key", { x: 880, y: 420, duration: 0.55, ease: "power2.in" }, 0.75);',
         'tl.to("#s2-key", { scale: 0.3, opacity: 0, duration: 0.12 }, 1.3);',
         'tl.fromTo("#s2-box", { scale: 1 }, { scale: 1.06, duration: 0.1, yoyo: true, repeat: 1 }, 1.3);']
label(c, "l", "a server in between", 820, 0.25, how="wipe")

# ---------- S3 SOLVE: the box drops off the panel; the cable snaps straight from the orb to the jack.
c = shot("s3", B(11), B(15))
orb(c, "orb", 240, 420, 220, ORB_G, ORB_GLOW, spark=CREAM)
c.add(f'<div id="s3-box" style="position:absolute;left:820px;top:390px;width:280px;height:280px;border-radius:20px;background:{STEEL}">'
      + "".join(f'<div style="position:absolute;left:36px;top:{40 + k * 52}px;width:208px;height:30px;border-radius:8px;background:#23252b"></div>' for k in range(3))
      + f'<div class="lab" style="left:0;top:208px;width:280px;text-align:center;font-size:44px;color:{DIM}">server</div></div>')
c.add(svg(f'<path id="s3-old" d="{curve(450, 530, 820, 530, 70)} M1100 530 C1235 600 1351 600 1486 530" style="fill:none;stroke:{ORANGE};stroke-width:16px;stroke-linecap:round"/>'))
c.js += ['tl.to("#s3-old", { opacity: 0, duration: 0.12 }, 0.25);',
         'tl.to("#s3-box", { y: 760, rotation: 14, duration: 0.55, ease: "power2.in" }, 0.25);']
cable(c, "new", curve(450, 530, 1486, 530, 110), ORANGE, t=0.55, dur=0.35, signal=(0.9, 1))
jack(c, "j", 1530, 530, 44)
chip(c, "k", "slack", 1620, 470, 124)
lamp_on(c, "j", 0.9)
label(c, "l", "no server", 800, 0.95, size=110, how="stamp")
c.css.append("#s3-l { color: " + ORANGE + "; font-family: 'Barlow Condensed', sans-serif; font-weight: 700; }")

# ---------- S4 REVEAL: the name and the promise.
c = shot("s4", B(15), B(22))
c.add(f'<div class="t or" id="s4-n" style="left:140px;top:260px;font-size:300px">foxplug</div>',
      js='tl.fromTo("#s4-n", { scale: 1.3, opacity: 0, filter: "blur(18px)" }, { scale: 1, opacity: 1, filter: "blur(0px)", duration: 0.5, ease: "expo.out", transformOrigin: "0% 50%" }, 0.0);')
c.add('<div class="t" id="s4-l" style="left:146px;top:620px;font-size:96px;font-weight:600">Your keys never leave the browser.</div>',
      js='tl.fromTo("#s4-l", { opacity: 0, x: -60 }, { opacity: 1, x: 0, duration: 0.5, ease: "power3.out" }, 0.45);')
cable(c, "u", "M140 860 C700 900 1200 820 1780 860", ORANGE, w=12, t=0.6, dur=0.7)

# ---------- S5 PINNED KEY: the gold key cable fits the Slack jack, and bounces off another host's jack.
c = shot("s5", B(22), B(27))
jack(c, "a", 1000, 520, 50)
chip(c, "ka", "slack", 938, 640, 124)
jack(c, "b", 1500, 520, 50)
c.add(f'<div class="chip" style="left:1438px;top:640px;width:124px;height:124px;background:{STEEL}"><div class="t" style="position:static;font-size:84px;color:{DIM}">?</div></div>')
P0, P1, P2, P3 = (560, 700), (950, 520), (1340, 520), (1450, 520)
cpath = lambda p: curve(160, 520, p[0], p[1], 160)
c.add(svg(f'<path id="s5-cab" class="cab" pathLength="1" d="{cpath(P0)}" style="stroke:{GOLD};stroke-width:16px;stroke-dasharray:none;filter:drop-shadow(0 8px 8px rgba(0,0,0,0.5))"/>'))
c.add(f'<div id="s5-plug" style="position:absolute;left:0;top:0;width:110px;height:56px;margin:-28px 0 0 -100px;border-radius:14px;background:{GOLD};box-shadow:0 8px 16px rgba(0,0,0,0.5)">'
      f'<div class="mono" style="position:absolute;left:-20px;top:66px;font-size:48px;color:{GOLD};white-space:nowrap">slack.com</div></div>')
mv = lambda p, t, d, ease="power2.inOut": (f'tl.to("#s5-cab", {{ attr: {{ d: "{cpath(p)}" }}, duration: {d}, ease: "{ease}" }}, {t});'
                                          f' tl.to("#s5-plug", {{ x: {p[0]}, y: {p[1]}, duration: {d}, ease: "{ease}" }}, {t});')
c.js += [f'tl.set("#s5-plug", {{ x: {P0[0]}, y: {P0[1]} }}, 0);', mv(P1, 0.15, 0.5)]
lamp_on(c, "a", 0.66)
c.js += [mv(P0, 1.05, 0.3), 'tl.to("#s5-a-l", { backgroundColor: "#3b2a24", boxShadow: "none", duration: 0.08 }, 1.05);',
         mv(P3, 1.35, 0.3, "power2.in"), mv(P2, 1.66, 0.25, "back.out(3)")]
lamp_on(c, "b", 1.65, RED)
c.add(icon(c.id("x"), "cross", 1440, 460, 120, "ic r"), js=draw("#s5-x", 1.68, d=0.18, stagger=0.06))
label(c, "l", "one key, one host", 860, 0.2, how="rise")

# ---------- S6 CATALOG: eight jacks pop in; each integration is a small data file, not code.
c = shot("s6", B(27), B(32))
label(c, "l", "8 apps. Data, not code.", 110, 0.0, size=76, how="type")
for i, b in enumerate(["github", "linear", "notion", "todoist", "airtable", "slack", "stripe", "asana"]):
    x, y = 360 + (i % 4) * 400, 330 + (i // 4) * 340
    chip(c, f"k{i}", b, x - 70, y, 140)
    c.add(f'<div class="mono" id="s6-d{i}" style="position:absolute;left:{x - 70}px;top:{y + 160}px;width:140px;text-align:center;font-size:40px;color:{DIM}">{{ }}</div>')
    c.js.append(f'tl.fromTo(["#s6-k{i}", "#s6-d{i}"], {{ scale: 0, opacity: 0 }}, {{ scale: 1, opacity: 1, duration: 0.3, ease: "back.out(2)" }}, {0.45 + i * 0.14:.2f});')

# ---------- S7 THREE TOOLS: the orb wires to three knobs that switch on in turn.
c = shot("s7", B(32), B(36))
label(c, "l", "your model sees 3 tools", 100, 0.0, size=76, how="wipe")
orb(c, "orb", 200, 420, 260, ORB_G, ORB_GLOW, spark=CREAM)
for i, name in enumerate(["search", "describe", "call"]):
    kx = 820 + i * 380
    cable(c, f"c{i}", curve(430, 470, kx + 90, 424, -170 - i * 60), [ORANGE, GOLD, "#34d1bf"][i], w=12, t=0.1 + i * 0.1, dur=0.35)
    c.add(f'<div class="knob" id="s7-k{i}" style="left:{kx}px;top:420px;width:180px;height:180px"><b></b></div>')
    c.add(f'<div class="lamp" id="s7-q{i}-l" style="left:{kx + 180}px;top:400px;width:26px;height:26px"></div>')
    c.add(f'<div class="lab" style="left:{kx - 60}px;top:640px;width:300px;text-align:center;font-size:58px">{name}</div>')
    c.js.append(f'tl.fromTo("#s7-k{i}", {{ rotation: -130 }}, {{ rotation: 40, duration: 0.3, ease: "back.out(2)" }}, {0.6 + i * 0.35:.2f});')
    lamp_on(c, f"q{i}", 0.75 + i * 0.35)

# ---------- S8 APPROVAL (hero): a write card; the red lamp blinks; the cursor presses Approve; the pulse goes.
c = shot("s8", B(36), B(42))
label(c, "l", "every write waits for you", 100, 0.0, size=76, how="rise")
c.add(f'<div id="s8-card" style="position:absolute;left:220px;top:300px;width:900px;height:460px;border-radius:28px;background:{BOX};border:3px solid #44474f;box-shadow:0 24px 50px rgba(0,0,0,0.55)"></div>')
chip(c, "kc", "slack", 280, 360, 110)
c.add('<div class="t" style="left:420px;top:362px;font-size:76px">Post in Slack</div>')
c.add(f'<div class="lab mono" style="left:420px;top:458px;font-size:48px;color:{DIM}">#launch</div>')
c.add(f'<div id="s8-deny" style="position:absolute;left:280px;top:600px;width:340px;height:110px;border-radius:20px;border:4px solid #6a6d75"></div>'
      f'<div class="lab" style="left:280px;top:622px;width:340px;text-align:center;font-size:56px;color:{DIM}">Deny</div>')
c.add(f'<div id="s8-ok" style="position:absolute;left:680px;top:600px;width:380px;height:110px;border-radius:20px;background:{ORANGE}"></div>'
      f'<div class="lab" style="left:680px;top:622px;width:380px;text-align:center;font-size:56px;color:#1b0d03">Approve</div>')
c.add(f'<div class="lamp" id="s8-r-l" style="left:1060px;top:330px;width:34px;height:34px;background:{RED};box-shadow:0 0 22px {RED}"></div>')
c.js.append(f'tl.to("#s8-r-l", {{ opacity: 0.25, duration: 0.18, yoyo: true, repeat: 5, ease: "none" }}, 0.2);')
cable(c, "w", curve(1120, 530, 1536, 530, 80), "#5a5d65", w=14)
c.add(svg(f'<path id="s8-p" class="cab" pathLength="1" d="{curve(1120, 530, 1536, 530, 80)}" style="stroke:{GREEN};stroke-width:14px"/>'))
c.js.append('tl.set("#s8-p", { strokeDashoffset: 1 }, 0);')
jack(c, "j", 1580, 530, 44)
chip(c, "kj", "slack", 1670, 470, 124)
cursor(c, "cur", fill=CREAM, stroke="#000000", w=60, h=86)
c.js += ['tl.fromTo("#s8-cur", { x: 1300, y: 1120 }, { x: 900, y: 660, duration: 0.5, ease: "power3.out" }, 1.0);',
         'tl.to("#s8-ok", { scale: 0.94, duration: 0.08, yoyo: true, repeat: 1 }, 1.55);',
         'tl.to("#s8-r-l", { opacity: 1, backgroundColor: "' + GREEN + '", boxShadow: "0 0 22px ' + GREEN + '", duration: 0.08 }, 1.6);',
         'tl.to("#s8-p", { strokeDashoffset: 0, duration: 0.45, ease: "power2.in" }, 1.65);']
lamp_on(c, "j", 2.1)
c.add(icon(c.id("ck"), "check", 1530, 680, 110, "ic gr"), js=draw("#s8-ck", 2.12, d=0.25))

# ---------- S9 END CARD.
c = shot("s9", B(42), D)
c.add(f'<div class="t or" id="s9-n" style="left:140px;top:170px;font-size:230px">'
      + "".join(f'<span style="display:inline-block">{ch}</span>' for ch in "foxplug") + '</div>')
c.js.append('tl.fromTo("#s9-n span", { y: 80, opacity: 0 }, { y: 0, opacity: 1, duration: 0.4, ease: "power3.out", stagger: 0.04 }, 0.05);')
c.add(f'<div class="mono" id="s9-i" style="position:absolute;left:140px;top:480px;padding:20px 44px;border-radius:18px;font-size:66px;color:{CREAM};background:{BOX};border:3px solid #44474f;white-space:nowrap">npm i foxplug-agent</div>',
      js='tl.fromTo("#s9-i", { opacity: 0, scale: 0.85 }, { opacity: 1, scale: 1, duration: 0.4, ease: "power3.out", transformOrigin: "0% 50%" }, 0.45);')
c.add(f'<div class="mono" id="s9-g" style="position:absolute;left:146px;top:690px;font-size:52px;color:{CREAM}">github.com/pooriaarab/foxplug</div>',
      js='tl.fromTo("#s9-g", { opacity: 0 }, { opacity: 1, duration: 0.35 }, 0.75);')
c.add(f'<div class="lab" id="s9-m" style="left:146px;top:790px;font-size:44px;color:{DIM}">MIT · no server</div>',
      js='tl.fromTo("#s9-m", { opacity: 0 }, { opacity: 1, duration: 0.35 }, 0.95);')
orb(c, "orb", 1300, 330, 200, ORB_G, ORB_GLOW, spark=CREAM)
for i, b in enumerate(["github", "notion", "slack"]):
    y = 260 + i * 190
    cable(c, f"c{i}", curve(1490, 430, 1680, y + 50, 40), [ORANGE, GOLD, "#34d1bf"][i], w=10, t=0.3 + i * 0.1, dur=0.3)
    chip(c, f"k{i}", b, 1690, y, 100)

sfx = [("whoosh", B(7) + 0.75, 0.3), ("stamp", B(11) + 0.95, 0.45), ("pop", B(11) + 0.9, 0.3), ("hit", B(15), 0.45),
       ("click", B(22) + 0.66, 0.45), ("glitch", B(22) + 1.65, 0.35)]
sfx += [("pop", round(B(27) + 0.45 + i * 0.14, 3), 0.2) for i in range(8)]
sfx += [("click", round(B(32) + 0.75 + i * 0.35, 3), 0.35) for i in range(3)]
sfx += [("click", B(36) + 1.55, 0.45), ("chime", B(36) + 2.1, 0.4), ("sparkle", B(42) + 0.45, 0.35)]
music_auto = {"version": 1, "lanes": [{"target": "volume", "points": [{"t": 0, "v": 0.8}, {"t": D - 1.5, "v": 0.8}, {"t": D, "v": 0}]}]}
build(ROOT, comps, sched, D=D, bg=GROUND, base_css=base_css, fonts=fonts, safe=safe, stills=[], sfx=sfx,
      music_auto=music_auto, music_vol=0.8,
      fontfiles=["barlowcondensed-600.woff2", "barlowcondensed-700.woff2", "barlow-600.woff2", "jetbrains-mono-normal-500.woff2"])
