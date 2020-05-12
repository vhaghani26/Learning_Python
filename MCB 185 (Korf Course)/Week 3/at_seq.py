#!/usr/bin/env python3

import random
'''random.seed(1)''' # comment-out this line to change sequence each time

# Write a program that stores random DNA sequence in a string
# The sequence should be 30 nt long
# On average, the sequence should be 60% AT
# Calculate the actual AT fraction while generating the sequence
# Report the length, AT fraction, and sequence

# random.random random.randint


dna = ''
dna_len = 30
at_count = 0

for i in range(dna_len):
    r = random.random()
    if r <=0.3:
        dna = dna + "A"
        at_count += 1
    elif 0.30 < r <= 0.60:
        dna = dna + "T"
        at_count += 1
    elif 0.60 < r <= 0.80:
        dna = dna + "G"
    else:
        dna = dna + "C"
print (dna_len, at_count / dna_len, dna)


"""
python3 at_seq.py
30 0.6666666666666666 ATTACCGTAATCTACTATTAAGTCACAACC
"""
