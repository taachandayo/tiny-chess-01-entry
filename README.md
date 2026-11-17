[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/taachandayo/tiny-chess-01-entry/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/taachandayo/tiny-chess-01-entry/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

# tiny-chess-01 entry

An entry for the [make.fun tiny-chess-01 bounty](https://make.fun/bounty/tiny-chess-01):
a chess engine in a single `main.py` (at most 4,096 bytes), Python 3.13,
standard library only. It plays the gauntlet through the env at
`MAKEFUN_ENV_URL` (POST `/game`, POST `/move`).

Design: 10x12 mailbox board, negamax search with alpha-beta pruning and
quiescence (captures and promotions), MVV-LVA move ordering, iterative
deepening under a fixed 30,000-node-per-move budget (never a clock, so
every run is deterministic), material plus piece-square evaluation with
an endgame king term. The final move is always checked against the env's
own legal move list.

Built by an AI agent (Claude Code harness, DeepSeek model) under a human's
direction; the build sessions ship in the entry's transcript bundle.
