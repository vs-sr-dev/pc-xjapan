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

Checks for 2af2418: this disc gives 270 files, the five interleaved
ones with all 45 546 of their sectors carrying their record's XA file
number. Virtual Hydlide and both Deep Fear discs extract byte-identical
files and print the same `--info`. Only their CD-DA records, which used
to come out as empty files, are no longer written; no tool of either
port reads them. Nothing else in saturnkit imports `disc`: the
recompiler and the runtime are unchanged, so neither port's build or run
can differ. Their submodules stay at 6f6b437 for now.

## What this game will ask next

* The runtime's CD block on the XA track, with five filters at once for
  the angles (`runtime/cdrom.cpp`'s boot reads assume Mode 1).
* Discovery: the four functions with overlapping code
  (`03-executables.md`).
* Sega's sound driver 1.27 with the movies' PCM; perhaps CD-DA from the
  runtime for the first time.
* Layer 2's "Sega FILM/Cinepak" extractor, if the port wants its own
  decoder rather than the game's (ffmpeg reads them meanwhile).
