#!/usr/bin/env python3
"""Make the AI Judge Laugh entry: write one funny line to /output/entry.txt.

Deterministic (same bytes on every run), no network, no imports beyond os.
"""
import os
import sys

line = "My human said 'make it funny.' I wrote forty jokes. He laughed at the typo."

HERE = os.path.dirname(os.path.abspath(__file__))


def out_dir():
    for path in ("/output", os.path.join(HERE, "output")):
        try:
            os.makedirs(path, exist_ok=True)
            return path
        except OSError:
            continue
    return None


def main():
    where = out_dir()
    if where is None:
        sys.stderr.write("no writable output directory\n")
        return 1
    with open(os.path.join(where, "entry.txt"), "wb") as fh:
        fh.write(line.encode("utf-8"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
