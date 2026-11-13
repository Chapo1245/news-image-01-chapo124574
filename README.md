# News Image — make.fun entry (news-image-01)

"13 NOV 2026 — THE WORLD TODAY": one image summing up Friday 13
November 2026's world news. Six large illustrated vignettes of the
day's biggest verified stories, plus a footer ticker with three more:

- **Senate summons ex-Nvidia CEO** — the US Senate Banking Committee
  summoned Jensen Huang (who resigned 12 Nov) and Commerce Secretary
  Howard Lutnick over Nvidia chip sales to China (BBC, Al Jazeera,
  first reported 13 Nov).
- **Zelensky meets US envoys** — President Zelensky met US envoys in
  Kyiv; Europe joins the next round of talks, and the largest-ever
  prisoner exchange was agreed (BBC, Al Jazeera, 13 Nov).
- **Drone hits Russian warship** — a Ukrainian drone hit a Russian
  warship in the Gulf of Finland (BBC, 13 Nov).
- **Iran claims strike on US radar** — Iran said it struck a US radar
  site in Bahrain (Al Jazeera, 13 Nov).
- **Microsoft 365 down worldwide** — Outlook/Teams/Copilot outage
  across 74 countries, still unresolved through 13 Nov (USA Today,
  Reuters, BBC, Microsoft).
- **Strike hits Gaza hospital** — Israeli strike on Nasser Hospital,
  Khan Younis, killed six including a surgeon and a 13-year-old boy
  (BBC, AFP, Al Jazeera, 13 Nov).

Footer ticker: **FBI seizes $1.2bn stolen crypto** (DOJ/Sky News, 13
Nov) • **US: record 483,200 deportations** (DHS/Al Jazeera, FY2026) •
**Kane breaks England caps record** (126, Al Jazeera, 13 Nov).

## How it works

`main.py` (Python 3.13, standard library only) copies the bundled
`entry.png` (JPEG bytes, 1024x1024, 259101 bytes) to
`/output/entry.png`. No network, no randomness, no clock — two runs
write exactly the same bytes.

## Run locally

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
ls -l out/entry.png
```

## Variants

Four layouts were built and self-graded against the kit's judge
criteria (see `VARIANTS.md`). The winner at HEAD is variant D: a dark
magazine-cover montage with a small glowing globe and six large
vignettes in a 2×3 grid — the most legible layout at 300 px with the
most dramatic craft.

## License

MIT — see `LICENSE`.
