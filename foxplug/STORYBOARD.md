# foxplug launch: storyboard

Style: **Patch bay** (new; spec in `styles/patch-bay.md`). Build: `work/foxplug/build.py`.
Format: 1920 x 1080, 27.0 s, 9 shots, hard cuts on the beat of a 112 BPM bed.

## Why this replaces v1

v1 opened on a black frame, had no music, put a JSON code block on screen, and
stacked a headline, a card and a caption in most frames. This cut follows the
series rules (`styles/POLISH.md`): frame 0 is the poster, one idea per frame, at
most about 40 % of shots carry a sentence, graphics over text, no code, a music
bed with SFX on the actions.

## Metaphor

foxplug is a patch cable. Your agent plugs a cable straight into GitHub, Notion
or Slack. There is no box in the middle. Each key is a cable that fits one jack
only. A write lights a lamp and waits for your finger.

## Copy frame: PAS

Problem: where does your key go? Agitate: the usual way puts a server in the
middle. Solve: foxplug plugs straight in.

## Beats (B = one beat, 0.536 s)

| # | Time | Hold | Role | One idea on screen | Text (max) | SFX |
|---|---|---|---|---|---|---|
| 1 | 0.00 | 7 B, 3.75 s | hook, poster | A dark patch panel. A glowing orb jack on the left; three cables already run to jacks with the GitHub, Notion and Slack marks. Signal dots run along the cables. | "Plug your local AI into your apps." | none (music downbeat) |
| 2 | 3.75 | 4 B, 2.14 s | problem | The usual way: the cable runs into a grey "server" box in the middle, and a key icon slides into the box. | label "a server in between" | whoosh |
| 3 | 5.89 | 4 B, 2.14 s | agitate to solve | The box drops off the panel. The cable snaps straight from the orb to the Slack jack. | label "no server" | stamp, pop |
| 4 | 8.04 | 7 B, 3.75 s | reveal | Name slam. | "foxplug" / "Your keys never leave the browser." | hit |
| 5 | 11.79 | 5 B, 2.68 s | feature: pinned key | A gold key cable tagged "slack.com" plugs into the Slack jack (lamp green), then tries another jack and bounces off (red X). | label "one key, one host" | click, glitch |
| 6 | 14.46 | 5 B, 2.68 s | feature: catalog | Eight jacks pop in one by one: GitHub, Linear, Notion, Todoist, Airtable, Slack, Stripe, Asana. A small "{ }" tag under each. | label "8 apps. Data, not code." | pop x8 (low) |
| 7 | 17.14 | 4 B, 2.14 s | feature: 3 tools | The orb with three knobs that turn on in turn: search, describe, call. | label "your model sees 3 tools" | click x3 |
| 8 | 19.29 | 6 B, 3.21 s | hero: approval | A write card: "Post in Slack #launch". A red lamp blinks. A cursor presses Approve; the lamp turns green and one pulse runs down the cable. | label "every write waits for you" | click, chime |
| 9 | 22.50 | 4.5 s | close | foxplug, `npm i foxplug-agent`, github.com/pooriaarab/foxplug, small "MIT". Cables from shot 1 rest at the side. | install line + URL | sparkle |

Text shots with a sentence: 1, 4, 9 (3 of 9). The other labels are 2 to 5 words.

## First frame

Shot 1 is finished at t = 0: the hook line, the orb, three live cables and three
brand marks. No fade. It is also `foxplug-poster.png`.

## Music cue

elevenlabs/music, 27 s, force_instrumental. Prompt: "Modular analog synth
groove instrumental, 112 BPM, bubbling sequenced synth arpeggio, warm round
bass, punchy tight drum machine with crisp claps, bright and curious, confident
tech-launch energy. Drums and arpeggio from the very first second, no intro. A
lift with fuller drums at 12 seconds. Clean ending on the final bar at 27
seconds. No vocals." Alternate: minimax/music-02 with the same prompt. Pick by
the per-second loudness curve. Music at 0.8, fade the last 1.5 s.

## Truth check (README, foxplug-agent 0.1.0)

- No server or relay between the browser and the vendor: README "Use cases".
- Keys in foxvault, pinned to the manifest hosts: README "How it works" step 4.
- 8 gold integrations, JSON manifests, not code: README intro and "Gold catalog".
- The planner sees 3 tools: `plug_search`, `plug_describe`, `plug_call`.
- Each write asks the user, one approval per exact call: foxgate, step 3.
- Not claimed: live-API runs (README says the gold manifests ran against a local
  server only), Stripe writes (read only), any benchmark score.
