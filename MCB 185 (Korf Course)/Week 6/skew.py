#!/usr/bin/env python3

# Use argparse
# Compute gc and gc-skew

import gzip
import sys
import biotools as bt
import argparse

parser = argparse.ArgumentParser(
	description='Calculates GC content and GC skew.')
# required arguments
parser.add_argument('--file', required=True, type=str,
	metavar='<str>', help='required FASTA File')
parser.add_argument('--win', required=True, type=int,
	metavar='<int>', help='Window Size')

arg = parser.parse_args()

for name, seq in bt.read_fasta(arg.file):
	for i in range(len(seq)-arg.win+1):
		sequence = seq[i:i+arg.win]
		print(f'{name} {i} {bt.gc(sequence):.3f} {bt.skew(sequence):.3f}')

"""
python3 skew.py --file genome.fa.gz --win 100 | head
I	0	0.510	-0.333
I	1	0.500	-0.360
I	2	0.490	-0.347
I	3	0.490	-0.306
I	4	0.500	-0.320
I	5	0.510	-0.333
I	6	0.510	-0.333
I	7	0.500	-0.360
I	8	0.490	-0.347
I	9	0.490	-0.306
"""
