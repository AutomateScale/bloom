# Connecting Google Drive to Bloom

Bloom can read your medical documents straight from Google Drive. **Bloom has no server** — files travel only between *your* browser and *your* Google account. We never see them.

There are two ways. Pick the one that fits.

---

## ✅ Option 1 — Instant, zero setup (recommended for most parents)
If you have **Google Drive for Desktop** installed (the app that syncs your Drive to your computer):

1. Open Bloom (`app.html`) → **Documents** → **Connect a folder**.
2. Choose your **Google Drive** folder (e.g. `Google Drive/My Drive/Medical`).
3. Done. Bloom reads it locally — instantly, privately, no keys, no sign-in.

*Don't have Drive for Desktop? Get it free at google.com/drive/download — then use the steps above.*

---

## 🔑 Option 2 — Sign in to Google directly (for the hosted website)
This lets any user click **"Connect Google Drive"** and sign in — needed when Bloom is published online. One-time setup, ~5 minutes:

**A. Host Bloom** at a web address (GitHub Pages is free) — e.g. `https://yourname.github.io/bloom/`. Google won't allow a plain file on disk; it needs a real https address.

**B. In [Google Cloud Console](https://console.cloud.google.com):**
1. Create a project (or use one you have).
2. **APIs & Services → Library** → enable **Google Drive API** and **Google Picker API**.
3. **APIs & Services → Credentials → Create Credentials → API key.** Copy it.
4. **Create Credentials → OAuth client ID → Web application.**
   - Under **Authorized JavaScript origins**, add your Bloom address (e.g. `https://yourname.github.io`).
   - Copy the **Client ID**.
5. Configure the **OAuth consent screen** (External; add yourself as a test user while it's in testing).

**C. Paste your keys into Bloom:** open `app.html`, near the top find:
```js
const GOOGLE_CLIENT_ID=''; // paste your Client ID
const GOOGLE_API_KEY='';   // paste your API key
```
Fill both in, save, re-publish.

**D. Use it:** open the hosted Bloom → **Documents → Connect Google Drive** → sign in → pick your folder or files. Done.

---

### Notes
- Bloom only requests **read-only** access to Drive (`drive.readonly`).
- Nothing is uploaded to any Bloom server — there isn't one. Your token and files stay in your browser.
- Google Docs are read as text; PDFs/images are catalogued by name (share them with your AI assistant to have their contents read).
