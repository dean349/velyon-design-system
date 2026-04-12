# Los Romeros Limited — Brand Kit

*Last updated: April 10, 2026*

This document provides the raw design tokens (colors, font definitions, logo rules) necessary for developers and designers to build out the Los Romeros digital presence.

## 1. Corporate Color Palette
These colors form the foundation of the brand's stark, document-driven aesthetic.

| Color | HEX | Tailwind Token | Usage |
| :--- | :--- | :--- | :--- |
| **White** | `#FFFFFF` | `bg-white` | Primary background (Light mode). Represents raw documentation. |
| **Slate 50** | `#F8FAFC` | `bg-slate-50` | Primary text (Dark mode). |
| **Slate 200** | `#E2E8F0` | `border-slate-200` | Borders, subtle dividers, and table rule lines in light mode. |
| **Slate 600** | `#475569` | `text-slate-600` | Secondary body text, annotations, and metadata in light mode. |
| **Slate 900** | `#0F172A` | `text-slate-900` | Primary headings, base text (light mode), and Dark mode background. |
| **Slate 950** | `#020617` | `bg-slate-950` | Primary buttons, deep contrasted areas. |

## 2. Semantic Color Palette
These colors are specifically reserved for legal annotations, exposure statements, and structural alerts.

| Color | HEX | Tailwind Token | Usage |
| :--- | :--- | :--- | :--- |
| **Crimson (Action/Alert)** | `#B91C1C` | `bg-red-700` | Critical regulatory exposure, primary warnings, missing documentation alerts. |
| **Crimson Light** | `#FEF2F2` | `bg-red-50` | Background for highlighted regulatory breaches or statutory violations. |
| **Amber (Notice)** | `#B45309` | `text-amber-700` | Pending actions, outstanding debts (e.g., Modelo 210 non-filing), caution notices. |
| **Blue (Link/System)** | `#1D4ED8` | `text-blue-700` | Official external links (e.g., ICAEW, HMRC), actionable links. |
| **Green (Safe/Cleared)** | `#15803D` | `text-green-700` | Verified compliance, resolved liabilities. Use sparingly. |

## 3. Typographic Tokens

**Font Families:**
- **Headings (Serif):** `Playfair Display, Georgia, serif`
- **Body & UI (Sans-Serif):** `Inter, system-ui, -apple-system, sans-serif`

**Sizing Scale (Desktop):**
- **H1 (Document Title):** 2.25rem (36px), Line Height 1.2
- **H2 (Section Header):** 1.875rem (30px), Line Height 1.3
- **H3 (Sub-header):** 1.5rem (24px), Line Height 1.4
- **Body (Primary):** 1rem (16px), Line Height 1.6
- **Metadata/Legal Footnote:** 0.875rem (14px), Line Height 1.5

## 4. Logo Guidelines & Restrictions

As a forensic, evidence-driven entity, the Los Romeros Limited "logo" should primarily be typographic rather than a pictorial mark, unless a specific monogram abstracting legal scales/documents is developed.

**Typographic Logo Rules:**
- The logo should be set in **Playfair Display Semi-Bold**.
- It must always explicitly state "Limited" or "Ltd" to enforce the legal corporate boundary.
- **Clear Space:** The minimum clear space around the logo must be equivalent to the height of the capital "L" in Los. No imagery or text should enter this zone.
- **Minimum Size:** For print, 20mm width. For digital, 120px width to ensure the serif details remain sharp.

**Color Constraints:**
- The logo may only appear in **Slate 900** (Full Black) on light backgrounds, or **Slate 50** (Off-White) on dark backgrounds. 
- Usage in Crimson or other semantic colors is strictly prohibited to maintain objective corporate neutrality.
