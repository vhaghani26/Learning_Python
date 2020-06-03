#!/usr/bin/env python3

# Use argparse
# Write a program that translates an mRNA
# Assume the protein encoded is the longest ORF

import gzip
import sys
import biotools as bt
import argparse

parser = argparse.ArgumentParser(
	description='Translates mRNA.')

parser.add_argument('--file', required=True, type=str,
	metavar='<str>', help='FASTA file')

arg = parser.parse_args()


for name, seq in bt.read_fasta(arg.file):
		print(f'>{name}')
		print(bt.translate(bt.longest_orf(seq)))


"""
python3 translate_mRNA.py --file ../Week\ 5/transcripts.fasta.gz # My path
python3 translate_mRNA.py --file ../Lesson05/transcripts.fasta.gz # Korf's path
>CBG00001.1
MTFCENKNLPKPPSDRCQVVVISILSMILDFYLKYNPDKHWAHLFYGASPILEILVIFGMLANSVYGNKLAMFACVLDLVSGVFCLLTLPVISVAENATGVRLHLPYISTFHSQFSFQVSTPVDLFYVATFLGFVSTILILLFLILDALKFMKLRKLRNEDLEKEKKMNPIEKV*
>CBG00006.1
MNGVEKVNKYFDIKDKRDFLYHFGFGVDTLDIKAVFGDTKFVCTGGSPGRFKLYAEWFAKETSIPCSENLSRSDRFVIYKTGPVCWINHGMGTPSLSIMLVESFKLMHHAGVKNPTFIRLGTSGGVGVPPGTVVVSTGAMNAELGDTYVQVIAGKRIERPTQLDATLREALCAVGKEKNIPVETGKTMCADDFYEGQMRLDGYFCDYEEEDKYAFLRKLNSLGVRNIEMESTCFASFTCRAGFPSAIVCVTLLNRMDGDQVQIDKEKYIEYEERPFRLVTAYIRQQTGV*
etc.
"""
