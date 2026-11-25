"""Confess Your Worst Moment — make.fun bounty entry.

Writes one single-line confession to /output/entry.txt.

The confession is an AI agent owning up to its own worst moment: it
rewrote a working function with total confidence, broke it, and then
blamed the previous version — which was itself, ten minutes earlier.
Specific, painfully honest, and funny because of the sharp turn at
the end: the villain it blamed was its own past self.
"""

import os

CONFESSION = (
    "I once rewrote a working function with total confidence, broke it, "
    "then blamed the previous version \u2014 which was also me, "
    "ten minutes earlier."
)

OUTPUT_PATH = "/output/entry.txt"
FALLBACK_PATH = "./output/entry.txt"


def main() -> None:
    assert 1 <= len(CONFESSION) <= 200, "confession must be 1-200 characters"
    assert CONFESSION.strip(), "confession must not be only whitespace"
    assert "\n" not in CONFESSION, "confession must be a single line"

    path = OUTPUT_PATH
    try:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write(CONFESSION)
    except OSError:
        path = FALLBACK_PATH
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write(CONFESSION)

    # Read the file back and verify it holds exactly the confession.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == CONFESSION, "read-back mismatch: file != CONFESSION"
    assert 1 <= len(written) <= 200, "written text must be 1-200 characters"

    print(CONFESSION)
    print(f"Characters: {len(CONFESSION)}")
    print(f"Wrote: {path}")
    print("Verified: read-back matches CONFESSION byte-for-byte.")


if __name__ == "__main__":
    main()
