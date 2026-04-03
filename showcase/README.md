# Showcase Handoff

This directory is the handoff boundary between the product logic and the future visual presentation.

Use it when you want to build:
- a high-conviction GitHub README refresh
- a lightweight landing page
- social screenshots, cards, or demo visuals

Do not change the product behavior here.
This folder exists so a design-focused agent can shape presentation without re-deciding the core product.

## What lives here

- `content/landing-copy.md`: approved public-facing copy blocks
- `content/showcase-brief.json`: structured content contract for sections and proof points
- `content/demo-script.md`: short narrative for motion, screenshots, or a demo page
- `ANTIGRAVITY_PROMPT.md`: ready-to-use prompt for a design-heavy agent

## Boundary

Code and product behavior stay in:
- `skills/github-pr-checklist/`

Presentation and storytelling can evolve in:
- `showcase/`

## Design constraints for the visual layer

- Keep the product positioned as one sharp skill, not a platform
- Show concrete review workflow value before talking about automation
- Emphasize decision support, not autonomous approval
- Make GitHub workflow cues recognizable without copying GitHub's UI too literally
- Preserve the existing promises:
  - Review faster
  - Miss fewer risky changes
  - Avoid fluffy summaries
