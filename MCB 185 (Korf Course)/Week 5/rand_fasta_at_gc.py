#!/usr/bin/env python3

# Write a program that creates random fasta files
# Create a function that makes random DNA sequences
# Parameters include length and frequencies for A, C, G, T
# Command line:
#	python3 rand_fasta.py <count> <min> <max> <a> <c> <g> <t>

# This is a modified version of rand_fasta in which the AT and GC percentage of each generated sequence is reported back

import gzip
import sys
import math
import random

at_count = 0
gc_count = 0
dnaseq = []

def rand_dna(lenseq, a, c, g, t):
    global at_count
    global gc_count
    global dnaseq
    for i in range(lenseq):
        r = random.random()
        if r < a: 
            dnaseq.append('A')
            at_count += 1
        elif r < a+c:
            dnaseq.append('C')
            gc_count += 1
        elif r < a+c+g:
            dnaseq.append('G')
            gc_count += 1
        else:
            dnaseq.append('T')
            at_count += 1
    return ''.join(dnaseq)
    
count = int(sys.argv[1])

min = int(sys.argv[2])
max = int(sys.argv[3])
a = float(sys.argv[4])
c = float(sys.argv[5])
g = float(sys.argv[6])
t = float(sys.argv[7])

for i in range(count):
    x = random.randint(min, max)
    dna = rand_dna(x, a, c, g, t)
    print(f'>seq-{i}')
    print(dna)
    print(f'AT Percent: {at_count / len(dnaseq):.2f}')
    print(f'GC Percent: {gc_count / len(dnaseq):.2f}')

"""
python3 rand_fasta_at_gc.py 4 10 20 0.4 0.1 0.1 0.4
>seq-0
ATTGTACTATCCAG
AT Percent: 0.64
GC Percent: 0.36
>seq-1
ATTGTACTATCCAGAATTCTATTTTTTGAA
AT Percent: 0.77
GC Percent: 0.23
>seq-2
ATTGTACTATCCAGAATTCTATTTTTTGAATGATTATAAGATATAAAT
AT Percent: 0.81
GC Percent: 0.19
>seq-3
ATTGTACTATCCAGAATTCTATTTTTTGAATGATTATAAGATATAAATTTCTGTAAAGTAGA
AT Percent: 0.79
GC Percent: 0.21
"""
