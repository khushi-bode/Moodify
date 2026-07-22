# 02 Design System

**Version:** 1.0
**Status:** Draft (Phase 2)
**Purpose:** Establish the foundational visual language and component specifications for the Moodify application.
**Scope:** Design tokens, grid and layout rules, spacing, comprehensive component library, motion guidelines, naming conventions, and folder structure.
**References:** 
- Moodify Brand Guidelines v2.0
- Moodify Implementation Plan v3.0

---

## Global Considerations
*These apply to all components in this document unless otherwise specified.*

- **Accessibility:** All interactive elements must have a visible focus ring (2px, Accent color: `#14B8A6`). Minimum contrast ratio is 4.5:1 for text. Never rely on color alone to convey state or information.
- **Responsive Behaviour:** Elements scale gracefully for viewports <480px. Touch targets must be at least 44x44px on mobile devices. 
- **Developer Notes:** Implement using Tailwind CSS + shadcn/ui. Use defined semantic tokens instead of raw hex values to support the theme system.
- **Future Considerations:** The design system should scale to support custom themes or user-defined color modes in later phases.

---

## 1. Design Tokens

### Colors
Reference Brand Guidelines for full definitions. Use these semantic tokens:
- **Primary:** `color-primary` (`#4F46E5`)
- **Secondary:** `color-secondary` (`#60A5FA`)
- **Accent:** `color-accent` (`#14B8A6`)
- **Success:** `color-success` (`#22C55E`)
- **Warning:** `color-warning` (`#F59E0B`)
- **Error:** `color-error` (`#EF4444`)
- **Background:** `color-bg-light` (`#F8FAFC`) / `color-bg-dark` (`#0F172A`)
- **Surface:** `color-surface-light` (`#FFFFFF`) / `color-surface-dark` (`#1E293B`)
- **Border:** `color-border` (`#E2E8F0`)
- **Text:** `color-text-primary` (`#0F172A`), `color-text-secondary` (`#64748B`)

### Typography
- **Primary Font:** Inter (App)
- **Secondary Font:** Poppins (Headings/Marketing)
- **Monospace:** JetBrains Mono (Dev)
- **Scale Tokens:** `text-h1` (48px, bold), `text-h2` (36px, bold), `text-h3` (30px, semibold), `text-h4` (24px, semibold), `text-body` (16px, regular), `text-small` (14px, regular), `text-caption` (12px, regular).

### Shadows & Elevation
- **Small (Cards):** `0 1px 2px rgba(15, 23, 42, 0.06)`
- **Medium (Dropdowns):** `0 4px 12px rgba(15, 23, 42, 0.10)`
- **Large (Dialogs):** `0 12px 32px rgba(15, 23, 42, 0.14)`
- **Extra Large (Feature cards):** `0 20px 48px rgba(15, 23, 42, 0.18)`

---

## 2. Spacing System
8-point spacing scale. Use these tokens for padding and margins:
- `space-0-5` (4px)
- `space-1` (8px)
- `space-1-5` (12px)
- `space-2` (16px)
- `space-3` (24px)
- `space-4` (32px)
- `space-6` (48px)
- `space-8` (64px)
- `space-12` (96px)

---

## 3. Grid System & Layout Rules
- **Desktop:** 12-column grid, 24px gutters, max content width 1200px, centered layout.
- **Tablet:** 8-column grid, 20px gutters.
- **Mobile:** 4-column grid, 16px gutters, 16px outer margin.
- **Layout Rule:** Maximize whitespace. One focal point per screen. Soft over sharp (rounded corners, no glassmorphism).

---

## 4. Component Library

### Core UI
- **Buttons:** Rounded corners (12px default, pill for CTAs if needed), filled. States: Default, Hover (subtle shift using `motion-fast`), Pressed (0.98 scale-down), Disabled (40% opacity).
- **Inputs / Forms:** Minimal, single-column layout. 12px border radius. Gray borders (`color-border`) transitioning to `color-accent` on focus.
- **Cards:** Large border radius (20px), soft shadows (Small or Extra Large), lots of whitespace.
- **Tables:** Clean, readable, minimal gridlines. Alternating row backgrounds should be avoided in favor of clean whitespace.
- **Charts:** Smooth curves, soft fills over harsh bar edges. Rounded tooltips.
  - `[TBD — needs input: Dark mode chart color palette mappings to maintain contrast against #1E293B]`
