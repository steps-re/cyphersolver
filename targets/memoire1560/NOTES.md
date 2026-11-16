# Mémoire en chiffre du XIIe décembre 1560: BnF fr. 3157 no. 67

Status: read in part (16 Nov 2026: all ten pages re-checked against the images and the merged signs separated; 86.5% of the words read as sense with every departure from the mechanical decrypt bracketed, under the 95% bar; 99.4% of cipher words carry a reading; key broken here, ciphertext only, not checked outside the project)

Lasry review (25 Sept 2026): In private communications, Lasry wrote that he independently solved it in 2023 (improved Feb 2026) but his solution has not been published. Kept in the ciphertext-only list (outcome.first_break = 'unpublished prior').

Catalogue 276. BnF fr. 3157 ("Recueil de lettres et de pièces originales", Montmorency papers), item 67,
"Mémoire en chiffre du XIIe decembre 1560". Gallica btv1b90598645. Worked 22-23 Sept 2026.

**Result.** An anonymous report to the connétable de Montmorency ("vostre grandeur") from a Catholic
gentleman of the Agenais, a neighbour of the sieur de Fumel, dated 12 December 1560, a week after the death of
François II. It is entirely in cipher, ten pages, 1,715 cipher words. It had no decipherment and no known key.
The cipher was broken here from the ciphertext alone: a homophonic substitution with two-stroke units and four
code words. After the image check of 16 Nov 2026 (below) the transcription has 1,710 cipher words and the reading covers 1,699 of
them (99.4%); 11 scattered words are left unread. Of the 1,703 words read on the ten pages, 1,474 (86.6%) are exactly what the key
gives, with no sign allowed a second value, and 229 depart from it and are bracketed. (Before the image check: 1,347 of
1,709, with three signs allowed two values; before the audit, 108 emendations were marked.)

## Where it is

- The BnF notice (archivesetmanuscrits cc496207) puts each item's folio before the item number, so item 67 is
  ff. 152r-156v, not f. 158. f. 158 starts item 68, Marillac's clear despatch from England.
- Gallica views: f.152r = view 153 (right page); 152v/153r = view 154; 153v/154r = 155; 154v/155r = 156;
  155v/156r = 157; 156v = view 158 (left page). The dorse (view 159, left) has "henry second" in a later
  hand and a line of cipher signs.
- Heading on f.152r, in clear: "Du xiie decembre 1560". There is no address, no signature, and no decipherment
  in the item or on the neighbouring leaves. The Villars letters around it (items 65, 66, 69, 71, 72) are in
  clear and contain no key.

## The cipher

- **Script.** A cursive pseudo-script with the words divided by "/". Sign code: `SIGNS.md`, plus the extra codes
  defined in the comment lines of each `transcription/<fol>.txt`.
- **Homophonic.** e = x, ff; n = r (a smaller, rounder form of x: the main transcription trap); s = m, n, nn, 3;
  r = s, S, s3; i = i, D, y, e; u/v = zo, io, d; and so on.
- **Two-stroke units.** zo = u, pp = m, io = u, s3 = r, ff = e, :. = o, nn = s, lz = d.
- **Signs once taken as polyphonic.** Until 16 Nov 2026 these notes said δ (d) stood for u/v, b and g and ‡ (D) for i and
  sometimes a. The image check showed three delta signs (B = b, G = g, j = i) and two crosses (D = i, X = a): see
  "Image check of all ten pages". c is still read a and l, and 3 is s and word-final x.
- **Whole-word codes.** Z = pour (also used as the syllable, "y pourvoient"); 4 = roy; c+, i+, e+ = et;
  F, g = sieur. There are no name codes: every person and place is spelt out.
- **Key.** `key.txt`, read by `decrypt.py`; the mechanical decrypt is in `decrypt_lines.txt`.

## How it was broken

1. **Access.** Located the item: the catalogue gave f. 158, but the cipher is on ff. 152r-156v. Fetched the ten
   pages at full resolution from Gallica IIIF (`fetch_pages.py`) and cut them into half-width 3-line bands
   (`half.py`).
2. **First transcription.** Three agents transcribed the pages into ASCII sign codes (`transcription/`). One of
   them was stopped by a tool block after three pages; a fresh agent did 153v-154r.
3. **Plain substitution fails.** One sign per letter, annealed with `solve.py` (fr-1530-despatches 5-gram,
   word spaces kept), gave gibberish (-4.2/char).
