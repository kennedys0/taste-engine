#!/usr/bin/env python3
"""Build a versioned update ZIP suitable for scripts/update.sh; stdlib only."""
from pathlib import Path
import argparse
import re
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / 'skills' / 'taste-engine'
SKILL = (SKILL_DIR / 'SKILL.md').read_text(encoding='utf8')
match = re.search(r'(?m)^\s*version:\s*["\']?(\d+\.\d+\.\d+)', SKILL)
if not match:
    raise SystemExit('ERROR: skills/taste-engine/SKILL.md has no semver')
version = match.group(1)

parser = argparse.ArgumentParser()
parser.add_argument('--verify-tag', help='Require release tag to match skill version')
args = parser.parse_args()
if args.verify_tag and args.verify_tag != 'v' + version:
    raise SystemExit(f'ERROR: tag {args.verify_tag!r} does not match v{version}')

distribution = []
for p in [ROOT / 'README.md', ROOT / 'INSTALL.md', ROOT / 'CHANGELOG.md', ROOT / 'LICENSE', ROOT / 'update.sh']:
    distribution.append((p, p.relative_to(ROOT)))

for p in SKILL_DIR.rglob('*'):
    if p.is_file() and '__pycache__' not in p.parts and p.suffix != '.pyc':
        distribution.append((p, Path('taste-engine') / p.relative_to(SKILL_DIR)))

for p in (ROOT / 'optional-standalone-skills').rglob('*'):
    if p.is_file() and '__pycache__' not in p.parts and p.suffix != '.pyc':
        distribution.append((p, p.relative_to(ROOT)))

for src_path, _ in distribution:
    if not src_path.is_file() or src_path.is_symlink():
        raise SystemExit(f'ERROR: missing or symlinked file {src_path}')

out_dir = ROOT / 'dist'
out_dir.mkdir(exist_ok=True)
zip_path = out_dir / f'taste-engine-v{version}.zip'
with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
    for src_path, rel_dest in sorted(distribution, key=lambda item: item[1].as_posix()):
        rel = Path(f'taste-engine-v{version}') / rel_dest
        archive.write(src_path, rel.as_posix())
with zipfile.ZipFile(zip_path) as z:
    if z.testzip() is not None:
        raise SystemExit('ERROR: ZIP test failed')
print(f'PASS: built {zip_path.relative_to(ROOT)} with {len(distribution)} files')
