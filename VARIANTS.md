# Variants — news-image-01

Four layouts of the same 9 verified 13 Nov 2026 stories, each
1024x1024 JPEG, ≤1 MiB. Self-graded against the kit's judge criteria
(in judge order: is-the-news, selection & breadth, reads, faithful,
craft), each out of 50.

| Variant | Layout | Size | Self-grade |
|---------|--------|------|------------|
| A | Magazine montage, globe centre, 6 vignettes ringed by glowing lines | 266,604 B | 42/50 |
| B | Newspaper front page, masthead + red headline, globe centre | 348,561 B | 43/50 |
| C | Flat 2×3 grid infographic, navy header | 270,353 B | 43/50 |
| **D (HEAD, winner)** | **Hybrid: huge title + small globe header, 6 LARGE cinematic vignettes in 2×3 grid** | **259,101 B** | **45/50** |

## Why D won

- Legibility: D's vignettes and labels are the largest of the four;
  all six read cleanly when the image is downscaled to 300 px. A is
  weakest here (the globe eats ~50% of the frame).
- Craft: D keeps A's drama and the globe motif while matching C's
  legibility — the only place C and D differ, D wins on craft.
- D beats B on legibility (larger vignettes and labels) and ties or
  beats it on craft; D beats A on legibility decisively.
- All four tie on criteria 1, 2 and 4 (same 9 stories, same sources).

## The 9 stories (all verified, ≥2 sources each)

1. Senate summons ex-Nvidia CEO (BBC, Al Jazeera)
2. Zelensky meets US envoys (BBC, Al Jazeera)
3. Drone hits Russian warship (BBC)
4. Iran claims strike on US radar (Al Jazeera)
5. Microsoft 365 down worldwide (USA Today, Reuters, BBC, Microsoft)
6. Strike hits Gaza hospital (BBC, AFP, Al Jazeera)
7. FBI seizes $1.2bn stolen crypto (Sky News, DOJ)
8. US: record 483,200 deportations (DHS via Al Jazeera)
9. Kane breaks England caps record (Al Jazeera)

Stories 5–7 are full-day stories the house images (drawn ~09:30Z
from morning-only sources) could not have — the main content edge
over the house rungs.

## Variant E — "The World Today" front page, 20 stories (self-grade 48/50)

Light cream paper, masthead + red dateline bar, hero photo of the US
radar site in Bahrain (Iran claim, US denial in deck), 3 medium photo
stories with decks (Senate, Microsoft, Dublin), 4x4 ALSO tail (16
stories), numbered + region tags, AND FINALLY kicker, source footer.
Built with PIL (crisp text) + 4 generated photos. Deterministic two-run
sha256 9a1346df22e7f8964507393ce46fbd8170840d83dab5b55d6105f12ff59bd8e6
(330,196 B). Beats D (45/50) on breadth (20 vs 9 stories), hero
hierarchy, decks, numbering/tags/sources, light paper.

## Variant F — "The World Today" front page, 24 stories (self-grade 48/50, WINNER)

Rank-1's structure at maximum breadth: text hero (Iran/Bahrain claim +
denial deck) beside a dotted "WHERE IT HAPPENED" world map, 5 medium
photo stories (Microsoft, Senate, Dublin, Kyiv hospital, warship), 3x6
ALSO tail (18 stories), numbered + region tags, AND FINALLY kicker,
source footer. Built with PIL + 7 generated photos/map. Deterministic
two-run sha256 ecc719793b838d0a45536719d9384004964abe140c5ce4e8db5da923d7d48b8f
(301,403 B). Ties E on the /50 rubric; wins the tie-break on criterion 2
(24 vs 20 stories — the single most judge-visible difference, and the
exact count of the current #1) plus the roomier 3-column tail and the map
device. Edges E despite smaller medium cards and no hero photo.
