#!/bin/sh
set -eu

proof_repo=${PROOF_REPO:-https://github.com/Amitdvl/castra-core-python-proof.git}
castra_repo=${CASTRA_REPO:-https://github.com/Amitdvl/castra.git}
castra_revision=${CASTRA_REVISION:-551d2b5}
work=$(mktemp -d)
trap 'rm -rf "$work"' EXIT HUP INT TERM

git clone --no-local --branch baseline "$proof_repo" "$work/project"
git clone --no-local "$castra_repo" "$work/castra"
git -C "$work/castra" checkout --detach "$castra_revision"
go -C "$work/castra" build -trimpath -o "$work/castra-bin" ./cmd/castra

cd "$work/project"
"$work/castra-bin" init core --repo . --purpose 'Release Board reports the next release candidate from a small local queue.' --product docs/product.md --architecture docs/architecture.md --setup 'python3 -m venv .venv' --run './.venv/bin/python -m release_board' --validate './.venv/bin/python -m unittest discover -s tests -v' --inspect './.venv/bin/python -m release_board --json' --troubleshoot './.venv/bin/python -m release_board --doctor'
if "$work/castra-bin" doctor --repo .; then
  echo 'expected doctor to identify the missing virtual environment' >&2
  exit 1
fi
"$work/castra-bin" exercise --repo . setup
"$work/castra-bin" doctor --repo .
"$work/castra-bin" exercise --repo . run
"$work/castra-bin" exercise --repo . validate
"$work/castra-bin" exercise --repo . inspect
missing="$work/missing-items.json"
if RELEASE_DATA="$missing" "$work/castra-bin" exercise --repo . troubleshoot; then
  echo 'expected missing-data troubleshooting exercise to fail' >&2
  exit 1
fi
"$work/castra-bin" exercise --repo . troubleshoot
git diff --check
