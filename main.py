#!/usr/bin/env python3
"""Entry program for 'The Funniest Sick-Day Excuse'.

The whole submission is one sick-day line: a doctor's diagnosis of
acute spreadsheet poisoning, with the only cure being 48 hours away
from any cell that thinks it is a number — including the ones in the
caller's own body. Half believable, one concrete idea, and the laugh
lands before the last word.

The program writes that line to entry.txt inside the directory named
by MAKEFUN_OUTPUT_DIR (falling back to /output when unset), which is
where the make.fun harness looks for the artifact it scores.
"""

import os
from pathlib import Path

TEXT = (
    "I can't come in today: my doctor diagnosed acute spreadsheet "
    "poisoning, and the only cure is 48 hours away from any cell "
    "that thinks it is a number, including the ones in my own body. "
    "Send soup."
)

OUTPUT_NAME = "entry.txt"
CHAR_LIMIT = 200

def write_line(target_dir: Path, line: str) -> Path:
    """Place `line` into target_dir/entry.txt and return the file path.

    The gate wants exactly one line of 1 to CHAR_LIMIT characters, so
    anything longer, or holding a newline, is refused here instead of
    being written.
    """
    if "\n" in line or line != line.strip() or not 1 <= len(line) <= CHAR_LIMIT:
        raise ValueError("excuse must be one trimmed line of 1-200 characters")
    target_dir.mkdir(parents=True, exist_ok=True)
    artifact = target_dir / OUTPUT_NAME
    artifact.write_text(line, encoding="utf-8")
    return artifact


def run() -> None:
    destination = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    written = write_line(destination, TEXT)
    print(f"wrote {written}: {TEXT}")


if __name__ == "__main__":
    run()
