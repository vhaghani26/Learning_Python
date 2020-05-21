#!/usr/bin/env python3

# Write a program that computes typical stats for sequence files
# See below for command line and output

import gzip
import sys

def read_fasta(filename):
    name = None
    seqs = []
    
    fp = None
    if filename == '-':
        fp = sys.stdin
    elif filename.endswith('.gz'):
        fp = gzip.open(filename, 'rt')
    else:
        fp = open(filename)

    for line in fp.readlines():
        line = line.rstrip()
        if line.startswith('>'):
            if len(seqs) > 0:
                seq = ''.join(seqs)
                yield(name, seq)
                name = line[1:]
                seqs = []
            else:
                name = line[1:]
        else:
            seqs.append(line)
    yield(name, ''.join(seqs))
    fp.close()



size = []
total_nt = 0
a, c, g, t = 0, 0, 0, 0
for name, seq in read_fasta(sys.argv[1]):
    size.append(len(seq))
    total_nt += len(seq)
    for nt in seq:
        if nt == 'A': a += 1
        elif nt == 'C': c += 1
        elif nt == 'T': t += 1
        elif nt == 'G': g += 1

    
size.sort()
min = size[0]
max = size[-1]

count = int(len(size))
mean = total_nt/count

print(f'Count: {count}')
print(f'Total: {total_nt}')
print(f'Min: {min}')
print(f'Max: {max}')
print(f'Mean: {mean:0.1f}')
print(f'NTS: {a/total_nt:0.3f}, {c/total_nt:0.3f}, {g/total_nt:0.3f}, {t/total_nt:0.3f}')

"""
Command Line: python3 fasta_stats.py transcripts.fasta.gz
Count: 232
Total: 278793
Min: 603
Max: 1991
Mean: 1201.7
NTs: 0.291 0.218 0.210 0.281
"""