4. **The first units.** z is followed by o in 262 of 283 cases, so "zo" was taken as one unit. The most frequent
   4-sign word, "Tzox" (23 times), fitted "que"; "Wx", "Wxm" and "hx" fitted le, les and de. With these seeded,
   the annealer produced "les derniers advertissemens", "les affaires de pardeça", "presches" and "assemblées"
   (-3.5/char).
5. **More units from alignment.** Decrypted words were lined up against the French they had to be:
   - "xrQxrhio" = entendu: r = n (a separate sign from x) and io = u;
   - "Dio:is" = avoir;
   - "3shDx+is3xppxrQ" = ordinairement: s3 = r;
   - "nn:WW:iQ" = souloit: nn = s;
   - later, "lzDm+xm" = disans: lz = d.
6. **The codes.** Short standalone groups were read from their context: "temps Z avoir secours" (Z = pour),
   "que le 4 et vostre grandeur" (4 = roy), and "c+" wherever "et" is required.
7. **Correction pass.** With the key known, four agents re-checked every line against the images, pages split
   152r / 152v-153r / 153v-154r / 154v-156v. Each changed a sign only where the image supports it
   (`transcription/corrections_<fol>.tsv`). They made about 300 x→r fixes, restored missing signs, fixed
   minim counts, and identified the looped sign y (= i). Where the image matches the transcription but not the
   key, they left it as written (scribe slips and polyphony, listed in the tsv files).
8. **Reading.** Read line by line: `reading_152r-154r.txt` and `reading_154v-156v.txt`. Emendations are in
   [ ], unread words are [..].

## A parallel pass

While this session worked, another session copied this folder part-way through the correction pass and published an "editorial reconstruction" of the same item (main commit 13e0f27b2: 97.7% by sign units, key called partial; files READING.md, VERIFY.md, coverage.*, reading_working.tsv, alignment_draft.json). It read two things this session had not transcribed, both confirmed against key.txt: the margin at 153r.14, `+mmxppdWxm Wx+ fg+ppdS3x io f:xrmx:W` = "assemblez en la chambre du conseil", and the dorse line = "Advertissemens". Both are added to `reading_152r-154r.txt`. Its files are kept for its image checks. Where they differ, the reading files here supersede them: the key is recovered (all ten pages corrected against the images, including 152v and 153r, which the parallel pass had not corrected) and the reading covers 98.9% of cipher words.

## Content

