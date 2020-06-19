#!/usr/bin/env python3

# Write a program that compares two files of names to find:
#	Names unique to file 1
#	Names unique to file 2
#	Names shared in both files

import argparse

parser = argparse.ArgumentParser(
	description='Brief description of program.')
parser.add_argument('--file1', required=True, type=str,
	metavar='<str>', help='Name of File 1')
parser.add_argument('--file2', required=True, type=str,
	metavar='<str>', help='Name of File 2')
arg = parser.parse_args()


def file_to_dictionary(file_name):
	dict = {}
	with open(file_name) as fp:
		for word in fp.readlines():
			word = word.rstrip()
			dict[word] = True
	return dict

d1 = file_to_dictionary(arg.file1)
d2 = file_to_dictionary(arg.file2)

u1 = []
u2 = []
both = []

for word in d1:
	if word in d2: both.append(word)
	else:		   u1.append(word)
	
for word in d2:
	if word not in d1: u2.append(word)
	
print(u1, u2, both)

"""
python3 checklist.py --file1 --file2

# The example below usees actual files named "file1" and "file2"
python3 checklist.py --file1 file1 --file2 file2
['tiger', 'lion', 'wolf'] ['bear', 'iguana', 'lynx'] ['cat', 'dog', 'fish']
"""
