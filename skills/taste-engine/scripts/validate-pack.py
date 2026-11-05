#!/usr/bin/env python3
"""No-dependency pack validator. Usage: python3 scripts/validate-pack.py"""
from pathlib import Path
import json
import re
import sys

root = Path(__file__).resolve().parents[1]
registry = json.loads((root / 'styles' / 'registry.json').read_text(encoding='utf-8'))
required = ['## Typography and typewriting', '## Color direction', '## Layout and geometry',
            '## Surfaces, depth, texture', '## Component anatomy and interaction',
            '## Motion', '## Hero composition (full first viewport)', '## UI writing and microcopy', '## Style-specific quality gate', '## Anti-slop: style-specific', '## Optional Anime.js v4 recipe']
errors=[]
project_root = root.parent
# The distributed ZIP includes optional standalones; a normal installation only
# contains taste-engine/. Validate cross-copy parity when siblings are present.
standalone_bundle_present = (project_root / 'optional-standalone-skills').is_dir()
required_references = ['references/responsive-baseline.md', 'references/anti-slop.md','references/anti-slop-copywriting.md','references/anti-slop-audit.md','tests/anti-slop.md', 'references/decision-system.md', 'references/quality-tiers.md', 'references/redesign-preservation.md', 'references/browser-validation.md', 'references/writing-calibration.md', 'references/research-notes.md', 'tests/research-acceptance.md', 'references/seo.md', 'references/seo-implementation.md', 'tests/seo-routing.md', 'references/motion-engine.md', 'tests/motion-routing.md', 'references/hero-layout.md', 'tests/hero-layout.md', 'tests/test_hero_policy.py', 'styles/motion-profiles.json', 'examples/react/anime-v4-press.jsx', 'references/engineering-router.md', 'references/web-interface-quality.md', 'references/react-performance.md', 'references/react-composition.md', 'references/native-mobile.md', 'references/view-transitions.md', 'references/docs-writing.md', 'references/vercel-research.md', 'tests/engineering-routing.md', 'tests/glassmorphism-visual.md', 'examples/glassmorphism/frosted-surfaces.css', 'tests/claymorphism-visual.md', 'examples/claymorphism/sculpted-surfaces.css', 'examples/neo-brutalism/pop-surfaces.css', 'examples/skeuomorphism/tactile-controls.css', 'examples/retro-terminal/crt-console.css', 'examples/bento/modular-grid.css', 'examples/swiss-editorial/grid-typography.css', 'examples/brutalism/raw-surfaces.css', 'examples/minimalism/clean-surfaces.css', 'examples/enterprise/data-cockpit.css', 'references/tailwind-shadcn.md', 'presets/tailwind/tailwind.preset.js', 'presets/tailwind/taste-components.css', 'presets/shadcn/shadcn-themes.css']
for filename in required_references:
    if not (root / filename).is_file(): errors.append(f'missing anti-slop resource: {filename}')

# Ensure every auto-invocation asset exists and the registry aliases are well-formed.
for rel in ['references/auto-invocation.md', 'tests/auto-invocation.md', 'scripts/style_probe.py', 'tests/test_style_probe.py']:
    if not (root/rel).is_file(): errors.append(f'missing automatic invocation asset: {rel}')
assertion_tokens=['portfolio', 'skeumorphsm', 'without asking', 'no style', 'seo-only', 'public website']
for token in assertion_tokens:
    if token not in (root/'SKILL.md').read_text(encoding='utf-8').lower():
        errors.append(f'SKILL.md missing auto-discovery cue: {token}')
seen_aliases={}
for style in registry['styles']:
    for raw in [style['id']]+style.get('aliases', []):
        norm=' '.join(re.sub(r'[^a-z0-9]+', ' ', raw.casefold()).split())
        if not norm: errors.append(f'empty alias in {style["id"]}'); continue
        previous=seen_aliases.get(norm)
        if previous is not None and previous != style['id']:
            errors.append(f'alias collision {raw!r}: {previous} vs {style["id"]}')
        seen_aliases[norm]=style['id']

