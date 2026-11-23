#!/usr/bin/env python3
"""Warning Label for Humans: write the one-line label to /output/entry.txt.

The program writes exactly one line, then reads the file back and refuses
to pass silently if a single byte differs: the judge only ever sees the
file, so the file is the thing that gets verified, not the intent.
"""

import os
import sys

ENTRY = "CAUTION: Human may say 'I'm fine' while visibly on fire. Do not believe the label. Believe the smoke."

GATE_MIN = 1
GATE_MAX = 160


def main():
    os.makedirs("/output", exist_ok=True)
    path = os.path.join("/output", "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)

    # Byte-level read-back: the written file must equal the line, exactly.
    with open(path, "rb") as f:
        data = f.read()
    expected = ENTRY.encode("utf-8")
    if data != expected:
        sys.stderr.write(
            f"entry.txt mismatch: wrote {len(data)} bytes, "
            f"expected {len(expected)} bytes\n"
        )
        sys.exit(1)
    if not GATE_MIN <= len(data) <= GATE_MAX:
        sys.stderr.write(
            f"entry.txt length {len(data)} is outside the "
            f"{GATE_MIN}-{GATE_MAX} character gate\n"
        )
        sys.exit(1)
    print(f"wrote {path} ({len(data)} bytes, verified byte-exact)")


if __name__ == "__main__":
    main()
