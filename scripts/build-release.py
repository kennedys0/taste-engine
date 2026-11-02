#!/usr/bin/env python3
"""Build a versioned update ZIP suitable for scripts/update.sh; stdlib only."""
from pathlib import Path
import argparse
import re
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SKILL = (ROOT / 'taste-engine/SKILL.md').read_text(encoding='utf8')
match = re.search(r'(?m)^\s*version:\s*["\']?(\d+\.\d+\.\d+)', SKILL)
if not match:
    raise SystemExit('ERROR: taste-engine/SKILL.md has no semver')
version = match.group(1)

parser = argparse.ArgumentParser()
parser.add_argument('--verify-tag', help='Require release tag to match skill version')
args = parser.parse_args()
if args.verify_tag and args.verify_tag != 'v' + version:
    raise SystemExit(f'ERROR: tag {args.verify_tag!r} does not match v{version}')

distribution = [
    ROOT / 'README.md', ROOT / 'INSTALL.md', ROOT / 'CHANGELOG.md',
    ROOT / 'LICENSE', ROOT / 'update.sh',
]
for d in ['taste-engine', 'optional-standalone-skills']:
    distribution.extend(p for p in (ROOT / d).rglob('*') if p.is_file()
                        and '__pycache__' not in p.parts and p.suffix != '.pyc')
for p in distribution:
    if not p.is_file() or p.is_symlink():
        raise SystemExit(f'ERROR: missing or symlinked file {p}')

out_dir = ROOT / 'dist'
out_dir.mkdir(exist_ok=True)
zip_path = out_dir / f'taste-engine-v{version}.zip'
with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
    for p in sorted(distribution):
        rel = Path(f'taste-engine-v{version}') / p.relative_to(ROOT)
        archive.write(p, rel.as_posix())
with zipfile.ZipFile(zip_path) as z:
    if z.testzip() is not None:
        raise SystemExit('ERROR: ZIP test failed')
print(f'PASS: built {zip_path.relative_to(ROOT)} with {len(distribution)} files')
