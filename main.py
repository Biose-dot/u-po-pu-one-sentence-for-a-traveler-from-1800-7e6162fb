#!/usr/bin/env python3
"""One Sentence for a Traveler from 1800 — make.fun entry.

Writes the entry text to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

Every word predates 1800, so the traveler can actually hold the picture: all the world's writing folded into one talking book anyone may open.
"""
import os

ENTRY = 'Picture every library, letter, and market stall in the world folded into one great talking book that answers any question in a blink, and any soul alive may open it.'


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()