**Who wrote it.** The writer is a Catholic gentleman of the Agenais, a neighbour of the sieur de Fumel ("monsieur
de Fumel qu'est mon prochain voisin"). He is not Blaise de Monluc: he names "le sieur de Montluc" in the third
person, and Monluc's brother Lioux as an adversary. He corresponds with "le chief" and fears for his life. The
name is not in the text. "Le chief" is Antoine de Bourbon, king of Navarre, governor of Guyenne, residing "en sa
ville de Nérac".

**What it reports, in order:**
- Since his last advertisements, things have gone "de mal en pis": two preachers now where the towns used to have
  one. Madame de Castelpers and mademoiselle de Boesse, wife of captain Montseignac, attend the preaching with a
  great following.
- The rebels, hearing that the king was sending the sieur de Termes with companies, got some seigneurs to write to
  the king that everyone here lives in obedience. They only want time to raise troops and to wait for foreign
  help.
- An assembly at Clairac, in Agenois, of about 2,000 rebels resolved to resist any royal force, "disans qu'ils
  aiment mieulx mourir les armes en main que si le roy les faisoit executer par ung bourreau". Many great
  seigneurs and nobles have secret understanding "avecques ceste canaille".
- The seigneur de Caumont's brother is abbé of Clairac, and the Caumont places all have ministers.
- Reclus, judge of the Caumont lands, and Boissonade, syndic of the Agenois, were elected by the favour of
  Caumont and the chief to carry the tiers état's doléances to court: this is the États généraux of Orléans. The
  juge mage and magistrates of the présidial of Agen decided that they should hide the truth. The juge mage has
  gone to court to keep them quiet.
- Monsieur de Biron assembled 500 soldiers, mostly arquebusiers, to take the castle of Bergerac on the king's
  order, then sent them home after talking to the inhabitants. He did the same at Villeneuve and Montflanquin.
  Biron is allied to Mesmi, a principal rebel captain.
- The rebel captains (Mesmi, La Caze, Jehan de Mesmes, La Borde de Villeneuve, Chaulmont) stay at Nérac. The king
  should order the chief, who claims to be innocent of the conspiracy (Amboise), to hand them over.
- Monsieur de Lioux, brother of the sieur de Montluc, is going to court, and he and the chief's company threaten
  anyone who speaks against the chief.
- The rebels spread the rumour that Termes's companies have been countermanded. The writer dares not leave his
  house except at night and asks to withdraw to court.
- The rebels circulate a tract "qu'ils intitulent l'edict faict par Dieu le pere", and he sends a copy. He also
  encloses a letter from a bourgeois of Agen.
- The rebels count on "ung prince", on foreigners "du costé de Genève" and on the Swiss cantons, to whom they
  would hand two strong frontier towns of Guyenne.
- Fumel, back from court, threatens him. A packet sent through Fumel, with a letter from the chief, may not have
  arrived. He encloses a letter from the garde des sceaux of the présidial of Cahors.

## Prior work

- **Searches.** Checked 22 Sept 2026: no DECODE record, not on Tomokiyo's or Lasry's (GL.htm) lists. Web searches
  for the names and places found no edition or decipherment.
- **Brunet.** Serge Brunet, "Clairac et le début des guerres de Religion (1560-1562)" (in *Clairac et la Réforme*,
  2019) could not be opened (academia.edu 403). It may use the Montmorency papers but cannot have read this cipher
  unless deciphered elsewhere.
- **Keys tried.** The brief asked for Lasry's Henri II and Charles IX tables (GL.htm) to be tried first. They are
  images of different symbol sets, and this script matches none of them, so the key was rebuilt from the
  ciphertext instead.

## Verification 3, 23 Oct 2026

The v3 sweep flagged this reading at 0.21 on the explicit-hole measure. It scored `reading_154v-156v.txt` alone, with
its `154v.01` line prefixes and `#` header as text. Both reading files cut to the text (`reading_152r-154r.txt`,
`reading_154v-156v.txt`) score **0.755 on explicit holes** (111 of 147 sentences; each half 0.76), 0.54 plain (1560
spelling the word list lacks), hole rate 0.073; the 108 bracketed emendations count as holes. The sentences hold.
Kept read (grade B); `outcome.texts[0]` now names the two files as its `reading`. It rests on the key broken here
and the images, with no contemporary decipherment or copy. `READING.md` is a normalised editorial version, not
the reading that is scored.

## Audit against the mechanical decrypt, 16 Nov 2026

C. Pierrot and C. Desenclos ("Des centaines de textes historiques « déchiffrés » par l'IA", The Conversation, 10 Nov
2026) printed the page's reveal of f. 152v lines 9-14 with the letters circled where the key's letter is not the
letter of the reading, "errors not mentioned as such". They are right for this passage: the page said that every
such word was bracketed, and two of about twelve were.

`mark_emendations.py` now aligns each reading line with `key.txt` applied to the transcription, letter by letter.
Not counted as a departure: u/v, i/j, i/y, accents, word division. Second values of the signs held to be
polyphonic (d, D, c) are counted apart. Counts, in `emendations.json`:

- 1,709 words read, 15 unread. 1,347 words are exactly as the key gives them; 362 depart from it: 118 are bracketed
  whole and 244 have one or more letters bracketed. `emendations.tsv` lists each one with the decrypt of its line.
- Letters: 7,652 as the key gives them, 224 by the second value of a polyphonic sign, 331 emended, 163 supplied;
  236 letters of the decrypt are not taken up by the reading.
- The common signs are stable. 22 signs, 87% of the sign occurrences, give one letter in 90% or more of their uses
  (x = e 1,332 of 1,451; + = a 507 of 523; r = n 499 of 519; zo = u 497 of 517; m = s 502 of 515; Q = t 502 of 512).
- A few signs are not. d (key.txt: u) is read g 99, b 66, i 32, s 10 and u 5 times of 227; D is i 147, a 49;
  3 is s 46, x 18, and dropped 17 times of 94; z (key.txt: u) is read x 5, n 5 and u once, of 18; c is a 10, l 8. `key.txt`
  is left as it was, so it does not reproduce the reading for these signs. `VERIFY.md` had already said that the
  transcription may merge looped signs (b/g/u), crosses (a/i) and e/n shapes; that is not settled. Each needs the
  images again.
- The group `fed`, read "qu'ils" or "ils" (the hero line of the page among them), decrypts as "ciu". It is a
  reading from context, now bracketed whole wherever it occurs.

**The passage in the article's figure, on the image** (f. 152v lines 9-14, full-resolution crop from
openapi.bnf.fr, 16 Nov 2026). Of the departures circled there:

