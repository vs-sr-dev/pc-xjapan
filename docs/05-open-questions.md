# Open questions

What is not known yet, numbered so that later sessions can refer to it.

1. **The walking graph.** Which movie follows which button in which
   place: the table that links `A_n`, `A_nR`, the still views and the
   events. The names sit in one block of data (0x060337B0–0x06034C30);
   the links are probably next to them.
2. **The four angles.** Does the program read the whole interleaved
   stretch through five CD block filters (one per XA file number) and
   decode all four 144×108 movies at once, with `SOUND.CPK`? How is the
   edit recorded, and what plays at the end?
3. **Who decodes Cinepak.** SBL's CPK library can decode on the slave
   SH-2; the program writes SINIT in three places. Master, slave, or both?
4. **Frame pacing.** The movies run at 10 or 15 fps: paced by their sound
   (the PCM play position, as in Virtual Hydlide's movie), by a timer, or
   by VBlanks? And the program outside the movies?
5. **Track 3 and `CDDA1`.** A 4-second sound the program never names.
   The user heard it: a short "bling", a confirming, positive sound. Is
   it played (by track number), and when? The user will say when they
   hear it in the game.
6. **The five missing names** (`GAME.DGT`, `OVER.DGT`, `CONTINUE.DGT`,
   `BACK_CG.DGT`, `B_TACHIK.CPK`): dead code, or reachable, and what does
   the program do when a file is missing?
7. **0x0600026C**, read in 37 places: all error exits like the one in
   `main`?
8. **Discovery**: the four large functions at 0x0601EB08–0x0601EF72 whose
   code overlaps, and their 34 indirect calls (0x06028000–0x06028940): a
   jump table, an interpreter, or a run of `switch` cases that discovery
   follows as one body? Two functions Ghidra finds (0x06022B7C,
   0x060315BA) are reached by nothing discovery follows.
9. **How files are found**: no GFS. The CD block's own file system
   commands (0x70–0x75, which saturnkit's runtime has), or the program's
   own ISO 9660 reading?
10. **The title's delay.** In Beetle, START on the title was taken only at
    the third press, about 5 seconds after the title appeared (at 135 s
    of the run; presses at 131 and 133 s did nothing). A delay before the
    title takes input, or a press too short for a slow poll?
11. **The photographs.** Are the 144×108 `.DGT` photographs the pictures
    the player "takes", chosen by when the shutter is pressed in a movie,
    and how is a shot judged ("CHANCE!")?
12. **The sound**: is all of it the movies' PCM through the driver 1.27,
    and what does `BOOTSND.MAP` lay out?
