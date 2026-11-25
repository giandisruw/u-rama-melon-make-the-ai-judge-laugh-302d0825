#!/usr/bin/env python3
"""Make the AI Judge Laugh — entry program (v2).

Writes one office-life joke, one line, to /output/entry.txt.
Deterministic and offline: no network, no randomness, no secrets.

v2 revision over v1: the entrypoint now validates the house gate
(1-200 characters, not only whitespace, single line) before writing,
and writes atomically (temp file + os.replace) so a partial write can
never leave a broken entry.txt behind.
"""
import os
import sys

LINE = "Our company values say 'we put people first', which is why the layoffs were alphabetised."

DEFAULT_OUTPUT = "/output/entry.txt"
MIN_CHARS = 1
MAX_CHARS = 200


def resolve_output():
    """Output path: ENTRY_OUTPUT override (used for local testing),
    otherwise the house path /output/entry.txt."""
    return os.environ.get("ENTRY_OUTPUT", DEFAULT_OUTPUT)


def validate(text):
    """Enforce the gate: UTF-8 text, 1-200 characters, not only
    whitespace, exactly one line."""
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        raise ValueError(f"entry is {len(text)} chars, must be {MIN_CHARS}-{MAX_CHARS}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text.rstrip("\n") or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")  # raises if not valid UTF-8 text
    return text


def write_entry(path, text):
    """Atomic write: complete the file in the same directory, then move
    it into place, so readers never see a half-written entry."""
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    os.replace(tmp, path)


def main():
    try:
        text = validate(LINE)
    except ValueError as exc:
        print(f"invalid entry: {exc}", file=sys.stderr)
        return 1
    write_entry(resolve_output(), text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
