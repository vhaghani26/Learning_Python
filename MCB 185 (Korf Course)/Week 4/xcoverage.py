#!/usr/bin/env python3

# Write a program that simulates random BAC coverage over a genome
# Use assert() to check parameter bounds
# Report min, max, and histogram of coverage
# Note that your output may vary due to random function
# Command line:
#	python3 xcoverage.py <genome size> <x>

import sys
import random

assert(len(sys.argv) == 3)
size = int(sys.argv[1])
coverage = float(sys.argv[2])
assert(size > 0)
assert(coverage > 0)

bacs = int(size * coverage)
genome = [0] * size
for i in range(bacs):
    r = random.randint(0, size -1)
    genome[r] += 1
genome.sort()
min = genome[0]
max = genome[-1]

hist = [0] * (max + 1)
for v in genome:
    hist[v] += 1
    
print(f'Size: {size}')
print(f'X: {coverage}')
print(f'BACs: {bacs}')
print(f'Min: {min}')
print(f'Max: {max}')
print(f'Counts:')
for i in range(len(hist)):
    print(i, hist[i])

"""
python3 xcoverage.py 1000 5
Size: 1000
X: 5.0
BACs: 5000
Min: 0
Max: 13
Counts:
0 5
1 39
2 88
3 144
4 175
5 150
6 151
7 116
8 59
9 40
10 20
11 5
12 6
13 2
"""
