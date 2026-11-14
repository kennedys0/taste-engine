# Bugfix Requirements Document

## Introduction

The `taste-engine init --force` CLI command scaffolds Tailwind CSS and shadcn/ui presets from the source `presets/` directory into a target project's `taste-presets/` directory. When the destination already exists, the `--force` flag is intended to overwrite it. However, the current implementation copies files into the existing directory with `fs.cpSync({ recursive: true })`, which performs a merge rather than a clean replacement. Files that exist in the destination but are absent from the source presets are left in place. Users upgrading Taste Engine and re-running `init --force` accumulate stale CSS files from older versions, which can cause confusion, import errors, or style conflicts.

## Bug Analysis

### Current Behavior (Defect)

1.1 WHEN `init --force` is run and the destination `taste-presets/` directory already exists THEN the system merges the new source preset files into the existing destination directory without removing its prior contents.

1.2 WHEN `init --force` is run and the destination contains files that no longer exist in the source presets THEN the system leaves those stale files in the destination after the copy completes.

### Expected Behavior (Correct)

2.1 WHEN `init --force` is run and the destination `taste-presets/` directory already exists THEN the system SHALL replace the destination contents entirely so that the destination exactly matches the source presets directory.

2.2 WHEN `init --force` is run and the destination contains files that no longer exist in the source presets THEN the system SHALL remove those stale files during the force overwrite.

### Unchanged Behavior (Regression Prevention)

3.1 WHEN `init` is run WITHOUT `--force` and the destination already exists THEN the system SHALL CONTINUE TO throw an error directing the user to use `--force` to overwrite.

3.2 WHEN `init` is run and the destination does not exist THEN the system SHALL CONTINUE TO create the directory and copy the source presets into it.

3.3 WHEN `init --dry-run` is run THEN the system SHALL CONTINUE TO print the dry-run message describing where presets would be scaffolded, without modifying any files.

3.4 WHEN `init --force` is run and the destination does not exist THEN the system SHALL CONTINUE TO create the directory and copy the source presets into it.

3.5 WHEN `init` is run with a custom target directory argument or `--cwd` THEN the system SHALL CONTINUE TO resolve and use that directory as the scaffolding target.
