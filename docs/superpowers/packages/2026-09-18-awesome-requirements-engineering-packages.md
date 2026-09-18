---
date: 2026-09-18
project: awesome-requirements-engineering
mode: light
rounds: 1
input_digest: 8759e3f7a43703f44454019c442249a358687f0c179efc3d1fccdb763921d17b
open_objections: []
---

# Work packages: awesome-requirements-engineering (2026-09-18, light mode, round 1)

First package-loop run. Trigger: feature branch feat/pages-landing-and-packages with DESIGN, Path S landing, release gate, and CI drafted. Taste audit 2026-09-18: visitor-clean chrome, no required redesign. Triage: all packages PASS, zero critical defects. X1 resolved: P3 owns Pages/About/Releases ledger; P4 owns catalogue row and products.yml. Font-asset gate folded into P1. pin-validate-setup-python absorbed into P2.

Execution order: P1, P7, P2, P5, P3, P4.

## P1: landing-truth-gate

| Field | Value |
|---|---|
| id | P1 |
| name | landing-truth-gate |
| size | M |
| deps | none |
| status | done |
| promoted_ids | [b-font-gate] |
| corroboration | 2 (value, cohesion) + risk font fold |
| first_prompt | `/superpowers-process full landing truth gate` |

**Problem.** Dual product surface (README + docs/index.html) is branch-only vs main: chips and seven section-index fragments are hand-maintained; check_release.py already asserts them, but the gate is not on main, has no maintainer write-path note, and REQUIRED omits the four self-hosted woff2 fonts plus OFL/SOURCE the landing preloads. Without freezing this gate, drift or missing fonts can ship while CI stays green.

**Evidence.** scripts/check_release.py truth gate; docs/index.html chips 0.1.0 / 2026-09 / 40 and seven section anchors; docs/fonts assets present; validate.yml runs the gate; local PASS on branch.

**In scope.** Verify PASS for chips and seven fragments; extend REQUIRED for four woff2 + OFL.txt + SOURCE.txt; optional relative-only font URL check; document write path for chips/anchors; keep validate.yml as sole gate runner; land on path to main.

**Out of scope.** Visitor copy; links.yml; org catalogue; Pages enable; README entries; mirroring; sindresorhus PR.

**Why now.** First DoD package; copy and catalogue need a non-drifting router.

## P7: landing-visitor-copy

| Field | Value |
|---|---|
| id | P7 |
| name | landing-visitor-copy |
| size | S |
| deps | P1 |
| status | done |
| promoted_ids | [] |
| corroboration | 1 (cohesion) |
| first_prompt | `/superpowers-process full landing visitor copy` |

**Problem.** Landing already visitor-clean (Top/Status/Open full list, favicon, woff2 preload, 44px nav, no IE shim). Remaining same-file nits: support line searchable Contents; sections blurb Seven README anchors.

**Evidence.** docs/index.html support and sections blurb; taste audit nits only.

**In scope.** Tighten those nits; preserve gated chip dt/values and section-index href fragments; confirm chrome.

**Out of scope.** Gate rewrite; CI; DISTRIBUTION; catalogue; awesome PR.

**Why now.** Finishes landing HTML after truth-gate freeze.

## P2: link-check-product-surface

| Field | Value |
|---|---|
| id | P2 |
| name | link-check-product-surface |
| size | S |
| deps | none |
| status | done |
| promoted_ids | [] |
| corroboration | 2 (value, cohesion) |
| first_prompt | `/superpowers-process full landing link check coverage` |

**Problem.** Branch replaces legacy link-check workflows with links.yml covering README.md + docs/index.html and PR-blocking fail; validate.yml SHA-pins setup-python. Main is not protected until this lands.

**Evidence.** links.yml product-surface args + PR fail; validate.yml setup-python SHA; deleted legacy link-check workflows on branch.

**In scope.** Confirm product-surface lychee + PR block; keep schedule report-issue; confirm full SHA pins including setup-python; pin-bump comment convention.

**Out of scope.** Chip/fragment gate; DISTRIBUTION; landing copy.

**Why now.** Independent CI DoD.

## P5: awesome-acceptability-assessment

| Field | Value |
|---|---|
| id | P5 |
| name | awesome-acceptability-assessment |
| size | S |
| deps | none |
| status | done |
| promoted_ids | [] |
| corroboration | 2 (value, cohesion) |
| first_prompt | `/superpowers-process full awesome acceptability assessment` |

**Problem.** sindresorhus/awesome deferred because acceptability unassessed.

**Evidence.** DISTRIBUTION deferred row; README Awesome badge; 40 entries.

**In scope.** Written go/no-go assessment + prerequisites; DISTRIBUTION decision date; do not open PR unless clear go-now (default assessment only).

**Out of scope.** Opening PR before go; catalogue; landing/CI refactors.

**Why now.** Optional DoD; independent.

## P3: pages-enable-distribution

| Field | Value |
|---|---|
| id | P3 |
| name | pages-enable-distribution |
| size | M |
| deps | P1, P2 |
| status | done |
| promoted_ids | [] |
| corroboration | 2 (value, risk) |
| first_prompt | `/superpowers-process full pages enable distribution` |

**Problem.** Canonical advertises Pages URL while API has_pages false, homepage null, private true. DISTRIBUTION marks Pages/Releases planned.

**Evidence.** docs/index.html canonical; DISTRIBUTION Pages/Releases/About; gh API.

**In scope.** After landing/gate/links on main: enable Pages main /docs (org plan permitting); set homepage; smoke-check; update DISTRIBUTION Pages, About/homepage, Releases only (X1: P3 owns these rows).

**Out of scope.** products.yml (P4); public flip; landing redesign; CI; awesome PR.

**Why now.** Live Path S after CI-backed landing; catalogue needs stable URL status.

## P4: org-catalogue-entry

| Field | Value |
|---|---|
| id | P4 |
| name | org-catalogue-entry |
| size | S |
| deps | P1, P3, P7 |
| status | done |
| promoted_ids | [] |
| corroboration | 3 (value, risk, cohesion) |
| first_prompt | `/superpowers-process full org catalogue entry` |

**Problem.** Labs catalogue missing this spoke; DISTRIBUTION catalogue planned.

**Evidence.** DISTRIBUTION catalogue planned; products.yml has archimate not this list.

**In scope.** Add products.yml entry; regenerate labs docs/index.html if required; clean labs branch ready to merge; DISTRIBUTION catalogue row to submitted (X1: P4 owns catalogue row only).

**Out of scope.** sindresorhus PR; community directories; landing redesign; public flip; Pages enable (P3).

**Why now.** Next growth channel after landing URL trustworthy.

## Conflict X1 (resolved)

P3 owns Pages enable, homepage, Releases, those DISTRIBUTION rows. P4 owns catalogue row + products.yml only.

## Folded / absorbed

- P6 gate-require-landing-font-assets into P1
- pin-validate-setup-python into P2
