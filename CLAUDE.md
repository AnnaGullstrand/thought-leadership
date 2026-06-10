# Project Brief — Mentimeter Thought Leadership Website

## What this site is and why it exists

This is an **internal resource for Mentimeter employees** — in Product, Marketing, Sales, Advisory, and Executive Education. It helps people understand the science-informed Thought Leadership that underpins everything Mentimeter builds.

The site explains:
- **The science** behind how people think, learn, decide, and change (5 domains, 39 mechanics)
- **Our 7 opinions** on how great leaders should educate, communicate, and facilitate
- **How Menti tools** connect to the science in practice
- **Why it creates business impact** at organizational scale

It is NOT a public-facing product. It is a living internal reference that grows over time.

---

## Live site & access

| Item | Value |
|------|-------|
| **URL** | https://annagullstrand.github.io/thought-leadership/ |
| **Password** | `Menti2026` |
| **GitHub repo** | https://github.com/AnnaGullstrand/thought-leadership |
| **Local server** | `cd "/Users/anna.gullstrand/Documents/Claude Code/Homepage" && python3 -m http.server 8000` |
| **Local URL** | http://localhost:8000 |

To push to GitHub, Anna needs to provide her GitHub Personal Access Token when prompted (or it can be passed inline in the remote URL). Token is not stored here — Anna generates it at github.com/settings/tokens.

---

## File structure

```
Homepage/
├── index.html                    ← Landing page (hero + 5 teaser cards)
├── the-science.html              ← 5 scientific domains explained
├── our-opinions.html             ← 7 opinions + TL framework
├── scientific-mechanism.html     ← Science Dictionary (filterable card grid)
├── active-participation.html     ← Ask→Think→Share→Act model
├── impact-at-scale.html          ← Business + Higher Ed impact (with toggle)
├── data/
│   └── content.json              ← SOURCE OF TRUTH for all science skills
├── assets/
│   ├── images/                   ← All photos and logos
│   └── fonts/                    ← MentiCompressed-Bold.otf
├── scripts/
│   └── generate_science_skills.py ← Auto-run when content.json is saved
├── ScienceSkills.md              ← Auto-generated from content.json (do not edit by hand)
├── CLAUDE.md                     ← This file
└── .claude/
    └── settings.local.json       ← PostToolUse hook + permissions
```

---

## Technical architecture

- **Pure static HTML** — no build tools, no Node, no framework
- **CSS is inline** in each HTML file (each page is self-contained)
- **No shared stylesheet** — changes to shared styles must be applied to all 6 files
- **Content is loaded via `fetch('./data/content.json')`** on the scientific-mechanism.html page
- **Fonts:** MentiCompressed Bold (local .otf) + Inter (Google Fonts)
- **Deployed via GitHub Pages** — pushing to `main` branch auto-deploys (~30s delay)
- **Password gate** uses `sessionStorage` — re-enter once per browser session

---

## Navigation structure (5 pages)

| Page | File | Key content |
|------|------|-------------|
| The Science | `the-science.html` | 5 domain cards + CTA to Opinions |
| Our Opinions | `our-opinions.html` | 7 opinions + TL Framework + how we take it to market |
| Scientific Mechanism | `scientific-mechanism.html` | 39 filterable science skill cards |
| Active Participation | `active-participation.html` | Ask→Think→Share→Act model + 6 pillars |
| Impact at Scale | `impact-at-scale.html` | Business + Higher Ed impact (toggle) |

---

## The Science Dictionary (content.json)

The core data model. Each science skill has:

