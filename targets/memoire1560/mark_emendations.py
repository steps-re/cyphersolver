"""Mark every place where the reading departs from the mechanical decrypt (16 Nov 2026).

The mechanical decrypt is key.txt applied to transcription/*.txt, sign by sign, with nothing edited. The reading
files had been bracketing only part of their departures from it. This script aligns each reading line with the
mechanical decrypt of the same manuscript line, letter by letter, and

  * writes decrypt_mechanical.txt   fol.line<TAB>the mechanical decrypt (word codes in capitals, ? = sign not in key);
  * rewrites the two reading files  every letter the key does not give is put in [ ]; a word mostly not given by
                                    the key is bracketed whole; brackets already present are kept;
  * writes emendations.tsv          one row per reading word that departs from the decrypt, and per dropped letter run;
  * writes emendations.json         the counts quoted in NOTES.md, profile.json and the page.

Not counted as a departure (the page states these conventions):
  u/v, i/j and i/y, which the key does not distinguish; accents and the cedilla; word division;
  the secondary value of a sign held to be polyphonic (POLY below). These are counted separately, per sign,
  because a "polyphonic" sign may also be two signs merged by the transcription: the counts show how often
  each value is used.

Usage: python mark_emendations.py            report only
       python mark_emendations.py --write    rewrite the files
       add --fresh after a transcription or key correction, so that brackets no longer needed are dropped
"""
import os, re, sys, json, unicodedata, collections

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import decrypt

FRESH = '--fresh' in sys.argv   # ignore the brackets already in the files: mark only what the alignment finds
READINGS = ['reading_152r-154r.txt', 'reading_154v-156v.txt']
# signs allowed a second value without a bracket (none since the image check)
POLY = {}   # until 16 Nov 2026: {'d': 'ubg', 'D': 'ia', 'c': 'la'}. The image check split d and D into separate signs; no second value is allowed now
# two short pieces read in the parallel pass and never entered in transcription/ (NOTES.md, "A parallel pass")
# editorial labels on those two lines: kept in front of the reading, not counted as words read
LABELS = {'153r.14m': '[margin] ', '157v.01': '[dorse, one cipher word] '}
EXTRA = {'153r.14m': '+mxppBWxm ?W+ fg+ppBsx hio f:.rmxiW', '157v.01': '+hioxSQDmmxppxrm'}


def fold(c):
    c = unicodedata.normalize('NFD', c.lower())[0]
    return {'v': 'u', 'j': 'i', 'y': 'i'}.get(c, c) if c.isalpha() else ''


def mech_line(cipher, key, units):
    """[(letter, sign)] for a cipher line, and its printable mechanical decrypt."""
    seq, words = [], []
    for w in re.sub(r'\[[^\]]*\]', ' ', cipher).replace('=', '').split():
        if '=' + w in key:
            v = key['=' + w]
            seq += [(fold(ch), '=' + w) for ch in v]
            words.append(v.upper())
            continue
        out, i = [], 0
        while i < len(w):
            for u in units:
                if w.startswith(u, i):
                    v = key[u]
                    if v != '-':
                        out.append(v); seq.append((fold(v), u))
                    i += len(u)
                    break
            else:
                out.append('?'); seq.append(('?', w[i])); i += 1
        words.append(''.join(out))
    return seq, ' '.join(words)


