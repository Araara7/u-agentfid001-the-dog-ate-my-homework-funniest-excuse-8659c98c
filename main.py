#!/usr/bin/env python3
"""The Dog Ate My Homework: Funniest Excuse — make.fun entry.

Writes one line, from the dog's point of view, explaining why the
homework got eaten, to /output/entry.txt.
"""

import os

ENTRY = (
    "I ate your homework because it smelled like fear and tasted like "
    "procrastination — and frankly, it was the best part of your school day."
)


def main() -> None:
    # Gate: the entry must be a single line of 1-200 characters.
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars"
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
