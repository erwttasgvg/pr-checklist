# Example Requests

Use these to calibrate how the skill should be invoked and how concise the output should feel.

## Example 1: direct PR URL

Prompt:
`Use $github-pr-checklist on https://github.com/acme/api/pull/481 and focus on rollout risk.`

Expected shape:
- `Actionable PR Checklist` summary with a short count and priority labels
- brief `Key Changes`
- numbered `Risks` that mention state changes, migrations, or API compatibility
- `Suggested Tests` that match the changed endpoints

## Example 2: compact identifier

Prompt:
`Use $github-pr-checklist on acme/web#912 and tell me what I should verify before approving.`

Expected shape:
- `Actionable PR Checklist` summary that is easy to scan
- clear `Questions` for missing context
- no `Reply Draft` unless requested

## Example 3: diff fallback

Prompt:
`Use $github-pr-checklist on this patch and give me the top risks only.`

Expected shape:
- same checklist structure
- `Priority Labels` that call out the top risks in plain language
- explicit note that GitHub comments/check status were not available
