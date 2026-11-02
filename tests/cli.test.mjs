import test from 'node:test';
import assert from 'node:assert/strict';
import { spawnSync } from 'node:child_process';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const cli=path.join(root,'bin','taste-engine.mjs');
function run(args, env={}) { return spawnSync(process.execPath,[cli,...args],{encoding:'utf8',env:{...process.env,...env}}); }
test('prints version and rejects unknown agents',()=>{
 assert.equal(run(['version']).stdout.trim(),'0.10.0');
 assert.notEqual(run(['install','--agent','unknown']).status,0);
});
test('installs project skill for Antigravity and Codex',()=>{
 const dir=fs.mkdtempSync(path.join(os.tmpdir(),'taste-cli-'));
 try {
  let r=run(['install','--agent','all','--cwd',dir]);
  assert.equal(r.status,0,r.stderr);
  for(const location of ['.agents/skills/taste-engine/SKILL.md','.claude/skills/taste-engine/SKILL.md'])
   assert.equal(fs.existsSync(path.join(dir,location)),true);
  r=run(['doctor','--agent','all','--cwd',dir]);assert.equal(r.status,0,r.stderr);
 } finally {fs.rmSync(dir,{recursive:true,force:true});}
});
test('global Antigravity IDE uses official location and backups previous installs',()=>{
 const home=fs.mkdtempSync(path.join(os.tmpdir(),'taste-home-'));
 try {
  let r=run(['install','--agent','antigravity','--global'],{HOME:home});
  assert.equal(r.status,0,r.stderr);
  let folder=path.join(home,'.gemini/config/skills/taste-engine');
  assert.equal(fs.existsSync(path.join(folder,'SKILL.md')),true);
  r=run(['install','--agent','antigravity','--global'],{HOME:home});
  assert.equal(r.status,0,r.stderr);
  assert.equal(fs.readdirSync(path.dirname(folder)).some(x=>x.startsWith('taste-engine.backup-')),true);
 } finally {fs.rmSync(home,{recursive:true,force:true});}
});
