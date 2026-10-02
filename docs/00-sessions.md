# Sessions

## Session 1 (2026-10-02): the disc, the code, the plan

* **The disc** (`01-disc-layout.md`): the Japanese release, GS-9023
  V1.000 (1995-09-09), one disc of three tracks. The ISO 9660 file system
  runs over a Mode 1 track and a CD-ROM XA track (Form 1). Five files
  (the four 144×108 angles of "Rusty Nail" and their sound) are
  interleaved sector by sector, as their ISO records say. A 4-second
  audio track is pointed at by a `CDDA1` record. 270 files: one
  program, 186 movies, 78 pictures, the sound driver.
* **saturnkit learned the disc** (`10-saturnkit.md`): sectors by disc LBA
  over several tracks, Mode 2 user data, interleaved files, CD-DA records
  left out, a date written YYYY-MM-DD. Virtual Hydlide and Deep Fear
  extract the same files as before.
* **The formats** (`02-data-formats.md`): every `.CPK` is Sega FILM with
  Cinepak (320×224 at 10 or 15 fps, 8-bit PCM), about 42 minutes plus the
  four angles; every `.DGT` a 6-byte header and Saturn RGB pixels, all 78
  decoded (`tools/dgt.py`). The Japanese subtitles are drawn in the
  movies' frames. Sound: Sega's driver 1.27 and the movies' PCM.
* **The code** (`03-executables.md`): one program, `AA`, at 0x06010000,
  never swapped; SHC's crt0, SBL (the CPK library 1.10), no SGL, no GFS
  strings. `main` read to its first loads. Discovery: 782 functions,
  555 of Ghidra's 564; four large functions with overlapping code to read
  next.
* **The oracle** (`tools/oracle.py`): Beetle Saturn with the Japanese
  BIOS (`sega_101.bin`, from the user's BIOS archive, MD5 checked, added
  to RetroArch's system folder). From the boot through the opening movie
  (about 20–128 s), the title (about 130 s; START taken at the third
  press, 135 s), the briefing (`S_0.CPK`) to the first backstage
  corridor (160 s).
* **The plan** (`06-attack-plan.md`): static recompilation on saturnkit,
  likely the simplest of the three ports (one SHC/SBL program, a Cinepak
  player saturnkit has already run); the gains are no waiting between
  steps, clean playback, honest scaling, and perhaps English subtitles.
* **Seen and heard by the user** in Beetle: the voices are English, the
  subtitles Japanese; the player is a photographer sent backstage to take
  pictures of the band. "Shiroi Yoru" (31 December 1994) is one of the
  band's best-known concerts. Track 3 is a short "bling", a confirming,
  positive sound; when the game plays it, and whether it ever shows a game
  over or continue screen, the user will report while playing.

## Session 2 (2026-10-02): the recompiler, the first run, the first corridor

* **Discovery's open point** (`09-recompiler.md`): the four "large
  functions" are small ones tail-jumping into 0x06027CD0, whose 34 calls
  through r11 saturnkit's constant propagation could not see past a
  `jmp`. Fixed in saturnkit, with callbacks that do nothing (`rts; nop`)
  taken as functions: 786 functions, 53 unresolved jumps instead of 164.
* **The program as C++** (`tools/recomp.py`): 75 658 instructions, built
  with clang; self-test 11 632 of 11 632 vectors.
* **The first run** (`tools/run.py`, `11-runtime.md`): the recompiled
  game boots on saturnkit's runtime, plays the opening with its sound
  (its waveform correlates at 0.97 to 1.00 with `OPEN.CPK`'s own audio,
  at the same level), shows the title, takes START, plays the briefing
  and reaches the first backstage corridor at 170 s, as in Beetle.
  saturnkit's runtime learned TVSTAT's HBLANK bit, the pad read directly
  through PDR1 (the program never reads it by INTBACK), and the disc's
  area code.
* **saturnkit** 835e91a and 4061b12 (`10-saturnkit.md`), checked on
  Virtual Hydlide (51 542 vectors, the run to the field byte-identical)
  and Deep Fear (7 227 vectors, the run byte-identical); both ports moved
  to them.
