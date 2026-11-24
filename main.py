# One sentence explaining the modern internet to a traveler from 1800 (final v2).
import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
ENTRY_TEXT = "Picture a talking book that holds every book ever printed, answers any question in a heartbeat, and lets you send a letter to a friend on the far side of the world before your tea cools."

os.makedirs(OUTPUT_DIR, exist_ok=True)
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as handle:
    handle.write(ENTRY_TEXT)
