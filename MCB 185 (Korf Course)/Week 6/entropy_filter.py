#!/usr/bin/env python3

# Write a program that masks areas of low complexity sequence
# Use argparse for command line arguments (see example below)
# Use read_fasta() from biotools.py

import argparse
import biotools as bt
import math
import random 

parser = argparse.ArgumentParser(
	description='Low complexity sequence masker')

parser.add_argument('--input', required=False, type=str,
	metavar='<path>', help='FASTA file')
parser.add_argument('--window', required=False, type=int, default=15,
	metavar='<int>', help='optional integer argument [%(default)i]')
parser.add_argument('--threshold', required=False, type=float, default=1.100000,
	metavar='<float>', help='Entropy Threshold')
parser.add_argument('--lowercase', required=False, type=str, default='N',
	metavar='<str>', help='report lower case instead of N [%(default)s]')
	
arg = parser.parse_args()

def entropy(seq, w):
	for i in range(len(seq) -w +1):
		win = seq[i: i+ w]
		a_ct = 0.00001
		c_ct = 0.00001
		g_ct = 0.00001
		t_ct = 0.00001
		for nt in win:
			p = []
			if nt == 'A': a_ct += 1
			elif nt == 'C': c_ct += 1
			elif nt == 'G': g_ct += 1
			elif nt == 'T': t_ct += 1
			aprob = float(a_ct/w)
			p.append(aprob)
			cprob = float(c_ct/w)
			p.append(cprob)
			gprob = float(g_ct/w)
			p.append(gprob)
			tprob = float(t_ct/w)
			p.append(tprob)
			h = 0
		for i in range(len(p)):
			h -= p[i] * math.log2(p[i])
			if h < 0.0001:
				h = 0
	return h
	
for name, seq in bt.read_fasta(arg.input):
	seq_list = []
	for nt in seq:
		seq_list.append(nt)
	for i in range(len(seq) - arg.window +1):
		win = seq[i:i + arg.window]
		if entropy(win, arg.window) < arg.threshold:
			for j in range(i, i+arg.window):
				seq_list[j] = 'N'
	seq_final = ''.join(seq_list)
	print(f'>{name}')
	print(seq_final)


"""
python3 entropy_filter.py --help
usage: entropy_filter.py [-h] --input <path> [--window <int>]
                         [--threshold <float>] [--lowercase]

Low complexity sequence masker.

optional arguments:
  -h, --help           show this help message and exit
  --input <path>       fasta file
  --window <int>       optional integer argument [15]
  --threshold <float>  entropy threshold [1.100000]
  --lowercase          report lower case instead of N


python3 entropy_filter.py --input genome.fa.gz | head -20
>I
GCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAA
GCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAA
GCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAA
GCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAA
GCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAA
GCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAA
GCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAA
GCCTAAGCCTAAAAAATTGAGATAAGAAAACATTTTACTTTTTCAAAATTGTTTTCATGC
TAAATTCAAAACNNNNNNNNNNNNNNNAAGCTTCTAGATATTTGGCGGGTACCTCTAATT
TTGCCTGCCTGCCAACCTATATGCTCCTGTGTTTAGGCCTAATACTAAGCCTAAGCCTAA
GCCTAATACTAAGCCTAAGCCTAAGACTAAGCCTAATACTAAGCCTAAGCCTAAGACTAA
GCCTAAGACTAAGCCTAAGACTAAGCCTAATACTAAGCCTAAGCCTAAGACTAAGCCTAA
GCCTAATACTAAGCCTAAGCCTAAGACTAAGCCTAATACTAAGCCTAAGCCTAAGACTAA
GCCTAAGACTAAGCCTAAGACTAAGCCTAATACTAAGCCTAAGCCTAAGACTAAGCCTAA
GCCTAAAAGAATATGGTAGCTACAGAAACGGTAGTACACTCTTCTGNNNNNNNNNNNNNN
NTGCAATTTTTATAGCTAGGGCACTTTTTGTCTGCCCAAATATAGGCAACCAAAAATAAT
TGCCAAGTTTTTAATGATTTGTTGCATATTGAAAAAAACANNNNNNNNNNNNNNNGAAAT
GAATATCGTAGCTACAGAAACGGTTGTGCACTCATCTGAAANNNNNNNNNNNNNNNNNNN
NNGCACTTTGTGCAGAATTCTTGATTCTTGATTCTTGCAGAAATTTGCAAGAAAATTCGC
"""
