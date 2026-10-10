# Art deco

First used on foxpass (`work/foxpass/build.py`, 25.4 s). A 1920s hotel lobby at night: thin gold lines on deep emerald, sunburst arches, a brass padlock.

**Why this style for this product.** foxpass is about keys, locks and doors. Art deco is the visual language of grand doors, brass locks and lobby keys, so the metaphor (the agent stops at a locked door and hands you the key) reads before a word appears. Gold on emerald also feels trustworthy and careful, which a product that touches passwords must feel. No earlier fox video uses deco.

- **Ground:** one solid deep emerald `#0f2b25`, plus one static double gold frame (2 px at 45 % and 1 px at 25 %, inset 34 and 46 px). Nothing moves behind the graphics. Why: one solid ground lets the gold line drawings carry the contrast; the frame is the deco signature and never changes.
- **Palette:** gold `#d9b45a`, pale gold `#f1d68b` (light behind an open door), cream `#f4ead2` (text, typed dots), panel `#143a31`, ruby `#e0795c` (only for the leak), jade `#5fc3a2` (only for "unlocked" and "[redacted]"). Ruby means danger, jade means safe; nothing else uses them.
- **Type pair:** Limelight (deco display) and Josefin Sans 700/600 (geometric caps labels with 0.04 em tracking). JetBrains Mono 500 for the log line, `[redacted]` and the install line.
- **The agent:** a gold-cream orb with a sparkle that walks a gold double line (the floor). Labelled "test agent" whenever it acts, because the E2E and the demo agent has fixed rules and is not a model.
- **Signature graphics:** an arched door (outer 6 px gold arch, inner 2.5 px arch, spring line, 11 sunburst rays, a hub circle), two leaves that swing open with `scaleX` from their outer edges, a brass padlock whose shackle lifts and turns jade, deco cards with a 3 px border plus a 1.5 px outline at 8 px offset.
- **Text entrances (none repeats back to back):** finished poster, clip-path wipe from the centre for the name, letters that settle from wide to tight (done with per-letter `x`, because the linter rejects `letterSpacing` tweens), drop from above, cards that swing in on `rotationY` from their outer edges, rise from below.
- **Seams:** hard cuts on the beat. Doors, locks and dots carry the motion.
- **Pacing:** 8 shots in 25.4 s. Sentences hold 3.73 to 3.75 s; one-word or pure-graphic shots hold 2.14 to 2.68 s.
- **Copy frame:** PAS. Problem: "Would you give your AI your password?" Agitate (no words): the password dots fly into the agent and come out in its log in plain text. Solve: "The agent pauses. You sign in."
- **Music prompt (elevenlabs/music, 25 s):** "1920s art deco jazz noir instrumental, 112 BPM swing, walking upright bass, brushed snare, muted trumpet stabs, stride piano, sly heist mood. Starts on a strong downbeat, no intro. A big band hit and fuller swing at 10 seconds. Clean ending on the final bar. No vocals." One bar (9.088 to 11.233 s) is copied in at 11.233 s, so the clean last hit lands under the end card; the 4-beat splice keeps the grid. The minimax/music-02 take had drop-outs at 10 s and 15 to 17 s.
- **SFX cue map:** whoosh as the dots fly; glitch as the log strip opens; hit on the name; stamp on the pause mark; type under your password; brass unlock on the shackle; door swing on the leaves; chime on the balance; pop on the proof cards; hit on the end card.

## Shot list (foxpass)

| # | Time | Hold | On screen | Why |
|---|---|---|---|---|
| 1 | 0.00 | 3.73 s | Poster. "Would you give your AI your password?" The orb before a locked deco door. | The worry, and the door that the story opens. |
| 2 | 3.73 | 2.68 s | No words. Password dots fly into the orb; an "AGENT LOG" strip slides out with "password: correct horse". | Agitate: what happens when an agent handles your password. |
| 3 | 6.41 | 3.75 s | "foxpass" / "The agent pauses. You sign in." | The promise (README tagline, shortened). |
| 4 | 10.16 | 2.68 s | "Pause." The orb walks to the locked door and stops; a pause mark lands; "test agent". | foxpass pauses the agent at a sign-in step. |
| 5 | 12.84 | 3.75 s | "You open the lock." The password field is outlined; you type; the padlock opens and turns jade. | foxpass outlines the field and hands the step to you. |
| 6 | 16.59 | 2.14 s | The leaves swing open; the orb goes through; "BALANCE $1,204.56", "test agent, sample bank page". | The E2E agent goes on after sign-in and reads the balance. |
| 7 | 18.73 | 3.75 s | "The agent never sees it." YOU TYPE: dots. THE AGENT READS: [redacted]. | E2E R1/R2/L1: the agent's read and the planner context hold no password and no code. |
| 8 | 22.49 | 2.91 s | foxpass, `npm i foxpass`, github.com/pooriaarab/foxpass, an open door. | End card. |
