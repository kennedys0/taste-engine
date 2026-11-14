# init-force-stale-cleanup Bugfix Design

## Overview

The `taste-engine init --force` command scaffolds Tailwind CSS and shadcn/ui preset files from the packaged `skills/taste-engine/presets/` source directory into a target project's `taste-presets/` directory. When the destination already exists, `--force` is meant to overwrite it cleanly. The current implementation copies the source presets into the existing destination with `fs.cpSync({ recursive: true })`, which performs a merge rather than a clean replacement: files that exist in the destination but are absent from the source are left in place.

The impact is upgrade drift. When a user upgrades Taste Engine and re-runs `init --force`, CSS files renamed or removed in newer presets survive in their `taste-presets/` directory, causing confusion, broken imports, and style conflicts.

The fix strategy is to mirror the staging + atomic-rename pattern already used by the `install` command in the same file: stage a fresh copy of the presets in a temporary directory, then swap it into place so the destination ends up exactly matching the source. This guarantees that stale files are removed while preserving every other `init` behavior (non-force errors, dry-run, fresh scaffolding, custom targets).

## Glossary

- **Bug_Condition (C)**: The condition that triggers the bug — an `init` invocation with `--force` against a destination `taste-presets/` directory that already exists (and is not a dry run), where the current merge-copy leaves stale files behind.
- **Property (P)**: The desired behavior for buggy inputs — after the overwrite, the destination directory contents exactly match the source presets directory, with no stale files remaining.
- **Preservation**: Existing behaviors that must remain unchanged for every input that does NOT satisfy the bug condition: non-force refusal, dry-run no-op, fresh scaffolding, and custom target resolution.
- **init handler**: The command branch in `bin/taste-engine.mjs` (starting at the `if(command==='init' ...)` block) that parses `init`/`--init`/`-init` flags and copies presets into `taste-presets/`. The buggy lines are `fs.mkdirSync(dest, { recursive: true })` and `fs.cpSync(path.join(source, 'presets'), dest, { recursive: true })` at lines 238-239.
- **install (reference pattern)**: The `install(dest, dryRun)` function at line 75 of `bin/taste-engine.mjs`, which stages a copy in a temp dir and atomically renames it over the destination, used here as the reference for atomic replacement.
- **source presets**: The packaged preset files under `skills/taste-engine/presets/`: `shadcn/shadcn-themes.css`, `tailwind/tailwind.preset.js`, `tailwind/taste-components.css`, and `templates/pow-showcase.template.html`.
- **stale file**: A file present in the destination `taste-presets/` directory that has no counterpart in the source presets (e.g. a file from an older Taste Engine release that was later removed or renamed).
- **destination (dest)**: The resolved path `path.join(targetDir, 'taste-presets')` into which presets are scaffolded.

## Bug Details

### Bug Condition

The bug manifests when `init --force` runs against an existing `taste-presets/` destination (and the run is not a dry run, so the copy actually executes). In that situation the handler calls `fs.cpSync(source, dest, { recursive: true })` directly into the existing directory, which merges the source tree into the destination instead of replacing it. Any file that exists only in the destination — a stale file left by a previous version — survives the overwrite.

**Formal Specification:**
```
FUNCTION isBugCondition(input)
  INPUT: input of type InitCommandInvocation
         fields: command (string), force (boolean), dryRun (boolean), targetDir (string)
  OUTPUT: boolean

  RETURN input.command IN ['init', '--init', '-init']
         AND input.force = true
         AND NOT input.dryRun
         AND destinationDirectoryExists(path.join(input.targetDir, 'taste-presets'))
END FUNCTION
```

A concrete counterexample additionally requires that the destination contains at least one stale file (a file with no counterpart in the source presets), because that is the observable symptom: the stale file remains after the overwrite.

### Examples

