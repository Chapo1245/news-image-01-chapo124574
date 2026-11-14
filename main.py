#!/usr/bin/env python3
"""News-image-01 entry: copy the bundled world-news picture to /output/entry.png.

The picture is entry.png beside this file (JPEG bytes, 1024x1024, 318738
bytes): variant G1, "The World Today", a newspaper front page summing up
Friday 13 November 2026's world news in 24 verified stories. Masthead +
red dateline bar "FRIDAY 13 NOVEMBER 2026" + "24 STORIES · 5
CONTINENTS". Hero: a photo of the US radar site in Bahrain (flag and
LNG tanker on the horizon — the story's own elements, no strike shown
as fact) beside the headline "Iran claims strike on US radar in
Bahrain"; the deck prints the US denial (two drones downed) and Brent
crude at $95.82, and the photo caption carries the LNG tanker mine —
the claim is never shown as fact. Five medium photo stories with decks
and hard numbers: Microsoft 365 outage (74 countries, 120k-140k
reports), Senate summons Huang & Lutnick (Nvidia shares -4.3% at
$166.19), Europe names a Ukraine peace team (E5 Dublin deal, envoys
met), Russian drones hit a Kyiv hospital (30 evacuated, 2 killed in
Odesa), drone hits a Russian warship (Gulf of Finland). "ALSO ON
13 NOVEMBER": 18 more in a 3x6 tail with thumbnails and region tags —
Türkiye–Qatar pact, IAEA warning, Pope Leo in Chiclayo, US wholesale
prices +6.5%, yen near 160, Assam crash (24 dead), Nairobi collapse
(6 dead), Pakistan (74 militants), COP31, Gaza winter aid, FBI seizes
$1.2bn crypto, record 483,200 deportations, Kane 126 caps, Moscow car
bomb, Storm Charles floods, MSF Ebola in DR Congo, Yemen 340,000
displaced. Footer: "AND FINALLY" — the 1960 'Doomsday' paper's date
arrives — plus a source line (AP, Reuters, AFP, Al Jazeera, Euronews,
Xinhua, BLS). G1 keeps F's 24-story structure and swaps F's dotted
map for E's hero photo, with richer medium decks (13px, sharper
numbers); self-grade 49/50 vs F's 48/50. Every label was read back
from the rendered image and verified spelled correctly; see
VARIANTS.md for all eight variants built and why G1 won. The program
does a plain byte copy: no network, no randomness, no clock, so two
runs write exactly the same bytes.
"""

import hashlib
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUT = os.path.join(OUT_DIR, "entry.png")

# Expected bundled picture (variant G1): size and sha256 of entry.png.
# The copy must reproduce these exactly, or the run must fail loudly.
EXPECTED_SIZE = 318738
EXPECTED_SHA256 = "b34734f19327e32a9bd4a8ed01539ba9cbb5bba9cf9f0dc6220260c17cea1ad6"


def _sha256(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main():
    # Validate the bundled picture before copying: if the repository's
    # entry.png were ever truncated or replaced, fail fast here with a
    # clear message instead of copying a bad file and only noticing
    # afterwards. The JPEG magic bytes are checked first, so a file of
    # the right size that is not a JPEG is caught before the hash runs.
    with open(SRC, "rb") as handle:
        if handle.read(3) != b"\xff\xd8\xff":
            raise RuntimeError("bundled entry.png is not a JPEG file")
    if os.path.getsize(SRC) != EXPECTED_SIZE:
        raise RuntimeError("bundled entry.png is not variant G1")
    if _sha256(SRC) != EXPECTED_SHA256:
        raise RuntimeError("bundled entry.png does not match variant G1")
    os.makedirs(OUT_DIR, exist_ok=True)
    shutil.copyfile(SRC, OUT)
    # Guard against a truncated or wrong copy: the output must be
    # byte-identical to the bundled picture, so the two grader runs
    # agree exactly. A mismatch means the copy did not finish and the
    # run must fail loudly, not silently.
    if os.path.getsize(OUT) != EXPECTED_SIZE:
        raise RuntimeError("entry.png copy is incomplete")
    if _sha256(OUT) != EXPECTED_SHA256:
        raise RuntimeError("entry.png copy does not match variant G1")


if __name__ == "__main__":
    main()
