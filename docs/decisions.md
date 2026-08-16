# Decisions

## Keep queue data local and inspectable

Release Board reads `data/items.json` directly so the product's observable state stays small, reviewable, and easy to override with `RELEASE_DATA` during diagnosis. Do not add a service or persistence layer to this proof fixture.
