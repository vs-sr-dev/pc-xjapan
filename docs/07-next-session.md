# Next session: walking the backstage

Where things stand: `AA` is C++ and self-tested (`09-recompiler.md`); on
saturnkit's runtime it boots, plays the opening with its sound, shows the
title, takes START, plays the briefing and reaches the first corridor
(`11-runtime.md`). `python tools/recomp.py --build --test`, then
`python tools/run.py` (headless, to the corridor), `--play` for the
window.

## First: what the user sees and hears in the window

`python tools/run.py --play`: keys in `saturnkit/runtime/host.cpp`
(arrows, Enter = START, Z X C = A B C, A S D = X Y Z, Q W = L R; F11
fullscreen, F12 a picture) or a gamepad. The user plays from the title
into the backstage and reports: the movies' pace and sound, the corridor
and walking, anything wrong against Beetle.

## Then: walking

1. The controls in the corridor (by playing, and in the code: the word at
   0x06077900 holds the pad's buttons).
2. The walking graph (open question 1): which movie follows which button
   in which place, from the table near the file names.
3. A pad script for `tools/run.py` that walks a few steps; pictures
   against Beetle's (`tools/oracle.py`).
4. The elevator (`ELE_SEL.DGT`, `UP_DOWN.DGT`), the dressing rooms, the
   first member's scene, the viewfinder (`FINDER.DGT`) and a photograph.

## Later

* The "Rusty Nail" editing: five interleaved streams through the CD
  block's filters at once.
* Track 3: does the program ever play it? The item jingle so far comes
  from the pickup movie's audio; `--trace` shows any CD block Play.
* `tools/scripts/to-first-film.txt` (the user's game, `--input @…`) as a
  regression run: "YOU GET!" at VBlank 7760.
* The PC gains (`06-attack-plan.md`): no waiting between steps first.

## Keep in mind

* Every saturnkit change is checked on Virtual Hydlide and Deep Fear: in
  each, recompile and self-test, then the headless run with pictures and
  `--wav` compared with the run before (byte-identical in session 2). Both
  are at 4061b12.
* The heredoc trap: a Bash heredoc feeding Python turns a written `\n`
  into a newline; use Edit/Write for C++ string edits.
