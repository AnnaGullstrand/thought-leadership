#!/usr/bin/env python3
"""
Auto-generates ScienceSkills.md from data/content.json.
Called automatically by the PostToolUse hook whenever content.json is modified.
"""
import json, os, sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC  = os.path.join(BASE, "data", "content.json")
OUT  = os.path.join(BASE, "ScienceSkills.md")

if not os.path.exists(SRC):
    print(f"content.json not found at {SRC}")
    sys.exit(0)

with open(SRC) as f:
    d = json.load(f)

skills     = d["scienceSkills"]
ops_lookup = {o["id"]: o["label"] for o in d["filters"]["opinions"]}

DOMAIN_ORDER = [
    ("individual-cognition", "Individual Cognition"),
    ("learning-science",     "Learning Science"),
    ("social-psychology",    "Social Psychology"),
    ("decision-science",     "Decision Science"),
    ("behavioral-science",   "Behavioral Science"),
]

domain_skills = {k: [] for k, _ in DOMAIN_ORDER}
for s in skills:
    domain_skills[s["domain"]].append(s)

lines = [
    "# Science Skills — Mentimeter Thought Leadership Website\n",
    f"This file describes all **{len(skills)} science mechanics** that underpin Mentimeter's Thought Leadership. "
    "Each skill is grounded in peer-reviewed research and translates directly into leader behavior and Menti application use.\n",
    "> **Auto-generated from** `data/content.json` — do not edit by hand. "
    "Re-generated automatically whenever `content.json` is saved.\n",
    "---\n",
]

n = 1
for domain_id, domain_label in DOMAIN_ORDER:
    group = domain_skills[domain_id]
    lines.append(f"## {domain_label} ({len(group)} skills)\n")
    for s in group:
        ops = ", ".join(ops_lookup.get(o, o) for o in s.get("opinions", []))
        lines += [
            f"### {n}. {s['headline']}",
            f"**Problem:** {s['problem']}\n",
            f"**Solution:** {s['solution']}\n",
            f"**Science:** {s['back']['scienceBehind']}\n",
            f"> *{s['source']['text']}*\n",
            f"**In practice:** {s['back']['inPractice']}\n",
            f"**Related opinions:** {ops}\n",
            "---\n",
        ]
        n += 1

# Summary table
lines += [
    "## Summary: All Skills\n",
    "| # | Skill | Domain | Related Opinions |",
    "|---|-------|--------|-----------------|",
]
n = 1
for domain_id, domain_label in DOMAIN_ORDER:
    for s in domain_skills[domain_id]:
        ops = " · ".join(ops_lookup.get(o, o) for o in s.get("opinions", []))
        lines.append(f"| {n} | {s['headline']} | {domain_label} | {ops} |")
        n += 1

with open(OUT, "w") as f:
    f.write("\n".join(lines))

print(f"ScienceSkills.md regenerated — {n-1} skills ✓")
