# Soft clay

First used on foxvoice (`work/foxvoice/build.py`, 24.4 s). Everything looks like soft modelling clay: puffy, rounded, lit from the top left.

**Why this style for this product.** Voice is warm and personal. A soft, touchable look says "this is friendly and it is yours", which is the feeling of speech that stays on your own device. Clay also gives a modern AI look for free: the assistant is a soft orb, not a robot. No earlier fox video uses a light, tactile 3D look.

- **Ground:** one solid warm clay-cream `#f4e9df` for the whole video. Nothing moves behind the graphics. Why: the clay shapes carry their own light and shadow, so a busy ground would fight them.
- **Clay shading:** every shape gets the same three shadows: an inner dark at the bottom right, an inner light at the top left, and a soft brown drop shadow (`inset -10px -14px 24px rgba(0,0,0,.14), inset 10px 12px 22px rgba(255,255,255,.55), 0 26px 50px rgba(120,64,40,.2)`). One light source for every object keeps the world believable.
- **Palette:** coral `#ff7a59` (the talk button, the orb), lilac `#9c8cff` (the waveform, the laptop), mint `#43c4a1` (the private bubble, the Whisper chip), ink `#3a2c26`. Text-safe variants, because the contrast audit needs 3:1 on cream: coral text `#bf4228`, button coral `#cf4d2c`, chip mint `#23927a`, mint text `#1f7d64`.
- **Type pair:** Fredoka 700/600 (round, soft display that matches the clay) and JetBrains Mono 500 for the install line only.
- **The agent:** a clay orb (radial gradient white, peach, coral, lilac) with a cream four-point sparkle. Never a robot.
- **Signature graphics:** a capsule waveform (13 clay bars that pulse with a finite yoyo), a pill "Hold to talk" button that squashes when the cursor presses it, a mint glass dome over a clay laptop, a grey clay cloud with a coral "0" badge.
- **Text entrances (none repeats back to back):** finished at frame 0 (poster), UI label swap (Hold to talk to Listening), mask wipe on the topline, per-word rise for the transcript, blur-to-sharp scale slam for the name, slide from the left, per-letter rise on the end card.
- **Seams:** hard cuts on the beat. The motion is inside the shot: a press, a flow, a draw-on.
- **Pacing:** 7 shots in 24.4 s. Text shots hold 3.5 s or more (round-3 rule: 3.5 s plus 0.3 s per word over 6). The only short shot (2.0 s) is a pure graphic: the press.
- **Copy frame:** BAB. Before: "Too long to type?" After: "Say it." Bridge: the name and "Speech that stays on your device."
- **Music prompt (elevenlabs/music, 25 s):** "Warm lo-fi chillhop instrumental, 90 BPM, soft Rhodes electric piano chords, round sub bass, crisp dusty hip-hop drums, a light airy synth pad, intimate and friendly. Starts on a strong downbeat with drums from the first second, no intro. A lift with fuller drums at 12 seconds. Clean ending on the final bar. No vocals." Chosen over minimax/music-02 because the minimax take was 22.4 s and whisper.cpp heard "Oh, oh, oh" in it (a vocal).
- **SFX cue map:** clay squish on the press; pop and sparkle when the waveform enters the chip; soft type under the words; hit on the name; whoosh and click when the cloud call stops at the dome wall; sparkle when the orb answers; chime on the end card. All at 0.25 to 0.5.

## Shot list (foxvoice)

| # | Time | Hold | On screen | Why |
|---|---|---|---|---|
| 1 | 0.00 | 3.68 s | Poster. "Too long to type? Say it." Waveform over a clay "Hold to talk" button. | Everyday pain, plus the product's one gesture. |
| 2 | 3.68 | 2.01 s | A cursor presses the button; it squashes; the label turns to "Listening"; the bars grow. | Push to talk, shown not told. |
| 3 | 5.69 | 4.67 s | "Voice in. Words out." The waveform flows into a "Whisper" chip ("in your browser") and comes out as "ask not what your country can do for you". Tag: "test clip: JFK, 1961 (public domain)". | The mechanism. The words are the real E2E transcript of the test WAV (0 % word error rate). |
| 4 | 10.36 | 4.01 s | "foxvoice" / "Speech that stays on your device." | The promise. |
| 5 | 14.37 | 3.34 s | A mint bubble ("private mode") over a laptop; a call to the cloud stops at the bubble wall; the cloud reads "0 requests". | The E2E cloud trap server got 0 requests in private mode. |
| 6 | 17.71 | 2.68 s | The orb, a speaker and sound arcs. "It talks back." | `speak()` reads the reply with a voice on the device. |
| 7 | 20.39 | 4.01 s | foxvoice, `npm i foxvoice`, github.com/pooriaarab/foxvoice. | End card. |
