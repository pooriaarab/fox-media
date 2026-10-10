# Fox launch videos — polish round (owner feedback, 2026-10-09)

Keep each video's style, music and palette. The owner likes them. This round is polish only.
Read BRIEF.md first; its rules still hold (truth, privacy guard, audit, install line, no "Muse"/"Firefox" product names).

## Global rules (all 19)
1. **Pacing — people must be able to read.** Hold any frame with text for at least ~2.5 s, plus about 0.3 s for each word over 6 words. Text frames: max ~8 words. Fewer, longer shots: about 8–10 shots in 20–26 s, not 18–20. Cut on beats, but skip beats. A fast cut is fine only between pure graphic frames with no text.
2. **One idea per frame.** Show text OR a graphic as the hero, not dense text on one side and a busy screenshot on the other. If both, the text is a short label (≤5 words) and the graphic is simple.
3. **Graphics over screenshots.** Mix and match. Use mostly designed graphics: SVG diagrams, flow arrows, simple UI components (a button, a toast, a permission prompt, a chat bubble, a card) drawn in the video's style, and icons. Use real screenshots sparingly, only as proof, held long enough to read, and cropped tight to the one thing that matters. You may use the WaveSpeed CLI/API to generate illustrations (key in ~/Documents/Personal/.secrets/wavespeed.env, never print it). Keep image spend ≤$0.15 per video and log it in spend.jsonl.
4. **No terminal or code screenshots** unless the viewer needs that exact command. No raw CLI output, JSON or logs.
5. **Plain language.** ELI5 for a person who knows nothing about browser agents. Use ASD-STE100 Simplified Technical English (short sentences, active voice, common words). Run the humanizer skill on the copy if you can invoke skills; otherwise apply its rules: no AI-slop phrases, no hype words, no em-dash chains.
6. **Hooks people relate to (October 2026).** Open on a concrete, everyday situation or the worst case, not the product name. Use a copywriting frame: PAS (problem, agitate, solve), BAB (before, after, bridge) or AIDA. Pick one per video and vary it across the set. Real-world examples and current culture references are welcome, but every factual claim about a real product or event must be true. Do not invent incidents, and do not name a company as breached unless it is public record.
7. **Proof without the test count.** Do not show "N/N e2e checks" in every video. Keep proof only where it lands (foxpay keeps its numbers). Prefer one concrete outcome ("0 requests left your laptop").
8. **First frame = poster frame.** Frame 0 must be a finished, striking graphic plus a hook line, never blank, black or a fade-in. It is the social thumbnail. Export it as <repo>-poster.png next to the mp4.
9. **Audio.** Voice must sit clearly above everything. Music ducks to ~0.26 under voice. SFX ducks to ≤0.35 under voice, and stays ≤0.6 elsewhere. Integrated loudness about -16 to -14 LUFS, peak ≤ -1 dB.
10. **Animation variety.** No two consecutive shots use the same entrance. Prefer motion on the graphic (draw-on lines, a toggle flipping, a card sliding, a counter ticking) over more text.

## Avatar videos
The owner says the teeth look fake (foxpay, foxmind) and wants a different outfit in every avatar video, never repeated. Wait for the lead's avatar decision (look IDs or a new engine) before rendering a new avatar. Do not re-render avatars on your own.

## Owner feedback on the foxbench pilot (applies to ALL videos)
- Much better overall. Still wants MORE interactive SVGs, drawings and graphics, and LESS text.
- Treat graphics as the story: animated SVG scenes where things happen (a cursor clicks, a form fills itself, a toggle flips, a stamp lands, a line traces a path, a shield blocks an arrow). Text is a caption, not the content.
- Target: at most about 40% of shots carry a text line. The others are pure animated graphics, with a 1–3 word label at most.
- Never stack several layers in one shot (screenshot + scan + callout + label). One visual action per shot. foxbench 11.5–14.4 s (the shop still + x-ray + note + caption) is the example of too much.
- Real screenshots: use 0–1 per video, and only as a quick "this is real" beat. Otherwise redraw the UI as a simple SVG in the video's style.

## Avatar outfits (looks are being made now; the lead sends the IDs)
foxmate = olive overshirt + black rectangular glasses; foxsync = cream knit; foxkit = denim jacket; foxpay = navy blazer + clear round glasses; foxmind = grey hoodie; foxvault = white oxford + gold wire glasses.
Render on Avatar V: engine {type: avatar_v, reference_look_id: 61c287ae190b4ae7935469717a4a9f07}, 1:1, 1080p, voice 11de34550bd747379681c84d07aaf48a. Do not send "expressiveness". Keep the script to about 40–50 words, and make every claim true. Build everything else first, and add the avatar when the lead sends the look ID.

