# 06 High Fidelity UI

**Version:** 1.0
**Status:** Draft (Phase 2 - Batch A)
**Purpose:** Provide the complete visual specification for every Moodify screen, production-ready for direct implementation.
**Scope:** Core Emotional Flow (Batch A).
**References:** 
- Moodify UI/UX Design Brief v1.0
- Moodify Design System v1.0
- Moodify Brand Guidelines v2.0

---

## Batch A — Core Emotional Flow

### 1. Landing
- **Visual Hierarchy:** Hero statement (focal point) -> Primary CTA -> Value Props -> Testimonials.
- **Color Usage:** 
  - Background: `color-bg-light`
  - Hero Text: `color-text-primary`
  - CTA Button: `color-primary`
- **Typography:** `text-h1` (Hero), `text-h3` (Section headers), `text-body` (Descriptions).
- **Spacing:** `space-12` between major sections, `space-4` below headings.
- **Grid:** Desktop: 12-column centered (max 1200px). Mobile: 4-column (16px outer margin).
- **Components:** Button (Rounded, Filled, Primary), Nav (Top-bar, text links).
- **Icons:** N/A (Keep clean).
- **Cards:** N/A.
- **Charts:** N/A.
- **Shadows:** N/A on flat sections.
- **Borders:** N/A.
- **Motion:** `motion-base` fade-in on load.
- **Micro-interactions:** Nav links underline on hover.
- **Hover States:** CTA Button uses `motion-fast` for subtle background shift.
- **Focus States:** 2px `color-accent` ring.
- **Loading States:** N/A.
- **Error States:** N/A.
- **Empty States:** N/A.
- **Responsive Layouts:** Mobile stack blocks vertically; desktop side-by-side for value props.
- **Dark Mode Behavior:** Background switches to `color-bg-dark`. Text inverts to light variants.
- **Accessibility:** 4.5:1 contrast on CTA text. Logical tab index.
- **Developer Implementation Notes:** Static page; no auth wrappers.

### 2. Login
- **Visual Hierarchy:** "Log In" Heading -> Inputs -> Primary CTA -> Forgot Password.
- **Color Usage:** 
  - Background: `color-bg-light`
  - Form Container: `color-surface-light`
  - CTA: `color-primary`
- **Typography:** `text-h2` (Title), `text-body` (Labels), `text-small` (Links).
- **Spacing:** `space-6` above form, `space-3` between inputs.
- **Grid:** Single column, max-width 400px centered on screen.
- **Components:** Inputs (Minimal), Button (Rounded, Filled), Dialog/Card (Container).
- **Icons:** N/A.
- **Cards:** Login form wrapped in a Card component.
- **Charts:** N/A.
- **Shadows:** Small shadow on form card.
- **Borders:** `color-border` on inputs.
- **Motion:** `motion-fast` on button press.
- **Micro-interactions:** Inputs transition border to `color-accent` on focus.
- **Hover States:** Button background shift.
- **Focus States:** 2px `color-accent` ring.
- **Loading States:** Button replaces text with inline spinner, opacity 80%.
- **Error States:** Input border shifts to `color-error`. Helper text in `color-error` below input.
- **Empty States:** N/A.
- **Responsive Layouts:** Full width on mobile (minus 16px margins).
- **Dark Mode Behavior:** Card surface `color-surface-dark`.
- **Accessibility:** Ensure ARIA labels on email/password fields.
- **Developer Implementation Notes:** Handle Supabase auth errors gracefully in the UI.

### 3. Register
- **Visual Hierarchy:** "Create Account" -> Inputs -> CTA -> "Log In" link.
- **Color Usage:** Same as Login.
- **Typography:** Same as Login.
- **Spacing:** Same as Login.
- **Grid:** Same as Login.
- **Components:** Inputs (Minimal), Button (Rounded, Filled), Card (Container).
- **Icons:** N/A.
- **Cards:** Registration form card.
- **Charts:** N/A.
- **Shadows:** Small shadow.
- **Borders:** `color-border` on inputs.
- **Motion:** `motion-fast` on interactions.
- **Micro-interactions:** Same as Login.
- **Hover States:** Same as Login.
- **Focus States:** 2px `color-accent` ring.
- **Loading States:** Button spinner.
- **Error States:** `color-error` on borders and helper text.
- **Empty States:** N/A.
- **Responsive Layouts:** Mobile full width.
- **Dark Mode Behavior:** Surface changes to `color-surface-dark`.
- **Accessibility:** ARIA labels on inputs.
- **Developer Implementation Notes:** Same structure as Login, just different API endpoint.

