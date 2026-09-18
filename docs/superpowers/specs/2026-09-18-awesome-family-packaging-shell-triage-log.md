| Finding | First seen | Last seen | Verdict | Rationale |
|---------|------------|-----------|---------|-----------|
| C1 SECURITY URL | R1 | R1 | Genuine | Fixed: pin advisories/new URL + SECURITY.md clause |
| C2 BUG/SUGGEST detection | R1 | R1 | Genuine | Fixed: *bug* / *suggest* filename patterns + form URLs |
| C3 CLONE_URL | R1 | R1 | Genuine | Fixed: origin get-url normalize to org https URL |
| C4 Contributing optional vs required | R1 | R1 | Genuine | Fixed: Contributing H2 required on all in-scope |
| C5 public awesome-bound undefined | R1 | R1 | Genuine | Fixed: enumerated table + private EA carve |
| C6 SIBLING placeholder drift | R1 | R1 | Genuine | Fixed: single SIBLING_LINE + example + false sibling |
| C7 Licence ban EA | R1 | R1 | Genuine | Fixed: ban on all in-scope including EA |
| C8 VERSION precedence | R1 | R1 | Genuine | Fixed: ordered sources + stop on conflict |
| C9 Acceptance placeholders | R1 | R1 | Genuine | Fixed: checks 6-7 for clone/forms/security |
| C10 Contributing H2 acceptance | R1 | R1 | Genuine | Fixed: acceptance 1 exact H2 order |
| C11 DATE extraction | R1 | R1 | Genuine | Fixed: YYYY-MM-DD algorithm + conflict stop |
| M1 Contents purity list-only | R1 | R1 | Genuine | Fixed: forbid names anywhere in Contents block |
| M2 curated unchanged loose | R1 | R1 | Genuine | Fixed: diff bounds cut rule |
| M3 in-scope not at Goals | R1 | R1 | Genuine | Fixed: exhaustive in-scope table under Goals |
| M4 append duplicates Contributing | R1 | R1 | Genuine | Fixed: replace packaging block once |
| M5 keep shell vs reorder | R1 | R1 | Genuine | Fixed: replace with canonical order |
| M6 sibling example | R1 | R1 | Genuine | Fixed: canonical sibling bullet example |
| M7 Version bold acceptance | R1 | R1 | Genuine | Fixed: acceptance 5 requires **VERSION** |
| M8 last curated empty commercial | R1 | R1 | Genuine | Fixed: empty topic H2 still cut anchor |
| M9 REPO undefined | R1 | R1 | Genuine | Fixed: REPO placeholder row |
| A1 optional lint | R1 | R1 | Advisory-skipped | Contents grep mandatory; full lint still optional |
| A2 Capella usage subjective | R1 | R1 | Genuine | Fixed: Capella USAGE_STEP2_EXTRA empty |
| A3 false sibling | R1 | R1 | Genuine | Fixed: definition under SIBLING_LINE |
| A4 Footnotes body | R1 | R1 | Genuine | Fixed: body Footnotes untouched |
| A5 Licensing Goal3 | R1 | R1 | Genuine | Fixed: Licensing in Goal 3 |
| A6 SA-LICENCE-PROSE scope | R1 | R1 | Genuine | Fixed: heading+bullet only this pass |

## Round 1 Summary

| Finding | Lens | Severity | Verdict | Action |
|---------|------|----------|---------|--------|
| SECURITY URL | saboteur, new_hire, auditor | CRIT | Genuine | Fixed |
| BUG/SUGGEST detection | saboteur, new_hire, auditor | CRIT | Genuine | Fixed |
| CLONE_URL | saboteur, auditor | CRIT | Genuine | Fixed |
| Contributing optional/required | auditor, new_hire | CRIT | Genuine | Fixed |
| public awesome-bound | auditor, new_hire | CRIT | Genuine | Fixed |
| SIBLING drift | auditor, saboteur, new_hire | CRIT | Genuine | Fixed |
| Licence EA | saboteur, auditor | CRIT | Genuine | Fixed |
| VERSION precedence | saboteur | CRIT | Genuine | Fixed |
| Acceptance placeholders | saboteur | CRIT | Genuine | Fixed |
| Contributing H2 acceptance | saboteur, auditor | CRIT | Genuine | Fixed |
| DATE extraction | saboteur, auditor | CRIT | Genuine | Fixed |
| Contents purity | saboteur | MAJ | Genuine | Fixed |
| curated bounds | saboteur | MAJ | Genuine | Fixed |
| in-scope Goals | saboteur | MAJ | Genuine | Fixed |
| append duplicate | new_hire | MAJ | Genuine | Fixed |
| reorder | auditor | MAJ | Genuine | Fixed |
| sibling example | auditor | MAJ | Genuine | Fixed |
| version bold | auditor | MAJ | Genuine | Fixed |
| last curated | auditor | MAJ | Genuine | Fixed |
| REPO | new_hire, auditor | MAJ | Genuine | Fixed |
| optional lint | saboteur | ADV | Advisory-skipped | Skipped |
| Capella usage | saboteur | ADV | Genuine | Fixed |
| false sibling | auditor | ADV | Genuine | Fixed |
| Footnotes body | auditor | ADV | Genuine | Fixed |
| Licensing Goal3 | auditor | ADV | Genuine | Fixed |
| SA-LICENCE-PROSE | auditor | ADV | Genuine | Fixed |

Fixes applied: 25
Inflation rate: 0% (0/20 CRITICAL+MAJOR triaged FP/Design/Recurring)
Validation: SKIP
Dropped out of scope: 0
Scope unchecked: 0
Note: saboteur+auditor Round1 via GP fallback (quota on arl-saboteur/arl-auditor/arl-merge).

## Round 2 Summary (confirmation)

| Finding | Lens | Severity | Verdict | Action |
|---------|------|----------|---------|--------|
| All R1 fix locs | saboteur, new_hire, auditor | — | resolved by this change | Confirmed |
| nested fence template | saboteur | MAJ | Genuine | Fixed then confirmed |
| Licensing: bullet ban | saboteur | MAJ | Genuine | Fixed then confirmed |

Fixes applied: 2 (in confirmation wave)
Inflation rate: n/a (confirmation wave)
Validation: SKIP

## Converged: Round 2

Track 1: Merged verdict NO_CRITICAL_OR_MAJOR.
Total rounds: 2  |  Total fixes: 27
Document is ready.

## Amendment 1 (in progress)

| Finding | First seen | Last seen | Verdict | Rationale |
|---------|------------|-----------|---------|-----------|
| EA VERSION bullet vs RELEASE-INFO on disk | A1 | A1 | Genuine | Spec per-repo said 0.1.0-private/no RELEASE-INFO; disk has RELEASE-INFO Version 0.1.0. Aligned per-repo bullet to first-match rule. |

Why: plan author open question; live RELEASE-INFO.txt and README Version line are 0.1.0 (2026-09-18).

## Amendment 1

Confirmation: no confirmation wave (docs-only alignment to already-stated VERSION first-match rule; no new behavior surface).

## Converged: Round 2 (amended)

Track 1: Merged verdict NO_CRITICAL_OR_MAJOR.
Total rounds: 2  |  Total fixes: 28
Document is ready.