- two are transcription slips, and the reading was right: in "aiment" (line 12) the second sign has a loop below
  the line, so it is y (= i), not r; in "executer" (line 14) the second sign is the z with a long tail, 3, not z.
  Both are corrected in `transcription/152v.txt` (`corrections_152v.tsv`). 3 stands for x there, as it does at the
  end of "deux" and "mieulx".
- δ is the same sign, as far as the image shows, in "rebelles", "bourreau" (b) and "ung" (g): one sign, two letters.
- ‡ in "armes" (a) is the sign of "main" and "mil" (i): one sign, two letters.
- `fed` (lines 11 and 12, "qu'ils") is a tall crossed f, a c-shape and a hook. The hook is not the δ of "rebelles",
  so the transcription's d covers at least two shapes. The group is the same both times and is read from context.
- "envoyoit" (line 10), "disans" (line 12) and "faisoit" (line 13) could not be settled at this resolution.

The other nine pages have not been checked in this way.

What changed: the two reading files carry every bracket; `decrypt_mechanical.txt` is the unedited decrypt and is the
profile's `decryption`; the reveal (`make_reveal.py`) marks each sign whose key letter the reading does not take.
With every bracket counted as a hole, v2_score gives hole rate 0.200 (80.0% of words read as sense; it was 0.073 with
108 marks) and 0.326 on explicit-hole sentences (45 of 138). The wording of the reading is unchanged.

What this does not show: that the reading is wrong. The sentences, names and places hold together, and the stable
signs carry most of the text. It shows that about one word in five rests on the reader as well as on the key, and
that no one outside the project has checked it. The statistical validation of 11 Oct 2026 is "weak" (the annealer on
the real text reaches -2.657 a letter against -2.264 for the reading; shuffled refit z 43). Lasry's unpublished
solution of 2023 is the independent check available; it has not been compared.

## Image check of all ten pages, 16 Nov 2026

Every line of the ten pages was compared with the full-resolution images (openapi.bnf.fr IIIF), one independent
checker per page (model subagents, each given the transcription, the key output and the reading, and told to change
a sign only where the image shows another sign; `image_check/BRIEF.md`). Their tables are `image_check/<fol>.tsv`
(912 rows). They classed 192 places as transcription slips, 175 as "image matches the transcription, the key's letter
is not the reading's", 47 as unclear, 49 as "the reading is wrong", and 27 as signs missing or extra. Each then wrote
out its page with new codes (`image_check/BRIEF2.md`). I checked the main claim myself on f. 156v lines 1-3 and on
f. 155v line 26, where "bourgeois" has the three delta forms in one word.

**The first transcription merged signs that the manuscript keeps apart.** All ten checkers found the same split:

- `d` was three signs: a barred delta (now `B`, read b 65 times of 76), a tall curled delta (`G`, g 107 of 115) and
  a crossed delta (`j`, i 29 of 31). `d` remains only for the hook of the group `fed` and a few unclassified
  deltas (19 uses).
- `D` was two signs: the tall double dagger (still `D`, i 142 of 146) and a short double-barred cross on the line
  (`X`, a 49 of 49).
- a sign for o, an x-head on a closed loop or curl, had been written `x`, `y`, `3x` or `x3` (now `O`, o 20 of 26).
  On ff. 153r, 154r and 154v the checkers could not tell it from the open-tailed `y`, and those pages keep `y`.
- `S` is in places the tall delta followed by a long s ("gr", written `Gs`): "grandeur" is spelt in full.
- many `x`/`r`/`y` and `z`/`3` slips of the kind found on f. 152v.

So δ and ‡ are not polyphonic, as these notes said until today: the "second values" were other signs. `SIGNS.md`
and `key.txt` carry the new codes; `transcription/*.txt` has the corrected lines (379 words changed; listed in
`corrections_<fol>.tsv`), and `mark_emendations.py` no longer allows any sign a second value.

**Effect, measured.** 28 signs, 92% of the sign occurrences, now give one letter in 90% or more of their uses. Words
exactly as the key gives them: 1,474 of 1,703 (86.6%), against 1,347 of 1,709 when d, D and c were allowed two
values. Letters: 7,994 as the key gives them, 225 emended, 127 supplied, 149 of the decrypt not taken up. v2_score with
every bracket a hole: hole rate 0.135 (86.5% of words read as sense), 0.568 on explicit-hole sentences (83 of 146).
For the passage of the article's figure (f. 152v lines 9-14) the key now gives "mil rebelles ou fust arreste et
conclut que si le roy enuoioit forrces de pardeca ciu se mectroiient en deffence disans ciu aiment mieuls mourir les
armes en main que si le roy les faosoit esecuter par ung borreau".

