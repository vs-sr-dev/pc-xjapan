# What this port gave saturnkit

saturnkit (`saturnkit/`, a submodule from
https://github.com/vs-sr-dev/saturnkit) was started by Virtual Hydlide's
port and grew through Deep Fear's. X JAPAN Virtual Shock 001 is its third
game: SHC and SBL like the first, but on a disc with a CD-ROM XA track and
interleaved files. Each entry is a saturnkit commit and what this game
asked of it.

| Session | saturnkit | What |
|---|---|---|
| 1 | 2af2418 | `disc`: sectors read by disc LBA from whatever track holds them (pregaps included), MODE2/2352 user data at offset 24; ISO 9660 records' file unit size, interleave gap and XA field (attributes, file number); `--extract` follows the interleave, `--list` shows it; records of CD-DA tracks (XA attribute 0x4000, or an LBA in an audio track) listed and not extracted; an IP.BIN date written YYYY-MM-DD |
| 2 | 835e91a | `recomp.discover`: the constant propagation follows a `jmp @rn` to a constant the descent followed, so calls through callee-saved registers in code reached that way resolve; a literal pointing at `rts; nop` is a function (a callback that does nothing) |
| 2 | 4061b12 | runtime: TVSTAT's HBLANK bit from virtual time; the SMPC's PDR1 in direct mode (the pad's TH/TR nibbles, ID 0xB, the same state as INTBACK's); INTBACK's area code from the disc's first area symbol instead of always Europe |

Checks for 2af2418: this disc gives 270 files, the five interleaved
ones with all 45 546 of their sectors carrying their record's XA file
number. Virtual Hydlide and both Deep Fear discs extract byte-identical
files and print the same `--info`. Only their CD-DA records, which used
to come out as empty files, are no longer written; no tool of either
port reads them. Nothing else in saturnkit imports `disc`: the
recompiler and the runtime are unchanged, so neither port's build or run
can differ. Their submodules stayed at 6f6b437 until session 2.

Checks for 835e91a and 4061b12, on all three games:

* **Discovery**: the same function entries in all 15 of Virtual Hydlide's
  programs and in Deep Fear's; unresolved indirect jumps fall (Virtual
  Hydlide's STARTUP 665 to 225, its maps about 235 to 135 each, Deep Fear
  177 to 149, this game 164 to 53). In ENDING four functions change
  their reached size: helpers now found earlier are tail calls instead
  of shared code, which the recompiler duplicated before. Both are
  correct.
* **Virtual Hydlide** at 4061b12: 15 programs recompiled; self-test
  51 542 of 51 542 vectors (51 485 before: more functions run alone now
  that their calls resolve); the headless run to the field with 3
  program starts, 1 539 frame changes, 2 691 draws; its four pictures
  and its sound **byte-identical** to the run at 6f6b437.
* **Deep Fear** at 4061b12: recompiled; self-test 7 227 of 7 227 vectors
  (and saturnkit's 9 300); the headless run to VBlank 3000 with its
  four pictures and its sound **byte-identical** to the run at 6f6b437.
* **This game**: self-test 11 632 of 11 632 vectors; from the boot to the
  first corridor (`11-runtime.md`).

Both ports' submodules moved to 4061b12 (Virtual Hydlide e32e6eb, Deep
Fear bf8cb67).

## What this game will ask next

* The runtime's CD block with five filters at once for the angles
  (`runtime/cdrom.cpp`'s boot reads assume Mode 1; reads from the XA
  track already work).
* Perhaps CD-DA from the runtime for the first time (track 3's "bling").
* Layer 2's "Sega FILM/Cinepak" extractor, if the port wants its own
  decoder rather than the game's (ffmpeg reads them meanwhile).
