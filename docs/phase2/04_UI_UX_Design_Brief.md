# 04 UI/UX Design Brief

**Version:** 1.0
**Status:** Draft (Phase 2)
**Purpose:** Provide comprehensive, screen-by-screen specifications guiding the user experience and interface design of Moodify.
**Scope:** Core flows (Landing to AI Suggestions) and Secondary flows (Analytics to Settings).
**References:** 
- Moodify Implementation Plan v3.0 (Sections 6, 9, 17)
- Moodify Brand Guidelines v2.0

---

## Global Considerations
*These apply to all screens in this document unless otherwise specified.*

- **Accessibility:** Ensure high contrast text (4.5:1), visible focus states (2px accent ring) for all interactive elements, and proper ARIA labels for screen readers.
- **Responsive Behaviour:** All layouts are designed mobile-first. Desktop layouts utilize a centered max-width (1200px) approach to preserve whitespace.
- **Developer Notes:** Components are built with Tailwind CSS. Maintain state carefully across API delays.
- **Future Considerations:** Future states may accommodate multi-user orgs and complex reporting, requiring more robust dashboard navigation.

---

## Core Flow

### 1. Landing
- **Purpose:** Introduce Moodify to a first-time visitor and drive sign-up.
- **User Goal:** Understand what the product does and decide if it's trustworthy.
- **Business Goal:** Maximize conversion to Registration.
- **Entry Point:** Direct URL, marketing campaigns.
- **Exit Point:** "Start Journey" button -> `/register`, or "Log in" -> `/login`.
- **Components Used:** Hero, About, Key Features, How It Works, Testimonials, FAQ, Footer.
- **Layout Structure:** Single-column scrolling page. High-impact Hero section with primary CTA above the fold. 
- **User Actions:** Click CTA to register, scroll to read information, click FAQ toggles.
- **API Calls:** None (static page).
- **AI Integration:** None.
- **States:** 
  - *Empty/Loading/Error/Success:* N/A.
- **Edge Cases:** User is already authenticated (redirect to `/dashboard`).

### 2. Register
- **Purpose:** Create a new user account.
- **User Goal:** Securely create an account with minimal friction.
- **Business Goal:** Capture user credentials and initialize their profile.
- **Entry Point:** Landing page.
- **Exit Point:** Successful registration -> `/dashboard`, or "Already have an account?" -> `/login`.
- **Components Used:** Simple Form, Email/Password inputs, Primary Button, Auth Links.
- **Layout Structure:** Centered card on a clean background to focus attention.
- **User Actions:** Enter email, enter password, submit form.
- **API Calls:** `Supabase Auth: signUp`.
- **AI Integration:** None.
- **States:**
  - *Error:* Inline validation (e.g., "Password must be at least 8 characters"). Form-level error for existing emails.
  - *Loading:* Button shows spinner ("Creating account..."), inputs disabled.
- **Edge Cases:** Network failure during submission.

### 3. Login
- **Purpose:** Authenticate an existing user.
- **User Goal:** Access personal dashboard and history.
- **Business Goal:** Securely verify returning users.
- **Entry Point:** Landing page, Register page, or expired session redirect.
- **Exit Point:** Successful login -> `/dashboard`, or "Forgot Password" -> `/forgot-password`.
- **Components Used:** Simple Form, Email/Password inputs, Primary Button, Forgot Password link.
- **Layout Structure:** Centered card on a clean background.
- **User Actions:** Enter email, enter password, submit form.
- **API Calls:** `Supabase Auth: signInWithPassword`.
- **AI Integration:** None.
- **States:**
  - *Error:* "Invalid credentials" banner. 
  - *Loading:* Button shows spinner ("Logging in...").
- **Edge Cases:** Account deleted (show error).

### 4. Dashboard
- **Purpose:** Display the emotional overview and serve as the day-to-day hub.
- **User Goal:** Quickly understand current mood status and what actions to take.
- **Business Goal:** Encourage daily habit formation and task completion.
- **Entry Point:** Post-login, post-scan, or clicking Home in navigation.
- **Exit Point:** "New Scan" -> `/scan`, Chat shortcut -> `/chat`, Navigation to Reports/Profile.
- **Components Used:** Current Mood Card, AI Insight Snippet, Task Checklist, Timeline Charts.
- **Layout Structure:** Grid layout (12-column desktop). Top section: Current state & CTAs. Bottom section: Historical data.
- **User Actions:** Start a scan, check off tasks, change chart date ranges, navigate elsewhere.
- **API Calls:** `GET /api/mood-history`, `GET /api/tasks`, `PATCH /api/tasks/{id}`.
- **AI Integration:** None directly invoked here, but displays generated AI insights.
- **States:**
  - *Empty:* First-time user sees a welcoming state ("Your first scan will show up here") instead of empty charts.
  - *Loading:* Skeleton loaders for cards and charts.
  - *Success:* Green checkmarks when a task is marked complete.
- **Edge Cases:** Data fetch failure (show retry banner).

