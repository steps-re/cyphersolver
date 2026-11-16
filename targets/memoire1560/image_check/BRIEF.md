# Brief: check one page of a 1560 cipher transcription against the manuscript image

You are checking one page of BnF fr. 3157 no. 67 (a ten-page report wholly in cipher, 12 Dec 1560). A transcription
of its signs into ASCII codes exists, a key exists, and a French reading exists. A published criticism showed that
the reading often departs from what the key gives. Your job is to find out, sign by sign on the image, WHY, for
your page. You are the check on earlier work, so do not trust the transcription and do not trust the reading.

## Do not

- Do not edit anything under /home/user/cyphersolver. Do not run any script from a `targets/` folder.
- Do not fetch anything from the network. Everything you need is local.
- Do not "see" a sign because the reading wants it. If the image is unclear, say unclear. A wrong "confirmed" is
  worse than an honest "unclear". Expect a fair share of unclear.

## Files (S = <scratch>)

- `S/pages/f<PAGE>.jpg`: the page, about 3400-3650 x 5870 px. `S/pages/f<PAGE>_small.jpg`: 1/4-size overview.
- `S/tools/crop.py`: `python3 -I S/tools/crop.py S/pages/f<PAGE>.jpg S/out/<PAGE>_tmp.jpg x0 y0 x1 y1 [scale]`
  crops a region in full-image pixels. Then view the crop with the Read tool. A good crop is 2-3 manuscript lines
  high (about 300-450 px) and half the page wide (about 1500 px); view left half and right half separately. Signs
  are small: do not judge from the overview.
- `S/packets/<PAGE>.txt`: for every manuscript line of your page: `cipher` (the transcription, words separated by
  spaces; text in [ ] is struck through in the manuscript), `key` (the key applied mechanically to it) and
  `reading` (the published reading; letters or words in [ ] are those the key does not give; [..] = unread).
- `/home/user/cyphersolver/targets/memoire1560/SIGNS.md`: what each ASCII code stands for, plus the comment lines
  at the top of `/home/user/cyphersolver/targets/memoire1560/transcription/<PAGE>.txt` for extra codes.
- `/home/user/cyphersolver/targets/memoire1560/key.txt`: sign -> letter. Two-character units (zo, pp, io, s3, ff,
  nn, lz, `:.`) are one letter each. Whole-word codes: Z = pour, 4 = roy, c+ / i+ / e+ = et, F / g = sieur.

The words in the manuscript are separated by a slanted stroke "/". Manuscript lines map one to one to packet
lines, in order, top to bottom (a heading in clear at the top of f.152r is not a packet line; paragraph gaps exist).
First find the y position of each line on the overview, then work through the page.

## Known traps (from the one passage already checked)

- `x` (the common x-shaped sign, = e) versus `r` (a smaller, rounder variant, = n) versus `y` (an x/r-headed sign
  with a LOOP or tail BELOW the line, = i). `y` was found transcribed as `r`.
- `z` (small z on the line) versus `3` (z with a long tail below the line). `3` was found transcribed as `z`.
  `3` seems to stand for s and, at word end, for x (deux, mieulx).
- `d` in the transcription covers at least two shapes: a delta (small loop with a curved ascender, read b or g) and
  a plain hook like ")" seen in the recurring group `fed` (tall crossed f, c-shape, hook; read "qu'ils"/"ils").
- `D` is the double-barred cross (read i, sometimes a); `+` is the small plain cross (a).

## What to do, for every line of your page

1. Look at the line on the image and compare it sign by sign with `cipher`.
2. For EVERY word whose `reading` has a bracket, and every word where `key` and `reading` plainly differ, decide:
   - `T` transcription slip: the image clearly shows a different sign from the one transcribed. Give the corrected
     cipher word. It counts whether or not the correction helps the reading. Say what you see.
   - `K` the image clearly matches the transcription; the key's letter is simply not the reading's letter
     (a sign with two values, a scribe's slip, or the reading is wrong).
   - `U` unclear at this resolution, or you cannot find the word.
   - `R` the reading itself looks wrong or unsupported: the signs give something else that makes sense. Say what.
3. Also report any other transcription slip you notice in words without brackets (class `T`), and any sign or word
   present on the image and missing from `cipher`, or the reverse (class `M`).
4. For EVERY occurrence of the code `d` on your page, record the shape you see: `delta` (loop with curved
   ascender), `hook` (a plain ")" stroke without a loop), `other: <describe>`, or `unclear`; and the letter the
   reading takes there. Same for every `z` (is it on the line, or does it have a tail below?), every `c`, and for
   `D` only where the reading takes a letter other than i.

## Output

Write `S/out/<PAGE>.tsv` (tab separated, UTF-8, one row per finding, header line first):

`line	word_no	cipher_word	class	corrected_cipher_word	reading_word	confidence	what_you_see`

- `line` as in the packet (e.g. 153r.07); `word_no` counts cipher words on the line from 1 (struck-through
  bracketed groups are not counted);
- `class` is T, K, U, R, M, or `S` for the shape rows of step 4 (for S rows put the sign and its position in the
  word in `what_you_see`, e.g. "d #2 in word: delta; reading takes g");
- `corrected_cipher_word` only for T and M; `confidence` high / medium / low.

Then reply with a short report (under 250 words): how many lines you covered, counts per class, the three most
important findings, and what you could not do. If you run short of time, cover fewer lines properly rather than
all lines badly, and say exactly which lines you covered.
