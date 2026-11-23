#!/usr/bin/env python3
"""Entry for make.fun bounty 'One Word, One Username, One Reward'.

Writes our own make.fun handle, exactly "safari82", to /output/entry.txt.
The bounty gate requires a UTF-8 file of 1-30 characters, not whitespace
only. The entry is the username itself, one word, no newline, no padding.
"""

import os

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")
USERNAME = "safari82"


def main() -> None:
    if not (1 <= len(USERNAME) <= 30) or not USERNAME.strip():
        raise ValueError("entry must be 1-30 non-whitespace characters")
    if os.path.isfile(OUTPUT_DIR):
        raise NotADirectoryError(f"{OUTPUT_DIR} exists and is not a directory")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(USERNAME)
    print(f"Wrote entry ({len(USERNAME)} chars): {USERNAME} -> /output/entry.txt")


if __name__ == "__main__":
    main()