glass_style = (root / 'styles/glassmorphism.md').read_text(encoding='utf8')
for phrase in ['Glass material fidelity gate', 'backdrop-filter', 'Frosted light', 'Smoked dark', 'first viewport', 'Explicit background gradient exception', 'radial-gradient']:
    if phrase.lower() not in glass_style.lower():
        errors.append(f'glassmorphism missing visible material requirement: {phrase}')
css_source=(root/'examples/glassmorphism/frosted-surfaces.css').read_text(encoding='utf8')
for phrase in ['backdrop-filter', 'background:', 'prefers-reduced-transparency', '@supports not']:
    if phrase not in css_source:
        errors.append(f'glass recipe missing {phrase}')

clay_style = (root / 'styles/claymorphism.md').read_text(encoding='utf8')
for phrase in ['Clay material fidelity gate', 'dual inner shadow', 'first viewport', 'Explicit clay depth exception', 'inset', 'tactile']:
    if phrase.lower() not in clay_style.lower():
        errors.append(f'claymorphism missing visible sculpted material requirement: {phrase}')
clay_css_source = (root / 'examples/claymorphism/sculpted-surfaces.css').read_text(encoding='utf8')
for phrase in ['--taste-clay-inner-primary', '--taste-clay-inner-light', '--taste-clay-inner-well', 'inset', 'prefers-reduced-motion', ':focus-visible']:
    if phrase not in clay_css_source:
        errors.append(f'clay recipe missing {phrase}')
ids=set()
for style in registry.get('styles', []):
    id=style.get('id', '')
    if not re.fullmatch('[a-z][a-z0-9-]*', id) or id in ids:
        errors.append(f'invalid or duplicate style ID: {id!r}')
    ids.add(id)
    path=root / style.get('path', 'missing')
    if not path.is_relative_to(root / 'styles'):
        errors.append(f'path outside styles: {path}')
        continue
    if not path.is_file():
        errors.append(f'missing style file: {path}')
        continue
    text=path.read_text(encoding='utf-8')
    if '1.35rem' in text:
        errors.append(f'{id}: contains deprecated unscoped clamp string 1.35rem')
    if 'ui bengkak' in text.lower():
        errors.append(f'{id}: contains deprecated UI bengkak phrase')
    if 'responsive-baseline.md' not in text:
        errors.append(f'{id}: missing reference to responsive-baseline.md')
    for heading in required:
        if heading not in text:
            errors.append(f'{id}: missing {heading}')
    if f'**ID:** `{id}`' not in text:
        errors.append(f'{id}: inconsistent embedded style ID')
    standalone = project_root / 'optional-standalone-skills' / f'taste-style-{id}' / 'SKILL.md'
    if standalone_bundle_present and not standalone.is_file():
        errors.append(f'{id}: missing standalone skill')
    elif standalone_bundle_present:
        standtext=standalone.read_text(encoding='utf-8')
        if text.split('## Anti-slop: style-specific')[0].strip() not in standtext or ('## Anti-slop: style-specific' + text.split('## Anti-slop: style-specific')[1]).strip() not in standtext:
            errors.append(f'{id}: standalone style guidance is out of sync')
        for section in ['## Universal anti-slop gate (self-contained)', '## Anti-slop: style-specific', '## Quality tiers (standalone)']:
            if section not in standtext:
                errors.append(f'{id}: standalone missing {section}')
# Anime.js v4 is optional; motion guidance is cross-style and present in every pack.
try:
    motion = json.loads((root / 'styles/motion-profiles.json').read_text())['styles']
    if set(motion) != ids: errors.append('motion profile IDs do not match styles')
except Exception as exc:
    errors.append(f'invalid motion profiles: {exc}')
