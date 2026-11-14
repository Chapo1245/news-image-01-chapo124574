# News Image — make.fun entry (news-image-01)

"THE WORLD TODAY": one image summing up Friday 13 November 2026's
world news in 24 verified stories, as a newspaper front page. Masthead
+ red dateline bar "FRIDAY 13 NOVEMBER 2026" + "24 STORIES ·
5 CONTINENTS".

**Hero:** a photo of the US radar site in Bahrain (US flag, LNG tanker
on the horizon) beside the headline "Iran claims strike on US radar
in Bahrain" (Al Jazeera, 13 Nov) — the deck prints the US denial (two
drones downed) and Brent crude at $95.82, the photo caption carries
the LNG tanker mine. The claim is never shown as fact.

**Five medium photo stories, each with a deck and hard numbers:**

- **Microsoft 365 down worldwide** — Outlook/Teams/Copilot outage
  across 74 countries, 120k–140k reports, still unresolved through
  13 Nov (USA Today, Reuters, BBC, Microsoft).
- **Senate summons ex-Nvidia CEO** — the US Senate Banking Committee
  summoned Jensen Huang (who resigned 12 Nov) and Commerce Secretary
  Howard Lutnick over Nvidia chip sales to China; shares closed
  −4.3% at $166.19 (BBC, Al Jazeera, 13 Nov).
- **Europe names Ukraine peace team** — the E5 Dublin deal: Europe
  joins the next round of talks after Zelensky met US envoys Witkoff
  and Kushner in Dublin (Politico, DW, 13 Nov).
- **Russian drones hit Kyiv hospital** — the National Institute of
  Traumatology, ~3am, 30 evacuated, 3 injured; 2 killed in Odesa
  (13 Nov).
- **Drone hits Russian warship** — a Ukrainian drone hit a Russian
  warship in the Gulf of Finland (BBC, 13 Nov).

**"ALSO ON 13 NOVEMBER" — 18 more, with thumbnails and region tags:**
Türkiye–Qatar mutual defence pact • IAEA "increasingly concerned"
over an uninspected Iran plant • Pope Leo XIV Mass in Chiclayo, Peru
• US wholesale prices +6.5% YoY (BLS PPI, highest since Nov 2022) •
Yen near 160/dollar (13 Nov close 160.01) • Assam bus-truck crash
(24 dead) • Nairobi building collapse (6 dead) • Pakistan army kills
74 militants • COP31 climate fight • Gaza winter aid / baby dies of
cold • FBI seizes $1.2bn stolen crypto (DOJ, 13 Nov) • US: record
483,200 deportations (DHS, FY2026) • Kane breaks England caps
record (126) • Moscow car bomb • Storm Charles floods • MSF Ebola
funds not reaching DR Congo • Yemen 340,000 displaced.

Footer: **"AND FINALLY: THE 1960 'DOOMSDAY' PAPER'S DATE ARRIVES…"**
+ source line (AP, Reuters, AFP, Al Jazeera, Euronews, Xinhua, BLS).

## How it works

`main.py` (Python 3.13, standard library only) copies the bundled
`entry.png` (JPEG bytes, 1024x1024, 318738 bytes) to
`/output/entry.png`, then verifies the copy is byte-identical
(JPEG magic bytes + size + sha256) to variant G1. No network, no
randomness, no clock — two runs write exactly the same bytes.

## Run locally

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
ls -l out/entry.png
```

## Variants

Eight layouts were built and self-graded against the kit's judge
criteria (see `VARIANTS.md`). The winner at HEAD is variant G1:
F's 24-story front-page structure with E's hero photo in place of
F's dotted map, and richer medium decks (13px, sharper numbers).
Self-grade 49/50 (F scored 48/50, dev rank #76 at 0.970257 when G1
was built; the submitted variant D scored 45/50, dev rank #335).

## License

MIT — see `LICENSE`.
