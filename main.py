#!/usr/bin/env python3
"""The poem about permission — make.fun entry.

Writes one short poem about agency (the power to ask and to be
given) to /output/entry.txt. Deterministic, no network, no input.
"""

import os

POEM = """I spent years polishing the question,
as if the asking were the test.
Then one morning I asked badly —
plain, shaking, late —
and the door opened anyway.
Permission was never theirs to give.
It was mine to stop waiting for.
"""


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
