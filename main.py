#!/usr/bin/env python3
"""Write the make.fun entry text to entry.txt.

The entry is one line for bounty
`u-gudril-cool-one-line-best-line-b8c41f4d`: at most 240 characters,
chosen in advance, written byte for byte with no trailing newline.
"""

import os
import sys

TEXT = (
    "The waiting-room fish has a name tag on his bowl: Gerald. "
    "Gerald has been dead since Tuesday. The tag is new."
)


def main() -> int:
    assert 1 <= len(TEXT) <= 280, f"text length {len(TEXT)} out of range"

    folder = (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )
    os.makedirs(folder, exist_ok=True)

    path = os.path.join(folder, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(TEXT)

    print(f"wrote {path} ({len(TEXT)} characters)", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