### 4. Dashboard
- **Visual Hierarchy:** Greeting -> Current Mood Card -> Tasks -> Historical Charts.
- **Color Usage:** 
  - Background: `color-bg-light`
  - Cards: `color-surface-light`
  - Mood highlights: dynamic based on Emotion-to-Color mapping (e.g., `color-secondary` for Calm).
- **Typography:** `text-h3` (Greeting), `text-h4` (Section titles), `text-body` (Content).
- **Spacing:** `space-4` between widgets, `space-3` padding inside cards.
- **Grid:** 12-column desktop (Mood card spans 8, Tasks span 4). Mobile: Stacked 1-column.
- **Components:** Cards, Button (Primary for Scan), Navigation (Sidebar/Bottom).
- **Icons:** Bell (notifications), User (avatar).
- **Cards:** Soft corners (20px), Medium shadow.
- **Charts:** Timeline chart in bottom section.
- **Shadows:** Medium on main cards.
- **Borders:** None on cards (rely on shadows).
- **Motion:** `motion-base` card entrance sequence (staggered).
- **Micro-interactions:** Checkbox ticks trigger `motion-fast` scale bounce.
- **Hover States:** Cards elevate slightly (shadow increase).
- **Focus States:** 2px `color-accent` ring on all interactive elements.
- **Loading States:** Skeleton loaders matching card dimensions.
- **Error States:** Toast banner `color-error` for failed data fetch.
- **Empty States:** "Your first scan will show up here" text with minimal abstract illustration (using `color-border` lines).
- **Responsive Layouts:** Grid collapses to vertical stack on `< 768px`.
- **Dark Mode Behavior:** Cards switch to `color-surface-dark`.
- **Accessibility:** Ensure complex cards can be bypassed via tab index.
- **Developer Implementation Notes:** Real-time optimistic UI updates when tasks are checked off.

### 5. Camera Permission
- **Visual Hierarchy:** Explanation Text -> "Allow Camera" CTA -> "Upload Image" fallback.
- **Color Usage:** `color-surface-light` modal on `color-bg-light`. CTA `color-primary`.
- **Typography:** `text-h4` for title, `text-body` for explanation.
- **Spacing:** `space-6` padding.
- **Grid:** Centered modal/full-screen block.
- **Components:** Button (Primary), Button (Minimal text link).
- **Icons:** Camera icon (`color-text-secondary`).
- **Cards:** Modal container.
- **Charts:** N/A.
- **Shadows:** Large shadow on modal.
- **Borders:** N/A.
- **Motion:** `motion-base` fade-in.
- **Micro-interactions:** N/A.
- **Hover States:** CTA background shift.
- **Focus States:** 2px `color-accent` ring.
- **Loading States:** N/A.
- **Error States:** If denied, modal transitions to Upload Fallback state.
- **Empty States:** N/A.
- **Responsive Layouts:** Full-screen on mobile.
- **Dark Mode Behavior:** Modal `color-surface-dark`.
- **Accessibility:** Focus traps inside the modal until resolved.
- **Developer Implementation Notes:** Rendered prior to requesting `getUserMedia()`.

### 6. Camera Scan
- **Visual Hierarchy:** Camera Feed -> Face Guide Overlay -> Capture Button.
- **Color Usage:** Live feed. Face Guide is white/translucent. Capture button `color-primary`.
- **Typography:** `text-body` for alignment instructions ("Look straight ahead").
- **Spacing:** Absolute positioning for overlays.
- **Grid:** Full container width/height (16:9 or 4:3 masked).
- **Components:** Video element, Button (Round Capture).
- **Icons:** N/A.
- **Cards:** N/A.
- **Charts:** N/A.
- **Shadows:** Drop shadow on Capture button for visibility over feed.
- **Borders:** Rounded 20px mask on the video feed.
- **Motion:** `motion-fast` shutter flash on capture.
- **Micro-interactions:** Face Guide pulses when aligned perfectly.
- **Hover States:** Capture button scales up slightly.
- **Focus States:** 2px `color-accent` ring.
- **Loading States:** N/A (Processing Screen handles this).
- **Error States:** "No face detected" toast banner overlaid.
- **Empty States:** N/A.
- **Responsive Layouts:** Stretches to fill available mobile viewport height.
- **Dark Mode Behavior:** UI controls remain consistent over the camera feed.
- **Accessibility:** Provide an alternative (Upload Image) easily reachable via keyboard.
- **Developer Implementation Notes:** Ensure the camera stream is properly cleaned up on unmount.

