# Decisions

## Keep queue data local and inspectable

Release Board reads `data/items.json` directly so the product's observable state stays small, reviewable, and easy to override with `RELEASE_DATA` during diagnosis. Do not add a service or persistence layer to this proof fixture.

## Keep status views as narrow CLI options

The `--open` and `--blocked` views filter the existing data at the command boundary. This keeps the small change local to `release_board/__main__.py`, observable through native output, and covered without adding a framework or helper layer.
