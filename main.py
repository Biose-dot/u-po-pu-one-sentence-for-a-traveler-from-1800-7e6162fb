# One sentence explaining the modern internet to a traveler from 1800 (draft v1).
import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
ENTRY_TEXT = "Imagine a library the size of a city folded into a pocket watch, where any letter you write reaches a friend across the sea in a blink, and every question you ask is answered at once."

os.makedirs(OUTPUT_DIR, exist_ok=True)
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as handle:
    handle.write(ENTRY_TEXT)
