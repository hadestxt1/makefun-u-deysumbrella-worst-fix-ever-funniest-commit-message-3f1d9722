#!/usr/bin/env python3
"""Worst Fix Ever: Funniest Commit Message — make.fun entry.

Writes exactly one commit message (plus a trailing newline) to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt), and prints
the same line to stdout. Deterministic: no clock, no randomness, no
network, stdlib only. The message is at most 100 characters.

Output contract (sibling contract, kit unread — see README): the
sealed scorer reads /output/entry.txt and requires UTF-8 text of
1 to 100 characters, not only white space. The judge then compares
entries pairwise, blind, on how funny the worst fix ever is.
"""

import os
import sys

COMMIT_MESSAGE = (
    "fix(auth): nobody can log in anymore - "
    "zero logins, zero breaches, zero users"
)

MAX_LENGTH = 100
DEFAULT_OUTPUT = "/output/entry.txt"

# The fix worked: the breach is gone, along with every single user.


def main() -> int:
    message = COMMIT_MESSAGE.strip()
    if not message or len(message) > MAX_LENGTH:
        print("commit message must be 1-100 characters", file=sys.stderr)
        return 1
    output_path = os.path.join(
        os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.txt"
    )
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(message + "\n")
    print(message)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
