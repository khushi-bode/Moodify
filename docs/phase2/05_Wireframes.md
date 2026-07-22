# 05 Wireframes

**Version:** 1.0
**Status:** Draft (Phase 2)
**Purpose:** Provide low-fidelity ASCII wireframes to visualize structural layout and hierarchy prior to high-fidelity design.
**Scope:** ASCII wireframes and layout rationales for all core and secondary flow screens.
**References:** 
- Moodify UI/UX Design Brief v1.0
- Moodify Brand Guidelines v2.0

---

## Global Considerations
*These apply to all wireframes in this document unless otherwise specified.*

- **Accessibility:** Logical top-to-bottom and left-to-right DOM ordering ensures clean screen-reader traversal. Skip-to-content links will be placed at the top of the DOM.
- **Responsive Behaviour:** These wireframes represent the mobile-first (narrow) viewport to enforce prioritization of content. On desktop, content centers within a 1200px max-width container, and bottom navigation moves to a left sidebar.
- **Developer Notes:** Translate structural ASCII directly to Tailwind flex/grid layouts.
- **Future Considerations:** The layout should leave room for potential secondary navigation headers if new feature areas (like professional roles) are introduced later.

---

## 1. Landing

```text
+-----------------------------------+
| [Logo]                [Login]     |
|-----------------------------------|
|                                   |
|   "Because Every Emotion Has      |
|           a Story."               |
|                                   |
|      [ Start Journey CTA ]        |
|                                   |
|-----------------------------------|
|          How It Works             |
|                                   |
|  1. Scan   2. Learn   3. Act      |
|                                   |
|-----------------------------------|
|           Testimonials            |
|-----------------------------------|
| Footer                [Register]  |
+-----------------------------------+
```
- **Hierarchy & Placement:** Hero section dominates. The primary CTA ("Start Journey") is placed dead center above the fold.
- **Information Priority:** Value proposition -> Action -> Social Proof.
- **User Interactions:** Scroll down for information, click CTA to register.

---

## 2. Register & 3. Login (Shared Layout)

```text
+-----------------------------------+
| [Logo]                            |
|-----------------------------------|
|                                   |
|  +-----------------------------+  |
|  |       Create Account        |  |
|  |                             |  |
|  | [ Email Input           ]   |  |
|  |                             |  |
|  | [ Password Input        ]   |  |
|  |                             |  |
|  | [      Register CTA     ]   |  |
|  |                             |  |
|  |  Already have an account?   |  |
|  |        [ Log In ]           |  |
|  +-----------------------------+  |
|                                   |
+-----------------------------------+
```
- **Hierarchy & Placement:** Form is centered vertically and horizontally. Clean background with no distractions.
- **Information Priority:** Input fields -> Primary Action -> Secondary Action (Switch to login/register).
- **User Interactions:** Input text, submit form.

---

## 4. Dashboard

```text
+-----------------------------------+
| [Avatar]                [Bell]    |
|           Good Morning!           |
|-----------------------------------|
| +-------------------------------+ |
| | Current Mood: Calm            | |
| | Score: 78/100                 | |
| | "You seem relaxed..."         | |
| |                [ New Scan ]   | |
| +-------------------------------+ |
|-----------------------------------|
| Today's Plan                  [+] |
| [x] Take 5 deep breaths           |
| [ ] Drink a glass of water        |
|-----------------------------------|
| This Week (Chart)                 |
|  |       *                        |
|  |   *       *                    |
|  | *           *                  |
|  +---------------------           |
|-----------------------------------|
| [Home]  [Reports]  [Chat] [User]  |
+-----------------------------------+
```
- **Hierarchy & Placement:** "Current Mood" card is the single focal point. "New Scan" button is highly visible inside the mood card. Tasks follow directly below for immediate actionability.
- **Information Priority:** Current Status -> Actionable Tasks -> Historical Data.
- **User Interactions:** Click "New Scan", check off tasks, view chart data.

---

## 5. Camera Scan (Consent & Capture)

```text
+-----------------------------------+
| [X] Cancel                        |
|-----------------------------------|
|                                   |
|  +-----------------------------+  |
|  |                             |  |
|  |       [ Camera View ]       |  |
|  |       [ Face Guide  ]       |  |
|  |                             |  |
|  +-----------------------------+  |
|                                   |
|   Find good lighting and look     |
|   straight ahead.                 |
|                                   |
|         ( O ) Capture             |
|                                   |
|    [ Upload Image Instead ]       |
+-----------------------------------+
```
- **Hierarchy & Placement:** Camera preview occupies the top two-thirds. The capture button is prominent and centrally aligned at the bottom.
- **Information Priority:** Camera View -> Capture Button -> Upload Fallback.
- **User Interactions:** Capture photo, switch to upload.

