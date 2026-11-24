"""Everyday Wonder, Two Days to Find the Line — make.fun entry.

Writes a single original sentence about a small moment of wonder
in everyday life to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

The line: raindrops racing down a bus window, and the quiet surprise
that the one I am rooting for is the slowest of them. The moment is
real and specific (anyone who has ridden a bus in the rain has watched
this race), the angle is one the reader has not met before — nobody
expects to be a fan of the losing drop — and the turn lands in a
single read, in the last clause. No worn phrase, every word working. It also
steers clear of the brief's own example moments (lift door, kettle,
puddle), so the angle stays the reader's first meeting with it.

Pure Python standard library only.
"""

import os
import sys

# The sentence. One line, plain ASCII.
LINE = (
    "The rain on the bus window races in little rivers, "
    "and the slowest drop is the one I've been rooting for."
)

MIN_CHARS = 1
MAX_CHARS = 200


def validate(text):
    """Enforce the competition gate before anything is written."""
    if not isinstance(text, str):
        raise ValueError("line is not text")
    if not text.strip():
        raise ValueError("line is blank or whitespace only")
    if "\n" in text or "\r" in text:
        raise ValueError("line must be a single line")
    if any(ord(ch) < 32 for ch in text):
        raise ValueError("line contains control characters")
    if "  " in text:
        raise ValueError("line has doubled spaces (padding)")
    if text != text.strip():
        raise ValueError("line has leading or trailing whitespace")
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        raise ValueError(
            "line is %d characters, gate is %d-%d"
            % (len(text), MIN_CHARS, MAX_CHARS)
        )
    text.encode("utf-8")  # must be valid UTF-8
    return text


def main():
    line = validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(line)
    # Read it back and confirm what landed on disk is exactly the line.
    with open(path, "r", encoding="utf-8", newline="") as fh:
        written = fh.read()
    if written != line:
        raise SystemExit("read-back mismatch: entry.txt != line")
    print("wrote %d chars to %s" % (len(line), path))
    return 0


if __name__ == "__main__":
    sys.exit(main())
