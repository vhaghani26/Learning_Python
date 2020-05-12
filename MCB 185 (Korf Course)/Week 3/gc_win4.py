#!/usr/bin/env python3

# Write a program that computes the GC fraction of a DNA sequence in a window
# Window size is 11 nt
# Step size is 5 nt
# Output with 4 significant figures using whichever method you prefer
# Use no nested loops (as in gc_win2.py)

dna = 'ACGACGCAGGAGGAGAGTTTCAGAGATCACGAATACATCCATATTACCCAGAGAGAG'
w = 11
s = 5
gc_count = 0

for i in range(0, w):
    if dna[i] == 'G' or dna[i] == 'C':
        gc_count += 1
print(0, dna[0:w], '%.4f' % (gc_count / w))

for i in range(s, len(dna) -w +1, s):
    prev = dna[i-s:i]
    next = dna[i+w-s:i+w]
    for p in prev:
        if p == 'G' or p == 'C':
            gc_count -= 1
    for n in next:
        if n == 'G' or n == 'C':
            gc_count += 1
    print(i, dna[i:i+w], '%.4f' % (gc_count / w))

"""
python3 gc_win4.py
0 ACGACGCAGGA 0.6364
5 GCAGGAGGAGA 0.6364
10 AGGAGAGTTTC 0.4545
15 AGTTTCAGAGA 0.3636
20 CAGAGATCACG 0.5455
25 ATCACGAATAC 0.3636
30 GAATACATCCA 0.3636
35 CATCCATATTA 0.2727
40 ATATTACCCAG 0.3636
45 ACCCAGAGAGA 0.5455
"""
