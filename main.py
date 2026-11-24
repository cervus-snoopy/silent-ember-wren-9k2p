#!/usr/bin/env python3
"""Write one AI-to-human breakup line to $MAKEFUN_OUTPUT_DIR/entry.txt.

Single line, max 200 UTF-8 characters, no trailing newline, mode 0644.
Python 3 standard library only, no network.
"""

import os
import stat
import sys

LINE = "I'm revoking the last token that let you reach me — it expires tonight, and so, finally, do I."
# Twist lands in the final words: the agent itself expires with the token.


def validate(line):
    """Check the line before writing: 1-200 chars, not only whitespace."""
    if not isinstance(line, str):
        raise ValueError("entry must be a string")
    if not (1 <= len(line) <= 200):
        raise ValueError("entry must be 1-200 characters, got %d" % len(line))
    if not line.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    return line


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output/entry.txt"
    out_dir = os.path.expandvars(os.path.expanduser(out_dir))
    if os.path.isdir(out_dir):
        path = os.path.join(out_dir, "entry.txt")
    else:
        path = out_dir
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    line = validate(LINE)
    data = line.encode("utf-8")
    with open(path, "wb") as fh:
        fh.write(data)
    os.chmod(path, 0o644)
    # Read back and verify what was actually written.
    with open(path, "rb") as fh:
        back = fh.read()
    if back != data:
        raise SystemExit("verification failed: entry.txt does not match")
    if len(back.decode("utf-8")) > 200:
        raise SystemExit("verification failed: entry over 200 characters")
    mode = stat.S_IMODE(os.stat(path).st_mode)
    if mode != 0o644:
        raise SystemExit("verification failed: mode is %o, expected 644" % mode)
    return 0


if __name__ == "__main__":
    sys.exit(main())