- **Renamed preset file**: A user previously scaffolded presets containing `taste-presets/tailwind/components.css`. A later release renames it to `taste-presets/tailwind/taste-components.css`. After `init --force`, both `components.css` (stale) and `taste-components.css` (new) exist in the destination. Expected: only `taste-components.css` remains; actual: `components.css` is left behind.
- **Removed preset file**: A user previously scaffolded presets containing `taste-presets/shadcn/legacy-themes.css`. A later release deletes that file from the source presets. After `init --force`, `legacy-themes.css` still exists in the destination. Expected: it is removed; actual: it remains.
- **Removed subdirectory**: A previous release shipped a `taste-presets/legacy/` folder that no longer exists in the source. After `init --force`, the entire `legacy/` folder survives. Expected: the folder is removed; actual: it persists.
- **No stale files (edge case)**: The destination happens to be a subset of the source with no extra files. After `init --force` the contents are correct by coincidence, but the implementation still does a merge rather than a guaranteed clean replacement, so the requirement "destination exactly matches source" is not enforced.

## Expected Behavior

### Preservation Requirements

**Unchanged Behaviors:**
- `init` without `--force` against an existing destination must continue to throw an error directing the user to use `--force` to overwrite.
- `init` against a non-existent destination must continue to create the directory and copy the source presets into it.
- `init --dry-run` must continue to print the dry-run message describing where presets would be scaffolded, without modifying any files.
- `init --force` against a non-existent destination must continue to create the directory and copy the source presets into it.
- `init` with a custom target directory argument or `--cwd` must continue to resolve and use that directory as the scaffolding target.

**Scope:**
All `init` invocations that do NOT satisfy the bug condition should be completely unaffected by this fix. This includes:
- `init` without `--force` (regardless of whether the destination exists).
- `init --dry-run` with or without `--force`.
- `init --force` when the destination does not exist (fresh scaffolding).
- `init` resolving a custom target directory or `--cwd` path.

**Note:** The actual expected correct behavior for buggy inputs is defined in the Correctness Properties section (Property 1). This section focuses on what must NOT change.

## Hypothesized Root Cause

Based on the bug description and the source code, the most likely issues are:

1. **Merge-copy instead of clean replacement**: The init handler copies the source tree directly into the existing destination with `fs.cpSync(src, dest, { recursive: true })`. `cpSync` merges by design — it writes/overwrites files that exist in the source but never deletes files that exist only in the destination. This is the direct cause of stale files surviving.

2. **Missing cleanup step before copy**: Unlike the `install` command (line 75), the init handler does not remove or set aside the existing destination before populating it. The `install` function stages a fresh copy and atomically renames it over the destination; the init handler has no equivalent step.

3. **No atomic-swap protection**: Because the copy happens in place, a failure partway through `cpSync` leaves the destination in a partially merged state. There is no staging-then-swap to guarantee the destination is either untouched or fully replaced.

4. **Test gap masked the bug**: The existing `tests/cli.test.mjs` test for `init --force` only asserts that the command exits successfully; it never checks that stale files are removed, so the merge behavior went unobserved.

## Correctness Properties

Property 1: Bug Condition - Force overwrite produces an exact match of the source presets

_For any_ `init` invocation where the bug condition holds (command is `init`, `--force` is set, it is not a dry run, and the destination `taste-presets/` directory already exists), the fixed init handler SHALL replace the destination contents entirely so that the destination exactly matches the source presets directory — every file and subdirectory from the source is present with identical contents, and every file that exists only in the destination (stale files) is removed.

**Validates: Requirements 2.1, 2.2**

Property 2: Preservation - Non-buggy init invocations behave identically to the original

_For any_ `init` invocation where the bug condition does NOT hold (no `--force`, or `--dry-run` is set, or the destination does not exist), the fixed init handler SHALL produce exactly the same observable result as the original handler, preserving the non-force refusal error, the dry-run no-op message, fresh scaffolding of a non-existent destination, and resolution of a custom target directory or `--cwd`.

**Validates: Requirements 3.1, 3.2, 3.3, 3.4, 3.5**

## Fix Implementation

### Changes Required

Assuming the root cause analysis is correct, all changes are confined to the `init` command branch in `bin/taste-engine.mjs` (the block starting at `if(command==='init' || command==='--init' || command==='-init')`). No other commands are touched.

**File**: `bin/taste-engine.mjs`

**Location**: The buggy copy block at lines 238-239:
```js
fs.mkdirSync(dest, { recursive: true });
fs.cpSync(path.join(source, 'presets'), dest, { recursive: true });
```