### 5. Camera Scan (Consent & Capture)
- **Purpose:** Obtain camera consent and capture a photo for emotion detection.
- **User Goal:** Easily and privately take a photo to analyze mood.
- **Business Goal:** Capture high-quality input for the AI pipeline with low abandonment.
- **Entry Point:** "New Scan" button on Dashboard.
- **Exit Point:** Photo captured -> `/scan/result`.
- **Components Used:** Consent Overlay, Camera Preview mask, Capture/Retake Buttons, Upload Fallback.
- **Layout Structure:** Full-screen or large modal to maintain focus. Centered camera preview.
- **User Actions:** Grant permission, align face, click capture, click retake if unhappy.
- **API Calls:** `POST /api/scan` (triggered after capture).
- **AI Integration:** Sends image to backend for MediaPipe + DeepFace processing.
- **States:**
  - *Error:* Camera permission denied -> display Upload Fallback UI.
  - *Loading:* "Analyzing expression..." overlay while `POST /api/scan` resolves.
- **Edge Cases:** No face detected by MediaPipe (System returns guidance message: "We couldn't quite see your face — try moving closer to good light").

### 6. Emotion Result & AI Suggestions
- **Purpose:** Show the outcome of the scan, explain it, and offer actionable wellness tasks.
- **User Goal:** Understand what the emotion means and what to do about it.
- **Business Goal:** Deliver value (insight + action) to complete the core loop.
- **Entry Point:** Successful capture from `/scan`.
- **Exit Point:** "Add to Plan" or "Done" -> `/dashboard`.
- **Components Used:** Emotion Label (H2), Mood Score, AI Insight Text, Non-diagnostic Disclaimer, Suggestion Cards.
- **Layout Structure:** Vertical reading flow. Result at top -> AI context -> Disclaimer -> Actionable cards at bottom.
- **User Actions:** Read insight, click "Add to Plan" on 1-2 suggestions.
- **API Calls:** `POST /api/tasks` (when adding to plan).
- **AI Integration:** Displays the Gemini-generated insight based on the emotion and context.
- **States:**
  - *Error:* If AI insight fails to generate, show deterministic emotion/score with stubbed insight.
  - *Success:* Clicking "Add to Plan" warmly acknowledges the action.
- **Edge Cases:** Low confidence detection (Prompt user to rescan with better lighting).

---

## Secondary Flow

### 7. Analytics & Reports
- **Purpose:** Provide a weekly/monthly narrative summary and historical charts.
- **User Goal:** Understand long-term emotional patterns and trends.
- **Business Goal:** Prove long-term value and retain users.
- **Entry Point:** Sidebar/Navigation from Dashboard.
- **Exit Point:** Navigation back to Dashboard, or "Download PDF".
- **Components Used:** Weekly/Monthly Toggle, Summary Text block, Charts (Timeline, Distribution), Download Button.
- **Layout Structure:** Toggle at top, Summary narrative below it, followed by visual charts.
- **User Actions:** Toggle timeframes, hover on charts for tooltips, download PDF.
- **API Calls:** `GET /api/reports/weekly` (or `monthly`), `GET /api/reports/{id}/pdf`.
- **AI Integration:** Gemini API summarizes the data into a short narrative paragraph.
- **States:**
  - *Empty:* Insufficient data state (e.g., if history < 3 days) -> "Keep scanning! We need a few more days of data to build your report."
  - *Loading:* Skeleton text for the narrative summary.
- **Edge Cases:** PDF generation timeout (show retry button).

### 8. Chat
- **Purpose:** Provide a mood-aware conversational companion.
- **User Goal:** Talk through feelings in a safe, non-judgmental space.
- **Business Goal:** Deepen engagement through personalized AI interaction.
- **Entry Point:** Dashboard chat shortcut or navigation.
- **Exit Point:** Back to Dashboard.
- **Components Used:** Message List, Input Box, Suggested Prompt Chips, Context Badge.
- **Layout Structure:** Standard chat interface. Message list takes up most vertical space, fixed input at bottom.
- **User Actions:** Select a prompt chip, type a message, scroll history.
- **API Calls:** `GET /api/chat/history`, `POST /api/chat`.
- **AI Integration:** Gemini API responds using the 7-day mood context and "Caregiver/Sage" persona.
- **States:**
  - *Error:* Message failed to send (show red '!' with tap-to-retry).
  - *Loading:* Subtle AI typing indicator.
    - `[TBD — needs input: Exact visual specification of the AI typing indicator]`
- **Edge Cases:** User inputs crisis language (Triggers fixed safe-fallback response bypassing normal AI generation).

### 9. Profile & Settings
- **Purpose:** Manage account, preferences, and data privacy.
- **User Goal:** Control personal information and app appearance.
- **Business Goal:** Provide transparency and trust regarding user data.
- **Entry Point:** Sidebar/Navigation.
- **Exit Point:** Back to Dashboard, or Log out.
- **Components Used:** Forms, Toggles (Theme, Notifications), Destructive Buttons, Confirmation Modals.
- **Layout Structure:** List of distinct sections (Personal, Preferences, Data & Privacy).
- **User Actions:** Toggle theme, update info, request data deletion.
- **API Calls:** `DELETE /api/user/mood-history`, `DELETE /api/user/account`.
- **AI Integration:** None.
- **States:**
  - *Success:* Toast notification for saved preferences.
  - *Error:* Failed to delete data (show banner).
- **Edge Cases:** User deletes account (immediately log out and redirect to `/login`).

---
*⚠ Conflict Note: No conflicts with established Brand Guidelines or Implementation Plan identified in this document.*
