---
name: github-pr-checklist
description: Turn a GitHub pull request into a concise, actionable review checklist by reading PR metadata, diff, changed files, review comments, and check status. Use when Codex needs to review a PR from a PR URL, `owner/repo#number`, or a pasted diff/patch, highlight risky changes, propose follow-up questions, suggest targeted tests, or draft a short PR reply without producing a fluffy report.
---

# GitHub PR Checklist

## Overview

Turn a pull request into a compact review checklist that helps the user decide what matters next.
Prefer GitHub-native context first, then fall back to a pasted diff or patch if direct access is unavailable.

## Workflow

### 1. Normalize the input

Accept any of these entrypoints:
- A PR URL such as `https://github.com/owner/repo/pull/123`
- A compact identifier such as `owner/repo#123`
- A pasted `diff` or `patch`

If the request is ambiguous, restate the PR target you are about to inspect before continuing.

### 2. Gather the smallest useful review context

When GitHub access is available, read:
- PR title, body, author, and branch names
- Changed files and diff or patch
- Existing review comments and open questions
- Combined check status or notable failing checks

Do not crawl the whole repository unless the PR context makes it necessary.
Stay focused on the files that changed and any directly adjacent code needed to judge risk.

### 3. Review like a pragmatic teammate

Bias toward concrete risk over broad narration.
Look for:
- behavior changes hidden inside refactors
- state, auth, data migration, concurrency, or caching risks
- missing validation, rollback, error handling, or instrumentation
- tests that should exist but do not
- reviewer concerns that are still unresolved

Use the rubric in [references/review-rubric.md](references/review-rubric.md) when the PR is complex or noisy.

### 4. Produce the checklist

Always use this output contract:

```md
## Key Changes
- 3 to 6 bullets about what materially changed

## Risks
- concrete regressions, suspicious behavior, or fragile edges

## Questions
- missing context, assumptions to confirm, or follow-ups for the author

## Suggested Tests
- focused manual or automated checks worth running

## Reply Draft
- only include this section when the user explicitly asks for a reply
```

Keep the answer compact.
Prefer short bullets over paragraphs.
If a section has no meaningful items, say `- None worth calling out.` rather than padding it.

## Fallback Path

If GitHub access is unavailable or the connector cannot read the PR:
- ask for the PR `diff` or `patch`
- continue with the same checklist format
- explicitly note that review comments and check status were unavailable

Do not pretend you saw data that you could not access.

## Quality Bar

Do:
- summarize only the changes that affect review decisions
- rank the most important risks first
- suggest tests that match the actual code paths changed
- keep the tone direct, calm, and useful

Do not:
- rewrite the PR description unless the user asks
- produce vague praise or filler
- invent failures, comments, or repository context
- bury the checklist inside a long report

## Resources

Read these only when needed:
- [references/review-rubric.md](references/review-rubric.md): high-signal review heuristics for risky PRs
- [references/example-requests.md](references/example-requests.md): realistic invocation patterns and expected response shape
