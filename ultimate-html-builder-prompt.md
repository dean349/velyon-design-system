# 🚀 The Ultimate HTML Page Builder Prompt

Use this prompt in any Antigravity workspace agent conversation to build a premium, 
production-grade HTML landing page or web page.

---

## How to Use

1. Copy the prompt block below
2. Fill in all `[PLACEHOLDERS]` with your specifics
3. Delete any `[OPTIONAL]` blocks you don't need
4. Delete all save `[OPTIONS]` except the one you want
5. Paste into your agent conversation

---

## The Prompt

```
/ui Use the frontend-design skill, ui-ux-pro-max skill, and mcp_magic_21st_magic_component_builder 
to build me a premium, single-file HTML landing page for [YOUR PRODUCT/PAGE DESCRIPTION HERE].

───────────────────────────────────────────
CORE REQUIREMENTS
───────────────────────────────────────────
- Single self-contained .html file with all CSS and JS inline
- Use the ui-ux-pro-max design system script to generate the full design system first:
  python3 skills/ui-ux-pro-max/scripts/search.py "[your industry + keywords]" --design-system
- Use 21st_magic_component_builder to source UI components (hero, cards, nav, CTA, etc.)
- Apply frontend-design principles: bold aesthetic direction, distinctive fonts 
  (NOT Inter/Roboto/Arial), micro-animations, atmospheric backgrounds, unexpected layouts
- Dark mode premium aesthetic with glassmorphism and depth
- Fully responsive: 375px, 768px, 1024px, 1440px breakpoints
- SVG icons only (Heroicons/Lucide style) — no emojis as icons
- Smooth CSS transitions (150–300ms) on all interactive elements
- Google Fonts via CDN (pick something distinctive and appropriate)
- Pre-delivery checklist verified: contrast, hover states, cursor-pointer, no layout shift

───────────────────────────────────────────
[OPTIONAL – DELETE IF NOT NEEDED]
GENERATE HERO IMAGES
───────────────────────────────────────────
- Use the generate_image tool to create real images for the hero and any visual sections
- No placeholder images — generate all visuals from scratch to match the design aesthetic

───────────────────────────────────────────
[OPTIONAL – DELETE IF NOT NEEDED]
COPY & MESSAGING
───────────────────────────────────────────
- Use the copywriting skill to write all headlines, subheadings, and CTA copy
- Messaging should be benefit-led, punchy, and conversion-focused

───────────────────────────────────────────
[OPTIONAL – DELETE IF NOT NEEDED]
BRAND ALIGNMENT
───────────────────────────────────────────
- Apply the Velyon brand design system from conversation 984521be
  (Executive Dark Mode: deep navy/slate, gold accents, premium typography)

───────────────────────────────────────────
SAVE LOCATION — CHOOSE ONE OR MORE, DELETE THE REST
───────────────────────────────────────────

[OPTION A – LOCAL WORKSPACE]
Save the completed file to:
c:\ANTIGRAVITY PROJECTS\VELYON - LEGAL COMMAND CENTER\[subfolder]\[page-name].html

[OPTION B – GOOGLE DRIVE (if Drive for Desktop is installed)]
Save the completed file to your synced Google Drive folder:
G:\My Drive\[Your Folder]\[page-name].html
(Adjust the drive letter if your Google Drive maps differently — check in File Explorer)

[OPTION C – GITHUB REPO (uses your GitHub MCP)]
Commit the completed file directly to your GitHub repository using the github MCP tool:
- Repo owner: [your-github-username]
- Repo name: [your-repo-name]
- Branch: main
- File path in repo: pages/[page-name].html
- Commit message: "Add [page-name] landing page"

[OPTION D – ALL OF THE ABOVE]
Save locally AND push to GitHub AND sync via Google Drive.
```

---

## Quick Reference: What to Fill In

| Placeholder | Example |
|---|---|
| `[YOUR PRODUCT/PAGE DESCRIPTION]` | `Velyon AI consultancy — premium services landing page` |
| `"[your industry + keywords]"` | `"AI consulting premium executive dark mode"` |
| `[subfolder]` | `output` or `pages` |
| `[page-name]` | `velyon-landing` |
| `[your-github-username]` | `dean349` |
| `[your-repo-name]` | `velyon-design-system` |

---

## Skills & MCP Tools This Prompt Activates

| Tool / Skill | Purpose |
|---|---|
| `frontend-design` skill | Bold aesthetic direction, production-grade HTML/CSS/JS |
| `ui-ux-pro-max` skill | Design system: fonts, colours, spacing, effects |
| `mcp_magic_21st_magic_component_builder` | Sourcing premium React/HTML UI components |
| `generate_image` tool | AI-generated hero images (optional) |
| `copywriting` skill | Compelling headline and CTA copy (optional) |
| `github` MCP | Direct commit to GitHub repo (optional) |

---

## Notes

- The `/ui` trigger activates the magic component builder automatically
- Always specify an aesthetic direction to avoid generic AI output
- The `ui-ux-pro-max` design system script must be run **before** coding begins
- Google Drive Option B requires **Google Drive for Desktop** to be installed and synced
- GitHub Option C requires your repo to already exist in GitHub

---

*Saved: 2026-04-10 | Antigravity Workspace: VELYON - LEGAL COMMAND CENTER*
