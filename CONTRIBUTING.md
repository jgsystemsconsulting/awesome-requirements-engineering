# Contributing

Thanks for helping keep this the best-curated requirements engineering index anywhere.
Read this before opening a PR: the CI gates enforce most of it.

**Lint is mandatory.** `awesome-lint` on `README.md` must pass on every push and pull
request to `main` (`.github/workflows/lint.yml`). Do not merge with a red lint job.
Spoke maturity (RR-B packaging + sindresorhus/awesome SA bar) is documented in
[docs/MATURITY.md](docs/MATURITY.md).

The fastest path: open an [issue using the "Suggest a resource" form](../../issues/new/choose),
or open a pull request that edits `README.md` directly.

## 1. How to suggest a resource

- **Issue:** use the *Suggest a resource* form. Good for "I found this, you decide."
- **PR:** edit `README.md`, follow the entry format below, tick the PR checklist. CI
  link-checks your entry and lints the list.

## 2. Inclusion bar

An entry is accepted only if **all** hold:

1. **On-topic:** genuinely about requirements engineering as a discipline: elicitation,
   writing, management, traceability, interchange, standards, methods, tools, books,
   papers, community. SysML v2 the language lives in
   awesome-sysml-v2 (public spoke); Magic
   Grid and Cameo practice stays with the
   the awesome-mbse hub (private; text name only while hub is private).
2. **Substantive:** it teaches, demonstrates, specifies, or provides something usable.
   Not a stub. Not pure vendor marketing.
3. **Live:** the link resolves right now.
4. **Not duplicative:** not already listed (see the canonical-URL rule, §6).
5. **Legally linkable:** publicly accessible. We **link**, we never re-host model files,
   PDFs, or proprietary content.

Tie-breakers (nice-to-have, not gates): has a downloadable template or ReqIF sample
(`has-template` / `has-model`), recently updated, from a recognized source (ISO, IEEE,
OMG, IREB, Eclipse, a university, an established practitioner).

## 3. Entry format

One line per entry, **hyphen separator** (` - `, never an en/em-dash; awesome-lint
rejects those), tags as **inline code spans inside the sentence before the terminal
period**, year parenthesized as the last token:

```text
- [Resource Name](https://example.com) - One-line factual description `textual` `EARS` `tutorial` (2024).
```

- **Description:** factual, one line, **≤ 140 characters** (measured from the first
  character after ` - ` to the last character before the first tag, excluding the link
  markup and tags). No hype.
- **`has-model`** means: a **directly downloadable, non-paywalled** file in a recognized
  interchange or model format (`.reqif`, `.reqifz`, or a named tool's project file) that
  opens in a named tool. **`has-template`** means: a directly downloadable requirements
  template or pattern sheet. Screenshots and access-gated or request-only files do not
  qualify. If both apply to one resource, split it into two list entries.

## 4. Tag vocabulary, cardinality & order

Tags appear in this fixed order, drawn **only** from this vocabulary:

`language → method → tool → has-model → type → spec/standard → paid → year`

| Axis | Cardinality | Values |
| ------ | ------------- | -------- |
| language (requirement notation) | exactly 1 | `textual` · `model-based` · `RE-general` |
| method | 0 or 1 | `EARS` · `KAOS` · `Volere` · `other-method` |
| tool | 0 or more | `DOORS` · `ReqView` · `Jama` · `Visure` · `Polarion` · `other-tool` |
| has-model | 0 or 1 | `has-model` · `has-template` (pick one; a resource with two downloadables gets two entries) |
| type | exactly 1 (dominant form) | `tutorial` · `course` · `book` · `paper` · `blog` · `video` · `tool` · `plugin` · `template` · `standard` · `spec` · `guide` · `community` |
| spec/standard | 0 or 1 | `spec` · `standard` (optional echo of type when type is `spec` or `standard`) |
| paid | 0 or 1 | `paid` |
| year | exactly 1 | `(YYYY)` (see §5) |

Definitions:

- `textual`: natural-language requirement writing (EARS, quality guides, Volere template
  practice). `model-based`: goal-oriented or other model-centric RE (KAOS and kin).
  `RE-general`: the default for tools, interchange, certification, community, and
  discipline-wide standards or books with no notation focus.
- `other-tool` and `other-method` graduate to their own tags only once ≥ 3 entries share
  them.
- Type by source: ISO/IEEE normative documents are `standard`; OMG or consortium
  interchange formats are `spec`; informal practice guides are `guide`; organizations,
  conferences, and magazines are `community`; commercial and open-source products are
  `tool` (plugins are `plugin` unless they are paid commercial products). Never also use
  type `paper` on a normative document.
- Any non-free resource (tool, book, course, certification) carries `paid`. Free
  open-source tools omit it.

## 5. The year rule (`YYYY`)

`(YYYY)` = the year of the resource's **most recent author-published version**:

- a paper → its publication year;
- a repo → its latest tagged release, or the latest default-branch commit if untagged;
- a course → its current cohort year.

**Trivial edits (typo fixes) don't count.** Examples:

- A 2019 paper with a 2024 typo-fix commit → `(2019)`.
- A repo whose latest release tag is `v2.1` from 2023 → `(2023)`.

Spoke addition, for living pages: a vendor product site, organization page, or
documentation home uses the year of its most recent visible dated update; if the page
shows no date, use the year of the sweep that added the entry.

## 6. Canonical-URL rule (dedupe)

Before deciding "is this a duplicate", canonicalize both URLs: force `https`, lowercase
the host, strip a trailing slash, drop the query string and fragment unless they're
semantically required. If the canonical forms match, it's a duplicate.

## 7. Editorial neutrality

This list is maintained by JG Systems Consulting Ltd., which currently sells no
requirements-management product. To keep it trustworthy if that ever changes:

- JGS products would be listed by the **same inclusion bar** as everything else.
- Every JGS entry would sit next to **≥ 1 genuine competing/alternative entry**.
- **A superior competing tool is listed above a JGS one.** Neutrality is enforced by
  this rule, not by tone.

> **Table of Contents:** the `## Contents` ToC is hand-maintained and lists only the
> top-level sections (a flat ToC keeps awesome-lint happy). If you add or rename a
> **top-level** section, update the ToC by hand; sub-sections are not listed. CI validates
> every ToC anchor resolves (lychee `--include-fragments anchor-only`).

## 8. Local link-check

No install needed: check your changed links with Docker.

```sh
docker run --rm -v "$PWD:/d" -w /d lycheeverse/lychee --include-fragments anchor-only README.md
```

Or just open a **draft PR** and let CI check it for you.

## 9. Maintenance cadence

The maintainers run a **quarterly sweep** (add new resources, prune rot), logged in
`CHANGELOG.md` with the date, and update the *Last full sweep* badge at the top of the
README each time. If it's been **> 6 months** since the last sweep, the badge flips to
"maintenance lapsed"; call it out in an issue.
