# Project map

<!-- castra-core:start -->
## Castra Core

Purpose: Release Board reports the next release candidate from a small local queue.

Start with the product overview and architecture below. Use the declared native commands; Castra does not replace them.

- Product: docs/product.md
- Architecture: docs/architecture.md
- Setup: python3 -m venv .venv
- Run: ./.venv/bin/python -m release_board
- Validate: ./.venv/bin/python -m unittest discover -s tests -v
- Inspect: ./.venv/bin/python -m release_board --json
- Troubleshoot: ./.venv/bin/python -m release_board --doctor
- Interface check (does not run commands): castra doctor --repo .
- Exercise one trusted native command: castra exercise --repo . validate.
- Continuity: docs/active-work.md, docs/decisions.md, docs/improvements.md

Read a nearer AGENTS.md only when changing that area. Record recurring friction in the improvements file.
<!-- castra-core:end -->
