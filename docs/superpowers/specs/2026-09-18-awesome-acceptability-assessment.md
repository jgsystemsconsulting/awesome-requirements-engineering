# Spec and assessment: awesome-acceptability-assessment (P5)

Date: 2026-09-18
Package: P5

## Problem

sindresorhus/awesome list PR is deferred because the acceptability gate was never assessed.

## Research

Primary sources consulted this session:

- https://github.com/sindresorhus/awesome/blob/main/awesome.md
- https://github.com/sindresorhus/awesome/blob/main/pull_request_template.md
- https://github.com/sindresorhus/awesome

## Assessment criteria (from awesome contribution guidance)

1. List must be useful and focused; not a dumping ground.
2. Descriptions must be clear and not promotional fluff.
3. Table of contents and consistent formatting.
4. Links must work; dead links fail review.
5. Prefer established resources; avoid low-quality or spam.
6. Naming: Awesome X pattern; avoid trademark abuse.
7. Review bandwidth: maintainers are slow; list must be high quality before PR.
8. Badge and LICENSE expectations for listed projects.

## Awesome Requirements Engineering against the bar

| Criterion | Status | Notes |
|---|---|---|
| Focus | PASS | Requirements engineering only; seven curated sections |
| Format | PASS | Family entry format with tags and year; Contents present |
| Links | PARTIAL | lychee covers README + landing on this branch; must stay green on main before PR |
| Naming | PASS | Awesome Requirements Engineering matches Awesome X |
| Badge | PASS | awesome.re badge already on README |
| Depth | PASS | 40 entries after first full sweep (thicker than thin-list risk) |
| Licence | PASS | CC0-1.0 |
| Visibility | PASS | Repo public as of 2026-09-18 |

## Decision

**go with prerequisites** (not go-now).

Do not open the sindresorhus/awesome PR in this package or until all prerequisites clear.

### Prerequisites before PR

1. Repo visibility public — done 2026-09-18 (backlog b-01).
2. GitHub Pages live and homepage set; product-surface lychee green on main (README + docs/index.html).
3. Release gate green on main (chips, section anchors, font assets).
4. Re-read awesome PR template at submit time; fix any new template items.
5. Confirm no promotional fluff or dead links in a fresh full lychee run.

### Not prerequisites

- Org catalogue entry (helpful, not required by awesome).
- Entry-row mirroring on the landing.

## DISTRIBUTION update

Record decision date 2026-09-18 on the sindresorhus/awesome row: deferred, go with prerequisites; assessment path docs/superpowers/specs/2026-09-18-awesome-acceptability-assessment.md. Do not open PR until prerequisites clear.
