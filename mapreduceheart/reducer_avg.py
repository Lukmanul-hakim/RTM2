#!/usr/bin/env python3
import sys

current = None
total = 0
count = 0

for line in sys.stdin:
    key, value = line.strip().split("\t")
    age, c = value.split(",")
    age = float(age)
    c = int(c)

    if key == current:
        total += age
        count += c
    else:
        if current:
            print(f"{current}\t{total/count}")
        current = key
        total = age
        count = c

if current:
    print(f"{current}\t{total/count}")