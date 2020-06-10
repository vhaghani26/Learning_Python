#!/usr/bin/env python3

import json

# Move the triple quotes downward to uncover each segment of code

"""

# The simplest complex data structure is the 2-dimenionsal list

d2 = [[3, 5, 7], [2, 4, 6],[0, 1, 0]]
print(d2[1][1])

# The previous is much better looking as a grid

d2 = [
	[3, 5, 7],
	[2, 4, 6],
	[0, 1, 0],
	]
print(d2[0][2])

# We can also create this stepwise

d2 = []
d2.append([3, 5, 7])
d2.append([2, 4, 6])
d2.append([0, 1, 0])
print(d2)

# Note that lists and tuples are related by not the same!
# You cannot modify a tuple

t2 = (
	(3, 5, 7),
	(2, 4, 6),
	(0, 1, 0),
	)
print(t2)
# t2.append((0, 0, 0)) # error

# But you can append to a list

d2.append((2,3)) # this is terrible!
# Generally, make your 2d lists rectangular and the same data type!
print(d2)

# The list-of-tuples is a common data type

address_book = []
address_book.append(('Ian', 53, 'Davis'))
address_book.append(('Max', 10, 'Wild'))
for name, age, location in address_book:
	print(name)

# The list-of-dictionaries is similarly useful, but more descriptive

book2 = []
book2.append({'name':'Ian', 'age':53, 'location':'Davis'})
book2.append({'name':'Max', 'age':10, 'location':'Wild'})
for person in book2:
	print(person['name'])

# Scoring matrices are naturally dictionaries-of-dictionaries

nt_score_matrix = {
	'A':{'A': 1, 'C':-1, 'G': -1, 'T':-1},
	'C':{'A':-1, 'C': 1, 'G': -1, 'T':-1},
	'G':{'A':-1, 'C':-1, 'G':  1, 'T':-1},
	'T':{'A':-1, 'C':-1, 'G': -1, 'T': 1},
}
s1 = 'ACCGTT'
s2 = 'ACAGTT'
score = 0
for i in range(len(s1)):
	score += nt_score_matrix[s1[i]][s2[i]]
print(score)

# A position weight matrix is naturally a list of dictionaries

polyA = [
	{'A': 0.775, 'C': 0.061, 'G': 0.066, 'T': 0.098},
	{'A': 0.949, 'C': 0.007, 'G': 0.020, 'T': 0.023},
	{'A': 0.029, 'C': 0.004, 'G': 0.009, 'T': 0.958},
	{'A': 0.856, 'C': 0.007, 'G': 0.131, 'T': 0.007},
	{'A': 0.980, 'C': 0.014, 'G': 0.001, 'T': 0.006},
	{'A': 0.975, 'C': 0.002, 'G': 0.006, 'T': 0.017},
	]
seq = 'ATGCTGAATAAACCGATA'
for i in range(len(seq) -len(polyA) + 1):
	score = 1
	for k in range(len(polyA)):
		nt = seq[i+k]
		score *= polyA[k][nt]
	print(i, score)

# Making a dictionary of dictionaries can be confusing

d = {} # plain old dictionary, easy
for i in range(len(seq) -1):
	dnt = seq[i:i+2]
	if dnt not in d: d[dnt] = 1
	else:            d[dnt] += 1
print(json.dumps(d, indent=4))

dd = {} # dictionary of dictionaries
for i in range(len(seq) -1):
	d1 = seq[i]
	d2 = seq[i+1]
	if d1 not in dd: dd[d1] = {} # this is the confusing part
	if d2 not in dd[d1]: dd[d1][d2] = 1
	else:                dd[d1][d2] += 1
print(json.dumps(dd, indent=4))

"""
