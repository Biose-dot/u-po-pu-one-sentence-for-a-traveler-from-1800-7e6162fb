#!/usr/bin/env python3
"""One Sentence for a Traveler from 1800 — make.fun entry.

Writes the entry text to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

Every word predates 1800, so the traveler can actually hold the picture: one book holding everything ever written, which speaks back when asked.
"""
import os

ENTRY = 'Imagine a single book holding every letter, map, and song ever made, which speaks back at once when asked, and any person on earth may read it for free.'


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()
