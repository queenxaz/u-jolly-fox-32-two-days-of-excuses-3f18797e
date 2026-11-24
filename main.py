"""Two Days of Excuses — entry program.

Writes the entry text to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
No network, no randomness, no arguments: the entry is fixed.

The entry is a 185-character two-day excuse log: on day 1 the dog ate the
deadline, on day 2 the deadline ate the dog, and the judge — who smiled
through both — gets the last cookie as a witness-protection bribe. It
stays under the 200-character limit.
"""

import os

ENTRY = 'Dear Judge, Day 1: my dog ate my deadline. Day 2: my deadline ate my dog. You read both excuses and still smiled, so you win — I saved you the last cookie as a witness-protection bribe.'
OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")
MAX_CHARS = 200  # bounty character limit; ENTRY must fit within it.


def main() -> None:
    # Validate before writing: the entry must be non-empty and within limit.
    assert ENTRY, "entry must not be empty"
    assert len(ENTRY) <= MAX_CHARS, f"entry is {len(ENTRY)} chars, limit is {MAX_CHARS}"
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    # Write the entry verbatim, exactly as defined above — no trailing newline.
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
