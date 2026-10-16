# Juno

A phone-first personal assistant built as a single-page Claude artifact.

- Live: https://claude.ai/artifact/1PtPhxvBffNFJEpnV6Dyxu
- Source: `index.html` (HTML, CSS and JS in one file)

## How it works
- **Brain:** Claude through the artifact `sample` capability, with three tiers: Fast (quick), Smart (default) and Genius (complex). Page-side tools cover timers, tasks, notes, memory and the calculator.
- **Memory:** a per-user private `db` document at `data/users/<id>/brain`, mirrored to localStorage.
- **Capabilities declared:** `sample` (images: true), `db`, `user`.

## Updating
Edit `index.html`, then republish to the same artifact URL.
