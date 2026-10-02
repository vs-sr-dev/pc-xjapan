# Curiosities

Things found on the way that are not needed for the port but are worth
keeping.

* **A night on a disc.** The game is set on 31 December 1994 at the Tokyo
  Dome, the second of the "X JAPAN 1994 Tokyo Dome 2 Days" shows, the one
  called "Shiroi Yoru" (白い夜, "White Night"). The order sheet
  (`OD_SHEET.DGT`) gives the assignment: the date, the venue, "白い夜",
  the members' rehearsals, a meeting in the press room after the show
  starts. The disc was mastered on 1995-09-09, eight months later.
* **English voices, Japanese subtitles, in the picture.** The man in the
  suit who briefs the player speaks English. The Japanese subtitles are
  part of the Cinepak frames, in a blue box. The user heard and saw this
  in Beetle; the frames decoded by ffmpeg show it.
* **Four cameras at once.** The four angles of "Rusty Nail" are four
  144×108 movies interleaved 4 sectors at a time with a stereo sound file,
  so that one pass of the drive brings all of them in step. The ISO 9660
  records describe the interleave exactly (file unit 4, gap 15).
* **The only Japanese voice.** Turning a corner in area B, the player
  meets a security guard who stops them, shouting in Japanese ("今、ここは
  通れないよ", "you can't come through here now"). He is the only one
  who speaks Japanese, and the only one without subtitles: the
  subtitles are there to translate English for a Japanese player. The
  camera falls, and the game over is filmed: "Will You CONTINUE? GAME
  OVER" is part of the movie (`B_12_1.CPK`), only YES and NO are drawn by
  the program. (The user, playing the port.) An English version would
  need a subtitle here, where the original has none.
* **"YOU GET!"**: the 4-second audio track, never named by the program,
  is the jingle for finding an item (the user, playing the port).
* **Names without files.** The program names `GAME.DGT`, `OVER.DGT`,
  `CONTINUE.DGT` (a game over and a continue screen), `BACK_CG.DGT` and
  `B_TACHIK.CPK` ("tachiiri kinshi", no entry?), none of them on the disc.
  The disc does have a "立入禁止" (no entry) sign in one of its corridors.
* **A date too long.** IP.BIN's release date is written `1995-09-09`, ten
  characters in an eight-character field, pushing the device field to
  `CD1/1`.
* **A three-track disc with one audio track of 4 seconds**, which the
  program never names.
* **The credits** (`S_ROLL1..10.DGT`): producer Kaichirou Furuta (I²
  Project), program by Chongming Shi and Shuangcai Cui, a "3D character"
  by INA (probably the green-haired figure in the editing screen), and
  "X JAPAN 1994 Tokyo Dome 2 Days staffs" thanked.
* **Bottles.** Four pictures of drinks (`SAKE_SEL`, `NIHONSYU`, `WINE`,
  `BABON` for bourbon) and an item strip: something is chosen from a
  table of bottles.
