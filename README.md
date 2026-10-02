# pc-xjapan

Toward a native PC port of **X JAPAN Virtual Shock 001** (Sega Saturn,
1995, I² Project / Excess 24 / Sega), a full-motion-video game set
backstage at the Tokyo Dome on 31 December 1994, the night of X JAPAN's
"Shiroi Yoru" (白い夜) concert. The player is a photographer sent
backstage to take pictures of the band. The player walks the corridors in
filmed steps and looks for the five members (Yoshiki, Toshi, hide, Pata,
Heath) to photograph them through a viewfinder. From what the disc holds,
it ends with the player editing a video of "Rusty Nail" from four camera
angles that play together. It came out
only in Japan, only on the Saturn, and was never re-released. The goal is
the game running natively on PC: its movies at their own pace, without
the CD's waits between steps, and sharper where that can be done honestly.

This repository documents the disc, its formats and its code, and grows
the tooling for the port. It is the third port built on **saturnkit**,
the game-agnostic toolkit for Saturn reverse engineering that grew out of
[pc-virtualhydlide](https://github.com/vs-sr-dev/pc-virtualhydlide).
X JAPAN is where saturnkit meets a CD-ROM XA track, interleaved files and
Sega's Cinepak library. saturnkit is a submodule here: clone with
`--recursive`, or run `git submodule update --init`.

## BYOA: Bring Your Own Assets

This repository contains **documentation and tools only**. No game data, no
executables, no assets. You need your own original disc. The work is done
on the Japanese release, GS-9023 V1.000 (1995-09-09), one disc, as a
Redump-style .cue/.bin set in `iso/`.

## Layout

    docs/            disc, format and code analysis, and the plan
    tools/           X JAPAN-specific tools: dgt.py, oracle.py, recomp.py, run.py, names-aa.tsv
    saturnkit/       game-agnostic Saturn toolkit (submodule)
    iso/, build/     your disc and everything derived from it (ignored by git)

## Tools

The Python tools need only Python 3.8+ and no dependencies, except PIL for
writing pictures. Building the recompiled C++ needs CMake, Ninja, clang and
SDL3 (MSYS2's mingw64, found at `C:\msys64\mingw64\bin`). The oracle needs RetroArch with the Beetle Saturn core
and the Japanese BIOS (`sega_101.bin`). ffmpeg reads the movies. Run
everything from the repository root.

```sh
C="iso/X Japan - Virtual Shock 001 (Japan) (3M).cue"

# the disc: IP.BIN, the ISO 9660 volume over two data tracks, the interleaved files
python -m saturnkit.disc "$C" --info
python -m saturnkit.disc "$C" --list
python -m saturnkit.disc "$C" --extract build/extract
python -m saturnkit.disc "$C" --audio build/audio

# the pictures (.DGT) as PNG; the movies (.CPK, Sega FILM / Cinepak) with ffmpeg
python tools/dgt.py build/extract build/dgt
ffmpeg -i build/extract/OPEN.CPK build/open.mp4

# the code: where the program loads, its hardware, its functions
EXE=build/extract/AA
python -m saturnkit.sh2 $EXE --find-base
python -m saturnkit.sh2 $EXE --base 06010000 --at 06010128 --count 60      # main
python -m saturnkit.sh2 $EXE --base 06010000 --refs 25890000:258A0000      # the CD block
python -m saturnkit.recomp.discover $EXE --base 06010000 --report

# the program to C++, built with clang (MSYS2) and checked against the interpreter
python tools/recomp.py --build --test

# run it on saturnkit's runtime: headless to the first corridor, pictures at chosen VBlanks
python tools/run.py -- --shot 7200,9000,10200
python tools/run.py --play                 # a window, the keyboard or a gamepad

# the oracle: Beetle Saturn in RetroArch, pressed and photographed from here
python tools/oracle.py --at 131:START,133:START,135:START,160:shot          # to the first corridor
```

## Status

Session 1: the survey. One disc whose file system runs over a Mode 1
track and a CD-ROM XA track, with 186 Sega FILM / Cinepak movies (about 42
minutes), 78 pictures in a plain 16-bit format, and four camera angles of
"Rusty Nail" interleaved sector by sector with their shared sound. One
program, `AA`, at 0x06010000, compiled with SHC on SBL (the CPK library
1.10, the sound driver 1.27), never swapped. saturnkit learned to read the
XA track and the interleaved files. Beetle Saturn driven from the boot
through the title and the briefing to the first corridor. Static
recompilation looks like the simplest of the three ports so far
(`docs/06-attack-plan.md`).

Session 2: the program as C++ (786 functions, self-test 11 632 of 11 632
vectors) on saturnkit's runtime, from the boot through the opening movie
with its sound, the title and the briefing to the first backstage
corridor. saturnkit learned to see through far jumps in discovery,
TVSTAT's HBLANK, and the pad read directly through the SMPC's ports
(`docs/11-runtime.md`).

## Documentation

* [00-sessions.md](docs/00-sessions.md): what each session did
* [01-disc-layout.md](docs/01-disc-layout.md): IP.BIN, tracks, the file tree, the interleaved files
* [02-data-formats.md](docs/02-data-formats.md): the movies, the pictures, the sound driver
* [03-executables.md](docs/03-executables.md): the program, SBL, the hardware it touches, function discovery
* [04-curiosities.md](docs/04-curiosities.md): things found on the way
* [05-open-questions.md](docs/05-open-questions.md): what is not known yet
* [06-attack-plan.md](docs/06-attack-plan.md): feasibility, what saturnkit has and lacks, the phases, what a better Virtual Shock means
* [07-next-session.md](docs/07-next-session.md): the next session's list
* [09-recompiler.md](docs/09-recompiler.md): the program as C++, discovery's fixes, the self-test
* [10-saturnkit.md](docs/10-saturnkit.md): what this port gave saturnkit
* [11-runtime.md](docs/11-runtime.md): the program on saturnkit's Saturn, how far it runs

## Licence

MIT: see [LICENSE](LICENSE). X JAPAN Virtual Shock 001 is © 1995 I²
Project, Excess 24 and Sega; this project contains none of it.