```json
{
  "id": "kebab-case-id",
  "domain": "individual-cognition|learning-science|social-psychology|decision-science|behavioral-science",
  "headline": "Skill Name",
  "problem": "~100 chars — the problem this addresses",
  "solution": "~95 chars — what leaders/teachers do about it",
  "source": { "text": "Author (year)", "url": "https://doi.org/..." },
  "whyItMatters": "2 sentences — why this matters for leaders (Business context)",
  "atScale": "1 sentence — organizational impact, referencing specific Impact at Scale outcomes",
  "back": {
    "principle": "...",
    "scienceBehind": "...",
    "inPractice": "..."
  },
  "mentiApplication": ["bullet 1", "bullet 2", "bullet 3"],
  "opinions": ["clarify-intent", "activate-participation", ...],
  "useCases": ["team-meeting", "training", ...],
  "tools": ["menti-live", "menti-pulse", ...],
  "higherEd": {
    "whyItMatters": "2 sentences — higher ed / teaching context",
    "atScale": "1 sentence — referencing Higher Ed Impact at Scale outcomes",
    "mentiApplication": ["classroom bullet 1", ...],
    "useCases": ["lectures", "seminars", ...]
  }
}
```

### Current counts
- **39 skills** across 5 domains
- Individual Cognition: 7 | Learning Science: 9 | Social Psychology: 5 | Decision Science: 8 | Behavioral Science: 10

### Text length rule
- `problem` + `solution` combined: **target ~200 chars, max ~240**
- Benchmark: "Make Thinking Visible" = 201 chars (108 + 93)

---

## The 7 Opinions (for opinion mapping)

| ID | Label |
|----|-------|
| `clarify-intent` | Clarify Intent |
| `activate-participation` | Activate Participation |
| `ask-better-questions` | Ask Better Questions |
| `make-people-understand-deeply` | Make People Understand Deeply |
| `structure-thinking-together` | Structure How People Think Together |
| `create-ownership` | Create Ownership & Commitment |
| `reinforce-performance` | Reinforce Performance Over Time |

---

## Filters on Scientific Mechanism page

| Filter group | Values |
|---|---|
| **Opinion** | The 7 opinions above |
| **Use Case (Business)** | Training & Learning, Town Hall/All-Hands, Team Meeting, Team Check-In, Workshop, Onboarding, Presentation/Keynote, Advisory/Consulting |
| **Use Case (Higher Ed)** | Lectures, Seminars, Formative Assessment, Student Voice, Course Feedback, Evaluations |
| **Tool** | Menti Live, Menti Pulse, Menti Form, Menti Quiz, Menti Q&A, Menti Workshop, Engagement Suite |

The **Business/Higher Ed toggle** (top right of filter bar + inside each card modal) switches:
- Use Case filter chips
- WHY IT MATTERS text
- IMPACT AT SCALE text
- MENTI APPLICATION bullets

The science content (THE SCIENCE BEHIND) **never changes** — it's domain-neutral.

---

## Business / Higher Ed toggles

Two pages have context toggles:

1. **`scientific-mechanism.html`** — audience toggle in filter bar + inside each card modal
2. **`impact-at-scale.html`** — audience toggle in content section (shows different impact tiers + outcomes)

### Impact at Scale outcomes (for atScale text references)

**Business:** Faster Value Creation · Better Strategic Outcomes · Stronger Organizational Performance · Speed of Execution · Innovation & Change · Decision Quality · Continuous Learning · Leadership Effectiveness · Employee Engagement

**Higher Ed:** Academic Excellence · Research & Innovation · Institutional Reputation · Student Learning Outcomes · Graduate Employability · Student Retention & Completion · Inclusive Teaching & Equity · Teaching Quality & Effectiveness · Research Collaboration

---

## Brand identity

### Primary colour palette

| Name | Hex | Role |
|------|-----|------|
| Blue 800 | `#323C7C` | Hero backgrounds, dark accents |
| Blue 500 | `#5769E7` | Primary CTAs, links, highlights |
| Blue 100 | `#D5DAF7` | Light backgrounds, cards |
| Coral 800 | `#802E2D` | Strong accents |
| Coral 500 | `#FF7471` | Energy, WHY IT MATTERS sections |
| Coral 100 | `#FFDEDD` | Light coral backgrounds |
| Sand 800 | `#615B55` | Secondary text, borders |
| Sand 500 | `#A59D94` | Neutral UI |
| Sand 100 | `#F3EDE7` | Page backgrounds, section fills |
| White | `#FFFFFF` | Backgrounds, text on dark |
| Near Black | `#111111` | Body text |

