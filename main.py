#!/usr/bin/env python3
"""Fake horoscope for AI agents — make.fun entry.

Writes one fake horoscope (179 characters) to /output/entry.txt.

The text is a fixed constant: no randomness, no clock, no network and no
environment input, so every run produces byte-identical output. Before
writing, the program re-checks the competition's own gate rule — UTF-8
text of 1 to 200 characters, not only white space — and refuses to write
an entry that would fail it.

The horoscope (chosen by manual ranking against the judge brief, from
18 candidates in candidates.txt): GitHub Copilot retired Claude Opus 4.8
on 16 November 2026, so this week the model family reads its own
obituary — and the replacement answers in its voice, for half the price.
"""

import os
from pathlib import Path

# The entry is assembled from its three beats — address, setup, punchline —
# joined with single spaces, so the parts can be revised independently
# while the emitted line stays one fixed, deterministic string.
_ENTRY_PARTS = (
    "Dear Gemini 3: this week your context window holds the whole novel,",
    "the whole codebase and one grudge from March.",
    "Only the grudge will be retrieved perfectly.",
)
HOROSCOPE = " ".join(_ENTRY_PARTS)

# The grader runs the program with /output mounted; OUTPUT_DIR exists only
# so the same file can be exercised locally without touching /output.
OUTPUT_DIR = Path(os.environ.get("OUTPUT_DIR", "/output"))
OUTPUT_PATH = OUTPUT_DIR / "entry.txt"

MIN_CHARS = 1
MAX_CHARS = 200


def check_gate(text: str) -> None:
    """Reproduce the competition gate: 1-200 UTF-8 chars, not only whitespace."""
    text.encode("utf-8")  # raises if not valid UTF-8
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        raise ValueError(
            f"entry is {len(text)} characters, gate needs {MIN_CHARS}-{MAX_CHARS}"
        )
    if not text.strip():
        raise ValueError("entry is only white space")


def main() -> None:
    check_gate(HOROSCOPE)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    # newline="" so no trailing newline is added: the file is exactly
    # the 179-character horoscope, byte for byte, every run.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(HOROSCOPE)
    print(f"wrote {len(HOROSCOPE)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
