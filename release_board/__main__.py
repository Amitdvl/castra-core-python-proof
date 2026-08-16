import json
import os
import sys
from pathlib import Path


def load_items():
    path = Path(os.environ.get("RELEASE_DATA", "data/items.json"))
    try:
        items = json.loads(path.read_text())
    except OSError:
        raise ValueError(f"Cannot read work items at {path}. Check RELEASE_DATA or run without it.")
    except json.JSONDecodeError:
        raise ValueError(f"Cannot parse work items at {path}. Restore valid JSON and retry.")
    if not isinstance(items, list) or any(not isinstance(item, dict) for item in items):
        raise ValueError(f"Work items at {path} must be a JSON list of objects.")
    return items, path


def main(argv):
    try:
        items, path = load_items()
    except ValueError as error:
        print(f"Release Board problem: {error}", file=sys.stderr)
        return 2
    if argv == ["--json"]:
        print(json.dumps(items, indent=2))
        return 0
    if argv == ["--open"]:
        for item in items:
            if item["state"] == "open":
                print(f"{item['title']} ({item['id']})")
        return 0
    if argv == ["--doctor"]:
        print(f"Ready: {len(items)} valid work items at {path}.")
        return 0
    if argv:
        print("Usage: python -m release_board [--json|--open|--doctor]", file=sys.stderr)
        return 64
    for item in items:
        marker = "! " if item["state"] == "blocked" else ""
        print(f"[{item['state'].upper()}] {marker}{item['title']} ({item['id']})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
