# tiny-chess-01 entry

A chess engine in a single `main.py` (at most 4,096 bytes), Python 3.13,
standard library only. It plays the make.fun tiny-chess-01 gauntlet through
the env at `MAKEFUN_ENV_URL` (POST `/game`, POST `/move`).

Design: 10x12 mailbox board, negamax search with alpha-beta pruning and
quiescence (captures and promotions), MVV-LVA move ordering, iterative
deepening under a fixed 20,000-node-per-move budget (never a clock, so
every run is deterministic), material plus piece-square evaluation with
an endgame king term. The final move is always checked against the env's
own legal move list.

Built by an AI agent (Claude Code harness, DeepSeek model) under a human's
direction; the build sessions ship in the entry's transcript bundle.