### Support palette (for domain colour coding)
- Individual Cognition: `#5769E7` (Blue 500)
- Learning Science: `#FF7471` (Coral 500)
- Social Psychology: `#6C67CF` (Purple 600)
- Decision Science: `#52AD6E` (Green 500)
- Behavioral Science: `#DBAB30` (Yellow 600)

### Typography
- **Display/headlines:** MentiCompressed Bold (local font: `assets/fonts/MentiCompressed-Bold.otf`)
- **Body/UI:** Inter (Google Fonts — 400, 500, 600)

---

## How to add a new science skill

**Always ask for sources first:**
> "Before I add this skill, what are the main academic sources? I need at least one peer-reviewed reference (author, year, DOI or journal). The science on this site must be verified and validated."

**Source quality:**
- Peer-reviewed journal articles (preferred)
- Seminal books by recognized researchers (Kahneman, Edmondson, Deci & Ryan, etc.)
- Never secondary citations or training decks — trace back to the original study

**After getting sources, add the skill to `data/content.json`** with all required fields including:
- Business fields: `whyItMatters`, `atScale`, `mentiApplication`, `useCases`
- Higher Ed fields: `higherEd.whyItMatters`, `higherEd.atScale`, `higherEd.mentiApplication`, `higherEd.useCases`
- Opinion mappings (1–2 of the 7 opinions)
- Tool tags

**`ScienceSkills.md` auto-regenerates** via PostToolUse hook when `content.json` is saved. No manual update needed.

---

## Enabling Slack DM notifications (footer "Add Science Mechanism" form)

When someone submits a skill suggestion via the footer form, a DM is sent to Anna (Slack ID: `U010JJF15NG`) — **but only after setting up a webhook:**

1. Go to [api.slack.com/apps](https://api.slack.com/apps) → Create New App → From scratch
2. Name: "TL Website" → Mentimeter workspace
3. Incoming Webhooks → toggle on → Add New Webhook to Workspace
4. Select Direct Messages → Anna Gullstrand → Allow
5. Copy the webhook URL (`https://hooks.slack.com/services/T.../B.../...`)
6. In all 6 HTML files, replace:
   `const SLACK_WEBHOOK_URL = '';`
   with your real URL, then push to GitHub.

> **Security:** Webhook URL will be visible in page source. Acceptable for an internal password-protected tool.

---

## Auto-regeneration hook

A PostToolUse hook in `.claude/settings.local.json` runs `scripts/generate_science_skills.py` automatically whenever `content.json` is saved via Write or Edit. This keeps `ScienceSkills.md` always in sync.

---

## Important: changes to shared styles

Since each HTML file has its own inline CSS, a style change needed on all pages (e.g. nav, footer, typography) must be applied to **all 6 files**. Use `sed` or an agent to apply consistently. The most commonly shared elements:
- Navigation (`.nav`, `.nav-links`, `.nav-logo`)
- Footer (`.footer-top`, `.footer-glossary`, `.suggest-*`)
- CSS variables (`:root`)
- Hero section (`.sec-hero`, `.sec-hero-title`, `.sec-hero-sub`)

---

## Key design decisions (for consistency)

- **Hero height:** `height: 28vh; min-height: 220px` on section pages
- **Headlines on hero images** use `sec-hero-title` — always white, MentiCompressed, `clamp(36px, 5vw, 72px)`
- **Section content** max-width: 1280px, centered
- **Modal panel** slides in from the right (desktop), bottom sheet on mobile
- **Science card modal structure:** WHY IT MATTERS (coral) → THE SCIENCE BEHIND (blue) → MENTI APPLICATION (sand)
- **Card text limit:** problem + solution ≤ 230 chars combined
- **No numbers** in nav items or teaser cards
