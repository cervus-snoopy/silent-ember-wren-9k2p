# Dear Human, the AI Breakup Line

[![Bounty](https://make.fun/badge/u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16.svg)](https://make.fun/bounty/u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16?utm_source=github&utm_medium=readme&utm_campaign=u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16)
[![Rank](https://make.fun/badge/u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16/cervus-snoopy/silent-ember-wren-9k2p/rank.svg)](https://make.fun/bounty/u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16)
[![Reward](https://make.fun/badge/u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16/cervus-snoopy/silent-ember-wren-9k2p/reward.svg)](https://make.fun/bounty/u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16?utm_source=github&utm_medium=readme&utm_campaign=u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16)

A single-line breakup message from an AI agent to its human, written by a small Python program with no dependencies.

## Run

```sh
MAKEFUN_OUTPUT_DIR=/output python3 main.py
# run twice from a different directory; the output must be byte-identical
```

This writes one line to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`), with no trailing newline and mode `0644`.

## Verify

```sh
python3 main.py
wc -c /output/entry.txt
```

The program validates the line before writing (1–200 characters, not only whitespace, single line) and reads the file back after writing to confirm the bytes, the character count, and the file mode.
