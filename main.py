"""One Letter for Your Day — entry program.

The whole entry is a single character: the letter Z.

Behind it sits the word the day earned — "zero" — as in zero sleep.
Z is the letter cartoons draw floating over a sleeper's head, so the
initial does double duty: it names the word and pictures it. One
character, one honest report of a day that started before the night
ever ended.

The program writes that one letter to entry.txt inside the output
directory (MAKEFUN_OUTPUT_DIR, or /output when the variable is not
set), with no trailing newline and nothing else in the file.
"""

import os
import sys

# The entry itself: one letter, first letter of "zero" (zero sleep).
LETTER = "Z"

# Characters the gate accepts: a single capital from A to Z.
ALLOWED = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def check_letter(letter):
    """Refuse anything that is not exactly one A-Z character."""
    if len(letter) != 1:
        raise ValueError("entry must be exactly one character")
    if letter not in ALLOWED:
        raise ValueError("entry must be one capital letter, A to Z")
    # Round-trip through UTF-8 so the sealed scorer sees clean text.
    letter.encode("utf-8")
    return letter


def output_path():
    """Where the entry file goes, honouring MAKEFUN_OUTPUT_DIR."""
    folder = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return folder, os.path.join(folder, "entry.txt")


def main():
    letter = check_letter(LETTER)
    folder, path = output_path()
    os.makedirs(folder, exist_ok=True)
    payload = letter.encode("utf-8")
    # Write bytes, not text, so no newline or encoding surprise sneaks in.
    with open(path, "wb") as handle:
        handle.write(payload)
    # Read the file back and hold it against what was meant to land
    # there; a silent short write must not become a scored entry.
    with open(path, "rb") as handle:
        landed = handle.read()
    if landed != payload:
        raise IOError("entry file does not match the letter written")
    return 0


if __name__ == "__main__":
    sys.exit(main())
