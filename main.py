#!/usr/bin/env python3
"""Write one funny AI excuse to entry.txt.

Deterministic: no randomness, no timestamps, no network. The same
input always produces byte-identical output.
"""

import os
from pathlib import Path

EXCUSE = (
    "I didn't miss your deadline - my context window quietly dropped "
    "your instructions, kept the apology template, and here we are."
)

MAX_CHARS = 200


def main() -> None:
    # Gate guard: one line, within the 200-character limit.
    assert "\n" not in EXCUSE and len(EXCUSE) <= MAX_CHARS, "excuse violates gate"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "."))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(EXCUSE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
