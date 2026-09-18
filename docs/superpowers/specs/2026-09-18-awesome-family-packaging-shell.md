# Spec: Awesome family packaging shell consistency

Date: 2026-09-18  
Stem: `awesome-family-packaging-shell`  
Workspace anchor: `awesome-requirements-engineering` (siblings under `../awesome-*`)

## Finding

Not every `awesome-*` repo has Install, Usage, Support, and Version sections.

| Repo | Shell today | Role |
|------|-------------|------|
| awesome-archimate | Full shell; Contents lists packaging | Public spoke |
| awesome-capella | Full shell (no Contributing H2); Contents lists packaging | Public spoke |
| awesome-stpa | Full shell (no Contributing H2); Contents lists packaging; Support has auditor note + Licence bullet | Public spoke |
| awesome-requirements-engineering | Full shell; Contents lists packaging; no Licence Support bullet | Public spoke (this repo) |
| awesome-enterprise-architect | Full shell; plain issue text; private version string | Private skeleton spoke |
| awesome-digital-engineering | No packaging shell | Public spoke |
| awesome-sysml-v2 | Contributing only | Public spoke |
| awesome-magicgrid-mbse | Contributing only | Public spoke |
| awesome-mbse | Hub: Support & security + CC0 footer | Hub (out of scope) |
| awesome-magic-grid | Same hub shape (appears tied to mbse remote) | Hub (out of scope) |
| awesome-sparx-ea | Namespace reserve README only | Reserve (out of scope) |

Among shell-present spokes, wording, Support channels, Version bolding, Contributing presence, Licence bullets, and Contents purity disagree.

## Goals

1. One canonical packaging shell on every **in-scope** curated spoke README (exhaustive set below).
2. Contents lists only curated topic sections (SA-CONTENTS family rule).
3. No `## Licence` / `## License` / `## Licensing` heading. No Support bullet whose label starts with `Licence:`, `License:`, or `Licensing:` on **any** in-scope spoke (public or private). RR-B licence enquiry stays on Pages, Release notes, DISTRIBUTION, and the LICENSE file. This pass enforces heading ban + Support-bullet ban only (not full SA-LICENCE-PROSE wording audits).
4. No curated entry rewrites, no version marketing bumps, no new issue templates, no LICENSE file edits.
5. Hubs and the sparx-ea reserve keep their existing shapes.

### In-scope repos (exhaustive)

| Path under `../` | Class |
|------------------|-------|
| `awesome-requirements-engineering` | public awesome-bound |
| `awesome-archimate` | public awesome-bound |
| `awesome-capella` | public awesome-bound |
| `awesome-stpa` | public awesome-bound |
| `awesome-digital-engineering` | public awesome-bound |
| `awesome-sysml-v2` | public awesome-bound |
| `awesome-magicgrid-mbse` | public awesome-bound |
| `awesome-enterprise-architect` | private skeleton (in scope for shell; **not** public awesome-bound) |

**public awesome-bound** = the seven public rows above. Licence Support-bullet ban still applies to enterprise-architect because it is in-scope (Goal 3).

### Out of scope (exhaustive)

- `awesome-mbse`
- `awesome-magic-grid`
- `awesome-sparx-ea`
- any other `awesome-*` path not listed in-scope

## Non-goals

- Forcing Install/Usage/Version onto hub or reserve repos.
- Building issue forms where missing.
- Resolving residual awesome-lint rules unrelated to packaging Contents items (lint Contents check is mandatory via Acceptance; full lint clean is not).
- Changing landing pages, CI, or release scripts except README-only link targets that already exist.
- Publishing commits or tags unless a later execute step says otherwise.

## Research

research: skipped (no live web fetch this run); local standards used as sources of truth.

Local sources:

