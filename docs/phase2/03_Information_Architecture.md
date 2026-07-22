# 03 Information Architecture

**Version:** 1.0
**Status:** Draft (Phase 2)
**Purpose:** Map the structure, flow, and organization of content within the Moodify platform to ensure logical user journeys.
**Scope:** Sitemap, navigation hierarchies, user roles, user journeys, data flow, content strategy, and search strategy.
**References:** 
- Moodify Implementation Plan v3.0 (Sections 14, 17)
- Moodify Brand Guidelines v2.0

---

## Global Considerations
*These apply to all architecture maps in this document unless otherwise specified.*

- **Accessibility:** Navigation must be fully keyboard accessible (Tab flow matches visual hierarchy) and logical for screen readers. 
- **Responsive Behaviour:** Deeply nested navigation is collapsed into a drawer or bottom tab bar on mobile (width < 480px).
- **Developer Notes:** Adhere to Next.js App Router conventions. Protect all authenticated routes using Supabase middleware.
- **Future Considerations:** Ensure the navigation structure can scale to support future roles (e.g., therapists) and features (e.g., wearables).

---

## 1. User Roles
- **Guest / Unauthenticated User:** Can access public landing and marketing pages. Can register or log in.
- **Authenticated User (Primary):** Can access the core application (Dashboard, Scan, Chat, Reports, Profile, Settings).

---

## 2. Complete Sitemap & Page Relationships

```text
/ (Landing Page)
├── /login (Login)
│   └── /forgot-password (Forgot Password)
├── /register (Register)
│
└── /dashboard (Authenticated Hub)
    ├── /scan (Camera Consent & Capture)
    │   └── /scan/result (Emotion Result & Suggestions)
    ├── /reports (Analytics & PDF Generation)
    ├── /chat (AI Chat Companion)
    └── /profile (Settings & Privacy)
```

### Page Relationships
- **Dashboard:** The central hub. All secondary flows branch from and return here.
- **Scan Flow:** Modal-like or full-screen flow taking priority over the dashboard. Ends by returning to the Dashboard with updated context.
- **Global Availability:** Chat and Profile are globally accessible from the Dashboard layer.

---

## 3. Navigation Hierarchy & Rules

### Navigation Principles
- **Max 3 clicks:** Any core feature is reachable within 3 clicks from the Dashboard.
- **Dashboard Home:** Always the fallback state and primary anchor point.
- **Scan Always Accessible:** The primary action (Scan) is prominent from the Dashboard.
- **No Dead Ends:** Every page, including error states and empty states, must have a clear path forward or back to the Dashboard.

### Hierarchical Levels
1. **Global Navigation:** Visible to authenticated users on root-level views (Dashboard, Reports, Chat, Profile).
2. **Contextual Navigation:** Specific to a flow (e.g., "Cancel" or "Retake" within the Scan flow, "Download PDF" within Reports).

---

## 4. User Journeys (Core Flows)

### Journey A: The Core Scan Loop
1. **Entry:** User opens Dashboard.
2. **Action:** Clicks "New Scan" (navigates to `/scan`).
3. **Capture:** Grants camera permission (first time only), captures photo.
4. **Analysis:** Views loading state while vision pipeline and AI process data.
5. **Result:** Lands on `/scan/result`. Reads AI insight and views wellness suggestions.
6. **Interaction:** Clicks "Add to Plan" on a suggestion.
7. **Exit:** Navigates back to Dashboard, where the task appears in the checklist.

### Journey B: Seeking Deeper Understanding (Secondary Flow)
1. **Entry:** User opens Dashboard.
2. **Action:** Wants more context on their recent mood. Clicks Chat shortcut.
3. **Interaction:** Lands on `/chat`. Reviews context badge (last 7 days). Types a message.
4. **Response:** AI responds warmly based on recent scan data.
5. **Exit:** Navigates back to Dashboard or closes app.

---

## 5. Information Hierarchy

Content on individual pages is prioritized from top to bottom based on user need:

- **Dashboard:** Current Mood > AI Insight > Actionable Tasks > Historical Charts.
- **Scan Result:** Emotion Label > AI Explanation > Non-diagnostic Disclaimer > Actionable Suggestions.
- **Reports:** Weekly/Monthly Summary Text > Visual Distribution > Task Completion Rates.
- **Profile:** Personal Info > Theme/Notification Preferences > Destructive Actions (Delete Data/Account).

---

## 6. Data Flow

1. **Client to Edge:** Image captured in browser -> encoded as base64.
2. **Edge to AI Services:** Backend FastAPI receives base64 -> sends to MediaPipe (face detection) -> DeepFace (emotion classification) -> Gemini API (Insight generation).
3. **AI Services to Database:** Backend stores results (emotion, score, AI insight) in Supabase Postgres.
4. **Database to Client:** Backend returns the combined payload to the Next.js client for immediate display. State is updated locally to prevent full page reloads.

---

## 7. Content Strategy

- **Progressive Disclosure:** Present the simplest, most immediate information first (e.g., the emotion label). Reveal deeper layers (e.g., historical charts, detailed reports) only when the user scrolls or navigates to them.
- **Language:** Tone strictly adheres to "The Caregiver/Sage" persona defined in Brand Guidelines.
- **Disclaimers:** Non-diagnostic disclaimers must be treated as primary content structurally, appearing immediately below AI-generated insights, never hidden in footers.

---

## 8. Search Strategy

- **No Global Search MVP:** Given the scoped nature of the application, a global search bar is omitted to maintain a calm, uncluttered interface.
- **Contextual Filtering:** Users find historical data via date-range filters on the Dashboard and Reports pages, rather than keyword search.
- `[TBD — needs input: If task lists grow large, is a local filter/search required for the 'Today's Plan' widget?]`

---

## 9. Future Architecture (Post-MVP)

- **Therapist Dashboard:** A separate role and routing structure (`/pro/*`) for healthcare providers to view aggregate patient data (requires explicit consent modeling).
- **Wearable Integration:** New background data ingestion layer feeding into the mood history table asynchronously.
- **Multi-user / Org Accounts:** Architecture must eventually support organization IDs for enterprise wellness deployments.

---
*⚠ Conflict Note: No conflicts with established Brand Guidelines or Implementation Plan identified in this document.*
