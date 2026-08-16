# Core v2 trial

This fixture began as a product-only Python repository. The canonical Go `castra init core` generated `AGENTS.md`, `.castra/core.yaml`, and the three continuity files; it did not create Git state, install a tool, or alter product source.

## Cold orientation and loop

Start at `AGENTS.md`, then read `docs/product.md`, `docs/architecture.md`, and `.castra/core.yaml`. The map identifies `release_board/__main__.py` and `data/items.json`, plus exact native commands.

Observed commands:

```sh
python3 -m venv .venv
./.venv/bin/python -m release_board
./.venv/bin/python -m unittest discover -s tests -v
./.venv/bin/python -m release_board --json
./.venv/bin/python -m release_board --doctor
```

All exited 0. The product rendered its blocked item, the test suite passed three tests, JSON was inspectable, and doctor reported valid data.

The meaningful small change was adding `RB-104`, “Share release calendar,” to `data/items.json` and updating the JSON test. The human and JSON surfaces showed the fourth item; the tests still passed.

## Ordinary failure and recovery

Before setup, `castra doctor --repo .` exited 1 and named the missing `./.venv/bin/python` executable for every dependent command. Running the declared setup command resolved it.

`RELEASE_DATA=/tmp/castra-v2-missing-items.json ./.venv/bin/python -m release_board --doctor` exited 2 and reported the missing path plus `Check RELEASE_DATA or run without it.` Running without that override returned to ready state.

## Continuity and limits

A later session can use only the repository map, Core declaration, product/architecture docs, active-work state, decisions, and this trial. The assets that helped were the concise map, declared native commands, data ownership map, and actionable diagnostics. No generated skill, tool pin, adapter, receipt, scanner, or Git helper was needed; none was created.

This is one bounded Python product proof, not Python or general-distribution support.
