# The program on saturnkit's Saturn

`python tools/run.py`: the recompiled `AA` on saturnkit's runtime,
headless, in virtual time, with the pad script that reaches the first
corridor; `--play` opens the window.

## How far it runs (session 2)

From the boot to the first backstage corridor, the same sequence as in
Beetle, about 9 seconds earlier (the runtime boots the 1st read file at
once, without the BIOS's animation):

| VBlank | Time | |
|---|---|---|
| 0 | 0 s | `AA` loaded at 0x06010000 by the HLE boot |
| 300 | 5 s | the SEGA logo |
| ~700 | ~11.4 s | `OPEN.CPK` starts: "TOKYO DOME", the crowd, the order sheet, the man in the suit, the backstage |
| 7200 | 120 s | the title |
| 7500 | 125 s | START (the script) |
| 7560 | 126 s | "Please Press Start Button" on screen (in a run without START) |
| 7900–9000 | 132–150 s | the briefing, `S_0.CPK`, its subtitles in their blue box |
| 10200 | 170 s | the first corridor |

Without START, the title gives way to the attract at about VBlank 7900
("Dec,31,1994", then the opening again). START at VBlank 7500 or 7800 is
taken.

### The opening's sound against the movie's own

The run's sound (`--wav`) was compared with `OPEN.CPK`'s audio decoded by
ffmpeg. The opening starts 11.401 s into the run, at the same level
(−0.09 dB). Over 3-second windows from 2 s to 101 s, the waveforms
correlate at 0.974 to 1.000. The run drifts against the file by about
0.6 samples a second (about 15 ppm), 58 samples by the end. The game's
PCM path, from the CD block through Sega's driver 1.27 and the SCSP, is
right.

## What the program asked of the runtime

Three things stopped it, all saturnkit's (`10-saturnkit.md`):

1. **HBLANK.** Before it writes TVMD (display off and on), the program
   waits for TVSTAT's HBLANK bit (0x06011BE8, 0x06011C34). The runtime's
   TVSTAT had VBLANK and ODD only; it waited forever.
2. **A call to 0x06013AA4**, a callback that does nothing, which
   discovery had not taken as a function.
3. **The pad, read directly.** Once a frame (0x06011CC4) the program sets
   IOSEL, drives TH and TR through PDR1 and DDR1, reads the pad's ID
   (0xB, a standard pad) and its four nibbles; the run's only four SMPC
   commands are not a pad read each frame. The runtime's PDR1 read 0xFF,
   nothing pressed. With the
   nibbles in MAME's order (TH/TR 01 directions, 10 START A C B) START is
   taken; in the other order the ID still read 0xB, but no button reached
   the program's word at 0x06077900.

## What runs where

From the hardware log of the run to the corridor (`--report`):

* **The slave works**: SINIT written 1 987 times. SBL's CPK library
  hands work to the slave SH-2 (open question 3: which part of the
  decoding is still to be read).
* **VDP1 draws each movie frame** (one draw per frame change, the
  interrupt 0x4D, "sprite draw end", taken 2 810 times); VDP2 is set up
  in bitmap mode (CHCTLA, BMPNA, BGON, MPOFN written 5 times each).
* **SCU DMA level 0**: set up 96 times; its end interrupt (0x4B) taken
  155 times.
* **The CD block**: the CDC routines poll HIRQ and the command registers
  millions of times; reads from track 2 (Form 1, user data at 24) work
  through the runtime's CD block as they are.
* **SMPC**: four commands (COMREG), the pad read directly every frame.

## Next

The corridor, and walking: what the buttons do there, by playing
(`python tools/run.py --play`), then the walking movies, the stills, the
members' rooms, against Beetle.
