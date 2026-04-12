# Los Romeros Limited — Brand Style Guide

*Last updated: April 10, 2026*

This Style Guide dictates the visual application of the Los Romeros Limited brand across digital properties, legal filings, and public-facing forensic dashboards.

## 1. Design Philosophy

The visual philosophy is **"Forensic Minimalism."** 
There should be no aggressive brand illustrations or abstract vector art. The design exists exclusively to structure text, data, and evidence in a highly legible and accessible format. 

## 2. Typography

We select typefaces that convey established, formal legal authority while retaining modern digital readability.

### Typeface Pairings
- **Primary Typeface (Headings & Titles): `Playfair Display`**
  Used for all major structural headings (H1, H2, H3). Provides an editorial, established weight that evokes traditional legal documents and formal case filings. 
  - *Weights:* Semi-Bold (600) or Bold (700)
  - *Tracking:* Normal

- **Secondary Typeface (Body Text & UI Elements): `Inter`**
  A highly legible, neo-grotesque sans-serif designed for data-dense layouts. Used for paragraphs, annotations, tables, and UI controls.
  - *Weights:* Regular (400) for body, Medium (500) for labels/subheaders.
  - *Line Height:* Relaxed (1.6 to 1.7) to improve reading comprehension on lengthy analyses.

## 3. Grid & Layout Principles

To format evidence and forensic findings logically, layouts should mimic formal regulatory reports or documentation structures:

- **Asymmetrical Column Layouts:** Use a dominant reading column (max-width: 65ch to maintain legibility) with a smaller sidebar column for annotations, citations, or legal caveats.
- **Strict Margins & Padding:** Avoid floating components without structure. Use strict boxing (borders and distinct panel backgrounds) to frame sections of content. 
- **White Space (Negative Space):** Adopt generous padding around quantitative financial findings (e.g., exit tax sums) to emphasize numeric gravity.

## 4. UI Patterns & Constraints

Web execution requires adherence to professional interactive rules.

**1. Button & Interaction Stylings:**
- Avoid "friendly" hover states (bubble effects, bouncing). Use rigid color transitions (e.g., fading from Slate-800 to Slate-900).
- Buttons should feature sharp or minimally rounded corners (`rounded-sm` or `rounded-none`), rejecting pill-shaped (`rounded-full`) SaaS paradigms.

**2. Forms and Data Tables:**
- **Tables** must feature explicit ruling lines (e.g., `border-b border-gray-200`) and distinct column headers. Striped rows may be used for dense accounting data.
- **Forms** (for SAR generation, email capture for complaints) must use high-contrast borders and clear focus states (a stark blue or black outline) compliant with WCAG accessibility standards.

**3. Alerts and Evidence Blocks:**
- Callouts for vital legal points must use strict geometric borders (e.g., a left 4px solid border in crimson or warning-amber) rather than soft, background-faded blocks.
- **Do not use Emojis.** Use professional SVG iconography (Lucide or Heroicons) for document retrieval, external links, and alerts.
- Quotes from legal documents or statutes should be deeply indented and italicized, accompanied by a citation source.

## 5. Light vs. Dark Mode Strategy

- **Default Stance:** The primary experience should default to a crisp, high-contrast Light Theme (Black text on stark White) representing transparency and paper documentation.
- **Night/Dark Mode:** Accessible but inverted for severe contrast. Must use Slate-900 backgrounds rather than pure black (`#000000`) to avoid aggressive eye strain during deep reading, with Slate-50 used for primary typography. Ensure borders remain visible (e.g., `border-slate-700`).

## 6. Pre-Delivery Visual Checklist

Before any asset or page goes live, confirm:
- [ ] No emojis are present in the UI copy or icons.
- [ ] Light mode text contrast meets at least a 4.5:1 ratio against its background.
- [ ] Evidence/data tables have explicit headers and clean column alignment.
- [ ] Transitions and interactions are linear, fast (150ms), and predictable.
