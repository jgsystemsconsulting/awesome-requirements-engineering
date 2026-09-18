# Research: awesome family packaging shell

research: skipped (no live web fetch this run); local standards used as sources of truth.

## Sources (local)

- `~/.zcode/skills/release-repo-standard/references/release-repo-standard.md` (RR-B-05, RR-B-06, RR-B-07, RR-B-32)
- `~/.zcode/skills/sindresorhus-awesome-ready/references/awesome-inclusion-standard.md` (SA-CONTENTS, SA-LICENCE-README, SA-CONTRIBUTING-*)
- Inventory: `docs/superpowers/context/2026-09-18-packaging-shell-inventory.md`
- RR excerpts: `docs/superpowers/context/2026-09-18-rr-b-packaging-excerpts.md`
- Prior assessment: `docs/superpowers/specs/2026-09-18-awesome-acceptability-assessment.md`

## Conflict that drives the design

RR-B-05 Verify wants README headings Install, Usage, Licence, Support.
SA-LICENCE-README MUST: no ## Licence/License/Licensing heading in README (GitHub sidebar + landing cover licence).
SA-CONTENTS MUST: Contents must not list Contributing or Footnotes.
Family note in SA-CONTENTS: also omit Install/Usage/Support/Version from Contents.
awesome-lint reality (from prior assessment): if those ## headings exist, lint wants them listed in Contents; listing them fails the family's SA purity goal and currently FAILs this repo's lint.

Prior assessment recommendation: keep packaging shell sections at bottom for RR-B, remove them from Contents for SA, accept residual awesome-lint tension until family policy settles; drop "Licence:" bullet from Support on awesome-bound spokes to avoid SA-LICENCE-PROSE / heading-like licence prose.

## Inventory summary

Has full shell (Install/Usage/Support/Version): archimate, capella, enterprise-architect, requirements-engineering, stpa.
Partial / different: mbse and magic-grid hubs use Support & security + CC0 badge footer (hub shape).
Missing shell: digital-engineering, magicgrid-mbse, sysml-v2.
Not a list: sparx-ea (namespace reserve only).

Inconsistencies among shell-present repos:
- Contributing section present or absent
- Install wording variants
- Usage generic vs product-specific bullet 2
- Support: issue form links vs plain text; sibling pointer wording; Licence bullet present/absent; stpa has auditor-WARN note in Support
- Version: bold vs plain; RELEASE-INFO linked or not
- Contents: some list packaging headings (requirements, archimate, capella, stpa, enterprise-architect)

## Canonical shell (locked target for curated public spokes)

Order after curated content:
1. ## Contributing (short pointer to CONTRIBUTING.md) — outside Contents
2. ## Install — curated-index clone block with this repo URL
3. ## Usage — three numbered steps (Contents jump / browser find; open upstream links; Support or PR)
4. ## Support — bug form, suggestion form, security advisory+SECURITY.md, optional one sibling pointer; NO Licence heading; NO Licence: bullet on awesome-bound public spokes
5. ## Version — Current release: **X.Y.Z** (YYYY-MM-DD). See CHANGELOG.md and RELEASE-INFO.txt when the file exists.

Contents lists only curated topic sections (never Contributing, Install, Usage, Support, Version, Footnotes, Licence).
