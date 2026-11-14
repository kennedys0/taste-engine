import test from 'node:test';
import assert from 'node:assert/strict';
import { spawnSync } from 'node:child_process';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const cli=path.join(root,'bin','taste-engine.mjs');
const pkg=JSON.parse(fs.readFileSync(path.join(root,'package.json'),'utf8'));
function run(args, env={}) { return spawnSync(process.execPath,[cli,...args],{encoding:'utf8',env:{...process.env,...env}}); }
const presetsSource = path.join(root, 'skills', 'taste-engine', 'presets');
function listFilesRecursive(dir) {
  return fs.readdirSync(dir, { recursive: true })
    .filter(rel => fs.statSync(path.join(dir, rel)).isFile())
    .map(rel => rel.split(path.sep).join('/'))
    .sort();
}
function assertDirMatchesSource(dest) {
  const sourceFiles = listFilesRecursive(presetsSource);
  const destFiles = listFilesRecursive(dest);
  assert.deepEqual(destFiles, sourceFiles, `destination file set should match source presets exactly`);
  for (const rel of sourceFiles) {
    assert.equal(
      fs.readFileSync(path.join(dest, rel), 'utf8'),
      fs.readFileSync(path.join(presetsSource, rel), 'utf8'),
      `content mismatch for ${rel}`
    );
  }
}
test('prints version and rejects unknown agents',()=>{
 assert.equal(run(['version']).stdout.trim(),pkg.version);
 assert.equal(run(['-v']).stdout.trim(),pkg.version);
 assert.equal(run(['--version']).stdout.trim(),pkg.version);
 assert.notEqual(run(['install','--agent','unknown']).status,0);
 assert.notEqual(run(['install','--agent']).status,0);
 assert.notEqual(run(['install','--cwd']).status,0);
});
test('prints help on help, --help, -h, and subcommand help flags',()=>{
 const expected='Taste Engine '+pkg.version;
 for(const args of [
   [],
   ['help'],
   ['--help'],
   ['-h'],
   ['install','--help'],
   ['install','-h'],
   ['uninstall','--help'],
   ['doctor','--help'],
   ['init','--help'],
   ['init','-h'],
   ['preset','--help'],
   ['gallery','--help']
 ]) {
   const r=run(args);
   assert.equal(r.status,0,`Failed for args: ${args.join(' ')}: ${r.stderr}`);
   assert.equal(r.stdout.includes(expected),true,`Output missing header for: ${args.join(' ')}`);
   assert.equal(r.stdout.includes('Usage:'),true);
 }
});
test('installs and uninstalls project skill for Antigravity, Claude, Cursor, Cline, Roo, Windsurf, Copilot and Codex',()=>{
 const dir=fs.mkdtempSync(path.join(os.tmpdir(),'taste-cli-'));
 try {
  let dry=run(['install','--agent','cursor','--cwd',dir,'--dry-run']);
  assert.equal(dry.status,0,dry.stderr);
  assert.equal(fs.existsSync(path.join(dir,'.cursor/skills/taste-engine')),false);

  let r=run(['install','--agent','all','--cwd',dir]);
  assert.equal(r.status,0,r.stderr);
  for(const location of [
    '.agents/skills/taste-engine/SKILL.md',
    '.claude/skills/taste-engine/SKILL.md',
    '.cursor/skills/taste-engine/SKILL.md',
    '.cline/skills/taste-engine/SKILL.md',
    '.roo/skills/taste-engine/SKILL.md',
    '.windsurf/skills/taste-engine/SKILL.md',
    '.github/skills/taste-engine/SKILL.md'
  ])
   assert.equal(fs.existsSync(path.join(dir,location)),true);
  r=run(['doctor','--agent','all','--cwd',dir]);assert.equal(r.status,0,r.stderr);

  let uninstDry=run(['uninstall','--agent','cursor','--cwd',dir,'--dry-run']);
  assert.equal(uninstDry.status,0,uninstDry.stderr);
  assert.equal(fs.existsSync(path.join(dir,'.cursor/skills/taste-engine/SKILL.md')),true);

  let uninst=run(['uninstall','--agent','cursor','--cwd',dir]);
  assert.equal(uninst.status,0,uninst.stderr);
  assert.equal(fs.existsSync(path.join(dir,'.cursor/skills/taste-engine')),false);

  let docMissing=run(['doctor','--agent','cursor','--cwd',dir]);
  assert.notEqual(docMissing.status,0);
  assert.equal(docMissing.stdout.includes('MISSING'),true);
 } finally {fs.rmSync(dir,{recursive:true,force:true});}
});
test('refuses to overwrite or uninstall non-taste-engine folder',()=>{
 const dir=fs.mkdtempSync(path.join(os.tmpdir(),'taste-foreign-'));
 try {
  const alien=path.join(dir,'.cursor/skills/taste-engine');
  fs.mkdirSync(alien,{recursive:true});
  fs.writeFileSync(path.join(alien,'SKILL.md'),'name: foreign-skill');

  let r=run(['install','--agent','cursor','--cwd',dir]);
  assert.notEqual(r.status,0);
  assert.equal(r.stderr.includes('Existing folder is not a Taste Engine skill'),true);

  let u=run(['uninstall','--agent','cursor','--cwd',dir]);
  assert.notEqual(u.status,0);
  assert.equal(u.stderr.includes('Existing folder is not a Taste Engine skill'),true);
 } finally {fs.rmSync(dir,{recursive:true,force:true});}
});
test('global Antigravity IDE uses official location and backups previous installs',()=>{
 const home=fs.mkdtempSync(path.join(os.tmpdir(),'taste-home-'));
 try {
  let r=run(['install','--agent','antigravity','--global'],{HOME:home,USERPROFILE:home});
  assert.equal(r.status,0,r.stderr);
  let folder=path.join(home,'.gemini/config/skills/taste-engine');
  assert.equal(fs.existsSync(path.join(folder,'SKILL.md')),true);
  r=run(['install','--agent','antigravity','--global'],{HOME:home,USERPROFILE:home});
  assert.equal(r.status,0,r.stderr);
  const skillsDir=path.dirname(folder);
  assert.deepEqual(fs.readdirSync(skillsDir),['taste-engine']);
  const backupDir=path.join(path.dirname(skillsDir),'.taste-engine-backups');
  assert.equal(fs.existsSync(backupDir),true);
  assert.equal(fs.readdirSync(backupDir).some(x=>x.startsWith('taste-engine-')),true);
  let matching=0;
  for(const entry of fs.readdirSync(skillsDir)) {
    const skill=path.join(skillsDir,entry,'SKILL.md');
    if(fs.existsSync(skill) && fs.readFileSync(skill,'utf8').includes('name: taste-engine')) matching++;
  }
  assert.equal(matching,1);
 } finally {fs.rmSync(home,{recursive:true,force:true});}
});
test('prints presets list and inits presets into target folder with init and --init',()=>{
 const dir=fs.mkdtempSync(path.join(os.tmpdir(),'taste-preset-'));
 try {
  let r=run(['preset']);
  assert.equal(r.status,0,r.stderr);
  assert.equal(r.stdout.includes('tailwind.preset.js'),true);

  let rFlag=run(['--preset']);
  assert.equal(rFlag.status,0,rFlag.stderr);
  assert.equal(rFlag.stdout.includes('tailwind.preset.js'),true);

  let dry=run(['init',dir,'--dry-run']);
  assert.equal(dry.status,0,dry.stderr);
  assert.equal(fs.existsSync(path.join(dir,'taste-presets')),false);

  let initRes=run(['init',dir]);
  assert.equal(initRes.status,0,initRes.stderr);
  assert.equal(fs.existsSync(path.join(dir,'taste-presets','tailwind','tailwind.preset.js')),true);
  assert.equal(fs.existsSync(path.join(dir,'taste-presets','shadcn','shadcn-themes.css')),true);

  let initFail=run(['init',dir]);
  assert.notEqual(initFail.status,0);
  assert.equal(initFail.stderr.includes('already exists'),true);

  let initForce=run(['init',dir,'--force']);
  assert.equal(initForce.status,0,initForce.stderr);

  const subDir=path.join(dir,'sub');
  let initFlagRes=run(['--init',subDir]);
  assert.equal(initFlagRes.status,0,initFlagRes.stderr);
  assert.equal(fs.existsSync(path.join(subDir,'taste-presets','tailwind','tailwind.preset.js')),true);

  const cwdDir=path.join(dir,'cwd-test');
  let initCwdRes=run(['--init','--cwd',cwdDir]);
  assert.equal(initCwdRes.status,0,initCwdRes.stderr);
  assert.equal(fs.existsSync(path.join(cwdDir,'taste-presets','tailwind','tailwind.preset.js')),true);
 } finally {fs.rmSync(dir,{recursive:true,force:true});}
});
test('init --force removes stale files and exactly matches source presets', () => {
  const dir = fs.mkdtempSync(path.join(os.tmpdir(), 'taste-stale-'));
  try {
    // Scaffold presets initially so the destination exists.
    let initRes = run(['init', dir]);
    assert.equal(initRes.status, 0, initRes.stderr);
    assert.equal(fs.existsSync(path.join(dir, 'taste-presets', 'tailwind', 'tailwind.preset.js')), true);

    // Plant stale files that have no counterpart in the source presets.
    const staleTailwind = path.join(dir, 'taste-presets', 'tailwind', 'old-stale.css');
    fs.writeFileSync(staleTailwind, '/* stale tailwind file */');
    const staleShadcn = path.join(dir, 'taste-presets', 'shadcn', 'legacy-themes.css');
    fs.writeFileSync(staleShadcn, '/* stale shadcn file */');
    const staleDir = path.join(dir, 'taste-presets', 'legacy');
    fs.mkdirSync(staleDir, { recursive: true });
    fs.writeFileSync(path.join(staleDir, 'nested.css'), '/* stale nested file */');

    // Run init --force to overwrite the existing destination.
    let forceRes = run(['init', dir, '--force']);
    assert.equal(forceRes.status, 0, forceRes.stderr);

    // Assert stale files are removed (will FAIL on unfixed code — cpSync merges).
    assert.equal(fs.existsSync(staleTailwind), false,
      'stale tailwind/old-stale.css should be removed after init --force');
    assert.equal(fs.existsSync(staleShadcn), false,
      'stale shadcn/legacy-themes.css should be removed after init --force');
    assert.equal(fs.existsSync(staleDir), false,
      'stale legacy/ directory should be removed after init --force');

    // Assert destination recursively equals the source presets tree.
    assertDirMatchesSource(path.join(dir, 'taste-presets'));
  } finally { fs.rmSync(dir, { recursive: true, force: true }); }
});
// **Validates: Requirements 3.1, 3.2, 3.3, 3.4, 3.5**
test('init preservation: non-force, dry-run, fresh scaffolding, and custom targets unchanged', () => {
  const dir = fs.mkdtempSync(path.join(os.tmpdir(), 'taste-preserve-'));
  try {
    // --- 1. Non-force refusal preservation (Requirement 3.1) ---
    // Scaffold presets first, then try init again without --force → should error.
    let initRes = run(['init', dir]);
    assert.equal(initRes.status, 0, initRes.stderr);
    let refuseRes = run(['init', dir]);
    assert.notEqual(refuseRes.status, 0);
    assert.equal(refuseRes.stderr.includes('already exists'), true);

    // --- 2. Dry-run preservation (Requirement 3.3) ---
    // Dry-run when dest does not exist → dry-run message, no files created.
    const dryDest = path.join(dir, 'dry-dest');
    let dryFresh = run(['init', dryDest, '--dry-run']);
    assert.equal(dryFresh.status, 0, dryFresh.stderr);
    assert.equal(dryFresh.stdout.includes('[dry-run]'), true);
    assert.equal(fs.existsSync(path.join(dryDest, 'taste-presets')), false);

    // Dry-run when dest exists with --force → dry-run message, files unmodified.
    let dryForce = run(['init', dir, '--force', '--dry-run']);
    assert.equal(dryForce.status, 0, dryForce.stderr);
    assert.equal(dryForce.stdout.includes('[dry-run]'), true);
    assert.equal(fs.existsSync(path.join(dir, 'taste-presets', 'tailwind', 'tailwind.preset.js')), true);

    // Dry-run when dest exists WITHOUT --force → should error (destExists check precedes dryRun).
    let dryNoForce = run(['init', dir, '--dry-run']);
    assert.notEqual(dryNoForce.status, 0);
    assert.equal(dryNoForce.stderr.includes('already exists'), true);

    // --- 3. Fresh scaffolding preservation (Requirements 3.2, 3.4) ---
    // Fresh init without --force.
    const fresh1 = path.join(dir, 'fresh1');
    let fresh1Res = run(['init', fresh1]);
    assert.equal(fresh1Res.status, 0, fresh1Res.stderr);
    assert.equal(fs.existsSync(path.join(fresh1, 'taste-presets', 'tailwind', 'tailwind.preset.js')), true);
    assertDirMatchesSource(path.join(fresh1, 'taste-presets'));

    // Fresh init with --force (dest does not exist yet).
    const fresh2 = path.join(dir, 'fresh2');
    let fresh2Res = run(['init', fresh2, '--force']);
    assert.equal(fresh2Res.status, 0, fresh2Res.stderr);
    assert.equal(fs.existsSync(path.join(fresh2, 'taste-presets', 'tailwind', 'tailwind.preset.js')), true);
    assertDirMatchesSource(path.join(fresh2, 'taste-presets'));

    // --- 4. Custom target / --cwd preservation (Requirement 3.5) ---
    // Custom positional target.
    const subDir = path.join(dir, 'sub');
    let subRes = run(['init', subDir]);
    assert.equal(subRes.status, 0, subRes.stderr);
    assert.equal(fs.existsSync(path.join(subDir, 'taste-presets', 'tailwind', 'tailwind.preset.js')), true);
    assertDirMatchesSource(path.join(subDir, 'taste-presets'));

    // Custom --cwd target.
    const cwdDir = path.join(dir, 'cwd-test');
    let cwdRes = run(['init', '--cwd', cwdDir]);
    assert.equal(cwdRes.status, 0, cwdRes.stderr);
    assert.equal(fs.existsSync(path.join(cwdDir, 'taste-presets', 'tailwind', 'tailwind.preset.js')), true);
    assertDirMatchesSource(path.join(cwdDir, 'taste-presets'));
  } finally { fs.rmSync(dir, { recursive: true, force: true }); }
});
// **Validates: Requirements 3.1, 3.2, 3.3, 3.4, 3.5**
test('init preservation: generative test across non-buggy flag combinations', () => {
  const base = fs.mkdtempSync(path.join(os.tmpdir(), 'taste-gen-'));
  try {
    const forceOpts = [false, true];
    const dryRunOpts = [false, true];
    const destExistsOpts = [false, true];
    const targetModes = ['positional', '--cwd'];
    let comboIdx = 0;

    for (const force of forceOpts) {
      for (const dryRun of dryRunOpts) {
        for (const destExists of destExistsOpts) {
          for (const targetMode of targetModes) {
            // Skip bug condition: force=true, dryRun=false, destExists=true.
            if (force && !dryRun && destExists) continue;

            const targetDir = path.join(base, `combo-${comboIdx++}`);
            const dest = path.join(targetDir, 'taste-presets');

            // If destExists, scaffold presets first so the destination is present.
            if (destExists) {
              const scaffold = run(['init', targetDir]);
              assert.equal(scaffold.status, 0, `scaffold failed for combo ${comboIdx - 1}: ${scaffold.stderr}`);
            }

            // Build CLI args based on targetMode.
            const args = ['init'];
            if (targetMode === 'positional') {
              args.push(targetDir);
            } else {
              args.push('--cwd', targetDir);
            }
            if (force) args.push('--force');
            if (dryRun) args.push('--dry-run');

            const res = run(args);
            const label = `force=${force}, dryRun=${dryRun}, destExists=${destExists}, mode=${targetMode}`;

            if (destExists && !force) {
              // Non-force refusal: error with "already exists" regardless of dryRun.
              assert.notEqual(res.status, 0, `expected error for ${label}`);
              assert.equal(res.stderr.includes('already exists'), true, `stderr for ${label}: ${res.stderr}`);
            } else if (dryRun) {
              // Dry-run: success, dry-run message printed, no files created/modified.
              assert.equal(res.status, 0, `expected success for ${label}: ${res.stderr}`);
              assert.equal(res.stdout.includes('[dry-run]'), true, `stdout for ${label}: ${res.stdout}`);
              if (destExists) {
                assert.equal(fs.existsSync(path.join(dest, 'tailwind', 'tailwind.preset.js')), true,
                  `files should remain after dry-run for ${label}`);
              } else {
                assert.equal(fs.existsSync(dest), false,
                  `no files should be created after dry-run for ${label}`);
              }
            } else {
              // Fresh scaffolding: success, presets created, exact match to source.
              assert.equal(res.status, 0, `expected success for ${label}: ${res.stderr}`);
              assert.equal(fs.existsSync(path.join(dest, 'tailwind', 'tailwind.preset.js')), true,
                `presets should exist for ${label}`);
              assertDirMatchesSource(dest);
            }
          }
        }
      }
    }
  } finally { fs.rmSync(base, { recursive: true, force: true }); }
});
test('forwards -update, update and --update to the updater script',{skip:process.platform==='win32'},()=>{
 const r1=run(['-update','--help']);
 assert.equal(r1.status,0,r1.stderr);
 assert.equal(r1.stdout.includes('Taste Engine - safe updater'),true);

 const r2=run(['update','--help']);
 assert.equal(r2.status,0,r2.stderr);
 assert.equal(r2.stdout.includes('Taste Engine - safe updater'),true);

 const r3=run(['--update','--help']);
 assert.equal(r3.status,0,r3.stderr);
 assert.equal(r3.stdout.includes('Taste Engine - safe updater'),true);
});
test('update --agent claude-code --global targets .claude/skills/taste-engine',{skip:process.platform==='win32'},()=>{
 const home=fs.mkdtempSync(path.join(os.tmpdir(),'taste-update-home-'));
 try {
  const installRes=run(['install','--agent','claude-code','--global'],{HOME:home,USERPROFILE:home});
  assert.equal(installRes.status,0,installRes.stderr);
  const fixtureZip=path.join(root,'dist',`taste-engine-v${pkg.version}.zip`);
  if (!fs.existsSync(fixtureZip)) {
    const py = process.platform === 'win32' ? 'python' : 'python3';
    spawnSync(py, [path.join(root, 'scripts', 'build-release.py')], { stdio: 'ignore' });
  }
  const updateRes=run(['update','--agent','claude-code','--global','--zip',fixtureZip,'--dry-run'],{HOME:home,USERPROFILE:home});
  assert.equal(updateRes.status,0,updateRes.stderr);
  const output=updateRes.stdout+updateRes.stderr;
  assert.equal(output.includes('.claude/skills/taste-engine')||output.includes('.claude\\skills\\taste-engine'),true);
  assert.equal(output.includes('not installed'),false);
 } finally {fs.rmSync(home,{recursive:true,force:true});}
});
test('doctor output contains installed version',()=>{
 const home=fs.mkdtempSync(path.join(os.tmpdir(),'taste-doc-home-'));
 try {
  const installRes=run(['install','--agent','antigravity','--global'],{HOME:home,USERPROFILE:home});
  assert.equal(installRes.status,0,installRes.stderr);
  const docRes=run(['doctor','--agent','antigravity','--global'],{HOME:home,USERPROFILE:home});
  assert.equal(docRes.status,0,docRes.stderr);
  assert.equal(docRes.stdout.includes(`(v${pkg.version})`),true);
 } finally {fs.rmSync(home,{recursive:true,force:true});}
});
test('npm pack includes docs/index.html and CLI avoids shell interpolation',()=>{
 const pack=spawnSync('npm',['pack','--dry-run','--json'],{cwd:root,encoding:'utf8',shell:true});
 assert.equal(pack.status,0,pack.stderr);
 const data=JSON.parse(pack.stdout);
 const files=data[0].files.map(f=>f.path);
 assert.equal(files.includes('docs/index.html'),true);

 const cliContent=fs.readFileSync(cli,'utf8');
 assert.equal(cliContent.includes('exec('),false);
});
test('importing CLI produces no stdout and package exports no dot',()=>{
 const cliUrl=pathToFileURL(cli).href;
 const imp=spawnSync(process.execPath,['--input-type=module','-e',`import '${cliUrl}';`],{encoding:'utf8'});
 assert.equal(imp.status,0,imp.stderr);
 assert.equal(imp.stdout.trim(),'');
 assert.equal(pkg.exports['.'],undefined);
});
