#!/usr/bin/env python3
"""Build / verify skills/taste-engine for skills.sh discovery.

The canonical skill is taste-engine/. The skills/ copy is deterministic and
necessary for tools that only discover the standard skills/ folder.
"""
from pathlib import Path
import argparse
import filecmp
import shutil
ROOT=Path(__file__).resolve().parents[1]
SRC=ROOT/'taste-engine'
DST=ROOT/'skills'/'taste-engine'
IGNORE=shutil.ignore_patterns('__pycache__','*.pyc')
parser=argparse.ArgumentParser()
parser.add_argument('--check',action='store_true')
args=parser.parse_args()

def files(root):
 return {p.relative_to(root).as_posix():p.read_bytes() for p in root.rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.suffix!='.pyc'}
if args.check:
 s,d=files(SRC),files(DST)
 if s!=d:
  delta=sorted({*s,*d}- {p for p in s.keys() & d.keys() if s[p]==d[p]})
  raise SystemExit('ERROR: skills/ mirror differs from canonical skill: '+', '.join(delta[:10]))
 root_sh=ROOT/'update.sh'
 canon_sh=SRC/'scripts'/'update.sh'
 if not root_sh.is_file() or root_sh.read_bytes()!=canon_sh.read_bytes():
  raise SystemExit('ERROR: root update.sh differs from canonical taste-engine/scripts/update.sh')
 print(f'PASS: skills/taste-engine mirror synchronized ({len(s)} files) and update.sh byte-identical')
else:
 if DST.exists(): shutil.rmtree(DST)
 shutil.copytree(SRC,DST,ignore=IGNORE)
 shutil.copy2(SRC/'scripts'/'update.sh', ROOT/'update.sh')
 print('PASS: synchronized skills/taste-engine and root update.sh')
