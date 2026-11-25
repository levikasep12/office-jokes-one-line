#!/usr/bin/env python3
"""One-Line Office Jokes — make.fun entry.

Writes a single original one-line joke about office life to
/output/entry.txt. Standard library only, no network, no input files,
and the same bytes on every run from any working directory.
"""

import os
from pathlib import Path

# The joke: a real office detail (the meeting about meetings) with the
# laugh landing in the last few words — the follow-up meeting is the
# punchline. Original wording, one line, 124 characters, well under
# the 200-character gate.
JOKE = "My boss called a meeting to discuss why we have too many meetings and it ran an hour over, so we scheduled a follow-up."

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(JOKE, encoding="utf-8")
    print(f"Wrote {len(JOKE)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
