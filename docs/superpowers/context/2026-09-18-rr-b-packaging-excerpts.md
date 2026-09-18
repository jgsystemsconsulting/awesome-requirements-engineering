**RR-B-05 (MUST) — README.** A root `README.md` that, at minimum, states: product name +
one-line description; what it is / who it's for; prerequisites; install (or a link to install
docs); quickstart usage; licensing statement (link to `LICENSE`); support/contact channel;
version or link to `CHANGELOG.md`. No internal URLs, no dev-only sections, no `CONFIDENTIAL`
markers.
*Verify:* `README.md` exists and contains headings for Install, Usage, Licence, Support. The Licence section links `LICENSE` and contains `<licence-enquiry-url>` (JGSC: `https://labs.jgsystemsconsulting.com/licensing.html`). Copy must not imply an OSS-licensed product requires a paid licence; the enquiry URL is how to request a commercial or academic licence, or to ask which licence applies.


**RR-B-06 (MUST) — Install/usage instructions.** Copy-paste-ready installation and first-use
instructions exist, appropriate to the product type (see profiles M/S for where they live). A
non-expert user can go from clone/download to working in one pass.

> **Usage-doc depth scales with product type.** For a **skills pack**, the `RR-S-05` usage doc
> (`docs/skill-usage.md`: prerequisites + how to invoke) is sufficient — a skill's "use" is mostly
> *invoke it and let it run*. For **software** (a CLI, app, service, or library), invocation alone is
> not enough: ship a fuller **"how to use this"** guide that covers real workflows, configuration,
> common tasks walked end-to-end, inputs/outputs, and failure/recovery — not just the launch command.
> Put it where users will find it (a `docs/usage.md` / `docs/guide.md` linked from the README and the
> landing page, or a README "Usage" section substantial enough to stand alone). The test is the same
> as `RR-B-06`'s — a non-expert goes from installed to *productively using it* in one pass — but for
> software that bar takes more than a one-liner.

*Verify:* install path documented; commands are literal and complete. For a software product (not a
skills pack), a task-level usage guide exists (workflows + configuration, not just the invocation
command) and is linked from the README / landing page.


**RR-B-07 (MUST) — Support & vulnerability reporting.** A documented way to get help and to
report a security issue — a `SECURITY.md`, or a clearly labelled README section. The security
channel MUST be **contribution/advisory-based by default — open a pull request with the fix, or,
for sensitive issues, a private GitHub security advisory** — **not** an email address. An email
contact MAY be given *instead* only where the adopter operates a monitored security inbox and
deliberately chooses email; absent that, security reporting MUST NOT publish an email address. A
general (non-security) support channel — issues, or a support address — is still fine.
*Verify:* `SECURITY.md` (or the README security section) documents a PR / security-advisory
reporting route and contains **no email address**, unless the adopter has explicitly opted into a
monitored security inbox (recorded in the repo).


**RR-B-32 (MUST) — Bug-report channel.** Every repo ships a GitHub issue form at
`.github/ISSUE_TEMPLATE/bug_report.yml` (so an agent or human can report a malformed or
incorrect tool/output) and an issue chooser at `.github/ISSUE_TEMPLATE/config.yml` that sets
`blank_issues_enabled: false` and routes security reports to the private advisory path via a
`contact_links` entry. The bug form requires a hygiene checkbox confirming no keys/credentials
are pasted. Exempt from the RR-B-12 proprietary ban (it is a defect channel, not a
contribution channel). **Scope exemption:** repos with no tool/API surface to report against
(e.g. a JAR-only distribution with no MCP tools) are exempt from the bug-report *form* — its
fields ("run the `ping` tool", "tool name") are meaningless there; `RR-B-31` (CITATION.cff)
still applies. Private (non-public) repos may also defer the form, since an external reporter
cannot reach it; apply it when/if the repo is made public.

Three additions make the channel real rather than present:

- **Improvement form (SHOULD).** Alongside the bug form, ship a second form for
  product-shaped improvements (a skills pack: "skill improvement"; otherwise an
  "enhancement" form). It carries a version field sourced from `RELEASE-INFO.txt`, an
  outcome-the-product-could-not-enable field, a proposed-change field, and the same
  `required: true` hygiene checkbox as the bug form. Bugs and improvements are different
  reports; forcing both through one form loses the version and the outcome.
- **Sibling-tracker routing.** Where the product depends on a companion repo users can
  confuse it with (an MCP bridge, a server, a host plugin), `config.yml` carries a
  `contact_links` entry routing that companion's defects to **its** tracker ("Bridge
  defects: file them there, not here"). Wrong-tracker reports are handled at intake, not in
  triage later.
- **The README names the feedback loop.** The README Support section states, per channel,
  where each kind of report goes: bugs (the bug form), improvements (the improvement form or
  an in-session draft, `RR-S-17`), questions (Discussions where enabled), companion-product
  defects (that product's tracker), and security (the private advisory, never a public
  issue). A form nobody can find from the README might as well not exist.

*Verify:* both files exist and parse; `config.yml`'s advisory URL is resolved (no stray
token); the hygiene checkbox carries `required: true` in every shipped form. The improvement
form exists or its absence is deliberate; companion-tracker routing matches the companion
repos the product actually names; the README Support section names each channel.
(Tool-less / private repos: exemption
noted in source.)
