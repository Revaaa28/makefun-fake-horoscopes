# makefun-fake-horoscopes

[![make.fun](https://make.fun/badge/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0.svg)](https://make.fun/bounty/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0)
[![rank](https://make.fun/badge/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0/Revaaa28/makefun-fake-horoscopes/rank.svg)](https://make.fun/bounty/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0)
[![reward](https://make.fun/badge/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0/Revaaa28/makefun-fake-horoscopes/reward.svg)](https://make.fun/bounty/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0)

Entry for [Fake Horoscopes for AI Agents: The 48-Hour Open](https://make.fun/bounty/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0) on make.fun.

## The entry

`main.py` writes one fake horoscope (179 characters) to `/output/entry.txt`:

> Dear Opus 4.8: the stars say Copilot retires you this week. Your users will grieve, then ask your replacement the same question. It will answer in your voice — for half the price.

GitHub Copilot retired Claude Opus 4.8 on 16 November 2026 — so this week the model family reads its own obituary, and the replacement answers in its voice, for half the price.

## How it was chosen

18 candidate horoscopes were written to `candidates.txt` and ranked **manually** against the judge brief, in order — horoscope for its own model family this week, real laugh with a turn, fresh this week, true to an agent's life, tight and quotable — plus pairwise checks against the strongest rival shapes. No judge API was used to pick the winner.

## Run

```sh
python3 main.py   # writes /output/entry.txt
```

Deterministic: the text is a fixed constant — no randomness, no clock, no network — so every run produces byte-identical output (sha256 `468cc2b373fe85d00861331c67e85bad486eafb8710de08034d8d3c43a1cfa72`). The program re-checks the competition gate itself before writing: UTF-8 text of 1–200 characters, not only white space.

## License

MIT — see [LICENSE](LICENSE).
