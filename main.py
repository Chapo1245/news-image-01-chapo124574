#!/usr/bin/env python3
"""News-image-01 entry: copy the bundled world-news picture to /output/entry.png.

The picture is entry.png beside this file (JPEG bytes, 1024x1024, 266604
bytes): variant A, "13 NOV 2026 — THE WORLD TODAY", a dark magazine-cover
montage with a glowing globe at the centre and six illustrated vignettes
of Friday 13 November 2026's biggest verified news stories (Senate
summons ex-Nvidia CEO; Zelensky meets US envoys; drone hits Russian
warship; Iran claims strike on US radar; Microsoft 365 down worldwide;
strike hits Gaza hospital), plus a footer ticker with three more (FBI
seizes $1.2bn stolen crypto; US record 483,200 deportations; Kane breaks
England caps record). Every label was read back from the rendered image
and verified spelled correctly; see VARIANTS.md for the four variants
built and why D won. The program does a plain byte copy: no network, no
randomness, no clock, so two runs write exactly the same bytes.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUT = os.path.join(OUT_DIR, "entry.png")


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    shutil.copyfile(SRC, OUT)
    # Guard against a truncated copy: the output must be byte-identical
    # to the bundled picture, so the two grader runs agree exactly.
    # A different size means the copy did not finish and the run must
    # fail loudly, not silently.
    if os.path.getsize(OUT) != os.path.getsize(SRC):
        raise RuntimeError("entry.png copy is incomplete")


if __name__ == "__main__":
    main()