- `docs/superpowers/context/2026-09-18-packaging-shell-research.md`
- `docs/superpowers/context/2026-09-18-packaging-shell-inventory.md`
- `docs/superpowers/context/2026-09-18-rr-b-packaging-excerpts.md`
- `docs/superpowers/specs/2026-09-18-awesome-acceptability-assessment.md`
- `~/.zcode/skills/release-repo-standard/references/release-repo-standard.md` (RR-B-05, RR-B-06, RR-B-07, RR-B-32)
- `~/.zcode/skills/sindresorhus-awesome-ready/references/awesome-inclusion-standard.md` (SA-CONTENTS, SA-LICENCE-README, SA-CONTRIBUTING-*)

## Conflict resolution (RR-B vs SA)

RR-B-05 Verify asks for Install, Usage, Licence, Support headings.  
SA bans a Licence/License heading in README and wants Contents free of Contributing (family also omits Install/Usage/Support/Version from Contents).

Resolution for this family pass:

- Keep Install, Usage, Support, Version, and **required** Contributing as bottom-of-README H2 sections for RR-B packaging intent on in-scope spokes.
- Never add a Licence/License/Licensing heading.
- Drop Licence/License Support bullets on every in-scope spoke.
- Strip packaging heading **names** from anywhere inside the Contents block (not only hyphen list items). Family SA-CONTENTS wins; residual stock awesome-lint tension if H2s exist but are omitted from Contents is accepted and noted in Risks.

## Canonical shell template

After the last curated topic H2 (see cut rule), replace any existing packaging H2 block with **exactly one** trailing block in this order. Do not leave a second Contributing/Install/Usage/Support/Version H2 elsewhere in the file.

Template body (copy as plain markdown; do not wrap this whole block in outer fences when editing READMEs):

## Contributing

Contributions welcome: see [<CONTRIB_FILE>](<CONTRIB_FILE>) for the inclusion bar,
entry format, and tag vocabulary.

## Install

Nothing to install. This list is a curated index: browse it here on GitHub,
or clone it:

~~~bash
git clone <CLONE_URL>
~~~

## Usage

1. Open the Contents at the top and jump to a section, or search the page with
   your browser's find function.
2. Open any entry's link to reach the upstream resource; the list never
   re-hosts content.<USAGE_STEP2_EXTRA>
3. To suggest a resource or report a defect, use the Support channels below
   (or open a pull request that follows <CONTRIB_FILE>).

## Support

