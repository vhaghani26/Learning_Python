#!/usr/bin/env python3

# Write a program that predicts if a protein is trans-membrane
# Trans-membrane proteins have the following properties
#	Signal peptide: https://en.wikipedia.org/wiki/Signal_peptide
#	Hydrophobic regions(s): https://en.wikipedia.org/wiki/Transmembrane_protein
#	No prolines (alpha helix)
# Hydrophobicity is measued via Kyte-Dolittle
#	https://en.wikipedia.org/wiki/Hydrophilicity_plot
# For our purposes:
#	Signal peptide is 8 aa long, KD > 2.5, first 30 aa
#	Hydrophobic region is 11 aa long, KD > 2.0, after 30 aa

# Use a dictionary for the K-D values, and store in biotools
# Use argparse for command line

import argparse
import random
import biotools as bt

# File Location: ~/Code/Learning_Python/MCB 185 (Korf Course)/Week 6

# Setup
parser = argparse.ArgumentParser(
	description='Predicts trans-membrane proteins.')

# Required Arguments
parser.add_argument('--file', required=True, type=str,
	metavar='<path>', help='Protein File')

# Optional arguments with default parameters
parser.add_argument('--win1', required=False, type=int, default=8,
	metavar='<int>', help='length of signal peptide [%(default)i]')
parser.add_argument('--win2', required=False, type=int, default=11,
	metavar='<int>', help='length of trans-membrane domain [%(default)i]')
parser.add_argument('--kd1', required=False, type=float, default=2.5,
	metavar='<float>', help='kd value for signal peptide [%(default)f]')
parser.add_argument('--kd2', required=False, type=float, default=2.0,
	metavar='<float>', help='kd value for hydrophobic region [%(default)f]')

# Finalization
arg = parser.parse_args()


def hh(seq, w, kd):
    for i in range(len(seq) -w +1):
        win = seq[i:i+w]
        if bt.hydro(win) > kd and 'P' not in win:
            return True
    return False    

for name, seq in bt.read_fasta(arg.file):
    nterm = seq[0:30]
    rest = seq[30:]
    if hh(nterm, arg.win1, arg.kd1) and hh(rest, arg.win2, arg.kd2):
        print(name)

"""
python3 transmembrane_2.py --file ../Week\ 5/proteins.fasta.gz --win1 8 --win2 11 --kd1 2.5 --kd2 2.0
usage: transmembrane_2.py.py [-h] --file <path> [--win1 <int>] [--win2 <int>] [--kd1 <float>]
                             [--kd2 <float>]
18w
Dtg
Krn
Lac
Mcr
PRY
Pxt
Pzl
QC
Ror
S1P
S2P
Spt
apn
bai
bdl
bou
bug
cue
drd
ft
grk
knk
ksh
m
nac
ort
rk
smo
thw
tsg
waw
zye
"""