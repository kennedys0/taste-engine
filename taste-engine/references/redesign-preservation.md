# Existing-product protection: inspect before restyle

For redesigns, preserve core business behavior while updating visual expression. For small fixes, preserve existing design direction and skip unnecessary taste selection.

## Define the requested depth

- `audit`: findings only, **no changes**.
- `polish`: small optical/copy/UI state corrections, retain layout and existing brand.
- `restyle`: type, surface, color, component material change; retain page hierarchy and information architecture unless user asks.
- `redesign`: change visual layout/system to selected style while preserving routes, data, facts, input names, handlers and business workflow.

For a true redesign without a confirmed style, the normal style-selection question runs before visual implementation. For a bug fix or small polish in an established system, do not interrupt with a new style quiz.

## Before-changing checklist

Capture route inventory, headings and real content, component responsibilities, CSS tokens, dependencies, interactive elements, button destinations, form validation, keyboard behavior, API calls, identifiers/test IDs and status states. Mark third-party content, regulated/legal text and user-approved wording as **preserve verbatim** unless instructed otherwise.

## After-changing checklist

Compare before/after for route and action parity, forms, focus order, loading/errors, real-data integration, responsive handling and copy meaning. Confirm no fake claim was added and no real information removed to make a screen 'cleaner'. A functional change is separate scope; make it explicit.

If browser checks cannot run, do not claim functional parity. Report what was inspected, what was edited, and what remains unverified. Avoid treating a single screenshot as proof of app function.
