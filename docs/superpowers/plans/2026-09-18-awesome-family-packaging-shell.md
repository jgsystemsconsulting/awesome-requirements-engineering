# Awesome Family Packaging Shell Consistency Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Put one canonical packaging shell (Contributing, Install, Usage, Support, Version) on the README of every in-scope `awesome-*` spoke, strip packaging names out of every Contents block, and ban Licence headings and Licence Support bullets, without touching curated entries, hubs, or the sparx-ea reserve.

**Architecture:** README-only edits across eight sibling repositories under `C:\Users\gower\OneDrive\Documents\GitHub\`. Each repo gets one task: compute placeholders from on-disk facts (git remote, RELEASE-INFO.txt, ISSUE_TEMPLATE directory, SECURITY.md), apply the Contents purity edit, then replace the trailing packaging region with the single canonical block from the spec's cut rule. A final cross-repo Python verifier re-checks Acceptance 1–7 and 9 mechanically; Acceptance 8 stays on each task's git-diff porcelain step. Nothing is committed; diffs stay in the working trees for user review.

**Tech Stack:** Plain markdown, Git Bash (grep, git diff), Python 3 standard library for the cross-repo verifier. No new dependencies.

**Spec:** `docs/superpowers/specs/2026-09-18-awesome-family-packaging-shell.md` (workspace root: `C:\Users\gower\OneDrive\Documents\GitHub\awesome-requirements-engineering\`)

**Research marker:** research: skipped (local standards + inventory only)

## Codebase context

Context documents this plan was built from (all paths under the workspace root unless noted):

- `docs/superpowers/context/2026-09-18-packaging-shell-research.md`: conflict analysis and locked canonical shell
- `docs/superpowers/context/2026-09-18-packaging-shell-inventory.md`: per-repo shell inventory (stale in two places; the live files read for this plan win, see Task notes)
- `docs/superpowers/context/2026-09-18-rr-b-packaging-excerpts.md`: RR-B-05/06/07/32 text
- `~/.zcode/skills/release-repo-standard/references/release-repo-standard.md` and `~/.zcode/skills/sindresorhus-awesome-ready/references/awesome-inclusion-standard.md`: RR-B and SA rules the spec resolves

The plan body already contains the exact final text for every edit; no implementer should re-derive policy from the standards files. On-disk facts verified 2026-09-18: every in-scope repo has `RELEASE-INFO.txt`, `CHANGELOG.md`, `LICENSE`, and `SECURITY.md`. Origin remotes are all `https://github.com/jgsystemsconsulting/<REPO>.git`. Issue form filenames: `bug_report.yml` and `suggest-resource.yml` exist in requirements-engineering, archimate, capella, stpa, digital-engineering (digital-engineering also has `improvement.yml`, unused by the template). No `.github/ISSUE_TEMPLATE/` directory exists in enterprise-architect, sysml-v2, magicgrid-mbse.

## Global Constraints

These apply to every task. Values are copied from the spec.

- In-scope repos (exhaustive): `awesome-requirements-engineering`, `awesome-archimate`, `awesome-capella`, `awesome-stpa`, `awesome-digital-engineering`, `awesome-sysml-v2`, `awesome-magicgrid-mbse`, `awesome-enterprise-architect`.
- Out of scope (exhaustive): `awesome-mbse`, `awesome-magic-grid`, `awesome-sparx-ea`, and any other `awesome-*` path. Do not open or edit them.
- Section order after the last curated topic H2: `Contributing`, `Install`, `Usage`, `Support`, `Version`. Exactly one of each H2, no packaging H2s above the cut.
- No H2 titled `Licence`, `License`, or `Licensing`. No Support bullet whose label starts with `Licence:`, `License:`, or `Licensing:`.
- Contents block lists topic sections only. Forbidden **as whole Contents list labels** (the text inside `- [Label](...)`): Contributing, Install, Usage, Support, Version, Licence, License, Licensing, Footnotes. Compound topic titles such as `Tool Support` are allowed because the label is not exactly `Support`.
- Diff bounds: edits only inside the Contents block and from the first packaging H2 (or insert point after the last topic section) through EOF. Topic section bodies and entry lines above the cut are untouched.
- Version line shape (every in-scope repo has RELEASE-INFO.txt, so the RELEASE-INFO clause is always present): `Current release: **<VERSION>** (<DATE>). See [CHANGELOG.md](CHANGELOG.md) and` newline `[RELEASE-INFO.txt](RELEASE-INFO.txt).`
- Do not bump versions. VERSION and DATE come from `RELEASE-INFO.txt` (`Version:` field, `Built:` timestamp truncated to `YYYY-MM-DD` UTC) in every in-scope repo.
- No curated entry rewrites, no new issue templates, no LICENSE or SECURITY.md creation, no RELEASE-INFO creation. `contributing.md` (lowercase, sysml-v2 and magicgrid-mbse) is never renamed.
- Clone URL is always `https://github.com/jgsystemsconsulting/<REPO>.git`; all eight origin remotes already match.
- Default is uncommitted work: no `git add`, no `git commit` in any repo. Optional user commit step appears only at the very end.
- Residual stock awesome-lint tension (packaging H2s omitted from Contents) is accepted per spec; full lint clean is not a goal.

## Files touched

All eight are `README.md` in sibling repos. Absolute paths:

- `C:\Users\gower\OneDrive\Documents\GitHub\awesome-requirements-engineering\README.md`
- `C:\Users\gower\OneDrive\Documents\GitHub\awesome-archimate\README.md`
- `C:\Users\gower\OneDrive\Documents\GitHub\awesome-capella\README.md`
- `C:\Users\gower\OneDrive\Documents\GitHub\awesome-stpa\README.md`
- `C:\Users\gower\OneDrive\Documents\GitHub\awesome-enterprise-architect\README.md`
- `C:\Users\gower\OneDrive\Documents\GitHub\awesome-digital-engineering\README.md`
- `C:\Users\gower\OneDrive\Documents\GitHub\awesome-sysml-v2\README.md`
- `C:\Users\gower\OneDrive\Documents\GitHub\awesome-magicgrid-mbse\README.md`

No other files are created or modified anywhere. The Task 9 verifier is run from a heredoc, not saved to disk.

---

### Task 1: awesome-requirements-engineering

**Files:**
- Modify: `C:\Users\gower\OneDrive\Documents\GitHub\awesome-requirements-engineering\README.md`

**Model:** flash

This shell is already canonical on disk (Contributing through Version, generic Usage, form links, SECURITY.md clause, SysML v2 sibling line in canonical style, bold `**0.1.1** (2026-09-18)` with RELEASE-INFO clause). The only edit is Contents purity.

