#!/usr/bin/env python3

# Write a program that computes typical sequence stats
# No, you cannot import any other modules!
# Use rand_seq to generate the sequences
# Expected output is shown below

import fileinput

data = []
count = 0

for line in fileinput.input():
    if line.startswith('#'): continue
    line = line.rstrip()
    data.append(line)

count = int(len(data))

# Calculating min and max
data.sort(key = len)

min = len(data[0])
max = len(data[-1])

# Calculating compositon of nucleotides and total number of bases
a_count = 0
t_count = 0
c_count = 0
g_count = 0
total = 0

for i in range(len(data)):
    seq = data[i]
    for nt in seq:
        if nt == 'A': a_count += 1
        elif nt == 'T': t_count += 1
        elif nt == 'C': c_count += 1
        elif nt == 'G': g_count += 1
        total = g_count + c_count + t_count + a_count
   
# Calculating N50 (the median length of the sequences)
if count % 2 == 0:
    median1 = len(data[int(count/2)-1])
    median2 = len(data[int(count/2)])
    median = (median1 + median2)/2
else:
    median = len(data[int(count/2)])


print(f'Number of sequences: {count}')
print(f'Number of letters: {total}')
print(f'Minimum Length: {min}')
print(f'Maximum Length: {max}')
print(f'N50: {median}')
print(f'Composition: A={a_count/total:.3f} C={c_count/total:.3f} G={g_count/total:.3f} T={t_count/total:.3f}')



"""
python3 rand_seq.py 100 100 100000 0.35 | python3 seqstats.py
Number of sequences: 100
Number of letters: 4957689
Minimum length: 219
Maximum length: 99853
N50: 67081
Composition: A=0.325 C=0.175 G=0.175 T=0.325
"""
