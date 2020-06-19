#!/usr/bin/env python3

# Use argparse
# Write a program that translates mRNA
# Assume the protein encoded is the longest ORF
# Use a dictionary for translation and store in biotools

import argparse
import biotools as bt

# Setup
parser = argparse.ArgumentParser(
	description='Translates mRNA from proteins in a FASTA file')

# Required arguments
parser.add_argument('--file', required=True, type=str,
	metavar='<path>', help='Protein file (FASTA)')

# Finalization 
arg = parser.parse_args()


for name, seq in bt.read_fasta(arg.file):
	pro = []
	seq1 = bt.longest_orf(seq)
	for i in range(0, len(seq1), 3):
		codon = seq1[i:i+3]
		if codon in bt.aa: pro.append(bt.aa[codon])
		else:              pro.append('X') # how to deal with Ns and such
	print(f'>{name}')
	print(''.join(pro))

"""
python3 translate_mRNA_2.py --file ../Week\ 5/transcripts.fasta.gz
>CBG00001.1
MTFCENKNLPKPPSDRCQVVVISILSMILDFYLKYNPDKHWAHLFYGASPILEILVIFGMLANSVYGNKLAMFACVLDLVSGVFCLLTLPVISVAENATGVRLHLPYISTFHSQFSFQVSTPVDLFYVATFLGFVSTILILLFLILDALKFMKLRKLRNEDLEKEKKMNPIEKV*
>CBG00006.1
MNGVEKVNKYFDIKDKRDFLYHFGFGVDTLDIKAVFGDTKFVCTGGSPGRFKLYAEWFAKETSIPCSENLSRSDRFVIYKTGPVCWINHGMGTPSLSIMLVESFKLMHHAGVKNPTFIRLGTSGGVGVPPGTVVVSTGAMNAELGDTYVQVIAGKRIERPTQLDATLREALCAVGKEKNIPVETGKTMCADDFYEGQMRLDGYFCDYEEEDKYAFLRKLNSLGVRNIEMESTCFASFTCRAGFPSAIVCVTLLNRMDGDQVQIDKEKYIEYEERPFRLVTAYIRQQTGV*
etc.
"""
