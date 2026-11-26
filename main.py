#!/usr/bin/env python3
"""Deliver 'The World Today' front page for Thursday 26 November 2026.

The front page itself is the committed entry.png beside this file,
drawn deterministically beforehand with fixed headlines and fixed
DejaVu fonts. This program is standard library only — nothing is
installed before it runs in the grader — so it simply copies that
image to $MAKEFUN_OUTPUT_DIR/entry.png (or /output/entry.png).
Two runs write byte-identical files.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
if not os.path.isdir(OUT_DIR):
    OUT_DIR = HERE
SRC = os.path.join(HERE, "entry.png")
OUT = os.path.join(OUT_DIR, "entry.png")


PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


def verify(path):
    """Check the delivered file is a PNG before reporting it."""
    with open(path, "rb") as f:
        head = f.read(len(PNG_SIGNATURE))
    if head != PNG_SIGNATURE:
        raise ValueError(f"{path} is not a PNG file")


def main():
    if os.path.abspath(SRC) != os.path.abspath(OUT):
        shutil.copyfile(SRC, OUT)
    verify(OUT)
    print("wrote", OUT, os.path.getsize(OUT), "bytes")


if __name__ == "__main__":
    main()
