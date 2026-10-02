# The plan

## What the game is, for a port

A movie player with a map. Nearly everything on screen is a Sega FILM /
Cinepak movie or a 16-bit still; the program (165 KB, one file, never
swapped) chooses which movie comes next, draws a few overlays (the
viewfinder, digits, yes/no, the bottles, the editing screen), takes
photographs, and in the end lets the player cut "Rusty Nail" from four
angles. There is no 3D and no game world beyond the movies.

## Feasibility: static recompilation, on saturnkit

The same route as Virtual Hydlide and Deep Fear: `AA` to C++ through
saturnkit's recompiler, run on saturnkit's runtime, the hardware replaced
under it. It should be the simplest of the three:

* **One program**, SHC on SBL, the compiler and library family of Virtual
  Hydlide, which saturnkit was built on. Discovery already finds 98.4 % of
  Ghidra's functions unchanged.
* **SBL's Cinepak player has run on saturnkit before**: Virtual Hydlide's
  opening movie plays through the runtime's CD block, its PCM handshake
  and its VDPs at the movie's own 15 fps. Here the same library (CPK 1.10)
  plays everything.
* **No 3D, no SCU DSP, no SGL.** VDP1 and VDP2 in the forms the runtime
  draws already are likely enough (to be checked: what the movies are
  drawn as).

What saturnkit has, and what this game asks of it:

| Need | saturnkit now | To do |
|---|---|---|
| The file system over a Mode 1 and an XA track, interleaved files | `disc` (session 1) | |
| The CD block on an XA track: Form 1 data at 24, the subheader, filters by file number | `runtime/cdblock.cpp` reads the subheader and filters on it (file, channel, submode, coding); the boot's ISO reads in `cdrom.cpp` assume Mode 1 | check on the real reads; the boot only needs `AA`, in track 1 |
| Five streams at once through five filters (the angles) | the filters exist | the drive's speed and buffer as the game expects them, checked against Beetle |
| SBL's CPK, the slave, PCM through the sound driver 1.27 | Virtual Hydlide's movie | the driver 1.27 (Virtual Hydlide's is not yet identified by version) |
| CD-DA track 3, if it is played | CD-DA reaches the SCSP's input; no game has played it | if open question 5 says so |
| The function discovery | 782 functions, 0 with problems | the four overlapping functions and their 34 indirect calls |

## What a better Virtual Shock on PC means

* **No waiting.** On the Saturn every step is a seek and a load at double
  speed. From files on a PC drive the next movie can start at once. The
  runtime can serve the CD block's reads without the drive's delays,
  or the game layer can preload; to be measured against Beetle first.
* **Movies at their pace, decoded on the PC.** Cinepak at 10 and 15 fps
  stays 10 and 15 fps (the footage is what it is), but without dropped
  frames or stutter, and with the sound in step.
* **Sharper.** The source is 320×224 Cinepak: no detail to recover. What
  can be honest: scaling with a good filter to the window, integer or
  smooth at the user's choice, the overlays (viewfinder, digits) drawn at
  the window's resolution.
* **English subtitles, maybe.** The voices are already English. The
  Japanese subtitles are drawn in the frames, in a box at a fixed place.
  A game layer could cover that box with an English line at the right
  times (a table of start and end times per movie). It is optional, and
  the user decides.
* **The four angles**, which on the Saturn are 144×108 each so that four
  can be decoded at once, could be shown larger in the editing screen.

## Phases

1. **The survey** (session 1, done): the disc, the formats, the program,
   the oracle to the first corridor, saturnkit's `disc` over XA and
   interleave.
2. **The recompiler**: discovery's open points (the four big functions,
   the indirect calls), `AA` to C++, the self-test against the interpreter
   (`tools/recomp.py`, Deep Fear's shape).
3. **The first run**: the boot on the runtime, the opening movie with its
   sound, the title, START, the briefing, the first corridor
   (`tools/run.py`, headless, pictures against Beetle's).
4. **The whole game**: the walking graph (open question 1), the
   photographs, the bottles, the elevator, the members' scenes, the
   "Rusty Nail" editing with its five streams, the ending and the staff
   roll, all against Beetle and played by the user.
5. **The PC gains**: no waiting between steps, the scaling, the window,
   the pad; the subtitle layer if wanted.
6. **The release**: a build and a README for players (BYOA).