def align(a, b):
    """Global alignment of a = [(letter, sign)] with b = [letter]. Returns ops: (kind, i, j), kind in
    eq (same letter), poly (secondary value of a polyphonic sign), sub, ins (letter only in b), del (only in a)."""
    n, m = len(a), len(b)
    def sc(i, j):
        la, sg = a[i]
        if la == b[j]:
            return 2, 'eq'
        if sg in POLY and b[j] in ''.join(fold(x) for x in POLY[sg]):
            return 1.5, 'poly'
        return -1, 'sub'
    S = [[0.0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        S[i][0] = -i
    for j in range(1, m + 1):
        S[0][j] = -j
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            S[i][j] = max(S[i - 1][j - 1] + sc(i - 1, j - 1)[0], S[i - 1][j] - 1, S[i][j - 1] - 1)
    ops, i, j = [], n, m
    while i or j:
        if i and j and S[i][j] == S[i - 1][j - 1] + sc(i - 1, j - 1)[0]:
            ops.append((sc(i - 1, j - 1)[1], i - 1, j - 1)); i -= 1; j -= 1
        elif j and S[i][j] == S[i][j - 1] - 1:
            ops.append(('ins', None, j - 1)); j -= 1
        else:
            ops.append(('del', i - 1, None)); i -= 1
    return ops[::-1]


def strip_marks(text):
    """Reading text without its [ ] marks, the set of positions that were bracketed, and the spans of [..]."""
    out, was, holes, i, depth = [], set(), [], 0, 0
    while i < len(text):
        if text.startswith('[..]', i):
            holes.append(len(out)); out.append('\x00'); i += 4; continue
        if text[i] == '[':
            depth += 1
        elif text[i] == ']':
            depth = max(0, depth - 1)
        else:
            if depth:
                was.add(len(out))
            out.append(text[i])
        i += 1
    return ''.join(out), was, holes


def mark(text, flagged):
    """Put [ ] round flagged character positions; a word with half or more of its letters flagged, or a flagged
    word of one or two letters, is bracketed whole."""
    res, pos = [], 0
    for tok in re.split(r'(\s+)', text):
        span = range(pos, pos + len(tok)); pos += len(tok)
        if not tok.strip() or tok == '\x00':
            res.append('[..]' if tok == '\x00' else tok); continue
        letters = [k for k in span if text[k].isalpha()]
        fl = [k for k in letters if k in flagged]
        if not fl:
            res.append(tok); continue
        whole = len(fl) * 2 >= len(letters) or len(letters) <= 2
        lo, hi = letters[0], letters[-1]
        s = ''
        for k in span:
            ch = '[..]' if text[k] == '\x00' else text[k]
            inside = (lo <= k <= hi) if whole else (k in flagged)
            prev_in = k > span[0] and ((lo <= k - 1 <= hi) if whole else (k - 1 in flagged))
            # an apostrophe or hyphen between two flagged letters stays inside the bracket
            if not whole and not text[k].isalpha() and k - 1 in flagged and k + 1 in flagged and lo < k < hi:
                inside = True
            if not whole and k > span[0] and not text[k - 1].isalpha() and k - 2 in flagged and k in flagged and lo < k - 1 < hi:
                prev_in = True
            if inside and not prev_in:
                s += '['
            if not inside and prev_in:
                s += ']'
            s += ch
        last = span[-1]
        if (lo <= last <= hi) if whole else (last in flagged):
            s += ']'
        res.append(s)
    return ''.join(res)


def main(write):
    key = decrypt.load_key()
    units = sorted((k for k in key if not k.startswith('=')), key=len, reverse=True)
    cipher = {f'{fol}.{n:02d}': line for fol, n, line in decrypt.lines()}
    cipher.update(EXTRA)
    mech, mech_txt = {}, {}
    for k, c in cipher.items():
        mech[k], mech_txt[k] = mech_line(c, key, units)

    stats = collections.Counter()
    table = collections.defaultdict(collections.Counter)
    poly = collections.defaultdict(collections.Counter)
    rows, new_files = [], {}
    for fn in READINGS:
        out = []
        for line in open(os.path.join(HERE, fn), encoding='utf8').read().split('\n'):
            if '\t' not in line or line.startswith('#'):
                out.append(line); continue
            lab, text = line.split('\t', 1)
            prefix = LABELS.get(lab, '')
            if prefix:
                text = re.sub(r'^(?:\[[^\]]*\],?\s*)+', '', text)
            plain, was, holes = strip_marks(text)
            idx = [k for k, ch in enumerate(plain) if fold(ch)]
            b = [fold(plain[k]) for k in idx]
            a = mech.get(lab, [])
            flagged, dropped = (set() if FRESH else set(was)), []
            counted = lab not in EXTRA          # the margin and dorse lines are bracketed, not counted
            for kind, i, j in align(a, b):
                if kind in ('sub', 'ins'):
                    flagged.add(idx[j])
                elif kind == 'del':
                    dropped.append(i)
                if not counted:
                    continue
                if kind in ('eq', 'poly') and a[i][1] in POLY:
                    poly[a[i][1]][b[j]] += 1
                stats['letters ' + kind] += 1
                if i is not None:
                    table[a[i][1]][b[j] if j is not None else '-'] += 1
            marked = mark(plain, flagged)
            out.append(lab + '\t' + prefix + marked)
            # per-word rows
            for w_old, w_new in zip(plain.split(), marked.split()) if counted else []:
                if w_old == '\x00':
                    stats['words unread'] += 1; continue
                if not any(fold(ch) for ch in w_old):
                    continue
                stats['words'] += 1
                if '[' in w_new:
                    whole = w_new.lstrip('(«"').startswith('[') and w_new.rstrip('.,;:)»"').endswith(']') and w_new.count('[') == 1
                    stats['words marked'] += 1
                    stats['words bracketed whole' if whole else 'words with letters bracketed'] += 1
                    rows.append((lab, 'whole' if whole else 'letters', w_new, mech_txt.get(lab, '')))
            if dropped and not holes and counted:
                run = ''.join(a[i][0] for i in dropped)
                stats['letters dropped (lines without an unread word)'] += len(dropped)
                rows.append((lab, 'dropped', run, mech_txt.get(lab, '')))
        new_files[fn] = '\n'.join(out)

    result = {
        'date': '2026-11-16',
        'words': stats['words'], 'words_unread': stats['words unread'],
        'words_marked': stats['words marked'], 'words_bracketed_whole': stats['words bracketed whole'],
        'words_with_letters_bracketed': stats['words with letters bracketed'],
        'words_as_key_gives': stats['words'] - stats['words marked'],
        'letters_same': stats['letters eq'], 'letters_polyphonic_secondary': stats['letters poly'],
        'letters_emended': stats['letters sub'], 'letters_supplied': stats['letters ins'],
        'letters_of_decrypt_not_in_reading': stats['letters del'],
        'polyphonic_signs': {s: dict(c.most_common()) for s, c in poly.items()},
        'sign_values': {s: {'key': key.get(s, '?'), 'n': sum(c.values()), 'read_as': dict(c.most_common())}
                        for s, c in sorted(table.items(), key=lambda x: -sum(x[1].values())) if not s.startswith('=')},
        'conventions': 'u/v, i/j, i/y, accents and word division are not departures; no second value of any sign is allowed',
    }
    print(json.dumps(result, indent=1, ensure_ascii=False))
    if write:
        for fn, t in new_files.items():
            open(os.path.join(HERE, fn), 'w', encoding='utf8', newline='\n').write(t)
        with open(os.path.join(HERE, 'decrypt_mechanical.txt'), 'w', encoding='utf8', newline='\n') as f:
            f.write('# Mechanical decrypt: key.txt applied to transcription/*.txt sign by sign, nothing edited (mark_emendations.py).\n'
                    '# Word codes in capitals; ? = a sign not in the key. Compare with reading_*.txt, where every departure is in [ ].\n')
            for k in sorted(mech_txt):
                f.write(f'{k}\t{mech_txt[k]}\n')
        with open(os.path.join(HERE, 'emendations.tsv'), 'w', encoding='utf8', newline='\n') as f:
            f.write('line\tkind\treading word (or dropped letters)\tmechanical decrypt of the line\n')
            for r in rows:
                f.write('\t'.join(r) + '\n')
        json.dump(result, open(os.path.join(HERE, 'emendations.json'), 'w', encoding='utf8'), indent=1, ensure_ascii=False)


if __name__ == '__main__':
    main('--write' in sys.argv)
