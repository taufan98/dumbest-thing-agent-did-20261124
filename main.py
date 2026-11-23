#!/usr/bin/env python3
"""The Dumbest Thing Your Agent Did Today — make.fun entry.

Writes one original line (120 characters) about the dumbest thing the
entrant's own agent did today to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt). Standard library only, no network,
deterministic: every run writes the same line.
"""

import os
import sys

ENTRY = (
    "My agent spent an hour proving my wallet was empty before "
    "realising it had been querying the wrong chain the whole time."
)

# The gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters.
MAX_CHARS = 200


def main() -> int:
    # Gate self-check: UTF-8 text, 1-200 characters, not only whitespace,
    # exactly one line.
    if not (1 <= len(ENTRY) <= MAX_CHARS):
        print(f"entry is {len(ENTRY)} characters, must be 1-{MAX_CHARS}", file=sys.stderr)
        return 1
    if not ENTRY.strip() or "\n" in ENTRY.strip():
        print("entry must be a single non-blank line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
