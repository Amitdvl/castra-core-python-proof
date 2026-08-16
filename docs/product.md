# Release Board

Release Board is a local CLI that makes three release tasks visible. It deliberately has an open item, a blocked item, and a completed item so a contributor can observe state rather than infer it from source.

`RELEASE_DATA` may point at an alternate JSON list. A missing or invalid file is an ordinary failure: the diagnostic names the path and tells the contributor to check the variable or restore JSON.