motion_stand = project_root/'optional-standalone-skills'/'taste-motion'
if standalone_bundle_present:
    for rel, src in [('references/motion-engine.md','references/motion-engine.md'), ('examples/react/anime-v4-press.jsx','examples/react/anime-v4-press.jsx')]:
        if not (motion_stand/rel).is_file() or (motion_stand/rel).read_bytes()!=(root/src).read_bytes():
            errors.append(f'motion standalone mismatch: {rel}')
    if not (motion_stand/'SKILL.md').is_file(): errors.append('missing standalone taste-motion skill')
# SEO stays a separate cross-style layer and optional standalone bundle.
for rel in ['scripts/seo_audit.py', 'tests/test_seo_audit.py']:
    if not (root/rel).is_file(): errors.append(f'missing SEO resource: {rel}')
seo_stand=project_root/'optional-standalone-skills'/'taste-seo'
if standalone_bundle_present:
    if not (seo_stand/'SKILL.md').is_file(): errors.append('missing optional standalone taste-seo')
    for rel in ['seo.md', 'seo-implementation.md']:
        file=seo_stand/'references'/rel
        source=root/'references'/rel
        if not file.is_file() or file.read_bytes()!=source.read_bytes():
            errors.append(f'SEO standalone reference mismatch: {rel}')
main=(root/'SKILL.md').read_text(encoding='utf-8')
if not main.startswith('---\n') or 'name: taste-engine' not in main:
    errors.append('root SKILL.md missing valid-looking YAML frontmatter')
fm_parts = main.split('---', 2)
if len(fm_parts) >= 3:
    fm_body = fm_parts[1].strip()
    if any(line.strip() == '' for line in fm_body.splitlines()):
        errors.append('SKILL.md frontmatter contains blank lines')
for md_path in [root / 'SKILL.md', project_root / 'README.md']:
    if md_path.is_file():
        md_text = md_path.read_text(encoding='utf-8')
        if re.search(r'(?m)^\s*\|[^\n]*\n[ \t]*\n\s*\|', md_text):
            errors.append(f'{md_path.name}: blank line between table rows')
for filename in required_references[:3]:
    if Path(filename).name not in main:
        errors.append(f'root SKILL.md lacks anti-slop reference: {filename}')
for id in ids:
    if f'styles/{id}.md' not in main:
        errors.append(f'root SKILL.md lacks {id} route')
for filename in ['assets/project-style.example.json', 'assets/project-style.schema.json',
                 'assets/taste-profile.schema.json', 'assets/taste-profile.example.json']:
    try:
        json.loads((root/filename).read_text(encoding='utf-8'))
    except Exception as exc:
        errors.append(f'invalid {filename}: {exc}')
if not (root/'scripts/update.sh').is_file(): errors.append('missing updater script: scripts/update.sh')
pkg_file = project_root / 'package.json'
if pkg_file.is_file():
    try:
        pkg_version = json.loads(pkg_file.read_text(encoding='utf-8')).get('version')
        skill_ver_match = re.search(r'(?m)^\s*version:\s*["\']?(\d+\.\d+\.\d+)', main)
        skill_version = skill_ver_match.group(1) if skill_ver_match else None
        if skill_version != pkg_version:
            errors.append(f'version mismatch: package.json ({pkg_version}) vs SKILL.md ({skill_version})')
        cli_file = project_root / 'bin' / 'taste-engine.mjs'
        if cli_file.is_file():
            cli_match = re.search(r"const\s+VERSION\s*=\s*['\"]([^'\"]+)['\"]", cli_file.read_text(encoding='utf-8'))
            cli_version = cli_match.group(1) if cli_match else None
            if cli_version != pkg_version:
                errors.append(f'version mismatch: package.json ({pkg_version}) vs CLI ({cli_version})')
    except Exception as exc:
        errors.append(f'failed checking version sync: {exc}')
if errors:
    for error in errors:
        print('FAIL', error)
    sys.exit(1)
print(f'PASS: {len(ids)} style packs + engineering router + full-screen hero + SEO + optional Anime.js v4 motion, anti-slop, synced standalone skills, routes and JSON valid.')