- [ ] **Step 1: Confirm placeholders from disk (no edits yet)**

Run from `C:\Users\gower\OneDrive\Documents\GitHub\awesome-requirements-engineering`:

```bash
git remote get-url origin          # expect https://github.com/jgsystemsconsulting/awesome-requirements-engineering.git
grep -E "^(Version|Built):" RELEASE-INFO.txt   # expect Version: 0.1.1 and Built: 2026-09-18T...
ls .github/ISSUE_TEMPLATE          # expect bug_report.yml config.yml suggest-resource.yml
ls SECURITY.md                     # expect SECURITY.md
```

Expected placeholders: VERSION `0.1.1`, DATE `2026-09-18`, forms present, SECURITY.md present, sibling SysML line kept. If any output differs from these expectations, stop and report before editing.

- [ ] **Step 2: Contents purity edit**

Delete exactly these four list items from the `## Contents` block (they sit between `- [Learning, certification, and community](#learning-certification-and-community)` and the `## Standards and guides` heading):

```markdown
- [Install](#install)
- [Usage](#usage)
- [Support](#support)
- [Version](#version)
```

Nothing else inside Contents changes. Touch nothing above or below the Contents block.

- [ ] **Step 3: Verify the shell matches the canonical template verbatim**

The trailing block must read exactly (confirm with `git diff` and the greps; no text changes expected in this step):

````markdown
## Contributing

Contributions welcome: see [CONTRIBUTING.md](CONTRIBUTING.md) for the inclusion bar,
entry format, and tag vocabulary.

## Install

Nothing to install. This list is a curated index: browse it here on GitHub,
or clone it:

```bash
git clone https://github.com/jgsystemsconsulting/awesome-requirements-engineering.git
```

## Usage

1. Open the Contents at the top and jump to a section, or search the page with
   your browser's find function.
2. Open any entry's link to reach the upstream resource; the list never
   re-hosts content.
3. To suggest a resource or report a defect, use the Support channels below
   (or open a pull request that follows CONTRIBUTING.md).

## Support