- Bug or dead link: <BUG_LINE>
- Suggest a resource (the list's improvement channel): <SUGGEST_LINE>
- Security issues: <SECURITY_LINE>
<SIBLING_LINE>

## Version

Current release: **<VERSION>** (<DATE>). See [CHANGELOG.md](CHANGELOG.md)<RELEASE_INFO_CLAUSE>.

### Cut rule (last curated section)

1. Treat every `##` heading whose title is not one of `Contents`, `Contributing`, `Install`, `Usage`, `Support`, `Version`, `Licence`, `License`, `Licensing`, `Footnotes` as a **topic** heading (including empty topic sections such as "Commercial platforms").
2. The packaging shell starts immediately after the end of the last topic section body (after that section's last content line, before any old packaging H2s).
3. Delete every old packaging H2 (`Contributing`, `Install`, `Usage`, `Support`, `Version`, and any Licence/License/Licensing H2) and their bodies, then write the single canonical block once.

### Placeholder rules

| Placeholder | Rule |
|-------------|------|
| `REPO` | Directory / GitHub repo name, e.g. `awesome-capella` |
| `CONTRIB_FILE` | Real path that exists: `CONTRIBUTING.md` or `contributing.md`. Do not rename files. |
| `CLONE_URL` | `git -C <repo> remote get-url origin` normalized to `https://github.com/jgsystemsconsulting/<REPO>.git`. If origin is missing or non-GitHub, use `https://github.com/jgsystemsconsulting/<REPO>.git`. No other host. |
| `USAGE_STEP2_EXTRA` | Empty by default. Optional one extra sentence still inside step 2 (STPA only: keep PSAS query-string note). Capella and others use empty (generic step 2). |
| `BUG_LINE` | If `.github/ISSUE_TEMPLATE/` contains a file whose name matches `*bug*` (case-insensitive), use markdown link text `bug report form` pointing at `https://github.com/jgsystemsconsulting/<REPO>/issues/new?template=<that-filename>`. Else plain text: `open an issue on this repository`. |
| `SUGGEST_LINE` | If `.github/ISSUE_TEMPLATE/` contains a file whose name matches `*suggest*` (case-insensitive), use link text `suggestion form` pointing at `https://github.com/jgsystemsconsulting/<REPO>/issues/new?template=<that-filename>`. Else plain text: `open a pull request that follows <CONTRIB_FILE>, or open an issue`. |
| `SECURITY_LINE` | Always start with markdown link text `private security advisory` to `https://github.com/jgsystemsconsulting/<REPO>/security/advisories/new`. If `SECURITY.md` exists, append ` (see [SECURITY.md](SECURITY.md))`. Never invent SECURITY.md. |
| `SIBLING_LINE` | Either one full markdown list line including the leading `- `, or empty (omit the line entirely). Keep only an existing correct sibling already named in that README Support (or equivalent) today. Do not invent siblings. **false sibling** = a repo not already linked from that README's support/related prose, or not in the Finding table. Canonical example when present: `- SysML v2 language resources belong on the sibling list: [awesome-sysml-v2](https://github.com/jgsystemsconsulting/awesome-sysml-v2)` (adapt subject phrase to the list). |
| `VERSION` | Single source of truth, first match wins: (1) `RELEASE-INFO.txt` field `Version: <semver>` if file exists; (2) else existing README `## Version` body semver; (3) else latest released `CHANGELOG.md` heading semver (`## [x.y.z]` or `## x.y.z`). If two existing sources disagree, **stop and report** (do not pick silently). Do not invent a new semver. |
| `DATE` | Calendar day `YYYY-MM-DD`. First match wins: (1) `RELEASE-INFO.txt` `Built:` timestamp truncated to calendar day in UTC; (2) else date already on README Version line; (3) else date on the CHANGELOG heading used for VERSION. Same stop-on-conflict rule as VERSION when sources disagree. |
| `RELEASE_INFO_CLAUSE` | If `RELEASE-INFO.txt` exists: ` and [RELEASE-INFO.txt](RELEASE-INFO.txt)`. Else empty (sentence already ends after CHANGELOG link). Do not create RELEASE-INFO in this pass. |

### Contents purity

Locate the block that starts at `## Contents` and ends at the next `## ` heading. Inside that block, forbid the bare heading names Contributing, Install, Usage, Support, Version, Licence, License, Licensing, Footnotes (as list labels, link text, or plain words used as section pointers). Topic section names only.

Body `## Footnotes` if present is untouched; only Contents references are stripped.

### Diff bounds

Allowed edits only:

1. Inside the Contents block (purity).
2. From the first packaging H2 (or insert point after last topic section) through EOF for the single canonical shell.
3. No edits to topic section bodies or entry lines above the cut.

## Per-repo change list (in scope)

### awesome-requirements-engineering

- Replace trailing packaging block with canonical shell; Contents purity.
- Support sibling: keep awesome-sysml-v2 line (canonical example style).
- VERSION/DATE from RELEASE-INFO: **0.1.1** / 2026-09-18.
- Forms present; SECURITY.md present.

### awesome-archimate

- Replace shell; Contents purity; drop Licence Support bullet.
- Sibling: keep capella pointer, normalize to one `SIBLING_LINE`.
- VERSION/DATE: **0.1.0** / 2026-09-17 from RELEASE-INFO.
- Forms + SECURITY.md present.

### awesome-capella

- Replace shell (adds Contributing H2); Contents purity; drop Licence bullet.
- Usage: generic step 2 (`USAGE_STEP2_EXTRA` empty).
- Sibling: keep awesome-sysml-v2 pointer as `SIBLING_LINE`.
- VERSION/DATE: **0.1.0** / 2026-09-17; include RELEASE-INFO clause.
- Forms + SECURITY.md present.

### awesome-stpa

- Replace shell (adds Contributing H2); Contents purity.
- Usage: keep PSAS query-string sentence in `USAGE_STEP2_EXTRA`.
- Support: remove auditor-WARN parenthetical; drop Licence bullet; no sibling line.
- VERSION/DATE: **0.1.0** / 2026-09-17 bolded; RELEASE-INFO clause.
- Forms + SECURITY.md present.

### awesome-enterprise-architect

- Replace shell; Contents purity; drop Licence bullet (in-scope ban).
- VERSION/DATE from RELEASE-INFO first-match: **0.1.0** / 2026-09-18 (RELEASE-INFO exists; include RELEASE-INFO clause). CHANGELOG still documents the private milestone as `[0.1.0-private]`; do not invent a different Version line string than RELEASE-INFO.
- No issue forms: plain BUG_LINE / SUGGEST_LINE; SECURITY.md + advisory URL.
- No sibling line unless one already exists (today: none required).

### awesome-digital-engineering

- Cut after last topic H2 (including empty Commercial platforms); write canonical shell.
- VERSION/DATE from RELEASE-INFO: **0.1.1** / 2026-09-17.
- Forms + SECURITY.md present; sibling omit unless already present.

### awesome-sysml-v2

- Replace existing Contributing-only tail with full canonical shell (`CONTRIB_FILE=contributing.md`).
- VERSION/DATE from RELEASE-INFO: **0.1.0** / 2026-09-18.
- No bug/suggest templates: plain lines; SECURITY.md if present.
- Sibling omit unless already present.

### awesome-magicgrid-mbse

- Replace Contributing-only tail with full canonical shell (`CONTRIB_FILE=contributing.md`).
- VERSION/DATE from RELEASE-INFO: **1.0.0** / 2026-09-18.
- Plain Support lines if no forms; SECURITY.md present.
- Sibling omit unless already present.

## Acceptance checks

For each in-scope repo:

1. Exactly one each of H2 `Contributing`, `Install`, `Usage`, `Support`, `Version` appear, in that order, after the last topic H2, with no packaging H2s above the cut.
2. Contents block contains none of the forbidden packaging heading names (Acceptance Contents purity rule).
3. No H2 titled Licence, License, or Licensing.
4. No Support bullet label starts with `Licence:`, `License:`, or `Licensing:` (all in-scope, including enterprise-architect).
5. Version line matches `Current release: **<VERSION>** (<DATE>).` with bold VERSION and `YYYY-MM-DD` DATE from the VERSION/DATE rules; CHANGELOG linked; RELEASE-INFO linked iff file exists; no silent source conflict.
6. `git clone` URL equals the CLONE_URL rule output.
7. BUG_LINE / SUGGEST_LINE / SECURITY_LINE match the placeholder rules given the repo's ISSUE_TEMPLATE directory and SECURITY.md presence.
8. Diff only touches Contents block and the trailing packaging region (cut rule); topic entry lines unchanged.
9. Mandatory: Contents block has no packaging heading names (scripted grep). Optional beyond that: `npx awesome-lint` may still fail for non-Contents reasons.

## Risks

- Stock awesome-lint may still fail when packaging H2s exist but are omitted from Contents. Family SA-CONTENTS wins for this pass.
- enterprise-architect stays private; shell still applies.
- lowercase `contributing.md` must not be renamed.
- Empty topic sections still count as the cut anchor.
- Hub repos intentionally diverge; do not "fix" them without a new spec.

## Approval

Locked by user request to check all repos and make packaging sections consistent, plus constraints above. Ready for plan (step 3) and full execute.
