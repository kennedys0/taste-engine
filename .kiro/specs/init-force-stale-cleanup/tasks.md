# Implementation Plan

- [x] 1. Write bug condition exploration test
  - **Property 1: Bug Condition** - Force overwrite leaves stale files behind
  - **CRITICAL**: This test MUST FAIL on unfixed code - failure confirms the bug exists
  - **DO NOT attempt to fix the test or the code when it fails**
  - **NOTE**: This test encodes the expected behavior - it will validate the fix when it passes after implementation
  - **GOAL**: Surface counterexamples that demonstrate the bug exists
  - **Scoped PBT Approach**: Scope the property to concrete failing cases — stale files planted in the destination that have no counterpart in the source presets — to ensure reproducibility
  - Add tests to `tests/cli.test.mjs` using the existing `node:test` + `node:assert/strict` framework and the `run(args, env)` spawn helper already defined there
  - Test cases (all run on UNFIXED code and expected to FAIL):
    - Stale file in `tailwind/`: scaffold presets into a temp dir via `init [dir]`, write `taste-presets/tailwind/old-stale.css`, run `init [dir] --force`, assert `old-stale.css` no longer exists (will fail — `cpSync` merges, leaving stale file)
    - Stale file in `shadcn/`: scaffold presets, write `taste-presets/shadcn/legacy-themes.css`, run `init [dir] --force`, assert it is removed (will fail)
    - Stale subdirectory: scaffold presets, create `taste-presets/legacy/nested.css`, run `init [dir] --force`, assert the `legacy/` directory is gone (will fail)
  - For each test: after `init --force`, also assert the destination recursively equals the source presets tree (file set and contents), confirming exact-match semantics from Bug Condition in design
  - Run test on UNFIXED code: `node --test tests/cli.test.mjs` (or `npm test`)
  - **EXPECTED OUTCOME**: Test FAILS (stale files and stale subdirectories remain because `cpSync` merges rather than replaces)
  - Document counterexamples found (e.g., "taste-presets/tailwind/old-stale.css still exists after init --force")
  - Mark task complete when test is written, run, and failure is documented
  - _Requirements: 2.1, 2.2_

- [x] 2. Write preservation property tests (BEFORE implementing fix)
  - **Property 2: Preservation** - Non-buggy init invocations behave identically to the original
  - **IMPORTANT**: Follow observation-first methodology
  - Observe behavior on UNFIXED code for non-buggy inputs (cases where `isBugCondition` returns false), then write tests capturing that behavior
  - Add tests to `tests/cli.test.mjs` using the existing `node:test` + `node:assert/strict` framework and the `run(args, env)` spawn helper
  - Property-based / generative test cases (loop over generated flag combinations; all should PASS on UNFIXED code):
    - Non-force refusal preservation: scaffold presets into a temp dir, run `init [dir]` again (no `--force`), assert it exits non-zero with "already exists" in stderr (matches existing test behavior)
    - Dry-run preservation: run `init [dir] --dry-run` and `init [dir] --force --dry-run` in a temp dir, assert no `taste-presets/` is created and the dry-run message is printed
    - Fresh scaffolding preservation: run `init [dir]` and `init [dir] --force` against a temp dir with no existing destination, assert presets are created correctly (files exist and contents match source)
    - Custom target / `--cwd` preservation: run `init [subDir]` and `init --cwd [cwdDir]`, assert presets are scaffolded into the resolved target in both cases
  - Verify tests pass on UNFIXED code: `node --test tests/cli.test.mjs`
  - **EXPECTED OUTCOME**: Tests PASS (confirms baseline behavior to preserve)
  - Mark task complete when tests are written, run, and passing on unfixed code
  - _Requirements: 3.1, 3.2, 3.3, 3.4, 3.5_

