# The disc

Japanese release, one disc, as a Redump .cue with three .bin files in
`iso/`. Everything here is from `python -m saturnkit.disc … --info` and
`--list`, with the sectors read where it says so.

## IP.BIN

| Field | Value |
|---|---|
| Maker | SEGA ENTERPRISES |
| Product | GS-9023 |
| Version | V1.000 |
| Date | 1995-09-09, written as `1995-09-09` (ten characters, two into the device field, which then reads `CD1/1`) |
| Areas | J (Japan only) |
| Peripherals | J (control pad) |
| Title | `X-JAPAN CD-ROM` |
| IP size | 0x1800 |
| Stacks | master 0, slave 0 (the defaults) |
| 1st read | 0x06010000, the whole file |
| Area block | 0x0E04, `For JAPAN.` |

The ISO 9660 volume is `X_JAPAN_CD_ROM`, 273 552 sectors, created
1995-09-09 13:00:30, publisher and preparer `SEGA ENTERPRISES,LTD.`. The
copyright, abstract and bibliographic files (`XJ_CPY.TXT`, `XJ_ABS.TXT`,
`XJ_BIB.TXT`) all say `Copyright(c) SEGA ENTERPRISES,LTD 1995`.

## Tracks

| Track | Mode | LBA | Length | |
|---|---|---|---|---|
| 1 | MODE1/2352 | 0 | 395 sectors (5 s) | IP.BIN, the volume descriptors, the program and the small files |
| 2 | MODE2/2352 | 620 (pregap 225) | 272 482 sectors (60:33) | the movies and the large pictures |
| 3 | AUDIO | 273 252 (pregap 150) | 300 sectors (4 s) | a short sound; see below |

The file system spans tracks 1 and 2: 20 files lie in track 1 (up to LBA 394),
`OPEN.CPK` starts track 2 at LBA 620. Track 2 is CD-ROM XA. A scan of all
its 272 707 stored sectors shows:

* every sector after the pregap is **Form 1** (submode 0x08, data, or 0x88
  at a file's last sector), user data at offset 24. The pregap holds 75
  Mode 1 sectors, then 150 Form 2 ones;
* 226 196 sectors carry file number 0. 45 546 carry file numbers 1 to 5:
  these are the five interleaved files below.

## Files

270 files in the root directory, and a 271st record, `CDDA1`, that points
at track 3 (its XA attributes have bit 14 set, the CD-DA flag). No
subdirectories.

| Kind | Count | Size | |
|---|---|---|---|
| `AA` | 1 | 165 340 | the program, the 1st read file (`03-executables.md`) |
| `.CPK` | 186 | 554 MB | Sega FILM movies, Cinepak video (`02-data-formats.md`) |
| `.DGT` | 78 | 3.8 MB | 16-bit pictures |
| `SDDRVS.TSK`, `BOOTSND.MAP` | 2 | 20 482, 82 | Sega's sound driver and its sound RAM map |
| `XJ_*.TXT` | 3 | 40 each | the copyright notice |

The names say where things belong (read from names and frames; how the
program uses them is not yet followed):

* `A_*`, `B_*`: two areas of the backstage, numbered places. `A_n.CPK` and
  `A_nR.CPK` (10 fps, 11 kHz sound) look like walking from one place to the
  next and back; `A_n_m.CPK` (15 fps, 22 kHz) are what happens there;
  `*KABE*.CPK` ("wall") and other one- or two-frame files are still views.
  `A_1_1.CPK` is a door card, "HIDE's Room".
* `HIDE_*`, `YOSHI_*`, `TOSHI_*`, `PATA_*`, `HEATH_*`: ten 144×108
  photographs of each member.
* `HT_IMG`, `PT_IMG`, `TS_IMG`: a minute or more of footage each of Heath,
  Pata and Toshi (by their frames).
* `C_2_1.CPK` (8 minutes) and `ENDING.CPK` (4:45): concert footage.
* `M_0`, `M_1`, `M_2.CPK` and `MK_MY_1..4.CPK` with `SOUND.CPK`: the
  "Rusty Nail" editing screen (the song's name is on its display) and its
  four camera angles.
* `S_ROLL1..10.DGT`, `STAF_SND.CPK`: the staff roll and its music.
* `FINDER.DGT` (a viewfinder with "CHANCE!"), `SHUTER.CPK` (a sound only:
  the shutter), `OD_SHEET.DGT` (the order sheet, the day's assignment).
* `SAKE_SEL`, `NIHONSYU`, `WINE`, `BABON` (bourbon), `ITEMS.DGT`: bottles
  of drink and items.

### The interleaved files

Five files share one stretch of track 2 (LBA 227 154 to 272 933), sector
by sector. Their ISO 9660 records say so: the file unit size and the
interleave gap of the record, and the file number in its XA field.

| File | Unit | Gap | XA file | Sectors |
|---|---|---|---|---|
| `MK_MY_1.CPK` | 4 | 15 | 1 | 9 583 |
| `MK_MY_2.CPK` | 4 | 15 | 2 | 9 628 |
| `MK_MY_3.CPK` | 4 | 15 | 3 | 9 637 |
| `MK_MY_4.CPK` | 4 | 15 | 4 | 9 583 |
| `SOUND.CPK` | 3 | 16 | 5 | 7 115 |

A period of 19 sectors holds 4 of each angle and 3 of sound. saturnkit's
`--extract` follows the interleave (session 1). Every one of the 45 546
sectors it reads for these files carries the file number of the record it
was read for. Read at double speed (150 sectors a second), the stretch
gives each angle about 63 KB/s and the sound about 47 KB/s, all at once.

### Track 3 and `CDDA1`

Track 3 is 4.0 seconds of sound (peak −3 dB, mean −21.6 dB): to the
user's ear a short "bling", a confirming, positive sound. The program never names `CDDA1`. Who plays the track, and
when, is open (`05-open-questions.md`).

### What the program names

The program names 271 files. All 266 data files of the disc are among
them (only `AA` itself, the three `.TXT` files and `CDDA1` are not). Five
names in the program are **not on the disc**: `GAME.DGT`, `OVER.DGT`,
`CONTINUE.DGT`, `BACK_CG.DGT` (the disc has `BACK_CG1.DGT`) and
`B_TACHIK.CPK`.
