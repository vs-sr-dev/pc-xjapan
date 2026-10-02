# The formats

Two formats carry the whole game: Sega FILM movies and a plain 16-bit
picture. Neither is compressed beyond Cinepak.

## `.CPK`: Sega FILM with Cinepak

Every `.CPK` begins `FILM`, version `1.06`, `1.07` or `1.08`, then an `FDSC`
chunk (codec, height, width, bits per pixel, audio channels, audio bits,
audio compression, sample rate) and an `STAB` chunk (time base, then one
entry per sample). This is the container of Sega's CPK library, which the
program carries (`CPK Version 1.10 1995-03-31`, `03-executables.md`).
ffmpeg reads all 186 files (`segafilm` demuxer, `cinepak` decoder).
The table below is from each header and ffprobe on each file.

| Video | Sound | Files | |
|---|---|---|---|
| 320×224 Cinepak, 15 fps | 8-bit mono, 22 050 Hz | 67 | events and scenes (`A_n_m`, `B_n_m`), the members' footage |
| 320×224 Cinepak, 10 fps (two at 12 and 15) | 8-bit mono, 11 025 Hz | 48 | walking between places (`A_n`, `A_nR`, `B_n`, `B_nR`) |
| 320×224 Cinepak, 1–3 frames | none | 55 | still views (`*KABE*`, `A_1_3`…) |
| 320×224 Cinepak, 15 fps | 8-bit stereo, 22 050 Hz | 8 | `OPEN`, `C_2_1`, `ENDING`, `HT_IMG`, `M_0..2`, `A_9_3` |
| 176×128 Cinepak, 15 fps | 8-bit stereo, 22 050 Hz | 1 | `A_1_14`, hide on stage, smaller |
| 144×108 Cinepak, 15 fps | none | 4 | `MK_MY_1..4`, the four angles of "Rusty Nail" |
| none | 8-bit stereo, 22 050 Hz | 1 | `SOUND.CPK`, the angles' song (5:30) |
| none | 8-bit mono, 22 050 Hz | 1 | `STAF_SND.CPK`, the staff roll's music (47 s) |
| none | 8-bit mono, 22 254 Hz | 1 | `SHUTER.CPK`, the shutter (1 s) |

The frame rates come from the `STAB` time base (600) and the sample
times, as ffmpeg reports them. In all: about 42 minutes, and the four
angles of 5:28 each on top.

The **subtitles are in the pictures.** The voices are English. The
Japanese subtitles are drawn into the Cinepak frames, in a box at the
bottom of the frame (seen in frames of `OPEN.CPK` and `S_0.CPK` decoded by
ffmpeg). The program does not draw them. The user saw and heard the same
in Beetle.

## `.DGT`: 16-bit pictures

    0  "DC"
    2  width   (16-bit, big-endian)
    4  height  (16-bit, big-endian)
    6  width × height pixels, 16-bit big-endian, the Saturn's RGB:
       bit 15 opaque, bits 14–10 blue, 9–5 green, 4–0 red

Checked on all 78 files: each is exactly 6 + 2 × width × height bytes, and
`tools/dgt.py` decodes them all to PNG (pixels with bit 15 clear are
transparent: the bottles' outlines, the "YES"/"NO" buttons). The sizes:

| Size | Files | |
|---|---|---|
| 144×108 | 51 | the members' photographs (10 each), `X_LOG` |
| 320×224 | 14 | `TITLE`, `FINDER`, `BACK_CG1` ("You Have Edited this Video."), `SAKE_SEL`, `S_ROLL1..10` |
| others | 13 | `OD_SHEET` (160×218), `ITEMS` (48×504), `NUM0_9`, `RED1234`, `TM0_9` (digits), `PRESSBTN` (272×26), `YES`, `NO`, `UP_DOWN`, `ELE_SEL`, three 64×180 bottles |

The photographs are 144×108, the size of the four angle movies. The
pictures a player can take may be stills of the movies at that size
(open question).

## Sound

`SDDRVS.TSK` is Sega's sound driver for the 68000, `ver1.27 94/11/21
SATURN(S) master` (Deep Fear has 2.10). `BOOTSND.MAP` (82 bytes) is the
map of sound RAM it loads with (it looks like 8-byte entries of an id, an
address and a size, ending `FFFF`; not yet read in the code). No tone
bank, sequence or ADX file is on the disc: the game's sound seems to be
the movies' 8-bit PCM, to be confirmed in the running program.

Track 3 is a 4-second CD-DA sound (`01-disc-layout.md`).