- Bug or dead link: [bug report form](https://github.com/jgsystemsconsulting/awesome-requirements-engineering/issues/new?template=bug_report.yml)
- Suggest a resource (the list's improvement channel):
  [suggestion form](https://github.com/jgsystemsconsulting/awesome-requirements-engineering/issues/new?template=suggest-resource.yml)
- Security issues: [private security advisory](https://github.com/jgsystemsconsulting/awesome-requirements-engineering/security/advisories/new)
  (see [SECURITY.md](SECURITY.md))
- SysML v2 language resources belong on the sibling list:
  [awesome-sysml-v2](https://github.com/jgsystemsconsulting/awesome-sysml-v2)

## Version

Current release: **0.1.1** (2026-09-18). See [CHANGELOG.md](CHANGELOG.md) and
[RELEASE-INFO.txt](RELEASE-INFO.txt).
````

- [ ] **Step 4: Run verification commands (Acceptance 1 to 7, 9)**

Run in the repo root:

```bash
grep -n "^## " README.md
grep -nE "^- \[(Install|Usage|Support|Version)\]" README.md
grep -nE "^## (Licence|License|Licensing)$" README.md
grep -nE "^- (Licence|License|Licensing):" README.md
grep -n "Current release" README.md
grep -n "git clone" README.md
```

Expected: the H2 list shows Contents, the seven topic sections, then Contributing, Install, Usage, Support, Version in that order and nothing after; the first pattern grep returns no matches; the Licence greps return no matches; the Version line matches the template above; the clone line matches the origin URL.

- [ ] **Step 5: Diff bounds check (Acceptance 8)**

Run:

```bash
git status --porcelain        # expect only " M README.md"
git diff -- README.md         # expect one hunk, inside the Contents block only
```

If any hunk falls outside the Contents block, restore with `git restore README.md` and redo Step 2.

---

### Task 2: awesome-archimate

**Files:**
- Modify: `C:\Users\gower\OneDrive\Documents\GitHub\awesome-archimate\README.md`

**Model:** flash

Shell is canonical on disk except the sibling line points at the capella issues tracker instead of the repo root. Licence Support bullet is already absent from the live file (the inventory excerpt is stale); verify and drop only if found. Two edits: Contents purity, sibling normalization.

- [ ] **Step 1: Confirm placeholders from disk**

Run from `C:\Users\gower\OneDrive\Documents\GitHub\awesome-archimate`:

```bash
git remote get-url origin          # expect https://github.com/jgsystemsconsulting/awesome-archimate.git
grep -E "^(Version|Built):" RELEASE-INFO.txt   # expect Version: 0.1.0 and Built: 2026-09-17T...
ls .github/ISSUE_TEMPLATE          # expect bug_report.yml config.yml suggest-resource.yml
ls SECURITY.md                     # expect SECURITY.md
```

Expected placeholders: VERSION `0.1.0`, DATE `2026-09-17`, forms present, SECURITY.md present, sibling capella pointer kept and normalized. Stop and report if any output differs.

- [ ] **Step 2: Contents purity edit**

Delete exactly these four list items from the `## Contents` block (between `- [Communities](#communities)` and `## Specifications and standards`):

```markdown
- [Install](#install)
- [Usage](#usage)
- [Support](#support)
- [Version](#version)
```

- [ ] **Step 3: Normalize the sibling line inside Support**

Replace this pair of lines:

```markdown
- Capella and Arcadia resources belong on the sibling list:
  [awesome-capella issues](https://github.com/jgsystemsconsulting/awesome-capella/issues)
```

with:

```markdown
- Capella and Arcadia resources belong on the sibling list:
  [awesome-capella](https://github.com/jgsystemsconsulting/awesome-capella)
```

This is the one `SIBLING_LINE`, canonical style, pointing at the repo root.

- [ ] **Step 4: Confirm the rest of the shell is canonical and no Licence bullet remains**

The trailing block from `## Contributing` must already match the canonical template (same body as Task 1 Step 3 with repo name `awesome-archimate`, VERSION `**0.1.0**`, DATE `(2026-09-17)`, and the Step 3 sibling line). If a Support bullet starting with `- Licence:` or similar licence prose exists anywhere in Support, delete that bullet; on the live file none is expected.

- [ ] **Step 5: Run verification commands (Acceptance 1 to 7, 9)**

Run in the repo root:

```bash
grep -n "^## " README.md
grep -nE "^- \[(Install|Usage|Support|Version)\]" README.md
grep -nE "^## (Licence|License|Licensing)$" README.md
grep -nE "^- (Licence|License|Licensing):" README.md
grep -n "Current release" README.md
grep -n "git clone" README.md
grep -n "awesome-capella" README.md
```

Expected: H2 order Contents, eight topic sections, Contributing, Install, Usage, Support, Version; packaging names gone from Contents; no Licence heading or bullet; Version line `Current release: **0.1.0** (2026-09-17). See [CHANGELOG.md](CHANGELOG.md) and` / `[RELEASE-INFO.txt](RELEASE-INFO.txt).`; clone URL matches origin; the only `awesome-capella` reference in Support points at the repo root, not `/issues`.

- [ ] **Step 6: Diff bounds check (Acceptance 8)**

Run:

```bash
git status --porcelain        # expect only " M README.md"
git diff -- README.md         # expect two hunks: one in Contents, one in the Support sibling lines
```

No hunk may touch topic sections or entry lines above the cut.

---

### Task 3: awesome-capella

**Files:**
- Modify: `C:\Users\gower\OneDrive\Documents\GitHub\awesome-capella\README.md`

**Model:** flash

Capella has no Contributing H2 today (the spec adds it), a non-canonical Install sentence, a non-canonical Usage block, non-canonical Support labels, and no RELEASE-INFO clause in Version. Replace the whole trailing packaging region (first packaging H2 is `## Install`) with the canonical block, which also adds the missing Licence-bullet drop for free (none exists on the live file; the replacement guarantees it).

- [ ] **Step 1: Confirm placeholders from disk**

Run from `C:\Users\gower\OneDrive\Documents\GitHub\awesome-capella`:

```bash
git remote get-url origin          # expect https://github.com/jgsystemsconsulting/awesome-capella.git
grep -E "^(Version|Built):" RELEASE-INFO.txt   # expect Version: 0.1.0 and Built: 2026-09-17T...
ls .github/ISSUE_TEMPLATE          # expect bug_report.yml config.yml suggest-resource.yml
ls SECURITY.md CONTRIBUTING.md     # expect both present
```

Expected placeholders: VERSION `0.1.0`, DATE `2026-09-17`, forms present, SECURITY.md present, `CONTRIB_FILE=CONTRIBUTING.md`, generic Usage (`USAGE_STEP2_EXTRA` empty), sibling SysML v2 pointer kept as the canonical line. Stop and report if any output differs.

- [ ] **Step 2: Contents purity edit**

Delete exactly these four list items from the `## Contents` block (between `- [Commercial offers](#commercial-offers)` and `## Arcadia method`):

```markdown
- [Install](#install)
- [Usage](#usage)
- [Support](#support)
- [Version](#version)
```

- [ ] **Step 3: Replace the packaging region with the canonical block**

Delete everything from the line `## Install` through end of file (this removes the old Install, Usage, Support, and Version sections and any stray trailing blank lines). Then append exactly this block, preceded by one blank line after the last topic section body (the `## Commercial offers` list ends the file above the cut):

````markdown
## Contributing

Contributions welcome: see [CONTRIBUTING.md](CONTRIBUTING.md) for the inclusion bar,
entry format, and tag vocabulary.

## Install

Nothing to install. This list is a curated index: browse it here on GitHub,
or clone it:

```bash
git clone https://github.com/jgsystemsconsulting/awesome-capella.git
```

## Usage

1. Open the Contents at the top and jump to a section, or search the page with
   your browser's find function.
2. Open any entry's link to reach the upstream resource; the list never
   re-hosts content.
3. To suggest a resource or report a defect, use the Support channels below
   (or open a pull request that follows CONTRIBUTING.md).

## Support

- Bug or dead link: [bug report form](https://github.com/jgsystemsconsulting/awesome-capella/issues/new?template=bug_report.yml)
- Suggest a resource (the list's improvement channel):
  [suggestion form](https://github.com/jgsystemsconsulting/awesome-capella/issues/new?template=suggest-resource.yml)
- Security issues: [private security advisory](https://github.com/jgsystemsconsulting/awesome-capella/security/advisories/new)
  (see [SECURITY.md](SECURITY.md))
- SysML v2 language resources belong on the sibling list:
  [awesome-sysml-v2](https://github.com/jgsystemsconsulting/awesome-sysml-v2)

## Version

Current release: **0.1.0** (2026-09-17). See [CHANGELOG.md](CHANGELOG.md) and
[RELEASE-INFO.txt](RELEASE-INFO.txt).
````

The old `- Sibling SysML v2 list issues: [awesome-sysml-v2 issues](.../issues)` line is deleted by the block replacement and re-added in canonical repo-root style above.

- [ ] **Step 4: Run verification commands (Acceptance 1 to 7, 9)**

Run in the repo root:

```bash
grep -n "^## " README.md
grep -nE "^- \[(Install|Usage|Support|Version)\]" README.md
grep -nE "^## (Licence|License|Licensing)$" README.md
grep -nE "^- (Licence|License|Licensing):" README.md
grep -n "Current release" README.md
grep -n "git clone" README.md
grep -cn "## Contributing" README.md   # expect 1
```

Expected: H2 order Contents, nine topic sections, Contributing, Install, Usage, Support, Version; no packaging names in Contents; no Licence heading or bullet; Version line bold `**0.1.0**` with `(2026-09-17)` and both links; clone URL matches origin; exactly one Contributing H2.

- [ ] **Step 5: Diff bounds check (Acceptance 8)**

Run:

```bash
git status --porcelain        # expect only " M README.md"
git diff -- README.md         # expect hunks only in Contents and from old "## Install" through EOF
```

The nine topic section bodies above the cut must show no changes.

---

### Task 4: awesome-stpa

**Files:**
- Modify: `C:\Users\gower\OneDrive\Documents\GitHub\awesome-stpa\README.md`

**Model:** flash

STPA has no Contributing H2, a product-specific Usage step 2 (the PSAS query-string note, kept per spec as `USAGE_STEP2_EXTRA`), non-canonical Support labels, an auditor-WARN parenthetical to remove, and a plain (unbolded) Version. No sibling line in Support (the `## Related lists` topic section stays untouched). First packaging H2 is `## Install`.

- [ ] **Step 1: Confirm placeholders from disk**

Run from `C:\Users\gower\OneDrive\Documents\GitHub\awesome-stpa`:

```bash
git remote get-url origin          # expect https://github.com/jgsystemsconsulting/awesome-stpa.git
grep -E "^(Version|Built):" RELEASE-INFO.txt   # expect Version: 0.1.0 and Built: 2026-09-17T...
ls .github/ISSUE_TEMPLATE          # expect bug_report.yml config.yml suggest-resource.yml
ls SECURITY.md CONTRIBUTING.md     # expect both present
```

Expected placeholders: VERSION `0.1.0`, DATE `2026-09-17`, forms present, SECURITY.md present, `CONTRIB_FILE=CONTRIBUTING.md`, `USAGE_STEP2_EXTRA` keeps the PSAS sentence, no sibling line. Stop and report if any output differs.

- [ ] **Step 2: Contents purity edit**

Delete exactly these four list items from the `## Contents` block (between `- [Related lists](#related-lists)` and `## Foundations & Handbooks`):

```markdown
- [Install](#install)
- [Usage](#usage)
- [Support](#support)
- [Version](#version)
```

- [ ] **Step 3: Replace the packaging region with the canonical block**

Delete everything from the line `## Install` through end of file. Then append exactly this block, preceded by one blank line after the last topic section body (the `## Related lists` list):

````markdown
## Contributing

Contributions welcome: see [CONTRIBUTING.md](CONTRIBUTING.md) for the inclusion bar,
entry format, and tag vocabulary.

## Install

Nothing to install. This list is a curated index: browse it here on GitHub,
or clone it:

```bash
git clone https://github.com/jgsystemsconsulting/awesome-stpa.git
```

## Usage

1. Open the Contents at the top and jump to a section, or search the page with
   your browser's find function.
2. Open any entry's link to reach the upstream resource; the list never
   re-hosts content. PSAS handbook and paper links keep their query
   strings; they are part of the address.
3. To suggest a resource or report a defect, use the Support channels below
   (or open a pull request that follows CONTRIBUTING.md).

## Support

- Bug or dead link: [bug report form](https://github.com/jgsystemsconsulting/awesome-stpa/issues/new?template=bug_report.yml)
- Suggest a resource (the list's improvement channel):
  [suggestion form](https://github.com/jgsystemsconsulting/awesome-stpa/issues/new?template=suggest-resource.yml)
- Security issues: [private security advisory](https://github.com/jgsystemsconsulting/awesome-stpa/security/advisories/new)
  (see [SECURITY.md](SECURITY.md))

## Version

Current release: **0.1.0** (2026-09-17). See [CHANGELOG.md](CHANGELOG.md) and
[RELEASE-INFO.txt](RELEASE-INFO.txt).
````

Note what this replacement removes: the `Dead or wrong entry:` label (canonical is `Bug or dead link:`), the auditor-WARN parenthetical on the suggest bullet, the trailing `; non-sensitive fixes come as pull requests.` on the security bullet, and the unbolded Version. None of them reappear. Do not add a sibling line.

- [ ] **Step 4: Run verification commands (Acceptance 1–7 and 9)**

  Also confirm Usage contains: `PSAS handbook and paper links keep their query`.

Run in the repo root:

```bash
grep -n "^## " README.md
grep -nE "^- \[(Install|Usage|Support|Version)\]" README.md
grep -nE "^## (Licence|License|Licensing)$" README.md
grep -nE "^- (Licence|License|Licensing):" README.md
grep -n "Current release" README.md
grep -n "git clone" README.md
grep -n "WARN" README.md               # expect no match anywhere in README
```

Expected: H2 order Contents, seven topic sections, Contributing, Install, Usage, Support, Version; no packaging names in Contents; no Licence heading or bullet; Version bold `**0.1.0** (2026-09-17)` with both links; clone URL matches origin; no WARN text remains; the PSAS sentence survives inside Usage step 2.

- [ ] **Step 5: Diff bounds check (Acceptance 8)**

Run:

```bash
git status --porcelain        # expect only " M README.md"
git diff -- README.md         # expect hunks only in Contents and from old "## Install" through EOF
```

The seven topic section bodies, including `## Related lists` and its three entries, must show no changes.

---

### Task 5: awesome-enterprise-architect

**Files:**
- Modify: `C:\Users\gower\OneDrive\Documents\GitHub\awesome-enterprise-architect\README.md`

**Model:** flash

Private skeleton, still in scope for the shell. No issue forms: plain BUG and SUGGEST lines. SECURITY.md present. The live Support has a licence-prose bullet (`- This list is released under [CC0 1.0 Universal](LICENSE)...`) which the block replacement removes.

**Version note:** Spec per-repo bullet and RELEASE-INFO agree: `**0.1.0** (2026-09-18)` with the RELEASE-INFO clause. CHANGELOG still titles the milestone `[0.1.0-private]`; do not put that string on the Version line.

- [ ] **Step 1: Confirm placeholders from disk**

Run from `C:\Users\gower\OneDrive\Documents\GitHub\awesome-enterprise-architect`:

```bash
git remote get-url origin          # expect https://github.com/jgsystemsconsulting/awesome-enterprise-architect.git
grep -E "^(Version|Built):" RELEASE-INFO.txt   # expect Version: 0.1.0 and Built: 2026-09-18T...
ls .github/ISSUE_TEMPLATE 2>/dev/null || echo "no ISSUE_TEMPLATE"   # expect "no ISSUE_TEMPLATE"
ls SECURITY.md CONTRIBUTING.md     # expect both present
```

Expected placeholders: VERSION `0.1.0` (per the Version note above), DATE `2026-09-18`, plain BUG/SUGGEST lines, SECURITY.md clause, `CONTRIB_FILE=CONTRIBUTING.md`, no sibling line.

- [ ] **Step 2: Contents purity edit**

Delete exactly these four list items from the `## Contents` block (between `- [Related family lists](#related-family-lists)` and `## Official product and docs`):

```markdown
- [Install](#install)
- [Usage](#usage)
- [Support](#support)
- [Version](#version)
```

- [ ] **Step 3: Replace the packaging region with the canonical block**

Delete everything from the line `## Contributing` (the first packaging H2, line 132 area) through end of file. Then append exactly this block, preceded by one blank line after the last topic section body (`## Related family lists` ends with "...never copy full entries between the two." plus the sibling paragraph):

````markdown
## Contributing

Contributions welcome: see [CONTRIBUTING.md](CONTRIBUTING.md) for the inclusion bar,
entry format, and tag vocabulary.

## Install

Nothing to install. This list is a curated index: browse it here on GitHub,
or clone it:

```bash
git clone https://github.com/jgsystemsconsulting/awesome-enterprise-architect.git
```

## Usage

1. Open the Contents at the top and jump to a section, or search the page with
   your browser's find function.
2. Open any entry's link to reach the upstream resource; the list never
   re-hosts content.
3. To suggest a resource or report a defect, use the Support channels below
   (or open a pull request that follows CONTRIBUTING.md).

## Support

- Bug or dead link: open an issue on this repository
- Suggest a resource (the list's improvement channel): open a pull request
  that follows CONTRIBUTING.md, or open an issue
- Security issues: [private security advisory](https://github.com/jgsystemsconsulting/awesome-enterprise-architect/security/advisories/new)
  (see [SECURITY.md](SECURITY.md))

## Version

Current release: **0.1.0** (2026-09-18). See [CHANGELOG.md](CHANGELOG.md) and
[RELEASE-INFO.txt](RELEASE-INFO.txt).
````

The old CC0 licence-prose Support bullet is deleted by the replacement and does not reappear. No sibling line.

- [ ] **Step 4: Run verification commands (Acceptance 1 to 7, 9)**

Run in the repo root:

```bash
grep -n "^## " README.md
grep -nE "^- \[(Install|Usage|Support|Version)\]" README.md
grep -nE "^## (Licence|License|Licensing)$" README.md
grep -nE "^- (Licence|License|Licensing):" README.md
grep -n "Current release" README.md
grep -n "git clone" README.md
grep -n "CC0" README.md                # expect no match in README
```

Expected: H2 order Contents, eight topic sections, Contributing, Install, Usage, Support, Version; no packaging names in Contents; no Licence heading, Licence bullet, or CC0 licence bullet in Support; Version bold `**0.1.0** (2026-09-18)` with both links; clone URL matches origin.

- [ ] **Step 5: Diff bounds check (Acceptance 8)**

Run:

```bash
git status --porcelain        # expect only " M README.md"
git diff -- README.md         # expect hunks only in Contents and from old "## Contributing" through EOF
```

The eight topic section bodies must show no changes.

---

### Task 6: awesome-digital-engineering

**Files:**
- Modify: `C:\Users\gower\OneDrive\Documents\GitHub\awesome-digital-engineering\README.md`

**Model:** flash

No packaging shell today. The last topic H2 is `## Commercial platforms`, an empty topic section whose body is `_No verified entries yet._`; empty topic sections still count as the cut anchor per spec. The file has no packaging H2 to delete, so this task only appends. The inline intro paragraph (lines 18 to 25, the bolded `**Install:**` / `**Usage:**` / `**Support:**` prose) is above the cut and outside the allowed diff bounds: leave it byte-for-byte unchanged. Contents is already pure (no packaging names); verify, do not edit.

- [ ] **Step 1: Confirm placeholders from disk**

Run from `C:\Users\gower\OneDrive\Documents\GitHub\awesome-digital-engineering`:

```bash
git remote get-url origin          # expect https://github.com/jgsystemsconsulting/awesome-digital-engineering.git
grep -E "^(Version|Built):" RELEASE-INFO.txt   # expect Version: 0.1.1 and Built: 2026-09-17T...
ls .github/ISSUE_TEMPLATE          # expect bug_report.yml config.yml improvement.yml suggest-resource.yml
ls SECURITY.md CONTRIBUTING.md     # expect both present
```

Expected placeholders: VERSION `0.1.1`, DATE `2026-09-17`, forms present (`improvement.yml` is not referenced by the canonical Support block and is ignored), SECURITY.md clause, `CONTRIB_FILE=CONTRIBUTING.md`, no sibling line. Stop and report if any output differs.

- [ ] **Step 2: Verify Contents purity holds (no edit expected)**

Run:

```bash
sed -n '/^## Contents/,/^## Policy/p' README.md
```

Expected: the Contents block lists the eight topic sections only, none of the forbidden names. If any forbidden name appears, delete that list item and nothing else; on the live file none is expected.

- [ ] **Step 3: Append the canonical block after the last topic section**

The file currently ends with the `## Commercial platforms` section (`_No verified entries yet._` plus a trailing newline). Append exactly this block, preceded by one blank line:

````markdown
## Contributing

Contributions welcome: see [CONTRIBUTING.md](CONTRIBUTING.md) for the inclusion bar,
entry format, and tag vocabulary.

## Install

Nothing to install. This list is a curated index: browse it here on GitHub,
or clone it:

```bash
git clone https://github.com/jgsystemsconsulting/awesome-digital-engineering.git
```

## Usage

1. Open the Contents at the top and jump to a section, or search the page with
   your browser's find function.
2. Open any entry's link to reach the upstream resource; the list never
   re-hosts content.
3. To suggest a resource or report a defect, use the Support channels below
   (or open a pull request that follows CONTRIBUTING.md).

## Support

- Bug or dead link: [bug report form](https://github.com/jgsystemsconsulting/awesome-digital-engineering/issues/new?template=bug_report.yml)
- Suggest a resource (the list's improvement channel):
  [suggestion form](https://github.com/jgsystemsconsulting/awesome-digital-engineering/issues/new?template=suggest-resource.yml)
- Security issues: [private security advisory](https://github.com/jgsystemsconsulting/awesome-digital-engineering/security/advisories/new)
  (see [SECURITY.md](SECURITY.md))

## Version

Current release: **0.1.1** (2026-09-17). See [CHANGELOG.md](CHANGELOG.md) and
[RELEASE-INFO.txt](RELEASE-INFO.txt).
````

Do not touch the intro paragraph, any topic section, or the Contents block.

- [ ] **Step 4: Run verification commands (Acceptance 1 to 7, 9)**

Run in the repo root:

```bash
grep -n "^## " README.md
grep -nE "^- \[(Install|Usage|Support|Version)\]" README.md
grep -nE "^## (Licence|License|Licensing)$" README.md
grep -nE "^- (Licence|License|Licensing):" README.md
grep -n "Current release" README.md
grep -n "git clone" README.md
```

Expected: H2 order Contents, eight topic sections (Commercial platforms last among topics), Contributing, Install, Usage, Support, Version; no packaging names in Contents; no Licence heading or bullet; Version bold `**0.1.1** (2026-09-17)` with both links; clone URL matches origin.

- [ ] **Step 5: Diff bounds check (Acceptance 8)**

Run:

```bash
git status --porcelain        # expect only " M README.md"
git diff -- README.md         # expect exactly one hunk, pure addition at EOF after "_No verified entries yet._"
```

The intro paragraph (including its bolded packaging prose) must show as unchanged.

---

### Task 7: awesome-sysml-v2

**Files:**
- Modify: `C:\Users\gower\OneDrive\Documents\GitHub\awesome-sysml-v2\README.md`

**Model:** flash

Contributing-only tail today. Replace it with the full canonical shell. `CONTRIB_FILE=contributing.md` (lowercase on disk; never rename). No issue templates: plain BUG and SUGGEST lines. SECURITY.md present. No sibling line (nothing exists in Support today; the intro's magicgrid-mbse mention is prose above the cut and stays as is). Contents is already pure; verify, do not edit.

- [ ] **Step 1: Confirm placeholders from disk**

Run from `C:\Users\gower\OneDrive\Documents\GitHub\awesome-sysml-v2`:

```bash
git remote get-url origin          # expect https://github.com/jgsystemsconsulting/awesome-sysml-v2.git
grep -E "^(Version|Built):" RELEASE-INFO.txt   # expect Version: 0.1.0 and Built: 2026-09-18T...
ls .github/ISSUE_TEMPLATE 2>/dev/null || echo "no ISSUE_TEMPLATE"   # expect "no ISSUE_TEMPLATE"
ls SECURITY.md contributing.md     # expect both present, lowercase contributing.md
```

Expected placeholders: VERSION `0.1.0`, DATE `2026-09-18`, plain BUG/SUGGEST lines, SECURITY.md clause, `CONTRIB_FILE=contributing.md`, no sibling line. Stop and report if any output differs.

- [ ] **Step 2: Verify Contents purity holds (no edit expected)**

Run:

```bash
sed -n '/^## Contents/,/^## Specifications/p' README.md
```

Expected: the Contents block lists the eleven topic sections only, none of the forbidden names. Delete any forbidden list item if found; none is expected.

- [ ] **Step 3: Replace the Contributing-only tail with the canonical shell**

Delete everything from the line `## Contributing` through end of file. Then append exactly this block, preceded by one blank line after the last topic section body (`## Migrating from SysML v1`):

````markdown
## Contributing

Contributions welcome: see [contributing.md](contributing.md) for the inclusion bar,
entry format, and tag vocabulary.

## Install

Nothing to install. This list is a curated index: browse it here on GitHub,
or clone it:

```bash
git clone https://github.com/jgsystemsconsulting/awesome-sysml-v2.git
```

## Usage

1. Open the Contents at the top and jump to a section, or search the page with
   your browser's find function.
2. Open any entry's link to reach the upstream resource; the list never
   re-hosts content.
3. To suggest a resource or report a defect, use the Support channels below
   (or open a pull request that follows contributing.md).

## Support

- Bug or dead link: open an issue on this repository
- Suggest a resource (the list's improvement channel): open a pull request
  that follows contributing.md, or open an issue
- Security issues: [private security advisory](https://github.com/jgsystemsconsulting/awesome-sysml-v2/security/advisories/new)
  (see [SECURITY.md](SECURITY.md))

## Version

Current release: **0.1.0** (2026-09-18). See [CHANGELOG.md](CHANGELOG.md) and
[RELEASE-INFO.txt](RELEASE-INFO.txt).
````

Note the Contributing body is rewritten from the old "inclusion criteria, entry format, local lint commands, and maintenance cadence" wording to the canonical two-line body; that is part of the spec's "replace existing Contributing-only tail with full canonical shell".

- [ ] **Step 4: Run verification commands (Acceptance 1 to 7, 9)**

Run in the repo root:

```bash
grep -n "^## " README.md
grep -nE "^- \[(Install|Usage|Support|Version)\]" README.md
grep -nE "^## (Licence|License|Licensing)$" README.md
grep -nE "^- (Licence|License|Licensing):" README.md
grep -n "Current release" README.md
grep -n "git clone" README.md
ls contributing.md            # expect file still present, unrenamed
```

Expected: H2 order Contents, eleven topic sections, Contributing, Install, Usage, Support, Version; no packaging names in Contents; no Licence heading or bullet; Version bold `**0.1.0** (2026-09-18)` with both links; clone URL matches origin; `contributing.md` untouched.

- [ ] **Step 5: Diff bounds check (Acceptance 8)**

Run:

```bash
git status --porcelain        # expect only " M README.md"
git diff -- README.md         # expect exactly one hunk replacing the old Contributing tail through EOF
```

All eleven topic section bodies must show no changes.

---

### Task 8: awesome-magicgrid-mbse

**Files:**
- Modify: `C:\Users\gower\OneDrive\Documents\GitHub\awesome-magicgrid-mbse\README.md`

**Model:** flash

Same shape as Task 7: Contributing-only tail, replaced with the full canonical shell. `CONTRIB_FILE=contributing.md` (lowercase, never renamed). No issue templates: plain BUG and SUGGEST lines. SECURITY.md present. No sibling line (the `## Related Methodologies` topic section already names awesome-sysml-v2 as an entry and is untouched; the spec says sibling omit). Contents is already pure; verify, do not edit.

- [ ] **Step 1: Confirm placeholders from disk**

Run from `C:\Users\gower\OneDrive\Documents\GitHub\awesome-magicgrid-mbse`:

```bash
git remote get-url origin          # expect https://github.com/jgsystemsconsulting/awesome-magicgrid-mbse.git
grep -E "^(Version|Built):" RELEASE-INFO.txt   # expect Version: 1.0.0 and Built: 2026-09-18T...
ls .github/ISSUE_TEMPLATE 2>/dev/null || echo "no ISSUE_TEMPLATE"   # expect "no ISSUE_TEMPLATE"
ls SECURITY.md contributing.md     # expect both present, lowercase contributing.md
```

Expected placeholders: VERSION `1.0.0`, DATE `2026-09-18`, plain BUG/SUGGEST lines, SECURITY.md clause, `CONTRIB_FILE=contributing.md`, no sibling line. Stop and report if any output differs.

- [ ] **Step 2: Verify Contents purity holds (no edit expected)**

Run:

```bash
sed -n '/^## Contents/,/^## Official Resources/p' README.md
```

Expected: the Contents block lists the nine topic sections only, none of the forbidden names. Delete any forbidden list item if found; none is expected.

- [ ] **Step 3: Replace the Contributing-only tail with the canonical shell**

Delete everything from the line `## Contributing` through end of file. Then append exactly this block, preceded by one blank line after the last topic section body (`## Related Methodologies`, whose last entry is the SYSMOD line):

````markdown
## Contributing

Contributions welcome: see [contributing.md](contributing.md) for the inclusion bar,
entry format, and tag vocabulary.

## Install

Nothing to install. This list is a curated index: browse it here on GitHub,
or clone it:

```bash
git clone https://github.com/jgsystemsconsulting/awesome-magicgrid-mbse.git
```

## Usage

1. Open the Contents at the top and jump to a section, or search the page with
   your browser's find function.
2. Open any entry's link to reach the upstream resource; the list never
   re-hosts content.
3. To suggest a resource or report a defect, use the Support channels below
   (or open a pull request that follows contributing.md).

## Support

- Bug or dead link: open an issue on this repository
- Suggest a resource (the list's improvement channel): open a pull request
  that follows contributing.md, or open an issue
- Security issues: [private security advisory](https://github.com/jgsystemsconsulting/awesome-magicgrid-mbse/security/advisories/new)
  (see [SECURITY.md](SECURITY.md))

## Version

Current release: **1.0.0** (2026-09-18). See [CHANGELOG.md](CHANGELOG.md) and
[RELEASE-INFO.txt](RELEASE-INFO.txt).
````

- [ ] **Step 4: Run verification commands (Acceptance 1 to 7, 9)**

Run in the repo root:

```bash
grep -n "^## " README.md
grep -nE "^- \[(Install|Usage|Support|Version)\]" README.md
grep -nE "^## (Licence|License|Licensing)$" README.md
grep -nE "^- (Licence|License|Licensing):" README.md
grep -n "Current release" README.md
grep -n "git clone" README.md
ls contributing.md            # expect file still present, unrenamed
```

Expected: H2 order Contents, nine topic sections, Contributing, Install, Usage, Support, Version; no packaging names in Contents; no Licence heading or bullet; Version bold `**1.0.0** (2026-09-18)` with both links; clone URL matches origin; `contributing.md` untouched.

- [ ] **Step 5: Diff bounds check (Acceptance 8)**

Run:

```bash
git status --porcelain        # expect only " M README.md"
git diff -- README.md         # expect exactly one hunk replacing the old Contributing tail through EOF
```

All nine topic section bodies, including `## Related Methodologies`, must show no changes.

---

### Task 9: Cross-repo verification (Acceptance 1–7 and 9; A8 via per-task porcelain)

**Files:**
- Read only: all eight in-scope `README.md` files. No file is created or modified; the verifier runs from a heredoc.

**Model:** flash

- [ ] **Step 1: Run the consolidated verifier**

Run from any directory (adjust nothing; the script hard-codes the workspace base):

```bash
python - <<'EOF'
import re
import subprocess
from pathlib import Path

BASE = Path(r"C:\Users\gower\OneDrive\Documents\GitHub")
PKG = ["Contributing", "Install", "Usage", "Support", "Version"]
FORBIDDEN = PKG + ["Licence", "License", "Licensing", "Footnotes"]

EXPECT = {
    "awesome-requirements-engineering": dict(
        ver="0.1.1", date="2026-09-18", forms=True,
        contrib="CONTRIBUTING.md",
        sibling="- SysML v2 language resources belong on the sibling list: [awesome-sysml-v2](https://github.com/jgsystemsconsulting/awesome-sysml-v2)",
        usage_extra=None,
    ),
    "awesome-archimate": dict(
        ver="0.1.0", date="2026-09-17", forms=True,
        contrib="CONTRIBUTING.md",
        sibling="- Capella and Arcadia resources belong on the sibling list: [awesome-capella](https://github.com/jgsystemsconsulting/awesome-capella)",
        usage_extra=None,
    ),
    "awesome-capella": dict(
        ver="0.1.0", date="2026-09-17", forms=True,
        contrib="CONTRIBUTING.md",
        sibling="- SysML v2 language resources belong on the sibling list: [awesome-sysml-v2](https://github.com/jgsystemsconsulting/awesome-sysml-v2)",
        usage_extra=None,
    ),
    "awesome-stpa": dict(
        ver="0.1.0", date="2026-09-17", forms=True,
        contrib="CONTRIBUTING.md", sibling=None,
        usage_extra="PSAS handbook and paper links keep their query",
    ),
    "awesome-enterprise-architect": dict(
        ver="0.1.0", date="2026-09-18", forms=False,
        contrib="CONTRIBUTING.md", sibling=None, usage_extra=None,
    ),
    "awesome-digital-engineering": dict(
        ver="0.1.1", date="2026-09-17", forms=True,
        contrib="CONTRIBUTING.md", sibling=None, usage_extra=None,
    ),
    "awesome-sysml-v2": dict(
        ver="0.1.0", date="2026-09-18", forms=False,
        contrib="contributing.md", sibling=None, usage_extra=None,
    ),
    "awesome-magicgrid-mbse": dict(
        ver="1.0.0", date="2026-09-18", forms=False,
        contrib="contributing.md", sibling=None, usage_extra=None,
    ),
}

def contents_labels(block: str):
    labels = []
    for line in block.splitlines():
        m = re.match(r"^- \[([^\]]+)\]", line.strip())
        if m:
            labels.append(m.group(1).strip())
    return labels

def check(repo, e):
    fails = []
    path = BASE / repo / "README.md"
    text = path.read_text(encoding="utf-8")
    if "## Support" not in text or "## Version" not in text:
        fails.append("A1: missing Support or Version H2")
        return fails
    sup = text.split("## Support", 1)[1].split("## Version", 1)[0]
    usage = text.split("## Usage", 1)[1].split("## Support", 1)[0] if "## Usage" in text else ""

    h2 = re.findall(r"^## (.+?)\s*$", text, re.M)
    for name in PKG:
        if h2.count(name) != 1:
            fails.append(f"A1: H2 '{name}' appears {h2.count(name)} times")
    if len(h2) >= 5 and h2[-5:] != PKG:
        fails.append(f"A1: trailing H2s are {h2[-5:]!r}, want {PKG}")
    try:
        first_pkg = min(h2.index(n) for n in PKG)
        if first_pkg != len(h2) - 5:
            fails.append(
                f"A1: packaging not terminal after topics (first_pkg={first_pkg}, len={len(h2)})"
            )
    except ValueError:
        fails.append("A1: packaging H2 missing from h2 list")

    if re.search(r"^## (Licence|License|Licensing)\s*$", text, re.M):
        fails.append("A3: Licence/License/Licensing H2 present")

    m = re.search(r"^## Contents\n(.*?)(?=^## )", text, re.M | re.S)
    if not m:
        fails.append("A2: no Contents block")
    else:
        labels = contents_labels(m.group(1))
        for name in FORBIDDEN:
            if name in labels:
                fails.append(f"A2/A9: Contents list label is packaging section '{name}'")

    for line in sup.splitlines():
        if re.match(r"^- (Licence|License|Licensing):", line):
            fails.append(f"A4: Support licence bullet: {line[:60]}")

    ver_re = (
        rf"Current release: \*\*{re.escape(e['ver'])}\*\* \({re.escape(e['date'])}\)\. "
        rf"See \[CHANGELOG\.md\]\(CHANGELOG\.md\) and\n\[RELEASE-INFO\.txt\]\(RELEASE-INFO\.txt\)\."
    )
    ver_re2 = (
        rf"Current release: \*\*{re.escape(e['ver'])}\*\* \({re.escape(e['date'])}\)\. "
        rf"See \[CHANGELOG\.md\]\(CHANGELOG\.md\) and \[RELEASE-INFO\.txt\]\(RELEASE-INFO\.txt\)\."
    )
    if not re.search(ver_re, text) and not re.search(ver_re2, text):
        fails.append("A5: Version line mismatch")

    ri = (BASE / repo / "RELEASE-INFO.txt").read_text(encoding="utf-8")
    mver = re.search(r"(?m)^Version:\s*(\S+)\s*$", ri)
    if not mver or mver.group(1) != e["ver"]:
        fails.append(
            f"A5: RELEASE-INFO Version {mver.group(1) if mver else None!r} != expect {e['ver']}"
        )
    cl = (BASE / repo / "CHANGELOG.md").read_text(encoding="utf-8")
    # Collect released version tokens from Keep-a-Changelog brackets, leading semver
    # headings, or freeform headings that embed vX.Y.Z / X.Y.Z.
    ch = re.findall(r"(?m)^## \[([^\]]+)\]", cl)
    ch += re.findall(r"(?m)^## ([0-9]+\.[0-9]+\.[0-9][^\s]*)", cl)
    embedded = []
    for line in cl.splitlines():
        if line.startswith("## ") and "unreleased" not in line.lower():
            m = re.search(r"v?([0-9]+\.[0-9]+\.[0-9][0-9A-Za-z.-]*)", line)
            if m:
                embedded.append(m.group(1))
    ch = [c for c in ch if c.lower() != "unreleased"]
    latest = None
    if ch:
        latest = ch[0]
    elif embedded:
        latest = embedded[0]
    if latest is not None:
        if latest != e["ver"] and not (
            repo == "awesome-enterprise-architect"
            and latest == "0.1.0-private"
            and e["ver"] == "0.1.0"
        ):
            if not (latest.startswith(e["ver"]) or e["ver"] in latest):
                fails.append(
                    f"A5: CHANGELOG latest {latest!r} disagrees with VERSION {e['ver']!r} (stop-on-conflict)"
                )

    clone = f"git clone https://github.com/jgsystemsconsulting/{repo}.git"
    if clone not in text:
        fails.append("A6: clone URL missing from README")
    origin = subprocess.check_output(
        ["git", "-C", str(BASE / repo), "remote", "get-url", "origin"], text=True
    ).strip()
    if repo not in origin:
        fails.append(f"A6: origin remote unexpected: {origin!r}")

    if e["forms"]:
        if (
            f"[bug report form](https://github.com/jgsystemsconsulting/{repo}/issues/new?template=bug_report.yml)"
            not in sup
        ):
            fails.append("A7: bug form link missing or mislabeled")
        if (
            f"[suggestion form](https://github.com/jgsystemsconsulting/{repo}/issues/new?template=suggest-resource.yml)"
            not in sup
        ):
            fails.append("A7: suggestion form link missing or mislabeled")
    else:
        if "Bug or dead link: open an issue on this repository" not in sup:
            fails.append("A7: plain bug line missing")
        if not (
            "open a pull request" in sup
            and e["contrib"] in sup
            and "or open an issue" in sup
        ):
            fails.append("A7: plain suggest line missing")

    if (
        f"[private security advisory](https://github.com/jgsystemsconsulting/{repo}/security/advisories/new)"
        not in sup
    ):
        fails.append("A7: security advisory link missing")
    if "(see [SECURITY.md](SECURITY.md))" not in sup:
        fails.append("A7: SECURITY.md clause missing")

    def norm(s: str) -> str:
        return re.sub(r"\s+", " ", s).strip()

    if e["sibling"]:
        if norm(e["sibling"]) not in norm(sup):
            fails.append("A7: expected full sibling line missing from Support")
        # require repo-root URL, not /issues
        murl = re.search(r"https://github.com/jgsystemsconsulting/awesome-[a-z0-9-]+", e["sibling"])
        if murl and (murl.group(0) + "/issues") in norm(sup):
            fails.append("A7: sibling URL points at /issues instead of repo root")
    elif re.search(r"belong on the sibling list", sup):
        fails.append("A7: unexpected sibling line in Support")

    if e["usage_extra"] and e["usage_extra"] not in usage:
        fails.append("A7/Usage: STPA PSAS query-string sentence missing")

    try:
        contrib_body = text.split("## Contributing\n", 1)[1].split("## Install", 1)[0]
        if f"[{e['contrib']}]({e['contrib']})" not in contrib_body:
            fails.append(f"A1: Contributing does not link {e['contrib']}")
    except IndexError:
        fails.append("A1: Contributing/Install structure broken")

    return fails

total = 0
for repo, e in EXPECT.items():
    fails = check(repo, e)
    total += len(fails)
    status = "PASS" if not fails else "FAIL"
    print(f"{status} {repo}")
    for f in fails:
        print(f"     {f}")
print(
    f"\n{'ALL CHECKS PASS' if total == 0 else f'{total} FAILURES'} across {len(EXPECT)} repos"
)
raise SystemExit(1 if total else 0)
EOF
```

Expected output: `PASS` for all eight repos and the final line `ALL CHECKS PASS across 8 repos`, exit code 0.

- [ ] **Step 2: Confirm only the eight READMEs are dirty, across all eight repos**

Run from `C:\Users\gower\OneDrive\Documents\GitHub`:

```bash
for r in awesome-requirements-engineering awesome-archimate awesome-capella awesome-stpa awesome-enterprise-architect awesome-digital-engineering awesome-sysml-v2 awesome-magicgrid-mbse; do echo "== $r"; git -C "$r" status --porcelain; done
```

Expected: each repo shows exactly ` M README.md` and nothing else. Also confirm the out-of-scope repos are untouched:

```bash
git -C awesome-mbse status --porcelain; git -C awesome-magic-grid status --porcelain; git -C awesome-sparx-ea status --porcelain
```

Expected: no output from any of the three.

- [ ] **Step 3: Optional lint (not a gate)**

For each in-scope repo, `npx awesome-lint` may be run. Residual failures caused solely by packaging H2s omitted from Contents are accepted per spec Risks. Any other failure is out of scope for this pass; record it, do not fix it here.

- [ ] **Step 4: Report**

Summarize per repo: pass/fail for Acceptance 1–7 and 9 (A8 already verified per-task via git diff porcelain on topic bodies). Task 5 Version line is **0.1.0** per RELEASE-INFO; CHANGELOG milestone title may remain `[0.1.0-private]` and must not appear on the Version line.

---

## Out of scope reminder

`awesome-mbse`, `awesome-magic-grid`, and `awesome-sparx-ea` keep their existing shapes (hub Support & security with CC0 footer; namespace-reserve README). Do not add Install/Usage/Support/Version to them, do not "fix" their divergence, and do not open them for edits. Any change there needs a new spec.

## Optional user step (not executed by this plan)

All eight repos are left uncommitted by default. If, after reviewing `git diff` in each repo, the user wants the changes committed, a suitable command per repo is:

```bash
git -C <repo> add README.md && git -C <repo> commit -m "docs: align README packaging shell with family standard"
```

No push, no tag, no release from this pass.
