# Velyon Style Guide

The Velyon Style Guide translates our Brand Kit into functional, technical UI/UX patterns. This document provides the structure for developers and designers to build consistent, premium interfaces.

## 1. Technical Design Tokens (Tailwind CSS)

These tokens map our brand colors to actionable Tailwind classes.

```javascript
// tailwind.config.js extension
module.exports = {
  theme: {
    extend: {
      colors: {
        velyon: {
          obsidian: '#0A0A0A',  // bg-velyon-obsidian
          graphite: '#171717',  // bg-velyon-graphite
          offwhite: '#F5F5F5',  // text-velyon-offwhite
          grey: '#A3A3A3',      // text-velyon-grey
          azure: '#3B82F6',     // bg-velyon-azure
          gold: '#EAB308',      // text-velyon-gold
        }
      },
      fontFamily: {
        heading: ['"Plus Jakarta Sans"', 'sans-serif'],
        body: ['Inter', 'sans-serif'],
      }
    }
  }
}
```

## 2. UI Component Architecture

Every component must follow the "Liquid Glass & Premium Tech" aesthetic defined by the brand. 

### Shadows and Depth
We avoid flat design, but we also avoid harsh shadows. Depth is created through subtle layering.
*   **Base Background:** `bg-velyon-obsidian`
*   **Elevated Card:** `bg-velyon-graphite border border-white/5 shadow-lg shadow-black/50`
*   **Interactive Card (Hover):** Transition to `border-velyon-azure/30 shadow-velyon-azure/10` with a smooth `-translate-y-1` lift.

### Buttons & Call-to-Actions (CTAs)

1.  **Primary Button (The Conversion Driver)**
    *   **Background:** Electric Azure (`bg-blue-500`)
    *   **Text:** Pure White (`text-white font-medium/semibold`)
    *   **Hover State:** Brightens (`hover:bg-blue-400`) + slight glow (`shadow-lg shadow-blue-500/25`)
    *   **Animation:** `transition-all duration-300`
    *   *Usage:* "Book Consultation", "Get Started". At most one per viewport.

2.  **Secondary Button (The Alternative)**
    *   **Background:** Transparent with Submarine Border (`bg-transparent border border-white/10`)
    *   **Text:** Off-White (`text-velyon-offwhite`)
    *   **Hover State:** Background fill (`hover:bg-white/5`)
    *   *Usage:* "View Roadmap", "Learn More".

3.  **Ghost Button (Tertiary)**
    *   **Background:** Transparent, no border.
    *   **Text:** Neutral Grey (`text-velyon-grey`)
    *   **Hover State:** Text brightens (`hover:text-velyon-offwhite`)
    *   *Usage:* Cancel actions, minor footer links.

### Input Fields & Forms
*   **Background:** Very dark semi-transparent (`bg-black/20`)
*   **Border:** Subtle grey/white (`border border-white/10`)
*   **Focus State:** Border changes to Electric Azure (`focus:border-velyon-azure focus:ring-1 focus:ring-velyon-azure`).
*   **Placeholder Text:** Neutral Grey (`text-velyon-grey`).

## 3. Spacing & Grid System

Precision is critical for an executive aesthetic. Use an **8px linear scale** for all padding, margins, and component alignments.

*   `space-y-2` (8px): Inside small components (e.g., between an icon and a title).
*   `p-6` (24px): Standard inner padding for cards.
*   `gap-8` (32px): Standard gap for grid layouts (e.g., feature bento boxes).
*   `py-24` (96px): Standard vertical spacing between major landing page sections.
*   **Container Width:** Max width of `1280px` (`max-w-7xl`). Content should breathe.

## 4. Interaction & Motion

Animations must feel **deliberate, fluid, and never rushed.**

*   **Standard Transition:** `transition-all duration-300 ease-in-out`
*   **Page/Section Reveal:** Fades up (`opacity-0 translate-y-4` to `opacity-100 translate-y-0`) with a `700ms` duration.
*   **Micro-interactions:** Icons inside cards should slightly translate or change opacity on hover, giving a "live" feel to the interface without overwhelming the user.

## 5. Accessibility (A11y) Check

*   **Contrast Ratio:** Ensure primary text (`#F5F5F5`) against background (`#0A0A0A`) exceeds the **WCAG 2.1 AAA** standard (it does: ~16:1 ratio).
*   **Click Targets:** Minimum 44x44px for all hit boxes (buttons, mobile nav icons).
*   **State Indication:** Color cannot be the *only* indicator of state. Add focus rings, border changes, or text weight changes.
