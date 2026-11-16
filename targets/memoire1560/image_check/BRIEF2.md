# Follow-up: write out your page's corrected transcription

Your findings agree with those of the other pages: several ASCII codes each cover more than one manuscript sign.
New codes are now defined so that the transcription can carry the distinction. Please write the full corrected
transcription of YOUR page, from the image and your findings, as

`S/out/<PAGE>_fixed.txt`   (S = <scratch>)

## New codes (use them wherever you SAW the shape; shape decides, not the letter the reading wants)

| code | sign |
|---|---|
| `B` | barred / uncial delta: small loop with a long STRAIGHT bar or ascender going to the upper left (was `d`) |
| `G` | tall delta whose ascender CURLS or loops over to the right at the top, or the tall narrow S-shaped form (was `d`) |
| `j` | crossed delta: a loop whose ascender carries a small cross or X on top (was `d`, sometimes `J`, sometimes `D`) |
| `d` | keep ONLY for the plain hook ")" (as in the group f-e-hook) and for a `d` you could not classify |
| `X` | SHORT double-barred cross sitting on the line, no descender (was `D`) |
| `D` | keep for the TALL double dagger that descends below the line |
| `O` | x-head with a CLOSED loop or long curl below the line / x written over a z-like curl (was `x`, `y`, `3x`, `x3`) |
| `y` | keep for the x/r-headed sign with an OPEN tail or hook below the line |

If the code `S` on your page is really the `G` shape followed by a separate long s, write `Gs`. All other codes
stay as in SIGNS.md and the page's own comment lines.

## Rules

- One output line per packet line, in the same order, in the form `<label><TAB><cipher words>` (e.g.
  `153r.07<TAB>...`). Same number of lines as your packet. Keep struck-through groups in [ ] as they are.
- Start from the existing `cipher` line and change only what you saw: apply your T and M findings of high or medium
  confidence, and recode every d / D / tailed-x occurrence by its shape. Leave low-confidence and unclear places
  exactly as they were (for an unclassifiable `d`, leave `d`).
- Do not change a sign because the reading needs it. If you did not look at a word closely, leave it.
- Look again at the image where you need to; you may crop as before. Do not edit the repository.
- After writing the file, reply in under 120 words: number of lines written, number of words changed, how many
  `d` you recoded as B / G / j / left as d, how many D became X, how many O, and anything you were unsure of.
