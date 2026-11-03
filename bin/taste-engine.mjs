#!/usr/bin/env node
/** Taste Engine installer. Node.js 20+, no external dependencies. */
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const VERSION = '0.10.5';
const repoRoot = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const source = path.join(repoRoot, 'taste-engine');
const agents = {
  antigravity: { global: '.gemini/config/skills', project: '.agents/skills' },
  'antigravity-cli': { global: '.gemini/antigravity-cli/skills', project: '.agents/skills' },
  'claude-code': { global: '.claude/skills', project: '.claude/skills' },
  codex: { global: '.agents/skills', project: '.agents/skills' },
};
const alias = {
  agy: 'antigravity-cli', 'antigravity-ide': 'antigravity',
  claude: 'claude-code', 'claude_code': 'claude-code'
};
function help() {
  console.log(`Taste Engine ${VERSION}\n\nUsage:\n  taste-engine gallery                                                              Preview all 10 styles interactively in your browser\n  taste-engine install --agent <antigravity|antigravity-cli|claude-code|codex|all> [--global|--project] [--cwd DIR]\n  taste-engine doctor [--agent <name|all>] [--global|--project] [--cwd DIR]\n  taste-engine version\n  taste-engine help\n\nDefaults: project install; --agent all.\nFor GitHub-managed updates, use the installed scripts/update.sh (Antigravity)\nor npx skills update for installs managed by the skills CLI.\n`);
}
function parse(argv) {
  const options = { agent: 'all', scope: 'project', cwd: process.cwd() };
  for(let i = 0; i < argv.length; i++) {
    const val = argv[i];
    if(val === '--agent' || val === '-a') options.agent = argv[++i];
    else if(val === '--global' || val === '-g') options.scope = 'global';
    else if(val === '--project' || val === '-p') options.scope = 'project';
    else if(val === '--cwd') options.cwd = path.resolve(argv[++i]);
    else if(val === '--help' || val === '-h') options.help = true;
    else throw new Error(`Unknown option: ${val}`);
  }
  if(!options.agent) throw new Error('Missing --agent value');
  if(!options.cwd) throw new Error('Missing --cwd value');
  options.agent = alias[options.agent] || options.agent;
  if(options.agent !== 'all' && !(options.agent in agents)) {
    throw new Error(`Unknown agent: ${options.agent}`);
  }
  return options;
}
function targets(options) {
  const selected = options.agent === 'all' ? Object.keys(agents) : [options.agent];
  return [...new Set(selected.map(a => {
    const rel = agents[a][options.scope];
    return path.join(options.scope === 'global' ? os.homedir() : options.cwd, rel, 'taste-engine');
  }))];
}
function assertSource() {
  if(!fs.existsSync(path.join(source,'SKILL.md')) || !fs.existsSync(path.join(source,'styles','registry.json')))
    throw new Error('Skill source is missing. Install from the complete GitHub package.');
  const registry=JSON.parse(fs.readFileSync(path.join(source,'styles','registry.json'),'utf8'));
  for (const s of registry.styles) {
    if(!fs.existsSync(path.join(source,s.path))) throw new Error(`Missing style pack: ${s.path}`);
  }
}
function install(dest) {
  const parent=path.dirname(dest);
  fs.mkdirSync(parent,{recursive:true});
  const staging=fs.mkdtempSync(path.join(parent,'.taste-engine-stage-'));
  const staged=path.join(staging,'taste-engine');
  let backup;
  try {
    fs.cpSync(source,staged,{recursive:true,filter: p=> !p.includes('__pycache__') && !p.endsWith('.pyc')});
    assertSource();
    if(fs.existsSync(dest)) {
      // Never silently replace an unrelated directory.
      if(!fs.existsSync(path.join(dest,'SKILL.md')) || !fs.readFileSync(path.join(dest,'SKILL.md'),'utf8').includes('name: taste-engine'))
        throw new Error(`Existing folder is not a Taste Engine skill: ${dest}`);
      backup=`${dest}.backup-${new Date().toISOString().replace(/[:.]/g,'-')}`;
      fs.renameSync(dest,backup);
    }
    try { fs.renameSync(staged,dest); }
    catch(err) { if(backup && fs.existsSync(backup)) fs.renameSync(backup,dest); throw err; }
    console.log(`Installed ${dest}${backup ? `\nBackup: ${backup}`:''}`);
  } finally { fs.rmSync(staging,{recursive:true,force:true}); }
}
try {
  const [command='help', ...args]=process.argv.slice(2);
  if(command==='help' || command==='--help' || command==='-h') help();
  else if(command==='version' || command==='--version' || command==='-v') console.log(VERSION);
  else if(command==='gallery' || command==='preview') {
    const galleryPath = path.join(repoRoot, 'docs', 'index.html');
    if(!fs.existsSync(galleryPath)) throw new Error('Gallery not found at docs/index.html');
    console.log(`Taste Engine: opening interactive style gallery (${galleryPath})`);
    const openCmd = process.platform === 'win32' ? `start "" "${galleryPath}"` :
                    process.platform === 'darwin' ? `open "${galleryPath}"` : `xdg-open "${galleryPath}"`;
    import('node:child_process').then(cp => {
      cp.exec(openCmd, (err) => {
        if(err) console.log(`You can open the gallery manually in your browser:\n  file://${galleryPath}`);
      });
    });
  }
  else if(command==='install' || command==='doctor') {
    const o=parse(args);
    if(o.help) { help(); process.exit(0); }
    if(command==='install') assertSource();
    for(const dest of targets(o)) {
      if(command==='install') install(dest);
      else {
        const skill=path.join(dest,'SKILL.md');
        const ok=fs.existsSync(skill) && fs.readFileSync(skill,'utf8').includes('name: taste-engine');
        console.log(`${ok?'OK':'MISSING'} ${dest}`);
        if(!ok) process.exitCode=1;
      }
    }
  } else throw new Error(`Unknown command: ${command}`);
} catch(e) { console.error(`Taste Engine: ${e.message}`); process.exitCode=1; }
