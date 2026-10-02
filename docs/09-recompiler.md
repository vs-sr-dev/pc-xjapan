# The program as C++

`python tools/recomp.py --build --test`: `AA` to C++ through saturnkit's
recompiler, built with clang from MSYS2, checked against saturnkit's
interpreter.

## Discovery

What session 1 left open (`03-executables.md`) turned out to be two
things in saturnkit, both fixed there (`10-saturnkit.md`):

* **The four "large functions"** at 0x0601EB08, 0x0601EC0E, 0x0601ED60,
  0x0601EF72 are small: each is a `switch` on the word at 0x06038580 that
  stores its arguments into a record and ends in a tail call, `jmp @r3`,
  to 0x06027CD0. That function was found later than they were, so
  discovery followed it as part of each of them (shared code, which the
  recompiler duplicates: harmless). But the constant propagation that
  resolves calls through registers did not follow a `jmp` to a constant.
  The 34 `jsr @r11` of 0x06027CD0 (r11 = 0x0602763C, a callee-saved
  constant loaded once) therefore stayed unresolved in each copy: 102 of
  the 164. They now resolve.
* **Callbacks that do nothing.** 0x06013A9C, 0x06013AA0, 0x06013AA4 and
  0x06026B02 are `rts; nop`, handed to functions as literals. They were
  too short for discovery to tell from data records. The first run
  stopped on a call to 0x06013AA4.

| | session 1 | session 2 |
|---|---|---|
| functions | 782 | 786 |
| unresolved indirect jumps | 164 (92 sites) | 53 |
| functions with problems | 0 | 0 |

The 53 left are calls through pointers that the program sets at run time
(callbacks in structures, a few tables); the recompiled code dispatches
them at run time.

## The C++

| Module | Functions | Instructions | Files |
|---|---|---|---|
| AA | 786 | 75 658 | 11 |
| OPTEST (saturnkit's instruction test) | 775 | 2 130 | 2 |

Generated in about 6 s, built in about 20 s.

## The self-test

| Vectors | Functions | Vectors | Failures |
|---|---|---|---|
| `optest.txt` (every instruction form) | 775 | 9 300 | 0 |
| `aa.txt` (the program's functions that run alone) | 146 | 2 332 | 0 |

82 of the 786 functions run on their stack alone, 64 more with pointer
arguments.

## Names

`tools/names-aa.tsv`: `crt0`, `main`, the slot opener and the picture
loader `main` calls, and 0x06027CD0, named by its address until it is read.