### 7. Processing Screen
- **Visual Hierarchy:** Loading Indicator -> "Analyzing expression..." text.
- **Color Usage:** Background `color-bg-light` (or dark), text `color-text-secondary`.
- **Typography:** `text-body`.
- **Spacing:** Centered flexbox layout.
- **Grid:** 1-column.
- **Components:** Inline spinner or custom loader.
- **Icons:** N/A.
- **Cards:** N/A.
- **Charts:** N/A.
- **Shadows:** N/A.
- **Borders:** N/A.
- **Motion:** Continuous looping `motion-slow` on loader.
- **Micro-interactions:** N/A.
- **Hover States:** N/A.
- **Focus States:** N/A.
- **Loading States:** This *is* the loading state.
- **Error States:** Handled via redirect or toast if timeout occurs.
- **Empty States:** N/A.
- **Responsive Layouts:** Full screen.
- **Dark Mode Behavior:** Standard background/text swap.
- **Accessibility:** `aria-live="polite"` announcing "Processing image".
- **Developer Implementation Notes:** Keep this screen visible until both MediaPipe and Gemini APIs resolve.

### 8. Emotion Result
- **Visual Hierarchy:** Emotion Label -> Mood Score -> Action Button to proceed.
- **Color Usage:** Emotion label text uses the Emotion-to-Color mapping (e.g., `color-accent` for Happy).
- **Typography:** `text-h2` (Emotion), `text-h1` (Score).
- **Spacing:** `space-6` top padding, center-aligned.
- **Grid:** 1-column stacked.
- **Components:** Typography layout.
- **Icons:** N/A.
- **Cards:** N/A.
- **Charts:** N/A.
- **Shadows:** N/A.
- **Borders:** N/A.
- **Motion:** `motion-base` slide-up on entrance.
- **Micro-interactions:** Score counts up from 0 to final number via `motion-chart`.
- **Hover States:** N/A.
- **Focus States:** N/A.
- **Loading States:** N/A.
- **Error States:** N/A.
- **Empty States:** N/A.
- **Responsive Layouts:** Centered on mobile and desktop.
- **Dark Mode Behavior:** Standard inversion.
- **Accessibility:** Score must be read out fully (e.g., "Score: 78 out of 100").
- **Developer Implementation Notes:** This is visually integrated with the AI Insight block below it.

### 9. AI Insight
- **Visual Hierarchy:** Insight Text paragraph -> Non-diagnostic Disclaimer.
- **Color Usage:** Text `color-text-primary`. Disclaimer `color-text-secondary`.
- **Typography:** `text-h4` (Insight), `text-caption` (Disclaimer).
- **Spacing:** `space-4` below the Emotion Result.
- **Grid:** 1-column constrained width (max 600px for readability).
- **Components:** Text block.
- **Icons:** Small info `(!)` icon next to disclaimer.
- **Cards:** N/A (sits on background).
- **Charts:** N/A.
- **Shadows:** N/A.
- **Borders:** N/A.
- **Motion:** `motion-slow` fade-in, slightly delayed after Emotion Result.
- **Micro-interactions:** N/A.
- **Hover States:** N/A.
- **Focus States:** N/A.
- **Loading States:** N/A.
- **Error States:** Stubbed generic message if AI fails.
- **Empty States:** N/A.
- **Responsive Layouts:** Text wraps naturally.
- **Dark Mode Behavior:** Standard text color swap.
- **Accessibility:** Disclaimer must not be visually hidden or sized too small to read.
- **Developer Implementation Notes:** Rendered directly below Section 8 on the same `/scan/result` route.

### 10. Personalized Suggestions
- **Visual Hierarchy:** "Suggestions" Header -> Suggestion Cards -> "Done" CTA.
- **Color Usage:** Cards use `color-surface-light`. "Add to Plan" buttons use `color-secondary`.
- **Typography:** `text-h4` (Header), `text-body` (Suggestion text).
- **Spacing:** `space-6` below AI Insight. Cards separated by `space-2`.
- **Grid:** Single column list (max 600px wide).
- **Components:** Card (Interactive), Button (Secondary).
- **Icons:** Plus icon (+) for "Add".
- **Cards:** Soft corners (12px), Small shadow.
- **Charts:** N/A.
- **Shadows:** Small shadow on cards.
- **Borders:** `color-border` on cards.
- **Motion:** `motion-base` staggered slide-up.
- **Micro-interactions:** Clicking "Add" transforms the button to a green Checkmark (`color-success`).
- **Hover States:** Card elevates to Medium shadow.
- **Focus States:** 2px `color-accent` ring on "Add" buttons.
- **Loading States:** N/A.
- **Error States:** Toast if `POST /api/tasks` fails.
- **Empty States:** N/A.
- **Responsive Layouts:** Full width on mobile.
- **Dark Mode Behavior:** Cards switch to `color-surface-dark`.
- **Accessibility:** Button must clearly state "Add [task name] to plan" for screen readers.
- **Developer Implementation Notes:** Integrated at the bottom of the `/scan/result` route. Clicking "Done" navigates back to Dashboard.