- [x] 3. Fix for init --force merge-copy leaving stale files

  - [x] 3.1 Implement the fix
    - File: `bin/taste-engine.mjs`, the `init` command handler block (the `if(command==='init' || command==='--init' || command==='-init')` branch)
    - Replace the buggy copy block (`fs.mkdirSync(dest, { recursive: true })` followed by `fs.cpSync(path.join(source, 'presets'), dest, { recursive: true })`) with a conditional staging + atomic-swap path:
      - When `force` is true AND `fs.existsSync(dest)` is true AND `NOT dryRun` (the bug condition), stage a fresh copy in a temp dir under the destination's parent, then atomically swap it into place mirroring the `install` function's approach (lines 75-82):
        - `presetsSource := path.join(source, 'presets')`
        - `parent := path.dirname(dest)`
        - `staging := fs.mkdtempSync(path.join(parent, '.taste-presets-stage-'))`
        - `fs.cpSync(presetsSource, staging, { recursive: true })`
        - Move existing dest aside: `fs.renameSync(dest, oldDir)` where `oldDir` is a temp name under `parent`
        - Swap fresh copy in: `fs.renameSync(staging, dest)`; on failure, restore original from `oldDir` and rethrow (matching `install`'s rollback)
        - Remove the renamed-aside original after a successful swap: `fs.rmSync(oldDir, { recursive: true, force: true })`
        - Clean up staging temp dir in a `finally` block: `fs.rmSync(staging, { recursive: true, force: true })`
      - Otherwise (destination does not exist, regardless of `--force`), keep the existing fresh-scaffolding path unchanged: `fs.mkdirSync(dest, { recursive: true })` then `fs.cpSync(presetsSource, dest, { recursive: true })`
    - Leave all guard clauses untouched: the `destExists && !force` error throw (requirement 3.1) and the `dryRun` early return (requirement 3.3) remain exactly as they are
    - Keep the existing `console.log` success message unchanged so CLI output is identical before and after the fix
    - No new dependencies: use only `node:fs`, `node:path`, and `node:os` (already imported) plus `fs.mkdtempSync`/`fs.rmSync`/`fs.renameSync` (already used by `install`)
    - _Bug_Condition: isBugCondition(input) where input.command IN ['init','--init','-init'] AND input.force = true AND NOT input.dryRun AND destinationDirectoryExists(path.join(input.targetDir, 'taste-presets'))_
    - _Expected_Behavior: expectedBehavior(result) — destination exactly matches source presets directory, every stale file removed (Property 1 from design)_
    - _Preservation: Preservation Requirements — non-force refusal, dry-run no-op, fresh scaffolding, custom target resolution all unchanged (Property 2 from design)_
    - _Requirements: 2.1, 2.2, 3.1, 3.2, 3.3, 3.4, 3.5_

  - [x] 3.2 Verify bug condition exploration test now passes
    - **Property 1: Expected Behavior** - Force overwrite produces an exact match of the source presets
    - **IMPORTANT**: Re-run the SAME test from task 1 - do NOT write a new test
    - The test from task 1 encodes the expected behavior (stale files removed, destination exactly matches source)
    - Run bug condition exploration test from step 1: `node --test tests/cli.test.mjs`
    - **EXPECTED OUTCOME**: Test PASSES (confirms bug is fixed — stale files and stale subdirectories are removed, destination exactly matches source presets)
    - _Requirements: 2.1, 2.2_

  - [x] 3.3 Verify preservation tests still pass
    - **Property 2: Preservation** - Non-buggy init invocations behave identically to the original
    - **IMPORTANT**: Re-run the SAME tests from task 2 - do NOT write new tests
    - Run preservation property tests from step 2: `node --test tests/cli.test.mjs`
    - **EXPECTED OUTCOME**: Tests PASS (confirms no regressions — non-force refusal, dry-run, fresh scaffolding, and custom target resolution all still work)
    - Confirm all tests still pass after fix (no regressions)
    - _Requirements: 3.1, 3.2, 3.3, 3.4, 3.5_

- [x] 4. Checkpoint - Ensure all tests pass
  - Ensure all tests pass, ask the user if questions arise.
