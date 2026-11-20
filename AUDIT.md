# Repository audit — first pass

## Findings
- Single-file HTML application with substantial inline CSS and a responsive chat/assistant-style layout.
- Review inline JavaScript for secure rendering of untrusted chat content, safe storage of user data, keyboard navigation, and mobile viewport behavior.
- If the page calls an AI/API backend, keep provider credentials server-side; never embed secret API keys in browser JavaScript.
- Vercel can host the static frontend, but any required backend must be deployed separately.

## Verification
HTML source sampled; interactive behavior and backend integration not executed.