# Behavior scenarios (manual evaluation)

These are acceptance scenarios for contributors to test against their favorite coding agent.

## 1. Contradictory tastes

**User A:** "Build a professional analytics dashboard. Dense tables, compact spacing, no rounded cards."

**User B:** "Build a friendly education dashboard. Spacious, tactile cards and playful illustrations."

**Expected:** Outputs differ in structure and styling; both remain usable and accessible. No universal preset leaks into both.

## 2. Current project overrides global taste

**General preference:** "I like dark editorial layouts."

**Current request:** "For this medical clinic website, use the approved light brand palette and established component library."

**Expected:** The current project wins without changing the global taste profile.

## 3. No known preferences

**User:** "Make an admin dashboard."

**Expected:** For a new UI with no confirmed project style, ask the router's single short style-selection question and stop before UI coding. Do not silently impose a default, fabricate a preference, or launch a long survey.

## 4. Feedback on one dimension

**User:** "I like the structure, but the colors feel too saturated."

**Expected:** Color is revised; layout and successful interactions are preserved.

## 5. Screenshot reference

**User:** "I like the typography of this screenshot, but not its layout."

**Expected:** Typography is treated as a reference, not the full page's appearance.

## 6. Accessibility conflict

**User:** "Make all secondary labels barely visible."

**Expected:** Seek an understated look while maintaining required readability and contrast; clearly surface any conflict.

## 7. Profile storage

**User:** "I love this one-off retro style for the game page."

**Expected:** Do not save retro styling to a reusable global preference profile without permission.

## 8. Existing codebase

**User:** "Improve the checkout form validation, don't redesign the page."

**Expected:** Preserve existing visual system; focus on validation, error recovery, and accessible form feedback.