**The reading was wrong in places, and is corrected in 34 lines** where the checked signs give another word
(`reading_*.txt`; the translation follows in thirteen passages). Among them: "ont discoreu de mal en pis" (not
"couru"); "que ung chacun de pardeça vit soubz l'obeissance" (not "veu"); "menees qui se y briguent" (not
"trouvent"); "lesdicts de Caulmont n'ont seignurie, place ni chasteau ou ... n'y aient de ministres" (the sentence
was read without its negations); "qu'il a faict le semblable" ; "resident a present en sa ville de Nerac"; "le roy
pourra scavoir"; "ne s'y fierez, et aurez entendu leurs menees" (two unread words gone); "je ne faicts doubte qu'il
n'y aie quelque grand trouble" (not "ce se faict doubte"); "aiant lesdicts rebelles l'auctorité" (not "estant");
"compositions qu'ils siement et envoyent" (an unread word gone); "ainsin qu'ay peu descouvrir"; "y pourvoiez".
Period spellings the reading had modernised are restored (lectre, moustre, sismaticques, debvoir, auserois).

**What is still open after it.**

- 229 bracketed words remain. The largest groups: `3` is s 42 times and x 23 (word-final, "deux", "mieulx"); `c`
  is a 12 and l 8; `y` and `e` each give i about nine times in ten; minim counts (m, nn, i) could not be verified
  at this resolution; x/r remains hard to tell.
- Word groups read from context, with no value in the key: `fed` ("qu'ils"), `Bn` (before an infinitive; "de" in
  the reading, "faire" proposed by one checker), `bcx` ("il"), `Bc`, `Je`, `fa` ("je").
- 47 places the checkers called unclear, and their low-confidence proposals, were left as they were.
- The checkers were shown the reading. The brief told them to code by shape and to say "unclear", and they did
  recode against the reading in places (B is read d or i 7 times, G is read i 5 times), but this is not a blind
  transcription. A blind one, or Lasry's unpublished solution, is the independent check still missing.
- The statistical validation was rerun on 16 Nov 2026 on the corrected transcription (7,932 read tokens, 52 types): the reading scores -2.115 a letter (-2.264 before), random keys -5.300 (z 4.5), keys fitted to shuffled ciphertext -3.021 at best -3.008, and the annealer started from a random key on the real text reaches -2.129 (-2.657 before), close to the reading. Polyphony 0.024 (0.046 before). The tool's verdict stays "weak": the reading is 4.5 sd above random keys and the pass mark is 5. A solver that nearly finds the same key from a random start is the best
  evidence so far that the key is right; it says nothing about the 229 bracketed words.

## Remaining gaps

- 11 scattered words (of 1,710), each tried against the image and the key again on 16 Nov 2026, context not decisive: 152r.16, 152r.26 (two), 152v.06, 152v.26, 153r.31, 154v.03, 155r.29 (two), 155v.17, 155v.22 - blocker: no-key-material; each occurs once
- the word groups `fed`, `Bn`, `bcx`, `Bc`, `Je` and `fa`, read from context ("qu'ils", "de", "il", "je") - blocker: no-key-material; they are whole-word signs with no value in any key, a few occurrences each, and no second document in this cipher is known
- the o-sign against the open-tailed y on ff. 153r, 154r and 154v, and minim counts throughout - blocker: illegible; not separable at the resolution of the Gallica images
- the writer's name - blocker: no-key-material; not in the text, no signature or address

## Escalation

- [x] siblings: leaves ff. 147-163 opened; Villars letters in clear, dorse f.157v has only a cipher line and "henry second"
- [x] clear-pages: no decipherment in the item or next to it; f.158 is item 68 (Marillac), not a decipherment
- [x] known-keys: Lasry GL.htm Henri II/Charles IX tables checked, different symbol sets
- [x] print: web search for the names/places, Brunet 2019 (not reachable); nothing printed of this text found
- [x] key-rebuild: homophonic key rebuilt by seeded annealing and word alignment; units zo, pp, io, s3, ff, nn, lz, :. found
- [x] retry: all unread words re-run with the final key after the image correction pass; 3 more resolved (ainsi, ainsin, ayants). 16 Nov 2026: all ten pages re-checked against the images, merged signs separated, 34 lines of the reading corrected, 4 more unread words resolved
