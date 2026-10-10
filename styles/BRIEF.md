# Fox launch videos — shared brief (all four video agents)

Make one launch video per assigned repo. Personal project, personal keys only.

## Read first
1. Process skill (unmerged): ~/Documents/Personal/_wt/ski-520-ship-demo-video/ship-demo-video/SKILL.md. Follow its stages and gates: real footage from the product's own harness, storyboard, music, build, stills review, render, audit.
2. Reference implementation: ~/Documents/Personal/foxpilot-media/social2/tools/README.md (three proven styles with working build.py: Keynote whip with avatar PiP, Dossier, Pop flats; SFX pack; audit.py).
3. Videos the owner loved: ~/Documents/Personal/foxpilot-media/{foxpilot,pii-guard,consent-shield}-v2.mp4.
4. HeyGen launch films: /tmp/hfl (shallow clone of heygen-com/hyperframes-launches). Mine it for styles.
5. Each repo: ~/Documents/Personal/<repo> (README, e2e harness). Existing harness demo footage: ~/Documents/Personal/fox-media/<repo>/<repo>-demo.mp4 plus its README. Re-film from the harness when you need better shots. Do not commit anything to the repos; work in ~/Documents/Personal/fox-media/work/<repo>/.

## Rules
- Exactly the style assigned to you per repo. Write each new style's spec to ~/Documents/Personal/fox-media/styles/<style>.md: ground, type pair, text entrances, seams, pacing, music prompt, SFX cue map, copy pattern.
- 20 to 26 s. Shots 1 to 1.5 s. Cut on detected beats (`npx hyperframes beats`). Arc: hook in outcome language, value by beat two, demo on the musical drop, proof from measured numbers only (from the repo's tests/artifacts — never invent a number), end card with `npm i <npm name>` and the repo URL github.com/pooriaarab/<repo>.
- Product names: never call a product "Muse" or "Firefox"; you may say "for Firefox" / "runs in Firefox". No "demo" in on-screen product names.
- npm names: foxden -> foxden-sandbox, foxlink -> foxlink-oauth, foxpay -> foxpay-agent; others match the repo name (check package.json).
- Music: WaveSpeed key in ~/Documents/Personal/.secrets/wavespeed.env (source it inside the command; never print it). Two instrumental variants per video: elevenlabs/music (music_length_ms, force_instrumental) or minimax/music-2.6 (is_instrumental). Pick by per-second loudness curve (ffmpeg ebur128). SFX on cuts, clicks, slams. HARD CAP: $0.30 of WaveSpeed per video; the shared balance is about $6 for all 19. Check the balance before each call; stop and report if it drops under $0.50.
- Avatar (only where assigned): HeyGen key in ~/Documents/Personal/.secrets/heygen.env (never print it). POST /v3/videos, type avatar, aspect_ratio 1:1, voice_id 11de34550bd747379681c84d07aaf48a. Use the photo-avatar look assigned to you (different clothes/angles). Script about 50 words, every claim true (from the README/tests). Duck music to about 0.26 under the voice.
- Privacy: harness recordings show the desktop after the browser closes. Find each clip's last product frame and make the build refuse any clip that reads past it (see foxpilot build.py SAFE dict). Run audit.py on every final render. Also scrub frames for any personal window, notification, email address, file path with a username, or token. A leak is a stop-ship.
- Output: ~/Documents/Personal/fox-media/<repo>-launch.mp4. Keep sources in fox-media/work/<repo>/.
- Do not push, open PRs, or touch git remotes. Do not post anything anywhere.

## Report
Per video: path, style, length (s), music model + cost, avatar look if any, audit result, and any blocker (e.g. no runnable demo to film). List the style spec paths.