---

## 6. Emotion Result & AI Suggestions

```text
+-----------------------------------+
| [<] Back to Dashboard             |
|-----------------------------------|
|                                   |
|       Emotion: Surprised          |
|       Score: 65/100               |
|                                   |
|   "You might be feeling a bit     |
|   off-guard today. Taking a       |
|   moment to ground yourself       |
|   could help."                    |
|                                   |
|   *Disclaimer: AI generated, not  |
|    medical advice.                |
|-----------------------------------|
|  Suggestions:                     |
|  +-----------------------------+  |
|  | Take a 5-minute walk        |  |
|  | [ Add to Plan ]             |  |
|  +-----------------------------+  |
|                                   |
|           [ Done ]                |
+-----------------------------------+
```
- **Hierarchy & Placement:** Emotion and AI text are top-aligned to be read immediately. Disclaimer is directly attached to the AI text. Actionable suggestions appear sequentially below.
- **Information Priority:** Result -> AI Insight -> Disclaimer -> Actionable Steps.
- **User Interactions:** Read result, click "Add to plan", click "Done".

---

## 7. Analytics & Reports

```text
+-----------------------------------+
|          Reports                  |
| [Weekly] / [Monthly] Toggle       |
|-----------------------------------|
|                                   |
|   "This week, you've primarily    |
|   felt calm, with a slight dip    |
|   on Wednesday."                  |
|                                   |
|-----------------------------------|
| Mood Distribution (Pie Chart)     |
|         .---.                     |
|       /   |   \                   |
|      |    |    |                  |
|       \   |   /                   |
|         `---'                     |
|-----------------------------------|
|  [ Download PDF Report ]          |
|                                   |
|-----------------------------------|
| [Home]  [Reports]  [Chat] [User]  |
+-----------------------------------+
```
- **Hierarchy & Placement:** Time toggle at the absolute top. Human-readable narrative summary comes before abstract charts.
- **Information Priority:** Summary Text -> Visual Charts -> PDF Download.
- **User Interactions:** Toggle time period, view charts, click download.

---

## 8. Chat

```text
+-----------------------------------+
| [<]           Chat Companion      |
|-----------------------------------|
|  [ Context: 7-day trend calm ]    |
|                                   |
| [AI]: Hi there! How are you       |
|       feeling right now?          |
|                                   |
| [User]: A little overwhelmed.     |
|                                   |
| [AI]: I hear you. With everything |
|       going on, it makes sense.   |
|                                   |
|-----------------------------------|
|  ( Suggestion Chip 1 ) ( Chip 2)  |
| [ Type a message...        ] [>]  |
|-----------------------------------|
| [Home]  [Reports]  [Chat] [User]  |
+-----------------------------------+
```
- **Hierarchy & Placement:** Context badge at the top to reassure the user that the AI has context. Messages scroll vertically. Input is fixed at the bottom.
- **Information Priority:** Chat History -> Suggested Prompts -> Text Input.
- **User Interactions:** Scroll chat, tap suggestion chip, type and send message.

---

## 9. Profile & Settings

```text
+-----------------------------------+
|          Profile                  |
|-----------------------------------|
| Personal Info                     |
| [ Name Input                 ]    |
| [ Email Input                ]    |
|           [ Save ]                |
|-----------------------------------|
| Preferences                       |
| [x] Dark Mode                     |
| [ ] Notifications                 |
|-----------------------------------|
| Data & Privacy                    |
|                                   |
| [ Delete Mood History ]           |
|                                   |
| [ Delete Account ]                |
|                                   |
|-----------------------------------|
| [Home]  [Reports]  [Chat] [User]  |
+-----------------------------------+
```
- **Hierarchy & Placement:** Standard list-based settings view. Non-destructive actions (Name, Theme) at the top. Destructive actions grouped at the very bottom.
- **Information Priority:** Profile Info -> Display Preferences -> Destructive Actions.
- **User Interactions:** Update text, toggle switches, click delete buttons (triggering modals).

---
*⚠ Conflict Note: No conflicts with established Brand Guidelines or Implementation Plan identified in this document.*
