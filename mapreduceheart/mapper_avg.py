#!/usr/bin/env python3
import sys

for line in sys.stdin:
    line = line.strip()

    if line.startswith("age"):
        continue

    parts = line.split(",")

    try:
        target = parts[-1]
        age = float(parts[0])
        print(f"{target}\t{age},1")
    except:
        continue