#!/usr/bin/env python3
import sys

current = None
total = 0

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    key, value = line.split("\t")
    value = int(value)

    if current == key:
        total += value
    else:
        if current is not None:
            print(f"{current}\t{total}")
        current = key
        total = value


if current is not None:
    print(f"{current}\t{total}")
