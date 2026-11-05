#!/usr/bin/env python3
"""Updater smoke tests: isolated filesystem, no network, no user state touched."""
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
import shutil
import subprocess
import re
import tempfile

SKILL = Path(__file__).resolve().parents[1]
UPDATER = SKILL / "scripts/update.sh"
CURRENT_VERSION = re.search(r'version: "([0-9]+\.[0-9]+\.[0-9]+)"', (SKILL / "SKILL.md").read_text()).group(1)


def make_zip(path: Path, source: Path, tamper=None):
    with ZipFile(path, "w", ZIP_DEFLATED) as z:
        for p in source.rglob("*"):
            if p.is_file() and "__pycache__" not in p.parts:
                rel = Path("taste-engine") / p.relative_to(source)
                data = p.read_bytes()
                if tamper:
                    data = tamper(p, data)
                z.writestr(rel.as_posix(), data)


def run(*args, ok=True):
    print("RUN", list(map(str,args)), flush=True)
    p = subprocess.run(["bash", str(UPDATER), *map(str, args)], capture_output=True, text=True, timeout=15)
    if ok and p.returncode:
        raise AssertionError(f"Updater failed unexpectedly: {p.stdout}\n{p.stderr}")
    if not ok and not p.returncode:
        raise AssertionError(f"Updater incorrectly succeeded: {p.stdout}")
    return p


with tempfile.TemporaryDirectory(prefix="taste-engine-update-test-") as tmp:
    base = Path(tmp)
    target = base / "skills/taste-engine"
    target.parent.mkdir()
    shutil.copytree(SKILL, target)
    skill_file = target / "SKILL.md"
    skill_file.write_text(skill_file.read_text().replace(f'version: "{CURRENT_VERSION}"', 'version: "0.9.9"'))
    (target / "original-state.txt").write_text("preserve on failure")

    package = base / "update.zip"
    make_zip(package, SKILL)

    # Dry run must not replace files or create a backup.
    run("--zip", package, "--target", target, "--dry-run")
    assert "0.9.9" in skill_file.read_text()
    assert not (base / ".taste-engine-backups").exists()

    # Reject unverified downloads / broken or unsafe archives.
    run("--zip", package, "--sha256", "0" * 64, "--target", target, ok=False)
    unsafe = base / "unsafe.zip"
    with ZipFile(unsafe, "w") as z:
        z.writestr("../../outside.txt", "bad")
    run("--zip", unsafe, "--target", target, ok=False)
    assert "0.9.9" in skill_file.read_text()
    assert not (base / "outside.txt").exists()

    # Inject a validation failure that occurs only after installation.
    def break_installed(p, data):
        if p.relative_to(SKILL).as_posix() == "scripts/validate-pack.py":
            data += b'\nif root.name == "taste-engine" and root.parent.name == "skills":\n    sys.exit("intentionally failing installed-validator test")\n'
        return data

    corrupt = base / "post-install-failure.zip"
    make_zip(corrupt, SKILL, break_installed)
    run("--zip", corrupt, "--target", target, ok=False)
    assert "0.9.9" in skill_file.read_text(), "previous installation not rolled back"
    assert (target / "original-state.txt").read_text() == "preserve on failure"

    # Successful update, backup retained out of skill discovery path.
    run("--zip", package, "--target", target)
    assert CURRENT_VERSION in skill_file.read_text()
    backups = list((base / ".taste-engine-backups").glob("taste-engine-*/original-state.txt"))
    assert len(backups) == 1 and backups[0].read_text() == "preserve on failure"

    # Equal-version re-install is idempotent by default.
    p = run("--zip", package, "--target", target)
    assert "not newer" in p.stdout
    assert len(list((base / ".taste-engine-backups").iterdir())) == 1

    # Verify digest warning and SHA256SUMS fallback presence in updater script
    updater_src = UPDATER.read_text(encoding="utf-8")
    assert "WARNING: Download could not be verified against an expected SHA256 digest." in updater_src
    assert "SHA256SUMS" in updater_src

print("PASS: updater dry-run, hash check, ZIP path safety, automatic rollback, backup, upgrade, idempotence")
