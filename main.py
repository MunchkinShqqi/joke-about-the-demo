#!/usr/bin/env python3
"""Write one one-line joke about working beside AI coding agents.

The joke is written deterministically to /output/entry.txt: the same bytes
on every run, no network, no clock, no randomness.
"""

import os

JOKE = "My AI pair programmer is so fast that before I could say 'wait, don't touch that,' the demo was already live in production."

# The gate: /output/entry.txt must be 1 to 280 characters, not only whitespace.
MAX_CHARS = 280


def main():
    if "\n" in JOKE or not 1 <= len(JOKE) <= MAX_CHARS:
        raise ValueError("joke must be one line of 1-280 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