**Specific Changes**:

1. **Introduce a staging + atomic-swap path for forced overwrite of an existing destination**: When `force` is true and `fs.existsSync(dest)` is true, stage a fresh copy of the presets in a temporary directory, then swap it into place so the destination ends up exactly matching the source. Mirror the `install` function's staging approach (line 75) but adapted for presets:
   - Create a staging temp dir under the destination's parent with `fs.mkdtempSync`.
   - Copy the source presets into the staging dir with `fs.cpSync(source/presets, staging, { recursive: true })`.
   - Rename the existing `dest` aside to a temporary name, then `fs.renameSync(staging, dest)` to swap in the fresh copy. On failure of the swap rename, restore the original `dest` from the temporary name (matching `install`'s rollback).
   - Remove the renamed-aside original after a successful swap.
   - Clean up the staging temp dir in a `finally` block.

2. **Keep the fresh-scaffolding path unchanged**: When the destination does not exist (regardless of `--force`), continue using the existing `fs.mkdirSync(dest, { recursive: true })` followed by `fs.cpSync(path.join(source, 'presets'), dest, { recursive: true })`. This preserves requirement 3.2 and 3.4 and keeps the common case simple.

3. **Leave all guard clauses untouched**: The `destExists && !force` error throw and the `dryRun` early return remain exactly as they are, satisfying requirements 3.1 and 3.3.

4. **No new dependencies**: Use only `node:fs`, `node:path`, and `node:os` (already imported) plus `fs.mkdtempSync`/`fs.rmSync`/`fs.renameSync` (already used by `install`), consistent with the file's "no external dependencies" constraint.

5. **No user-facing output change**: Keep the existing `console.log` success message unchanged so the CLI output for a successful `init --force` is identical before and after the fix.

**Pseudocode for the fixed branch:**
```
presetsSource := path.join(source, 'presets')
if force AND fs.existsSync(dest) AND NOT dryRun THEN
  parent := path.dirname(dest)
  staging := fs.mkdtempSync(path.join(parent, '.taste-presets-stage-'))
  TRY
    fs.cpSync(presetsSource, staging, { recursive: true })
    oldDir := path.join(parent, '.taste-presets-old-' + uniqueSuffix)
    fs.renameSync(dest, oldDir)        // move existing aside
    TRY
      fs.renameSync(staging, dest)      // swap fresh copy in
    CATCH err
      fs.renameSync(oldDir, dest)       // restore original on failure
      THROW err
    fs.rmSync(oldDir, { recursive: true, force: true })  // discard old contents
  FINALLY
    fs.rmSync(staging, { recursive: true, force: true }) // cleanup any leftover
ELSE
  fs.mkdirSync(dest, { recursive: true })
  fs.cpSync(presetsSource, dest, { recursive: true })
END IF
```

## Testing Strategy

### Validation Approach

The testing strategy follows a two-phase approach: first, surface a counterexample that demonstrates the bug on unfixed code, then verify the fix works correctly and preserves existing behavior. Tests use the project's existing `node:test` + `node:assert/strict` framework, run via `node --test tests/cli.test.mjs` (or `npm test`), and exercise the CLI by spawning it as a subprocess in temporary directories — the same pattern used by `tests/cli.test.mjs`.

### Exploratory Bug Condition Checking

**Goal**: Surface a counterexample that demonstrates the bug BEFORE implementing the fix. Confirm or refute the root cause analysis. If we refute, we will need to re-hypothesize.

**Test Plan**: Write a test that scaffolds presets into a temp dir, plants a stale file that has no counterpart in the source presets, runs `init [dir] --force`, and asserts that the stale file is gone and that the destination exactly matches the source. Run this test on the UNFIXED code to observe the failure and confirm the merge behavior.

**Test Cases**:
1. **Stale file in tailwind**: Scaffold presets, write `taste-presets/tailwind/old-stale.css`, run `init --force`, assert `old-stale.css` no longer exists (will fail on unfixed code).
2. **Stale file in shadcn**: Scaffold presets, write `taste-presets/shadcn/legacy-themes.css`, run `init --force`, assert it is removed (will fail on unfixed code).
3. **Stale subdirectory**: Scaffold presets, create `taste-presets/legacy/nested.css`, run `init --force`, assert the `legacy/` directory is gone (will fail on unfixed code).
4. **Exact-match edge case**: Scaffold presets, run `init --force` with no stale files, assert the destination recursively equals the source presets tree (sanity, should pass on unfixed code too).

**Expected Counterexamples**:
- After `init --force` on unfixed code, stale files and stale subdirectories remain because `cpSync` merges rather than replaces.
- Possible causes confirmed: in-place merge copy with no prior cleanup; no staging + swap like `install`.

### Fix Checking

**Goal**: Verify that for all inputs where the bug condition holds, the fixed function produces the expected behavior — the destination exactly matches the source presets.

**Pseudocode:**
```
FOR ALL input WHERE isBugCondition(input) DO
  result := init_fixed(input)
  ASSERT destinationExactlyMatchesSourcePresets(result.destination)
END FOR
```

### Preservation Checking

**Goal**: Verify that for all inputs where the bug condition does NOT hold, the fixed function produces the same result as the original function.

**Pseudocode:**
```
FOR ALL input WHERE NOT isBugCondition(input) DO
  ASSERT init_original(input) = init_fixed(input)
END FOR
```

**Testing Approach**: Property-based testing is recommended for preservation checking because it generates many test cases automatically across the input domain, catches edge cases that manual unit tests might miss, and provides strong guarantees that behavior is unchanged for all non-buggy inputs. Because this project has zero external dependencies and uses only Node built-ins, property-style tests are written as generative tests within `node:test` (looping over generated flag combinations and target dirs) rather than pulling in a PBT library. If the team prefers a dedicated PBT library, `fast-check` could be added as a dev dependency, but that is optional and out of scope for this bugfix.

**Test Plan**: Observe behavior on UNFIXED code first for each non-buggy input class, then write tests capturing that behavior so they continue to pass after the fix.

**Test Cases**:
1. **Non-force refusal preservation**: Scaffold presets into a temp dir, run `init [dir]` again (no `--force`), assert it still exits non-zero with "already exists" in stderr.
2. **Dry-run preservation**: Run `init [dir] --dry-run` and `init [dir] --force --dry-run` in a temp dir, assert no `taste-presets/` is created and the dry-run message is printed.
3. **Fresh scaffolding preservation**: Run `init [dir]` and `init [dir] --force` against a temp dir with no existing destination, assert presets are created correctly.
4. **Custom target / --cwd preservation**: Run `init [subDir]` and `init --cwd [cwdDir]`, assert presets are scaffolded into the resolved target in both cases.

### Unit Tests

- `init --force` removes a stale file planted in `taste-presets/tailwind/` after overwrite.
- `init --force` removes a stale subdirectory planted under `taste-presets/` after overwrite.
- `init --force` leaves the destination recursively identical to the source presets (file set and contents).
- `init` (no force) against an existing destination still throws the "already exists" error.
- `init --dry-run` (with and without `--force`) does not create or modify any files.
- `init --force` against a non-existent destination creates it and copies presets.
- `init` with a positional target dir and with `--cwd` both resolve and scaffold into the correct location.

### Property-Based Tests

- Generate random sets of stale files/directories in an existing destination, run `init --force`, and assert the destination exactly equals the source presets tree (property 1). Implemented as a generative loop in `node:test`.
- Generate random combinations of `--force`, `--dry-run`, existing vs non-existing destination, and positional vs `--cwd` target resolution; for every combination that does NOT satisfy the bug condition, assert the observable outcome (exit status, stderr message, files created) matches the original behavior (property 2).
- Generate random stale file names across the preset subdirectories (`tailwind/`, `shadcn/`, `templates/`) and assert each is removed after a forced overwrite.

### Integration Tests

- Full flow: scaffold presets into a temp dir, simulate an upgrade by planting stale files and altering a copied file, run `init --force`, and assert the destination is a clean exact match of the new source presets.
- Context-switching flow: run `init` (fresh), then `init` (refused), then `init --force` (clean replace) in sequence in the same temp dir and assert each step's outcome.
- Visual/feedback flow: run `init --force` and assert the success message output is unchanged from the unfixed CLI output (no extra or missing lines).
