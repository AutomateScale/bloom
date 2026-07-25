# Setup Guide — written for parents, not coders

You do not need to be technical. Take it one step at a time.

---

## Step 1 — The Outreach Tracker (5 minutes)
1. Double-click **`tracker.html`**. It opens in your web browser (Chrome, Safari, etc.).
2. It comes with example categories (Treating Team, Second Opinions, Trials, Compassionate Use, Foundations). For each person or place you contact, set a **status** (Not started → Drafted → Sent → Replied) and jot a **note**.
3. It **saves automatically in your browser** on your computer. Nobody else can see it.
4. To make it your own, open `tracker.html` in any text editor and edit the `DATA` list near the bottom (each line is one contact — copy a line, change the name/email/ask). Save, refresh the page.

*Tip: keep this tab open. It's your single view of who you're waiting on.*

---

## Step 2 — The AI Assistant (the powerful part)
The reports below are best created with an **AI assistant** that can read your child's records. A good free/low-cost option is **Claude** (claude.ai) or **Claude Code** (runs on your own computer). The assistant becomes your tireless research partner and scribe.

**How to use it — privately:**
1. Gather your child's records (scans, pathology, doctor letters) in one folder, or your own Google Drive.
2. Give the assistant the records and ask it to help you build, from the templates in `templates/`:
   - a **Doctor Visit Guide** — the smartest questions to ask, in priority order;
   - a **Master Case Summary** — one page any new doctor can read in 30 seconds;
   - **Outreach emails** — to experts, trial teams, and foundations.
3. Ask it anything, grounded in your documents: *"What did the last scan show?" "What has my child already been treated with?" "Which trials might fit?" "Who haven't we heard back from?"*

Your data stays with you and your assistant — not with us.

---

## Step 3 — The War-Room Board (optional, at-a-glance)
In the `board/` folder:
1. Copy `status.example.json` to `status.json` and edit it with your fronts (medical, and anything else you're juggling).
2. Run it: open Terminal, type `python3 ` then drag in `board/board.py`, press Enter. A live status board appears and refreshes itself.
3. Edit `status.json` any time; the board updates.

*(If Terminal is unfamiliar, skip this — the tracker and templates are the core.)*

---

## Step 4 — Turn reports into PDFs to print/share (optional)
If you have `pandoc` and a browser installed, `build.sh` turns the markdown templates into clean, printable PDFs. Ask your AI assistant to help you run it — or just print from your browser.

---

## The mindset
- **Get every decision made *on purpose*, not by default.** These tools exist to make sure no option is skipped and no email is forgotten.
- **You are the coordinator of a team.** Doctors, lawyers, experts, foundations — this keeps them all in one view.
- **Bring questions, not conclusions, to your doctors.** The assistant helps you ask better questions; your medical team makes the calls.

Keep going. This system was built by a parent in the same fight. It's yours now.
