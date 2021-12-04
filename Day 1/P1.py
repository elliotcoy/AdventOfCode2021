import sys

prv = sys.maxsize
cur = 0
out = 0

with open('Day 1\input.txt', 'r') as s:
    for line in s:
        cur = int(line)
        if cur > prv:
            out += 1
        prv = cur

print(out)
