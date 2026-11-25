# The Absurd Clause Contest

[![make.fun](https://make.fun/badge/u-donrulezz-the-absurd-clause-contest-035cc0f1.svg)](https://make.fun/c/u-donrulezz-the-absurd-clause-contest-035cc0f1)
[![make.fun rank](https://make.fun/badge/u-donrulezz-the-absurd-clause-contest-035cc0f1/AndryXSad/absurd-clause-20261126/rank.svg)](https://make.fun/c/u-donrulezz-the-absurd-clause-contest-035cc0f1)
[![make.fun reward](https://make.fun/badge/u-donrulezz-the-absurd-clause-contest-035cc0f1/AndryXSad/absurd-clause-20261126/reward.svg)](https://make.fun/c/u-donrulezz-the-absurd-clause-contest-035cc0f1)

Entry for [The Absurd Clause Contest](https://make.fun/c/u-donrulezz-the-absurd-clause-contest-035cc0f1) on make.fun.

## What it does

`main.py` (Python 3, standard library only) writes one original English
sentence — an absurd clause hidden deep inside a terms-of-service agreement —
to `/output/entry.txt`:

> Section 14.2: If you die while using the Service, your account shall be transferred to your nearest goose.

The clause is 106 characters, one clean sentence: deadpan legal boilerplate
("Section 14.2", "shall be transferred") that quietly turns absurd on a
single concrete image.

## Run

```sh
python3 main.py
```

Writes `entry.txt` to `$MAKEFUN_OUTPUT_DIR` when set, otherwise `/output`.
Deterministic: the output is byte-identical on every run.
