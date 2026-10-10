# Ink and washi

First used on foxnotify (`work/foxnotify/build.py`, 24.6 s). Black brush ink on plain rice paper, with one vermilion seal for the thing that matters.

**Why this style for this product.** foxnotify is about calm: fewer interruptions, quiet nights, one gentle tap. Ink on paper is the quietest look there is, with a lot of empty space and almost no colour. That makes the one red mark (the urgent notice) jump out, which is the product's whole job. The brush-drawn moon (an ensō) is a natural picture of quiet hours. No earlier fox video uses ink brush.

- **Ground:** one solid washi `#f2ece1`. No texture, no motion. Why: empty paper is the calm; the ink carries the contrast.
- **Ink:** strokes are SVG paths with round caps and a fixed ink-bleed filter per shot (`feTurbulence` fractal noise, base frequency 0.035, 2 octaves, seed 7, then `feDisplacementMap` scale 7). The seed is fixed, so the edge never shimmers between frames. Each sub-composition defines its own filter id, because lint checks each one alone.
- **Palette:** ink `#1f1d1a`, grey `#6f685a` (text-safe on washi), vermilion `#c4382a` (only the urgent notice, its seal and the tap ripples), ochre `#d8a24a` (only the morning sun), card `#fbf8f2`.
- **Type pair:** Shippori Mincho 800 (a calm, high-contrast serif) and Zen Kaku Gothic New 700/500 for labels and notice text. JetBrains Mono 500 for the install line.
- **Signature graphics:** the ensō moon (a 325° brush arc that draws on), notice cards (ink border, a grey ring for normal, a red seal square for urgent), a held tray line under the moon, a one-line ink figure seen from behind (head and shoulders) with two red tap ripples, an ink browser with three tabs and a red underline that moves.
- **Text entrances (none repeats back to back):** finished poster, blur-rise for the name with a seal stamp, clip wipe for the promise, slow fade under the drawing moon, rise, slide from the left, drop from above, clip wipe on the end card.
- **Seams:** hard cuts on the bar (3.125 s at 76.8 BPM), so most shots hold one full bar. The moon and the tray stay in the same place across shots 3 to 5, so the cut feels like time passing, not a new scene.
- **Pacing:** 7 shots in 24.6 s, 3.1 to 4.2 s each. Every text line holds at least 3.1 s.
- **Copy frame:** AIDA. Attention: "Ten pings. One matters." Interest: "foxnotify. It taps you only when it matters." Desire: quiet hours, urgent gets through, one summary later, click to the right tab. Action: the install line.
- **Music prompt (minimax/music-02, trimmed from 4.0 s):** "Calm ambient instrumental, 76 BPM, soft felt piano, koto plucks, wind chimes, warm pad, gentle soft kick, peaceful night mood, clear downbeat start, no vocals." Chosen over the elevenlabs take, which was near silent for its first 3 s (bad under the poster) and faded out from 17 s.
- **SFX cue map:** small temple bell at 0.9 s; hit on the name; scribble as the moon draws; soft taps as held notices land; whoosh as the urgent card passes; tap plus bell when it reaches the shoulder; chime on the digest; click on the notice; pop as the tab moves; bell on the end card.

## Shot list (foxnotify)

| # | Time | Hold | On screen | Why |
|---|---|---|---|---|
| 1 | 0.00 | 3.99 s | Poster. "Ten pings. One matters." Nine grey notices and one red-sealed "Approve the form?" (urgent). | The everyday flood, and the one that counts. |
| 2 | 3.99 | 3.90 s | "foxnotify" with a red seal / "It taps you only when it matters." | The promise. |
| 3 | 7.90 | 3.12 s | "Quiet hours". The ensō moon draws on, "22:00 to 07:00"; a low and a high notice drift into the held tray. | E2E: quiet hours hold the low notice and the high one too. 22:00 to 07:00 is the README example. |
| 4 | 11.02 | 3.12 s | "Urgent gets through." A red-sealed "Approve?" passes the moon and reaches a shoulder: two red tap ripples. | E2E: quiet hours let the urgent notice through; Firefox shows the urgent notice only. |
| 5 | 14.14 | 3.12 s | "One summary, later." The moon sets, a sun rises; three held notices fold into "3 updates from your agent". | E2E: the alarm shows one digest of the three queued notices, with that exact text. |
| 6 | 17.27 | 3.12 s | "Click. Right tab." A "Sign-in needed" notice is clicked; the red underline moves to the task tab. | E2E: the click makes the task tab active while another tab was in front. |
| 7 | 20.39 | 4.21 s | foxnotify, `npm i foxnotify`, github.com/pooriaarab/foxnotify, the moon. | End card. |
