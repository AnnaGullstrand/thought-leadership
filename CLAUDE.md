# Project Instructions — Mentimeter Thought Leadership Website

## Adding a New Science Skill

When Anna asks to add a new science skill (science box / science card) to the registry (`data/content.json`), **always ask for sources before writing any content**:

> "Before I add this skill, could you share the main scientific sources you want to use? I need at least one peer-reviewed reference (author, year, title or DOI). The science on this site should be verified and validated — not inferred."

### What to ask for:
- **Primary source(s):** Author(s), year, publication name or DOI
- **If the user doesn't have sources:** Offer to suggest validated peer-reviewed sources yourself, but flag them clearly as suggestions for Anna to approve before publishing

### Source quality standard:
- Peer-reviewed journal articles (preferred)
- Seminal books by recognized researchers (e.g. Kahneman, Edmondson, Deci & Ryan)
- No secondary citations, no "generally accepted", no training decks — always trace back to the original study

### After adding a skill:
- `ScienceSkills.md` is auto-regenerated via hook — no manual update needed
- Assign the skill to 1–2 of the 7 opinions
- Add Business + Higher Ed versions for `whyItMatters`, `atScale`, and `mentiApplication`
- Keep `problem` + `solution` text under ~230 characters combined (benchmark: Make Thinking Visible = 201 chars)

---

## Enabling Slack DM notifications for "Add Science Mechanism" form

The footer form sends a DM to Anna (Slack user ID: `U010JJF15NG`) when someone suggests a skill. To activate this on the live site:

1. Go to [api.slack.com/apps](https://api.slack.com/apps) → **Create New App** → From scratch
2. Name it "TL Website" → select the Mentimeter workspace
3. Go to **Incoming Webhooks** → toggle on → **Add New Webhook to Workspace**
4. Select **Direct Messages** → choose yourself (Anna Gullstrand) → Allow
5. Copy the webhook URL (looks like `https://hooks.slack.com/services/T.../B.../...`)
6. Open all 6 HTML files and replace `const SLACK_WEBHOOK_URL = '';` with:
   `const SLACK_WEBHOOK_URL = 'https://hooks.slack.com/services/YOUR/WEBHOOK/URL';`
7. Push to GitHub

> **Security note:** The webhook URL will be visible in page source. Since the site is password-protected and internal, this is acceptable. Do not share the webhook URL publicly.

---

## The 7 Opinions (for opinion mapping)

1. Clarify Intent
2. Activate Participation
3. Ask Better Questions
4. Make People Understand Deeply
5. Structure How People Think Together
6. Create Ownership & Commitment
7. Reinforce Performance Over Time
