# Awesome acceptability assessment (updated)

Date: 2026-09-18 (research refresh after public flip and README shell)
Package: P5 / follow-on research
Decision: **not go-now**. Earliest calendar window ~**2026-10-17** (30-day rule), and only after list-shape fixes below.

## Sources

- https://github.com/sindresorhus/awesome/blob/main/pull_request_template.md
- https://github.com/sindresorhus/awesome/blob/main/awesome.md
- https://github.com/sindresorhus/awesome/blob/main/create-list.md
- Incubation: https://github.com/sindresorhus/awesome/issues/2242
- Local: `npx awesome-lint@2.3.0 README.md` (1 error today)

## Hard gates from the PR template

### Process (submitter side)

1. List fully ready before opening a PR. No Draft/WIP. Use incubation issue #2242 while waiting.
2. Review at least 4 other open awesome PRs with real critique (not "LGTM"). Comment which PRs you reviewed on your own PR.
3. PR title format: `Add Requirements Engineering` (no word "Awesome", title case, verb Add).
4. Entry in their readme: bottom of the right category; title-cased name; URL ends with `#readme`; short objective theme description ending in a period; does not name the list or sound like marketing.
5. Comment the single word `unicorn` on the PR (proof you read the licence guidelines).
6. Not fully AI-generated PR text. Responsive maintainer behaviour expected.

### List age and identity

7. **At least 30 days** since first real commit or open-source date (whichever is more recent).
8. Repo name lowercase slug: `awesome-requirements-engineering` (PASS).
9. Heading title case: `# Awesome Requirements Engineering` (PASS).
10. Default branch `main` (PASS).
11. Public GitHub topics include `awesome` and `awesome-list` (PASS; also has domain topics).
12. Not a duplicate of an existing awesome entry (no RE list found on the meta-list today).
13. CC / preferably CC0 licence file at root named `LICENSE` or `license`. Code licences (MIT etc.) rejected. **Do not** put a Licence/License section in the README (GitHub shows licence in the sidebar).

### README shape (awesome-lint + template)

14. Awesome badge next to the H1, linking awesome.re (PASS).
15. First section named **Contents** (not "Table of Contents"), preferably flat, **must not** list Contributing or Footnotes.
16. Succinct top description of the **theme** (not "curated list of X resources").
17. Contribution guidelines file (`CONTRIBUTING.md`) present; optional Contributing section at top or bottom of main content, **outside** Contents.
18. Consistent entry format: `- [Name](url) - Description.` uppercase start, ends with period, hyphen separator (not en/em dash).
19. No CI badge in README. No "Inspired by awesome-..." blurb.
20. No hard-wrapping preferred; no blockchain theme.
21. Only awesome curated items; avoid unmaintained/archived without a separate file.
22. Logo/illustration encouraged when possible (not strictly mandatory).
23. Run `awesome-lint` clean before open.

## This repo vs the bar (2026-09-18)

| Gate | Status | Evidence / fix |
|---|---|---|
| Public repo | PASS | visibility public |
| Topics awesome + awesome-list | PASS | present |
| Branch main | PASS | main |
| Repo slug + H1 title case | PASS | ok |
| Awesome badge | PASS | present |
| CC0 file present | PASS file / WARN detect | `LICENSE` is CC0 text but GitHub reports `Other` / NOASSERTION; prefer GitHub CC0 community template so sidebar shows CC0 |
| CONTRIBUTING.md | PASS | present |
| 30-day maturity | **FAIL calendar** | First real commit 2026-09-17; earliest submit ~2026-10-17 |
| awesome-lint | **FAIL** | ToC item "Contributing" does not match / Contents must not feature Contributing |
| Contents purity | **FAIL** | Contents currently lists Contributing, Install, Usage, Support, Version |
| Theme blurb (not list blurb) | **FAIL shape** | `> Curated list of requirements engineering resources...` describes the list; template wants theme e.g. "Requirements engineering: elicitation, specification, management, and traceability." |
| Licence section in README | **RISK** | Support bullet starts with "Licence:"; template bans a Licence section. Safer: drop licence prose from README (sidebar + landing/footer already cover it) or keep one bare Support link without a Licence heading |
| Entry grammar | PASS | family format; lint-friendly hyphen separators |
| CI badge / inspired-by | PASS | absent |
| Dead links | **VERIFY before PR** | run product-surface lychee green on main |
| Duplicate on meta-list | PASS today | no RE entry found in sindresorhus/awesome readme search |
| Logo | optional gap | none yet; nice-to-have before review |
| Review 4 open PRs | process at submit | not done yet |
| Incubation #2242 | optional while waiting | not posted |

## Recommended entry line (for their readme, not ours)

Category: choose the best fit under Programming / Related at submit time (re-read current category list).

```markdown
- [Requirements Engineering](https://github.com/jgsystemsconsulting/awesome-requirements-engineering#readme) - Discipline of eliciting, specifying, validating, and managing requirements for systems and software.
```

Do **not** use "Awesome" in the link title. Description must not say "curated list" or repeat the list name.

## Work to do before opening the PR

### Must (blocking)

1. Wait until **2026-10-17** (or later) for the 30-day rule.
2. Fix Contents: only curated section headings. Remove Contributing, Install, Usage, Support, Version from the Contents list (sections themselves may stay at the bottom for our release standard, except drop or relocate Licence wording per template).
3. Rewrite the top blockquote to a theme sentence (not "curated list of...").
4. Get `awesome-lint` clean on README.md.
5. Confirm GitHub licence sidebar shows a Creative Commons licence (fix LICENSE detection if still Other).
6. Fresh lychee green on README.md (and keep landing healthy).
7. Re-read the live PR template the day you open; tick every box honestly.
8. Review 4 open PRs with substance; list them in your PR body.
9. Open as ready PR titled `Add Requirements Engineering`; body has list URL, why include, checklist; comment `unicorn`.

### Should

10. Optional logo/illustration (high-DPI, half width, linked) without duplicating the "Awesome X" title text.
11. Drop or shorten family/hub private pointer if it reads as noise to awesome reviewers.
12. Post a short incubation note on #2242 while waiting out the 30 days (optional visibility).

### Must not

- Open the PR before 30 days or while Contents/lint still fail.
- Title the PR `Add Awesome Requirements Engineering`.
- Put Draft in the title or use a WIP PR instead of incubation.
- Claim go-now in DISTRIBUTION until the calendar + lint gates clear.

## Decision

**Still go-with-prerequisites, not go-now.**

Public visibility is cleared. Remaining blockers are (1) the **30-day clock**, (2) **Contents / awesome-lint / theme blurb** shape conflicts introduced partly by the release-standard shell, (3) process steps at submit time (4 PR reviews, unicorn, exact entry line).

Do not open sindresorhus/awesome until Must items 1-9 are done.
