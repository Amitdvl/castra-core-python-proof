# Architecture

`release_board/__main__.py` owns loading, rendering, JSON inspection, and diagnostics. `data/items.json` is the mutable product data. `tests/test_app.py` exercises the human, JSON, and missing-data paths. Change data or rendering here for a small behavior change.
