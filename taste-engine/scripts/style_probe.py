#!/usr/bin/env python3
"""Resolve explicit style aliases in a visual UI prompt using bundled registry.

Usage: python3 scripts/style_probe.py --prompt "build a skeumorphsm portfolio website"
Output JSON is a routing hint, not proof of agent skill activation. Designed for standard library only.
"""
import argparse
import json
import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NEGATIONS = {
    'no', 'not', 'without', 'avoid', 'exclude', 'jangan', 'tanpa', 'bukan', 'hindari', 'kecuali',
    'hate', 'dislike', 'benci',
    '_neg_dont_want_', '_neg_do_not_want_', '_neg_gak_mau_', '_neg_nggak_mau_', '_neg_ga_mau_', '_neg_tidak_mau_'
}


def normalize(value):
    value = unicodedata.normalize('NFKC', value).casefold()
    value = re.sub(r'([a-z])([A-Z])', r'\1 \2', value)  # other casing handled below
    return ' '.join(re.sub(r'[^a-z0-9]+', ' ', value).split())


def candidates(prompt, registry):
    # A space-separated normalization permits hyphen/case variation; input stays unmodified.
    # Split camel-case first, before casefold, so NeoBrutalism can match neo brutalism.
    prompt = re.sub(r'(?<=[a-z])(?=[A-Z])', ' ', prompt)
    prompt = unicodedata.normalize('NFKC', prompt).casefold()

    # Treat 'not only' and Indonesian equivalents as non-negating
    prompt = re.sub(r'\bnot\s+only\b', ' _not_only_ ', prompt)
    prompt = re.sub(r'\bbukan\s+hanya\b', ' _not_only_ ', prompt)
    prompt = re.sub(r'\btidak\s+hanya\b', ' _not_only_ ', prompt)
    prompt = re.sub(r'\bbukan\s+cuma\b', ' _not_only_ ', prompt)

    # Multi-word negation phrases
    prompt = re.sub(r"\bdo(?:n['’]?t| not)\s+want\b", ' _neg_dont_want_ ', prompt)
    prompt = re.sub(r'\b(gak|nggak|ga|tidak)\s+mau\b', ' _neg_tidak_mau_ ', prompt)

    # Clause boundaries: punctuation and conjunctions
    prompt = re.sub(r'[,;.:!?]+', ' _clause_boundary_ ', prompt)
    prompt = re.sub(r'\b(but|tapi|tetapi|namun|and|dan|melainkan)\b', ' _clause_boundary_ ', prompt)

    # Clean other symbols but preserve boundary and negation tokens
    prompt = re.sub(r'[^a-z0-9_]+', ' ', prompt)
    words = prompt.split()

    hits = []
    for style in registry['styles']:
        names = [style['id'], style['label']] + style.get('aliases', [])
        for raw in names:
            needle = normalize(raw)
            nwords = needle.split()
            if not nwords: continue
            for i in range(len(words) - len(nwords) + 1):
                if words[i:i+len(nwords)] != nwords: continue
                # Look for negation within the current clause before the style match
                before = []
                for k in range(i - 1, max(-1, i - 6), -1):
                    if words[k] == '_clause_boundary_':
                        break
                    before.append(words[k])
                negative = any(w in NEGATIONS for w in before)
                hits.append({'style':style['id'],'start':i,'end':i+len(nwords),'length':len(nwords),'negative':negative,'alias':raw})
    hits.sort(key=lambda h:(-h['length'], h['start']))
    used=set(); resolved=[]
    for hit in hits:
        inds=set(range(hit['start'],hit['end']))
        if inds & used: continue
        used.update(inds)
        resolved.append(hit)
    resolved.sort(key=lambda h:h['start'])
    positive=[]; excluded=[]
    for h in resolved:
        dest=excluded if h['negative'] else positive
        if h['style'] not in dest: dest.append(h['style'])
    positive=[p for p in positive if p not in excluded]
    return {'status':('ready' if len(positive)==1 else 'blend' if len(positive)>1 else 'needs-selection'), 'primary_style':positive[0] if positive else None,'secondary_styles':positive[1:],'excluded_styles':excluded,'style_matches':resolved}


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--prompt',required=True)
    args=parser.parse_args()
    registry=json.loads((ROOT/'styles'/'registry.json').read_text(encoding='utf-8'))
    print(json.dumps(candidates(args.prompt,registry),ensure_ascii=False,indent=2))

if __name__ == '__main__':
    main()
