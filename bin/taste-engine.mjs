#!/usr/bin/env node
/** Taste Engine installer. Node.js 20+, no external dependencies. */
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { spawnSync, spawn } from 'node:child_process';

const VERSION = '0.10.10';
const repoRoot = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const source = path.join(repoRoot, 'taste-engine');
const agents = {
  antigravity: { global: '.gemini/config/skills', project: '.agents/skills' },
  'antigravity-cli': { global: '.gemini/antigravity-cli/skills', project: '.agents/skills' },
  'claude-code': { global: '.claude/skills', project: '.claude/skills' },
  codex: { global: '.agents/skills', project: '.agents/skills' },
  cursor: { global: '.cursor/skills', project: '.cursor/skills' },
  cline: { global: '.cline/skills', project: '.cline/skills' },
  'roo-code': { global: '.roo/skills', project: '.roo/skills' },
  windsurf: { global: '.windsurf/skills', project: '.windsurf/skills' },
  copilot: { global: '.github/skills', project: '.github/skills' },
};
const alias = {
  agy: 'antigravity-cli', 'antigravity-ide': 'antigravity',
  claude: 'claude-code', 'claude_code': 'claude-code',
  'cursor-ai': 'cursor', cursoride: 'cursor',
  roo: 'roo-code', roocode: 'roo-code', 'roo-cline': 'roo-code',
  codeium: 'windsurf', 'codeium-windsurf': 'windsurf',
  'github-copilot': 'copilot', 'github_copilot': 'copilot',
};
function help() {
  console.log(`Taste Engine ${VERSION}\n\nUsage:\n  taste-engine -v | --version | version                             Check CLI version\n  taste-engine update [--agent <name|all>] [--global|--project]     Update skill to the latest release\n  taste-engine gallery | --gallery                                  Preview all 10 styles interactively in your browser\n  taste-engine preset | --preset                                    List available Tailwind CSS & shadcn/ui presets\n  taste-engine init | --init [dir] [--force] [--dry-run]              Scaffold Tailwind & shadcn presets into your project\n  taste-engine install --agent <name|all> [--global|--project] [--cwd DIR] [--dry-run]\n  taste-engine uninstall --agent <name|all> [--global|--project] [--cwd DIR] [--dry-run]\n  taste-engine doctor [--agent <name|all>] [--global|--project] [--cwd DIR]\n  taste-engine help\n\nSupported agents:\n  antigravity, antigravity-cli (agy), claude-code (claude), codex,\n  cursor, cline, roo-code (roo), windsurf, copilot, all\n\nDefaults: project install; --agent all.\nFor GitHub-managed updates, use taste-engine update or update.sh.\n`);
}
function parse(argv) {
  const options = { agent: 'all', scope: 'project', cwd: process.cwd(), dryRun: false };
  for(let i = 0; i < argv.length; i++) {
    const val = argv[i];
    if(val === '--agent' || val === '-a') {
      if(i + 1 >= argv.length || argv[i + 1].startsWith('-')) throw new Error('Missing --agent value');
      options.agent = argv[++i];
    }
    else if(val === '--global' || val === '-g') options.scope = 'global';
    else if(val === '--project' || val === '-p') options.scope = 'project';
    else if(val === '--cwd') {
      if(i + 1 >= argv.length || argv[i + 1].startsWith('-')) throw new Error('Missing --cwd value');
      options.cwd = path.resolve(argv[++i]);
    }
    else if(val === '--dry-run' || val === '-n') options.dryRun = true;
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
function assertSource(dir = source) {
  if(!fs.existsSync(path.join(dir,'SKILL.md')) || !fs.existsSync(path.join(dir,'styles','registry.json')))
    throw new Error('Skill source is missing. Install from the complete GitHub package.');
  const registry=JSON.parse(fs.readFileSync(path.join(dir,'styles','registry.json'),'utf8'));
  for (const s of registry.styles) {
    if(!fs.existsSync(path.join(dir,s.path))) throw new Error(`Missing style pack: ${s.path}`);
  }
}
function install(dest, dryRun = false) {
  if(dryRun) {
    console.log(`[dry-run] Would install ${dest}`);
    return;
  }
  const parent=path.dirname(dest);
  fs.mkdirSync(parent,{recursive:true});
  const staging=fs.mkdtempSync(path.join(parent,'.taste-engine-stage-'));
  const staged=path.join(staging,'taste-engine');
  let backup;
  try {
    fs.cpSync(source,staged,{recursive:true,filter: p=> !p.includes('__pycache__') && !p.endsWith('.pyc')});
    assertSource(staged);
    if(fs.existsSync(dest)) {
      // Never silently replace an unrelated directory.
      if(!fs.existsSync(path.join(dest,'SKILL.md')) || !fs.readFileSync(path.join(dest,'SKILL.md'),'utf8').includes('name: taste-engine'))
        throw new Error(`Existing folder is not a Taste Engine skill: ${dest}`);
      const backupDir = path.join(path.dirname(parent), '.taste-engine-backups');
      fs.mkdirSync(backupDir, { recursive: true });
      backup = path.join(backupDir, `taste-engine-${new Date().toISOString().replace(/[:.]/g, '-')}`);
      fs.renameSync(dest, backup);
    }
    try { fs.renameSync(staged,dest); }
    catch(err) { if(backup && fs.existsSync(backup)) fs.renameSync(backup,dest); throw err; }
    console.log(`Installed ${dest}${backup ? `\nBackup: ${backup}`:''}`);
  } finally { fs.rmSync(staging,{recursive:true,force:true}); }
}
function uninstall(dest, dryRun = false) {
  if(!fs.existsSync(dest)) {
    console.log(`NOT FOUND ${dest}`);
    return;
  }
  const skill = path.join(dest, 'SKILL.md');
  if(!fs.existsSync(skill) || !fs.readFileSync(skill, 'utf8').includes('name: taste-engine')) {
    throw new Error(`Existing folder is not a Taste Engine skill: ${dest}`);
  }
  if(dryRun) {
    console.log(`[dry-run] Would uninstall ${dest}`);
    return;
  }
  fs.rmSync(dest, { recursive: true, force: true });
  console.log(`Uninstalled ${dest}`);
}
function main() {
  const [command='help', ...args]=process.argv.slice(2);
  if(command==='help' || command==='--help' || command==='-h') { help(); return; }
  if(command==='version' || command==='--version' || command==='-v') { console.log(VERSION); return; }
  if(command==='update' || command==='-update' || command==='--update') {
    const updateScript = path.join(source, 'scripts', 'update.sh');
    if (!fs.existsSync(updateScript)) throw new Error(`Update script not found at ${updateScript}`);

    const targetArgv = [];
    const updaterArgs = [];
    let hasAgent = false;
    for(let i = 0; i < args.length; i++) {
      const a = args[i];
      if(a === '--agent' || a === '-a') {
        hasAgent = true;
        if(i + 1 >= args.length || args[i + 1].startsWith('-')) throw new Error('Missing --agent value');
        targetArgv.push('--agent', args[++i]);
      } else if(a === '--global' || a === '-g') {
        targetArgv.push('--global');
      } else if(a === '--project' || a === '-p') {
        targetArgv.push('--project');
      } else if(a === '--cwd') {
        if(i + 1 >= args.length || args[i + 1].startsWith('-')) throw new Error('Missing --cwd value');
        targetArgv.push('--cwd', args[++i]);
      } else {
        updaterArgs.push(a);
      }
    }

    const runUpdater = (targetPath, extraArgs) => {
      let bashCmd = 'bash';
      if(process.platform === 'win32') {
        const gitBash = 'C:\\Program Files\\Git\\bin\\bash.exe';
        if(fs.existsSync(gitBash)) bashCmd = gitBash;
      }
      const fullArgs = targetPath ? ['--target', targetPath, ...extraArgs] : extraArgs;
      const res = spawnSync(bashCmd, [updateScript, ...fullArgs], { stdio: 'inherit' });
      return res.status ?? 0;
    };

    if(hasAgent) {
      const o = parse(targetArgv);
      let targetList = targets(o);
      if(o.agent === 'all') {
        targetList = targetList.filter(t => fs.existsSync(t));
        if(targetList.length === 0) {
          console.log('No existing Taste Engine installations found to update.');
          return;
        }
      }
      for(const t of targetList) {
        console.log(`Updating target: ${t}`);
        const code = runUpdater(t, updaterArgs);
        if(code !== 0) process.exit(code);
      }
      return;
    }

    if(updaterArgs.includes('--help') || updaterArgs.includes('-h')) {
      const code = runUpdater(null, updaterArgs);
      process.exit(code);
    }
    const hasExplicitTarget = updaterArgs.includes('--target');
    const defaultTarget = hasExplicitTarget ? null : path.join(os.homedir(), agents.antigravity.global, 'taste-engine');
    if(!hasExplicitTarget) {
      console.log(`Updating target: ${defaultTarget}`);
    }
    const code = runUpdater(defaultTarget, updaterArgs);
    process.exit(code);
  }
  if(command==='gallery' || command==='preview' || command==='--gallery' || command==='--preview') {
    if(args.includes('--help') || args.includes('-h')) { help(); return; }
    const galleryPath = path.join(repoRoot, 'docs', 'index.html');
    if(!fs.existsSync(galleryPath)) throw new Error('Gallery not found at docs/index.html');
    console.log(`Taste Engine: opening interactive style gallery (${galleryPath})`);
    let child;
    if (process.platform === 'win32') {
      child = spawn('cmd', ['/c', 'start', '', galleryPath], { detached: true, stdio: 'ignore' });
    } else if (process.platform === 'darwin') {
      child = spawn('open', [galleryPath], { detached: true, stdio: 'ignore' });
    } else {
      child = spawn('xdg-open', [galleryPath], { detached: true, stdio: 'ignore' });
    }
    child.on('error', () => {
      console.log(`You can open the gallery manually in your browser:\n  file://${galleryPath}`);
    });
    child.unref();
    return;
  }
  if(command==='preset' || command==='presets' || command==='--preset' || command==='--presets') {
    if(args.includes('--help') || args.includes('-h')) { help(); return; }
    const presetDir = path.join(source, 'presets');
    console.log(`Taste Engine Presets (v${VERSION})\n\nAvailable presets in ${presetDir}:\n  - presets/tailwind/tailwind.preset.js (Tailwind CSS theme extension)\n  - presets/tailwind/taste-components.css (Component layers: .taste-clay-btn, etc.)\n  - presets/shadcn/shadcn-themes.css (shadcn/ui theme variable overrides)\n\nRun 'taste-engine init [dir]' to scaffold presets into your project.`);
    return;
  }
  if(command==='init' || command==='--init' || command==='-init') {
    let targetDir = process.cwd();
    let dryRun = false;
    let force = false;
    for(let i = 0; i < args.length; i++) {
      const a = args[i];
      if(a === '--help' || a === '-h') { help(); return; }
      if(a === '--dry-run' || a === '-n') dryRun = true;
      else if(a === '--force' || a === '-f') force = true;
      else if(a === '--cwd') {
        if(i + 1 >= args.length || args[i + 1].startsWith('-')) throw new Error('Missing --cwd value');
        targetDir = path.resolve(args[++i]);
      }
      else if(!a.startsWith('-')) targetDir = path.resolve(a);
      else throw new Error(`Unknown option: ${a}`);
    }
    const dest = path.join(targetDir, 'taste-presets');
    if(fs.existsSync(dest) && !force) {
      throw new Error(`Directory already exists: ${dest} (use --force to overwrite)`);
    }
    if(dryRun) {
      console.log(`[dry-run] Would scaffold Taste Engine presets to ${dest}`);
      return;
    }
    fs.mkdirSync(dest, { recursive: true });
    fs.cpSync(path.join(source, 'presets'), dest, { recursive: true });
    console.log(`Copied Taste Engine presets to ${dest}\nSee ${path.join(source, 'references', 'tailwind-shadcn.md')} for setup guide.`);
    return;
  }
  if(command==='install' || command==='doctor' || command==='uninstall') {
    const o=parse(args);
    if(o.help) { help(); return; }
    if(command==='install') assertSource();
    for(const dest of targets(o)) {
      if(command==='install') install(dest, o.dryRun);
      else if(command==='uninstall') uninstall(dest, o.dryRun);
      else {
        const skill=path.join(dest,'SKILL.md');
        const ok=fs.existsSync(skill) && fs.readFileSync(skill,'utf8').includes('name: taste-engine');
        if(ok) {
          const vMatch=fs.readFileSync(skill,'utf8').match(/version:\s*"?([^"\r\n]+)"?/);
          const vStr=vMatch?` (v${vMatch[1]})`:'';
          console.log(`OK ${dest}${vStr}`);
        } else {
          console.log(`MISSING ${dest}`);
          process.exitCode=1;
        }
      }
    }
    return;
  }
  throw new Error(`Unknown command: ${command}`);
}
const isMain = process.argv[1] && (() => {
  try {
    return fs.realpathSync(path.resolve(process.argv[1])) === fileURLToPath(import.meta.url);
  } catch {
    return false;
  }
})();
if (isMain) {
  try {
    main();
  } catch(e) { console.error(`Taste Engine: ${e.message}`); process.exitCode=1; }
}
