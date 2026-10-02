# Next session: the recompiler, then the first run

Where things stand: the disc is extracted (`build/extract`, with
saturnkit's `disc` reading the XA track and the interleaved files), the
formats are known, the program is mapped at a first level
(`03-executables.md`), Beetle is driven to the first corridor
(`tools/oracle.py`).

## First: discovery's open points (open question 8)

1. Read the four large functions at 0x0601EB08, 0x0601EC0E, 0x0601ED60,
   0x0601EF72 and the 34 indirect calls at 0x06028000–0x06028940 they
   reach: a table of handlers, or one function discovery runs together?
   Fix discovery in saturnkit if it is the latter (and check Virtual
   Hydlide and Deep Fear lose nothing).
2. 0x06022B7C and 0x060315BA: what reaches them (a table, a pointer)?

## Then: `AA` to C++

* `tools/recomp.py` in Deep Fear's shape: one module (`AA` at 0x06010000),
  saturnkit's instruction test, the vectors of the program's functions
  that run alone, `--build`, `--test`. Aim for 0 differences.
* `tools/names-aa.tsv`: the names known so far (`main`, the CPK library's
  entry points, the CDC routines, the file loader 0x06019A88).

## Then: the first run

* `tools/run.py`: headless, with a pad script that mirrors the oracle's
  (START three times on the title, at 131, 133 and 135 s of Beetle's run).
  First check: the boot's ISO 9660 reads (`runtime/cdrom.cpp` assumes
  Mode 1; `AA` is in track 1, so it should load), then the CD block's
  reads from track 2 (Form 1 data at offset 24).
* The opening movie with its sound, the title, the briefing, the first
  corridor; pictures against Beetle's
  (`python tools/oracle.py --at 131:START,133:START,135:START,160:shot`).
* A `--wav` of the opening against Beetle's `--record`.

## Ask the user

* To listen to track 3 (`build/audio/track03.wav`, 4 seconds) and say
  when, if ever, the game plays it.
* What the walking controls are in Beetle, and whether the game ever
  shows a game over or continue screen (`GAME.DGT`/`OVER.DGT` are not on
  the disc).

## Keep in mind

* Every saturnkit change is checked on Virtual Hydlide and Deep Fear.
  Their submodules are still at 6f6b437; session 1's `disc` change
  (2af2418) touches only the Python disc reader, which neither port's
  build or run uses.
* The title takes START only after a few seconds (open question 10).
