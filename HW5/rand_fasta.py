#!/usr/bin/env python3

import gzip
import sys
import math
import random

# Write a program that creates random fasta files
# Create a function that makes random DNA sequences
# Parameters include length and frequencies for A, C, G, T
# Command line: python3 rand_fasta.py <count> <min> <max> <a> <c> <g> <t>

assert(len(sys.argv)== 8)
count = int(sys.argv[1])
min = int(sys.argv[2])
max = int(sys.argv[3])
a = float(sys.argv[4])
c = float(sys.argv[5])
g = float(sys.argv[6])
t = float(sys.argv[7])

def rand_dna(length, a, c, g, t):
	dna = []
	for i in range(length):
		r = random.random()
		if r < a:       dna.append('A')
		elif r < a+c:   dna.append('C')
		elif r < a+c+g: dna.append('G')
		else:           dna.append('T')
	
	return ''.join(dna)
	

for i in range(count):
	lenseq = random.randint(min,max)
	DNA = rand_dna(lenseq, a, c, g, t)
	print(f'>seq-{i}')
	print(DNA)
	
	
	

"""

"""
