"""Build docs/reveal/memoire1560.json: ff. 152v.09-14 (the Clairac assembly), decoded sign by sign with key.txt.

A sign whose key letter the reading (reading_152r-154r.txt) does not take is marked 'unc' (mark_emendations.py).
"""
import os, re, json, sys, unicodedata, difflib
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import decrypt

LINES = [f'152v.{n:02d}' for n in range(9, 15)]


def plain(s):
    s = unicodedata.normalize('NFD', s.lower())
    s = ''.join(c for c in s if unicodedata.category(c) != 'Mn')
    return re.sub(r'[^a-z]', '', s).replace('j', 'i').replace('v', 'u')


import mark_emendations as M

key = decrypt.load_key()
units = sorted((k for k in key if not k.startswith('=')), key=len, reverse=True)
reading = {}
for l in open(os.path.join(HERE, 'reading_152r-154r.txt'), encoding='utf8'):
    if '\t' in l and not l.startswith('#'):
        k, t = l.rstrip('\n').split('\t')
        reading[k] = t
cipher = {f'{fol}.{n:02d}': line for fol, n, line in decrypt.lines()}

# Each tile shows the letter key.txt gives. A tile is 'unc' where the reading does not take that letter
# (second value of a polyphonic sign, or an emendation), found by the letter alignment of mark_emendations.py.
tokens = []
for ln in LINES:
    line_toks, a = [], []
    for w in re.sub(r'\[[^\]]*\]', ' ', cipher[ln]).split():
        if '=' + w in key:
            t = {'g': w, 'p': key['=' + w], 'cls': 'code'}
            line_toks.append(t); a += [(M.fold(ch), '=' + w, t) for ch in key['=' + w]]
        else:
            i = 0
            while i < len(w):
                for u in units:
                    if w.startswith(u, i):
                        t = {'g': u, 'p': key[u]}
                        line_toks.append(t); a.append((M.fold(key[u]), u, t)); i += len(u)
                        break
                else:
                    line_toks.append({'g': w[i], 'p': '?', 'cls': 'unk'}); i += 1
        line_toks.append({'g': '', 'p': ' ', 'cls': 'plain'})
    plain_text = M.strip_marks(reading[ln])[0]
    b = [M.fold(c) for c in plain_text if M.fold(c)]
    for kind, i, j in M.align([(x[0], x[1]) for x in a], b):
        if i is not None and kind != 'eq' and a[i][2].get('cls') != 'code':
            a[i][2]['cls'] = 'unc'
    tokens += line_toks
    tokens.append({'g': '', 'p': ' / ', 'cls': 'plain'})

text = ' '.join(reading[ln] for ln in LINES)
out = {
    'slug': 'memoire1560',
    'anchor': 'reading',
    'title': 'Clairac, December 1560: two thousand rebels in arms',
    'caption': 'BnF fr. 3157 f. 152v, lines 9-14. Each tile shows the letter the key gives for the sign, with nothing '
               'edited. Amber tiles are where the published reading does not take that letter: a doubtful sign, '
               'a word sign read from context, or an emendation. The reading of these lines, with every '
               'departure in brackets: \u201c' + text + '\u201d. Each two-stroke unit (zo, pp, io, s3, lz) is one '
               'letter; Z, 4 and c+ are whole-word codes.',
    'unit': 'signs',
    'key_note': 'Homophonic key rebuilt ciphertext-only (targets/memoire1560/key.txt); amber marks each sign whose key letter the reading does not take.',
    'tokens': tokens,
}
json.dump(out, open(os.path.join(HERE, '..', '..', 'docs', 'reveal', 'memoire1560.json'), 'w', encoding='utf8'),
          indent=1, ensure_ascii=False)
print(len([t for t in tokens if t['g']]), 'groups;', sum(t.get('cls') == 'unc' for t in tokens), 'unc')
