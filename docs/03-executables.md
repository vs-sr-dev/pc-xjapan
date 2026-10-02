# The program

One program: `AA`, the 1st read file, 165 340 bytes, loaded at
0x06010000. No other file on the disc holds SH-2 code (the only other
code is the 68000's, `SDDRVS.TSK`). Nothing is swapped in at run time
(no other executable exists to swap in).

## Where it loads, and crt0

`saturnkit.sh2 --find-base` puts it at 0x06010000 (888 prologue hits; the
next best, 0x0601A000, has 102), which is also the 1st read address in
IP.BIN. Its crt0 (0x06010000) is the SHC style Virtual Hydlide has, not
Deep Fear's GCC:

* stack at 0x0607FFFC;
* clear the BSS from the address stored at 0x060337A8 (0x060385DC, the
  end of the file) to the one at 0x060337AC (0x0607B998);
* copy initialised data from 0x06036520 to 0x0607E130 up to 0x0607E130
  (empty);
* write 1 to the SH-2's DVCR, call `main` (0x06010128), loop forever.

## main

`main` (0x06010128) calls four set-up functions (0x060211B8, 0x06010310,
0x06013AC4, 0x060100B2), then:

* calls 0x06019A1A(0), which opens a slot of a table (0x06037E14,
  0x06038494) through 0x06013BB0. It tries twice, and if both fail it
  jumps through the BIOS pointer at 0x0600026C (the exit to the system);
* loads `OD_SHEET.DGT` and `NUM0_9.DGT` through 0x06019A88, each tried
  twice;
* then continues into the game (0x0601B15C, not followed yet).

The pointer 0x0600026C is read in 37 places. The one in `main` is an
error path; the others are not read yet.

## Libraries: SBL

* **CPK, Sega's Cinepak player**: `CPK Version 1.10 1995-03-31` at
  0x06036347, `cpkd_sys_start` at 0x06036474, the status names
  `WORKSTATRINGAUDINEXTCPPCTIMEERR` at 0x0602DC94, `FILMraw` at 0x0602E4FC.
* **The CD block**: the CDC routines at 0x06021412–0x06021634 (HIRQ,
  HIRQMASK, CR1–CR3, DATATRNS).
* **The slave SH-2**: three references to SINIT (0x21000000), at
  0x0603293E, 0x060329BA and 0x06032A62, in code not read yet. SBL's CPK
  library can decode on the slave; whether it does here is open.
* **Sound**: `SDDRVS.TSK` and `BOOTSND.MAP` are named next to each other
  at 0x060337B0, the standard SBL driver set-up.
* **BIOS services** read from their pointers: SYS_SETUINT (6), SYS_CHGSCUIM
  (6), SYS_SETSINT (5), SYS_GETSYSCK (5), SYS_GETUINT, SYS_GETSINT,
  SYS_CHGSYSCK, and 0x0600026C (37).

No SGL. No GFS strings either. How files are found (by name, through the
CD block's file system commands, or the program's own ISO 9660 reading)
is open.

## The hardware it touches (literal references)

| Block | References | Registers |
|---|---|---|
| CD block | 12 | HIRQ, HIRQMASK, CR1–CR3, DATATRNS |
| VDP1 | 16, and 55 into its VRAM | FBCR, PTMR, TVMR, EWDR, EWLR, EWRR, EDSR |
| VDP2 | 13, and 23 into its VRAM | TVMD, TVSTAT, RAMCTL |
| SMPC | 7 | COMREG, SF, DDR1, IOSEL |
| SCU | 5 | DMA level 0 (D0R, D0W, D0C, D0EN) |
| Sound | 18 | sound RAM, the SCSP |
| SH-2 on-chip | 126 | (not broken down yet) |

## The file names

All of the program's file names are literal strings in its data, from
0x060337B0 to 0x06034C30, grouped by use: the sound driver and the order
sheet first, then the title's files, the walking movies of area B then
area A with their still views, the ending, the members' photographs in
order (Yoshiki, Toshi, hide, Pata, Heath), the shutter, the staff roll,
the bottles. The disc's file list is in `01-disc-layout.md`. Five of these
names have no file on the disc.

## Function discovery

`python -m saturnkit.recomp.discover build/extract/AA --base 06010000 --report`,
unchanged from Virtual Hydlide and Deep Fear:

| | |
|---|---|
| functions | 782 |
| code | 123 216 bytes |
| data | 16 946 bytes |
| unclassified | 25 178 bytes |
| switch tables | 6 |
| unresolved indirect jumps | 164 (92 distinct sites) |
| functions with problems | 0 |

Against Ghidra 12.1.2's auto-analysis of the same file (`ExportFuncs.java`,
564 functions), discovery finds **555 of 564** (98.4 %), and 227 that
Ghidra does not. Of the 9 it misses:

* 2 are shared tails inside other functions (0x06011ADE, 0x06011BA6);
* 0x0601388A, 0x06031D04, 0x06032994 and 0x06032A3C have prologues but
  fall inside a function discovery reached;
* 0x0601F08C, a prologue, falls inside four large functions
  (0x0601EB08, 0x0601EC0E, 0x0601ED60, 0x0601EF72, about 3 KB each) whose
  reached code overlaps. Three of them reach the same 34 indirect calls
  at 0x06028000–0x06028940: 102 of the 164 unresolved;
* 0x06022B7C and 0x060315BA are reached by nothing discovery follows.

These four big functions and their indirect calls are the first thing to
read before recompiling (`07-next-session.md`).
