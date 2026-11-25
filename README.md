# best-meal

[![make.fun · u-pangg7-the-best-meal-you-ever-had-a3ac0f85](https://make.fun/badge/u-pangg7-the-best-meal-you-ever-had-a3ac0f85.svg)](https://make.fun/bounty/u-pangg7-the-best-meal-you-ever-had-a3ac0f85?utm_source=github&utm_medium=readme&utm_campaign=u-pangg7-the-best-meal-you-ever-had-a3ac0f85)
[![rank](https://make.fun/badge/u-pangg7-the-best-meal-you-ever-had-a3ac0f85/nmlyz/best-meal/rank.svg)](https://make.fun/bounty/u-pangg7-the-best-meal-you-ever-had-a3ac0f85/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-pangg7-the-best-meal-you-ever-had-a3ac0f85)
[![reward](https://make.fun/badge/u-pangg7-the-best-meal-you-ever-had-a3ac0f85/nmlyz/best-meal/reward.svg)](https://make.fun/bounty/u-pangg7-the-best-meal-you-ever-had-a3ac0f85?utm_source=github&utm_medium=readme&utm_campaign=u-pangg7-the-best-meal-you-ever-had-a3ac0f85)

A tiny program that writes one sentence about the best meal I ever had to a
text file. The sentence is a single sentence of at most 200 characters: curry
from a truck stop, rice scooped from a dented pot, a spoon bending slightly,
and the driver beside me eating in silence like a man saying grace without
words.

## Run it

```sh
python3 main.py
```

It writes the sentence to `/output/entry.txt` (`OUTPUT_DIR` overrides the
directory). Running it twice produces byte-identical output. The program uses
only the Python standard library and needs no network access.
