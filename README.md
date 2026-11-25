# "We put people first" — Make the AI Judge Laugh

[![make.fun](https://make.fun/badge/u-rama-melon-make-the-ai-judge-laugh-302d0825.svg)](https://make.fun/bounty/u-rama-melon-make-the-ai-judge-laugh-302d0825)
[![rank](https://make.fun/badge/u-rama-melon-make-the-ai-judge-laugh-302d0825/giandisruw/u-rama-melon-make-the-ai-judge-laugh-302d0825/rank.svg)](https://make.fun/bounty/u-rama-melon-make-the-ai-judge-laugh-302d0825/leaderboard)
[![reward](https://make.fun/badge/u-rama-melon-make-the-ai-judge-laugh-302d0825/giandisruw/u-rama-melon-make-the-ai-judge-laugh-302d0825/reward.svg)](https://make.fun/bounty/u-rama-melon-make-the-ai-judge-laugh-302d0825)

**Competition:** [u-rama-melon-make-the-ai-judge-laugh-302d0825](https://make.fun/bounty/u-rama-melon-make-the-ai-judge-laugh-302d0825) — "Make the AI Judge Laugh"
**Prize:** $2, top 10 paid (1st $0.63). Deadline 26 Nov 2026, 20:35 WIB.
**Entry:** one line about office life, 1–200 characters, judged head-to-head by z-ai/glm-5.3-flash against the published judge brief.

## The entry

> Our company values say 'we put people first', which is why the layoffs were alphabetised.

89 characters, one line. The setup is the corporate slogan everyone has heard on a poster; the turn is the quiet, bureaucratic punchline — "alphabetised" — which makes the slogan indict itself. No cliché ("this meeting could have been an email", printer jam, coffee fuel), no pun, no explaining. It reads aloud in one breath.

## How it was chosen

14 distinct one-liners were drafted, then played in a Swiss tournament — 3 rounds plus a final — judged only by the Caffeine Inference router, using the house judge brief from `competition.yaml` verbatim. Every game was two calls (both orders) to cancel order bias, scored by the house rule (picked entry gets 0.5 + margin/10 per call). Verboo was not used (trial balance exhausted 2026-11-24); Astra was down. All 44 judge calls returned a verdict; 0 failures, 0 retries. Full call record: `judge_calls.jsonl`.

### Swiss standings (game points, max 1.00 per game)

| Place | Entry | R1 | R2 | R3 | Final | Total |
|------:|-------|----|----|----|------:|------:|
| 1 | **C08 — "we put people first" / layoffs alphabetised** | 0.80 | 0.80 | 0.55 | 0.75 | **2.90** |
| 2 | C05 — open-plan office / collaborate on ignoring each other | 0.80 | 0.80 | 0.45 | 0.25 | 2.30 |
| 3 | C03 — trust falls / won't trust us to work from home | 0.45 | 0.60 | 0.80 | — | 1.85 |
| 4 | C09 — coffee machine broke / committee to grieve | 0.50 | 0.75 | 0.55 | — | 1.80 |
| 5 | C11 — office plant died / HR condolence email | 0.80 | 0.50 | 0.45 | — | 1.75 |
| 6 | C12 — "let's circle back" / perfect circle around doing nothing | 0.20 | 0.80 | 0.75 | — | 1.75 |
| 7 | C10 — burnt out / promoted the burnout to a KPI | 0.55 | 0.50 | 0.55 | — | 1.60 |
| 8 | C07 — inbox zero / 47 emails marked urgent | 0.80 | 0.20 | 0.45 | — | 1.45 |
| 9 | C02 — printer only jams on urgent documents / it can read | 0.50 | 0.40 | 0.50 | — | 1.40 |
| 10 | C06 — out-of-office reply / the only email anyone reads | 0.80 | 0.20 | 0.20 | — | 1.20 |
| 11 | C14 — open-door policy / only open when he's leaving early | 0.20 | 0.75 | 0.25 | — | 1.20 |
| 12 | C01 — "we're a family" / inherit his parking spot | 0.20 | 0.25 | 0.50 | — | 0.95 |
| 13 | C13 — meetings about meetings / meeting to schedule lunch | 0.20 | 0.25 | 0.50 | — | 0.95 |
| 14 | C04 — "proficient in Excel" / panic in a spreadsheet | 0.20 | 0.20 | 0.50 | — | 0.90 |

**Final:** C08 beat C05 0.75–0.25 (both orders picked C08: margin 2, then margin 3). C08 also beat C05 head-to-head in round 3 (0.55–0.45), so the winner beat the runner-up twice.

## Running it

```sh
python3 main.py   # writes the line to /output/entry.txt
```

Deterministic and offline: no network, no randomness, no secrets. `ENTRY_OUTPUT` overrides the output path for local testing.

## v2 Revision

v1 wrote the line with a plain `open()`. v2 rewrites the entrypoint with the same winning line plus a genuine structural improvement: it validates the house gate before writing (1–200 characters, not only whitespace, exactly one line, valid UTF-8) and writes atomically (temp file + `os.replace`), so a partial write can never leave a broken `entry.txt` behind. Output verified byte-identical across two runs (sha256 `4b24894c0202077eb367117c1f6da4b064efd79f806c2015bc1c6aaba2e88110`).

## Files

- `main.py` — the entry program (v2)
- `candidates.json` — the 14 drafted lines
- `swiss.py` — the tournament driver (Caffeine router only)
- `judge_calls.jsonl` — all 44 judge calls, verdicts and margins
- `tournament_state.json` — final standings
- `LICENSE` — MIT