- **Dialogs (Modals):** 24px border radius, Large shadow. Used for destructive actions (Delete History/Account).
- **Dropdowns:** 12px border radius, Medium shadow.

### Camera Components
- **Consent Screen:** Clean text prompt with Primary button ("Allow Camera") and Secondary action ("Upload Image").
- **Camera Preview:** 16:9 or 4:3 aspect ratio mask with soft rounded corners.
  - `[TBD — needs input: Visual treatment for the face-detection bounding box/overlay]`
- **Capture / Retake Controls:** Prominent, rounded action button (e.g., shutter icon or "Take Photo").
- **Upload-image Fallback:** Dashed border dropzone with an upload icon.

### AI Components
- **AI Insight Snippet:** A text block featuring The Caregiver/Sage persona. Minimal container, perhaps with a subtle `color-bg-light` or `color-surface-dark` offset.
- **Suggested Prompt Chips:** Pill-shaped, `color-border` outline, `text-small`. Hover state fills background subtly.
- **Mood-context Badge:** Small visual indicator (e.g., "7-day context active") in Chat. 

### Dashboard Components
- **Current Mood Card:** Focal point. Displays the Emotion Label and Mood Score prominently.
- **Suggestion Cards:** Interactive cards (Accent color hints) for wellness actions. Includes "Add to Plan" button.
- **Task Checklist:** Simple checkbox list. Success Green (`#22C55E`) checkmarks upon completion.

### Navigation Components
- **Minimal Sidebar (Desktop):** Clear hierarchy, no unnecessary icons. Highlights active route with `color-primary`.
- **Bottom Nav (Mobile):** Icons with labels.

### Common States
- **Empty States:** Friendly copy ("Your first scan will show up here").
  - `[TBD — needs input: Specific illustration motifs for empty states like Dashboard or Reports]`
- **Loading States:** Descriptive text ("Reading your expression..."). 
  - `[TBD — needs input: Specific AI streaming/loading visual indicator]`
- **Error States:** Border shifts to Error Red (`#EF4444`). Helper text appears below the component with an icon. Errors are framed as solvable.

---

## 5. Motion
- `motion-fast` (120ms ease-out): Hover states, button presses.
- `motion-base` (200ms ease-in-out): Fade-ins, card entrances.
- `motion-slow` (350ms ease-in-out): Page transitions, chart draw-in.
- `motion-chart` (600ms cubic-bezier(0.22, 1, 0.36, 1)): Chart animation on data load.
- Avoid fast animations or flashing effects. All motion must feel smooth, natural, and purposeful.

---

## 6. Naming Conventions & Folder Structure
### Naming
- **Files (Frontend):** kebab-case (e.g., `scan-result.tsx`).
- **Files (Backend):** snake_case (e.g., `scan.py`).
- **Components:** PascalCase (e.g., `ScanResult`).
- **Design Tokens:** CSS variable format `--color-primary` mapped in Tailwind config.

### Folder Structure
```text
moodify/
├── frontend/
│   ├── app/                 # Next.js App Router pages
│   ├── components/          # Reusable UI components
│   ├── lib/                 # Supabase client, api helpers
│   ├── hooks/               # React hooks
│   └── styles/              # Global CSS, design tokens
└── backend/
    ├── app/
    │   ├── api/             # FastAPI routers
    │   ├── services/        # Vision pipeline, AI provider
    │   ├── models/          # Data models
    │   └── core/            # Config, security, rate limiting
    └── tests/               # Backend tests
```

---

## 7. Design Review Checklist
- [ ] Are typography and colors strictly using design tokens?
- [ ] Is there only one focal point per screen?
- [ ] Do interactive elements have a 2px `color-accent` focus ring?
- [ ] Are all shadow and border radius values adhering to the defined tiers?
- [ ] Are destructive actions confirming before execution?
- [ ] Do AI insight screens include the visible non-diagnostic disclaimer?
- [ ] Is the interface uncluttered, leveraging the 8-point spacing system?

---
*⚠ Conflict Note: No conflicts with established Brand Guidelines or Implementation Plan identified in this document.*