## Per-video notes
- **foxbench (pilot first):** apply all global rules.
- **foxpay:** keep the proof numbers. Add designed UI graphics (payment card, approval prompt, cap meter), one per frame. New avatar outfit and fixed teeth (wait for the lead).
- **foxden:** too technical. Say no code. Lead with the use case ("let an AI agent try a site without touching your real logins") and compare with tools people know (e.g. a private window, a VM, cloud sandboxes like E2B or Cloudflare sandboxes). Every comparison must be accurate.
- **foxgate:** edgier. Show the scary requests agents can make: read your inbox, export contacts, fill your card number, send your address. Show how foxgate stops them. The right-side screen grabs distract and do not hold long enough: replace them with designed graphics, or hold them.
- **foxloop:** same as foxgate. Slower, one idea per frame, designed graphics.
- **foxmate:** the SFX are too loud (rule 9), and there is too much text. More variety in the animated frames.
- **foxmemory:** a crazy relatable hook ("Do you remember what you DoorDashed yesterday? Neither does your AI."). Less text.
- **foxlink:** great. Fewer, slower cuts only.
- **foxtrail:** viewers do not understand what it is. ELI5: what problem, for whom, the before and the after. No jargon.
- **foxmind:** new avatar outfit and fixed teeth (wait for the lead).
- **foxshield:** too much on each slide. Show the worst-case examples with real-world website types (a shopping page with a hidden "ignore your instructions" note, a review site, a fake support chat), current trends, and pop-culture references. One example per frame.
- **foxlens:** simplify.
- **foxlend:** reduce. No CLI or terminal shots. Explain with a diagram. Try PAS.
- **All others** (foxkit, foxrunner, foxvault, foxbridge, foxsync, foxpaw): apply the global rules.

## Deliverables per video
- An updated <repo>-launch.mp4, keeping the previous version as work/<repo>/v1-launch.mp4.
- <repo>-poster.png (frame 0).
- hyperframes check, audit.py, a frame scrub, and a loudness report.
- A note of what changed.

## Avatar look IDs (v3: built from real photos with pooria-photo; round dark wire glasses on olive, blazer and oxford; render ONLY after the lead says GO; never use the old IDs)
- foxmate: 47281f80c3edd9f7d6979783b51903f3 (olive overshirt, thin dark round wire glasses)
- foxsync: 931e0db223ce48b56d9dfa6af804fb81 (cream knit)
- foxkit: 194ca2619db64426054e3bdc3f3f4203 (denim jacket)
- foxpay: 740611d3187f61c2aa93ab9704fd8927 (navy blazer, thin dark round wire glasses)
- foxmind: 4e90ee542646a5c137f24c49c079c2df (grey hoodie)
- foxvault: 605a1e2d312a36aad0db44bfa0544a8f (white oxford, thin dark round wire glasses)
Each clip costs about $0.05–0.09 per second, with a minimum per clip. Render one clip per video, about 15–20 s, at full script length (no short tests).

## Truth rule (added after foxbench v3)
- Never present a scripted or test agent as a real one. Label them "scripted" or "test agent".

- No invented URLs or domains. Show only github.com/pooriaarab/<repo> and npm names.

## Round 3: owner feedback, with the WHY (apply the why to every future video)
- **Solid, consistent backgrounds** (foxbridge). WHY: a busy or shifting background competes with the graphic, so the eye cannot find the one idea. Use one solid ground per video and let the graphic carry the contrast.
- **Graphics must explain, not decorate** (foxbridge). WHY: a graphic that does not show the mechanism is noise. Every graphic must show cause and effect clearly at a glance: what goes in, what is blocked, what comes out.
- **Story over statement: show, don't tell** (foxlens, foxtrail). WHY: people remember a story and a metaphor, not a claim. Find the product's metaphor and build the video on it: a needle in a haystack, a page seen as a painting, fox footprints that leave damage.
- **Art direction can match the music** (foxlens). WHY: when the music is artistic, a literal UI demo feels flat. Lean into the art reference, e.g. a website painted as a famous modern painting, a magnifier sweeping a dense haystack of UI and zooming in on the one target.
- **Reading pace again** (foxshield). WHY: the owner still could not read some text. If a frame has a sentence, hold it until a slow reader finishes, about 3.5 s plus 0.3 s per word over 6. When in doubt, cut words, not time.
- **Make the hidden vs visible contrast obvious** (foxshield). WHY: a prompt-injection video fails if the viewer cannot see what a human sees vs what the agent reads. Show the visible page, then reveal the hidden layer: expand the text above and below, peel the CSS off, show an aria-label or alt attribute on a real-looking element, show white-on-white or 1 px text. Use patterns seen on real websites (hidden divs, aria-label, alt text, off-screen text, HTML comments, zero-width text), and never name a real site as compromised.
- **Real brand logos where the viewer knows the brand** (foxlink, foxden, foxmemory). WHY: a recognisable logo makes people relate in a fraction of a second, and text cannot do that. Use the official brand SVG (e.g. Simple Icons, CC0, or the brand's press kit), unmodified, at a normal size, only to name the service the product works with or compares against. Never imply an endorsement. Gmail and Google Calendar (foxlink), DoorDash (foxmemory), E2B and Cloudflare (foxden), plus any service named on screen.
- **Portray AI the way people now see it** (foxden). WHY: a clunky cartoon robot reads as dated. Use the modern AI-assistant language: a soft orb, pulsing dots, a sparkle, a minimal face like current assistant UIs. Draw your own: do not copy a specific company's mark.
- **Poster: less text, one brand anchor** (foxmemory). WHY: the poster is a thumbnail. Header and footer text make it unreadable at small size. Use one hook line plus one strong graphic or logo.
- **Alignment must be exact** (foxmemory 0:16, soy milk not directly over oat milk). WHY: a sloppy alignment reads as fake and breaks the trust the video is building. Check every overlay and replacement for exact alignment in the stills review.
- **No backgrounds you would not choose on purpose** (foxmind). WHY: the owner disliked it. A background must support the style. If in doubt, use a solid or a subtle gradient in the palette.
