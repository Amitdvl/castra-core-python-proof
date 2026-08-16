# Core fresh-agent trial

## Scope and provenance

This is a small Python product proof, not Python or `general` distribution support. It was initialized from the inspectable `baseline` branch with Castra commit `551d2b5`, built using `go build -trimpath -o /tmp/castra-core ./cmd/castra` in the canonical Castra repository. That binary reported `castra dev`.

Core generated only `AGENTS.md`, `.castra/core.yaml`, and the three continuity files. It did not create Git state, install a tool, alter product source, or run a project command during initialization.

## Cold orientation and change

A fresh agent needs only the repository. `AGENTS.md` states the purpose and exact native commands, then routes to `docs/product.md`, `docs/architecture.md`, and the command declaration. Those documents identify `release_board/__main__.py`, `tests/test_app.py`, and `data/items.json` as the smallest relevant surfaces.

The initial agent added the `--open` view in `release_board/__main__.py` and its focused test in `tests/test_app.py`. An independent fresh session later added `--blocked`, again finding the same source and test locations from repository context alone. It observed `Prepare migration (RB-102)` while excluding open and completed work. In this generated fixture, `castra exercise --repo . validate` passed all five tests; `castra exercise --repo . inspect` exposed the same queue as JSON. The replay intentionally begins from the pre-change product baseline, where its three original tests pass before an agent applies either documented change.

## Executable loop and ordinary failure

The declared commands are setup (`python3 -m venv .venv`), run, validate, inspect, and troubleshoot. The explicit Core exercises used setup, run, validate, inspect, and troubleshoot individually; Core never sequenced or wrapped them automatically.

An induced ordinary data failure used `RELEASE_DATA=<missing file> castra exercise --repo . troubleshoot`. The native command exited 2 and retained its actionable `Check RELEASE_DATA or run without it` output. Core reported this honestly as a native command failure and pointed to the declared troubleshooting route. Removing the override made the same exercise pass.

On a clean clone without `.venv`, `castra doctor --repo .` reports each unavailable `./.venv/bin/python` interface before setup. Running the declared setup command resolves that prerequisite; this is a static interface check, not a claim that application behavior has been run.

## Continuity, comparison, and evidence

The independent later session resumed from `docs/active-work.md`, `docs/decisions.md`, and `docs/improvements.md`, then recorded the narrow status-view decision with its change. The useful assets were the concise map, literal command list, source ownership map, continuity files, and native failure output. No skill, tool pin, adapter, receipt, scanner, or Git helper helped, so none exists.

The `baseline` branch has the same runnable product but lacks all Core files. It is an inspectable comparison: Core removes command/context rediscovery without claiming measured time savings or broad Python support. `scripts/replay-core.sh` rebuilds the named Castra revision, clean-clones `baseline`, initializes Core, and repeats the loop and failure recovery.
