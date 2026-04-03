# Review Rubric

Use this rubric to decide what deserves space in the checklist.

## Prioritize these changes

1. Data correctness
- schema changes
- persistence logic
- idempotency and retries
- background jobs and ordering

2. User-visible behavior
- changed defaults
- permissions and auth paths
- loading, empty, and error states
- breaking API or CLI behavior

3. Operational risk
- cache invalidation
- missing metrics or logging
- rollout dependencies
- feature flags and safe fallback paths

4. Test coverage
- new branches without tests
- removed tests that lowered confidence
- checks that passed but missed the risky path

## What to ignore

- cosmetic renames with no behavior change
- broad restatements of the diff
- speculative edge cases with no link to the changed code

## Severity hints

- Put issues in `Risks` when they could cause regressions or on-call pain.
- Put issues in `Questions` when the code might be fine but the intent is unclear.
- Put items in `Suggested Tests` when they are a fast way to reduce uncertainty.
