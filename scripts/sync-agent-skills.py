#!/usr/bin/env python3
"""Verify canonical skills/taste-engine single source of truth and root update.sh sync."""
from pathlib import Path
import argparse
import shutil

ROOT = Path(__file__).resolve().parents[1]
CANON = ROOT / 'skills' / 'taste-engine'
LEGACY_DUP = ROOT / 'taste-engine'
ROOT_SH = ROOT / 'update.sh'
CANON_SH = CANON / 'scripts' / 'update.sh'

parser = argparse.ArgumentParser()
parser.add_argument('--check', action='store_true')
args = parser.parse_args()

if not (CANON / 'SKILL.md').is_file():
    raise SystemExit('ERROR: canonical skills/taste-engine/SKILL.md is missing')

if args.check:
    if LEGACY_DUP.exists():
        raise SystemExit('ERROR: duplicate root taste-engine/ directory exists; use skills/taste-engine/ as single source of truth')
    if not ROOT_SH.is_file() or ROOT_SH.read_bytes() != CANON_SH.read_bytes():
        raise SystemExit('ERROR: root update.sh differs from canonical skills/taste-engine/scripts/update.sh')
    count = sum(1 for p in CANON.rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.suffix != '.pyc')
    print(f'PASS: skills/taste-engine single source verified ({count} files) and root update.sh byte-identical')
else:
    if LEGACY_DUP.exists():
        shutil.rmtree(LEGACY_DUP)
    shutil.copy2(CANON_SH, ROOT_SH)
    print('PASS: synchronized root update.sh from canonical skills/taste-engine')
