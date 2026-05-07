#!/usr/bin/env python3
import sys

for line in sys.stdin:
    line = line.strip()

    # skip header
    if line.startswith("age"):
        continue

    parts = line.split(",")

    if len(parts) < 14:
        continue

    try:
        target = parts[13]   # kolom target (index 13)
        print(f"{target}\t1")
    except:
        continue
