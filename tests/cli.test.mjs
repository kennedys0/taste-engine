import test from 'node:test';
import assert from 'node:assert/strict';
import { spawnSync } from 'node:child_process';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const cli=path.join(root,'bin','taste-engine.mjs');
const pkg=JSON.parse(fs.readFileSync(path.join(root,'package.json'),'utf8'));
function run(args, env={}) { return spawnSync(process.execPath,[cli,...args],{encoding:'utf8',env:{...process.env,...env}}); }
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
test('forwards -update, update and --update to the updater script',()=>{
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
test('npm pack includes docs/index.html and CLI avoids shell interpolation',()=>{
 const pack=spawnSync('npm',['pack','--dry-run','--json'],{cwd:root,encoding:'utf8',shell:true});
 assert.equal(pack.status,0,pack.stderr);
 const data=JSON.parse(pack.stdout);
 const files=data[0].files.map(f=>f.path);
 assert.equal(files.includes('docs/index.html'),true);

 const cliContent=fs.readFileSync(cli,'utf8');
 assert.equal(cliContent.includes('exec('),false);
});
