#!/usr/bin/env python3

# Write a program that prints the reverse-complement of a DNA sequence
# You must use a loop and conditional

dna = 'ACTGAAAAAAAAAAA'

# This has the "reverse" aspect written into the code

comp = ''

for nt in dna:
    if nt == 'A': comp = 'T' + comp
    elif nt == 'C': comp = 'G' + comp
    elif nt == 'G': comp = 'C' + comp
    elif nt == 'T': comp = 'A' + comp
    else: comp = '_' + comp
print("DNA:", dna)
print("Reverse-Complement:", comp)

"""
# This creates the complement and reverses it at the end
comp = ''

for nt in dna:
    if nt == 'A': comp = comp + 'T'
    elif nt == 'C': comp = comp + 'G'
    elif nt == 'G': comp = comp + 'C'
    elif nt == 'T': comp = comp + 'A'
    else: comp = '_' + comp
print("DNA:", dna)
print("Complement:", comp)
print("Reverse Complement:", comp[::-1])
"""

"""
# This creates the complement 

comp = ''

for nt in dna:
    if nt == 'A': comp = comp + 'T'
    elif nt == 'C': comp = comp + 'G'
    elif nt == 'G': comp = comp + 'C'
    elif nt == 'T': comp = comp + 'A'
    else: comp = '_' + comp
print("DNA:", dna)
print("Complement:", comp)
"""

"""
python3 anti.py
TTTTTTTTTTTCAGT
"""
