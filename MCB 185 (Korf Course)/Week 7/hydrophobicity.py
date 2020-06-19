#!/usr/bin/env python3

# Write a program that computes hydrophobicity in a window
# Let the user choose the method (see below)
# https://en.wikipedia.org/wiki/Hydrophilicity_plot
# https://en.wikipedia.org/wiki/Hydrophobicity_scales

import argparse
import biotools as bt

# Setup
parser = argparse.ArgumentParser(
	description='Calculates hydrophobicity in a window using a certain amino acid scoring method')

# Required arguments
parser.add_argument('--file', required=True, type=str,
	metavar='<path>', help='Protein File')
parser.add_argument('--method', required=True, type=str, default='KD',
	metavar='<str>', help='Method used to calculate Hydrophobicity: KD, IS, OS, IS+OS')


# Optional arguments
parser.add_argument('--window', required=False, type=int, default=11,
	metavar='<int>', help='Window Size[%(default)i]')

# Finalization 
arg = parser.parse_args()


for name, seq in bt.read_fasta(arg.file):
	for i in range(len(seq) - arg.window +1):
		win = seq[i:i + arg.window]
		print(bt.cal_hydrophobicity(win, arg.method, arg.window))

"""
python3 hydrophobicity.py --file ../Week\ 5/proteins.fasta.gz --window 11 --method kd
17.1
17.0
22.8
22.8
25.3
28.6
33.2
32.5
31.800000000000004
36.3
36.00000000000001
33.3
28.000000000000004
...
"""
