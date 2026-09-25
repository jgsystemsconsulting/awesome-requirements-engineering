# Copyright (c) 2026 JG Systems Consulting Ltd. See LICENSE.
# SPDX-License-Identifier: CC0-1.0
from pathlib import Path
import csv, re, subprocess, sys, json
RE = Path(__file__).resolve().parents[1]
BASE = RE.parent
AUD = Path.home() / '.zcode/skills/sindresorhus-awesome-ready/tools/audit.py'
MATURITY = (RE / 'internal/MATURITY.md').read_text(encoding='utf-8')
PROMPT = (RE / 'internal/superpowers/prompts/awesome-spoke-maturity.md').read_text(encoding='utf-8')
GOLD_LIC = (RE / 'LICENSE').read_text(encoding='utf-8')
GI = chr(10).join(['', '# Local SA / link-check artifacts', 'docs/superpowers/sa-audit-*.json', 'sa-audit-*.json', ''])

def run(cmd, cwd=None):
    return subprocess.run(cmd, cwd=str(cwd) if cwd else None, capture_output=True, text=True, shell=(sys.platform=='win32'))


def raise_one(row):
    name = row['name']; mono = row['mono']; t1 = row['t1']; t2 = row['t2']; theme = row['theme']; make_public = row['public'] == '1'
    repo = BASE / name
    ch = []
    print('===', name, flush=True)
    if not repo.exists():
        print('missing'); return (name, 'missing', 'n/a', [], [])
    (repo / 'docs').mkdir(exist_ok=True)
    (repo / 'docs/superpowers/prompts').mkdir(parents=True, exist_ok=True)
    (repo / 'docs/MATURITY.md').write_text(MATURITY, encoding='utf-8'); ch.append('maturity')
    (repo / 'docs/superpowers/prompts/awesome-spoke-maturity.md').write_text(PROMPT, encoding='utf-8')
    gi = repo / '.gitignore'
    t = gi.read_text(encoding='utf-8') if gi.exists() else ''
    if 'sa-audit-*.json' not in t:
        gi.write_text(t.rstrip() + GI, encoding='utf-8'); ch.append('gitignore')
    cp = repo / 'CONTRIBUTING.md'
    if cp.exists():
        ct = cp.read_text(encoding='utf-8')
        if 'Lint is mandatory' not in ct:
            lines = ct.splitlines(True); ins = 1
            for i, l in enumerate(lines[:20]):
                if l.strip() == '':
                    ins = i + 1; break
            note = chr(10) + '**Lint is mandatory.** awesome-lint on README.md must pass on every push/PR to main. See [docs/MATURITY.md](docs/MATURITY.md).' + chr(10) + chr(10)
            lines.insert(ins, note)
            cp.write_text(''.join(lines), encoding='utf-8'); ch.append('contrib')

    wf = repo / '.github/workflows'
    if wf.exists():
        found = False
        for f in list(wf.glob('*.yml')) + list(wf.glob('*.yaml')):
            txt = f.read_text(encoding='utf-8')
            if 'awesome-lint' not in txt:
                continue
            found = True
            if 'Blocking maturity gate' not in txt and 'docs/MATURITY.md' not in txt:
                f.write_text(txt.replace('- name: awesome-lint' + chr(10), '# Blocking maturity gate (docs/MATURITY.md): do not remove or set continue-on-error.' + chr(10) + '      - name: awesome-lint' + chr(10)), encoding='utf-8')
                ch.append('lint-note')
        if not found:
            body = 'name: Lint' + chr(10) + 'on:' + chr(10) + '  pull_request:' + chr(10) + '    branches: [main]' + chr(10) + '  push:' + chr(10) + '    branches: [main]' + chr(10) + 'permissions:' + chr(10) + '  contents: read' + chr(10) + 'jobs:' + chr(10) + '  lint:' + chr(10) + '    runs-on: ubuntu-latest' + chr(10) + '    steps:' + chr(10) + '      - uses: actions/checkout@11d5960a326750d5838078e36cf38b85af677262 # v4' + chr(10) + '      - uses: actions/setup-node@49933ea5288caeca8642d1e84afbd3f7d6820020 # v4' + chr(10) + '        with:' + chr(10) + '          node-version: 20' + chr(10) + '      # Blocking maturity gate (docs/MATURITY.md): do not remove or set continue-on-error.' + chr(10) + '      - name: awesome-lint' + chr(10) + '        run: npx awesome-lint@2.3.0 README.md' + chr(10)
            (wf / 'lint.yml').write_text(body, encoding='utf-8'); ch.append('lint-created')
    lic = None
    for n in ('LICENSE', 'license'):
        if (repo / n).is_file():
            lic = repo / n; break
    if lic is None:
        (repo / 'LICENSE').write_text(GOLD_LIC, encoding='utf-8'); ch.append('lic-create')
    else:
        raw = lic.read_text(encoding='utf-8')
        if 'Creative Commons Legal Code' not in raw and ('CC0' in raw or 'Creative Commons' in raw):
            lic.write_text(GOLD_LIC, encoding='utf-8'); ch.append('lic-cc0')
    media = repo / 'media'; media.mkdir(exist_ok=True)
    # simple monogram SVG without nested quote pain
    y1 = '120' if t2 else '140'
    parts = []
    parts.append('<?xml version="1.0" encoding="UTF-8"?>')
    parts.append('<svg xmlns="http://www.w3.org/2000/svg" width="512" height="256" viewBox="0 0 512 256" role="img">')
    parts.append('  <rect width="512" height="256" fill="#f7f8fa"/>')
    parts.append('  <rect x="48" y="48" width="160" height="160" rx="28" fill="#157adb"/>')
    parts.append('  <text x="128" y="158" text-anchor="middle" font-family="sans-serif" font-size="72" font-weight="600" fill="#ffffff">' + mono + '</text>')
    parts.append('  <text x="240" y="' + y1 + '" font-family="sans-serif" font-size="36" font-weight="600" fill="#1a1d24">' + t1 + '</text>')
    if t2:
        parts.append('  <text x="240" y="168" font-family="sans-serif" font-size="36" font-weight="600" fill="#1a1d24">' + t2 + '</text>')
    parts.append('</svg>')
    (media / 'logo.svg').write_text(chr(10).join(parts) + chr(10), encoding='utf-8'); ch.append('logo')
    rp = repo / 'README.md'
    if rp.exists():
        rt = rp.read_text(encoding="utf-8")
        if "media/logo.svg" not in rt:
            href = ("https://jgsystemsconsulting.github.io/" + name + "/") if (repo / "docs/index.html").exists() else ("https://github.com/jgsystemsconsulting/" + name)
            lines = rt.splitlines(True); out = []; done = False
            block = chr(10).join(["", "<p align=\"right\">", "  <a href=\"" + href + "\">", "    <img src=\"media/logo.svg\" width=\"256\" alt=\"list mark\">", "  </a>", "</p>", ""])
            for line in lines:
                out.append(line)
                if (not done) and line.startswith("# "):
                    out.append(block); done = True
            rt = "".join(out); ch.append("logo-readme")
        if theme:
            m = re.search(r"^> (.+)$", rt, re.M)
            if m and re.search(r"(?i)curated list|awesome list of", m.group(1)):
                rt = rt.replace("> " + m.group(1), "> " + theme, 1); ch.append("blurb")
        lines = rt.splitlines(True); out = []; i = 0
        while i < len(lines):
            line = lines[i]
            if re.match(r"(?i)^- .*licen[cs]e:", line) or (line.strip().startswith("-") and re.search(r"(?i)licen[cs]e enquir", line)):
                i += 1
                while i < len(lines) and (lines[i].startswith("  ") or lines[i].startswith(chr(9))):
                    i += 1
                ch.append("strip-lic"); continue
            out.append(line); i += 1
        rp.write_text("".join(out), encoding="utf-8")
    gate = repo / "scripts/check_release.py"
    if gate.exists():
        gt = gate.read_text(encoding="utf-8")
        if "docs/MATURITY.md" not in gt and "docs/index.html" in gt:
            gate.write_text(gt.replace('"docs/index.html",', '"docs/index.html", "docs/MATURITY.md",'), encoding="utf-8"); ch.append("gate")
            run(["python", "scripts/check_release.py"], cwd=repo)
    if make_public and name != "awesome-mbse":
        meta = run(["gh", "api", "repos/jgsystemsconsulting/" + name])
        if meta.returncode == 0:
            try:
                data = json.loads(meta.stdout)
            except Exception:
                data = {}
            if data.get("private") is True:
                r = run(["gh", "api", "-X", "PATCH", "repos/jgsystemsconsulting/" + name, "-f", "private=false"])
                if r.returncode == 0:
                    ch.append("public")
            run(["gh", "repo", "edit", "jgsystemsconsulting/" + name, "--add-topic", "awesome", "--add-topic", "awesome-list"]); ch.append("topics")
    st = run(["git", "status", "--porcelain"], cwd=repo)
    git = "clean"
    if (st.stdout or "").strip():
        run(["git", "add", "-A"], cwd=repo)
        r = run(["git", "commit", "-m", "Raise spoke to family maturity bar (MATURITY, SA polish, awesome-lint)."], cwd=repo)
        git = "commit-%s" % r.returncode
        r = run(["git", "push", "origin", "HEAD"], cwd=repo)
        git += ",push-%s" % r.returncode
        if r.returncode != 0:
            print((r.stderr or r.stdout or "")[:300])
    ar = run(["python", str(AUD), "--repo", str(repo), "--gh", "--lint"])
    dec = "?"
    for ln in (ar.stdout or "").splitlines():
        if ln.startswith("Decision:"):
            dec = ln.split(":", 1)[1].strip()
    fails = [ln.strip() for ln in (ar.stdout or "").splitlines() if re.match(r"\s*SA-\S+\s+FAIL", ln)]
    print("decision", dec, "git", git, "changes", ch)
    for f in fails:
        print(" ", f)
    return (name, dec, git, ch, fails)

def main():
    rows = list(csv.DictReader((RE / "scripts/_maturity_jobs.csv").open(encoding="utf-8")))
    out = []
    for row in rows:
        out.append(raise_one(row))
    print("SUMMARY")
    for name, dec, git, ch, fails in out:
        print(name, dec, git, "FAILS", len(fails), ch)

if __name__ == "__main__":
    main()
