#!/usr/bin/env python3

import fileinput

# Write a program that computes typical sequence stats
# No, you cannot import any other modules!
# Use rand_seq to generate the sequences
# Expected output is shown below

seqs = 0
counter = 0
seqcounter = 0
G = 0
C = 0
A = 0
T = 0

seqlengths = []
for line in fileinput.input():
	if line[0] == '>': 
		seqs += 1
		seqlengths.append(seqcounter)
		seqcounter = 0
	else:
		for i in line:
			counter += 1
			seqcounter += 1
			if i == 'G': G += 1
			if i == 'C': C += 1
			if i == 'A': A += 1
			if i == 'T': T += 1
seqlengths.append(seqcounter)
seqlengths = seqlengths[1:]
seqlengths.sort(reverse = True)

contigcount = 0
for i in seqlengths:
	contigcount += i
	if contigcount >= counter/2:
		N50 = i
		break
	
print(f'Number of sequences: {seqs}')
print(f'Number of letters: {counter}')
print(f'Minimum length: {seqlengths[-1]}')
print(f'Maximum length: {seqlengths[0]}')
print(f'N50: {N50}')
print(f'Composition: A={A/counter:.3f} C={C/counter:.3f} G={G/counter:.3f} T={T/counter:.3f}')

"""
python3 rand_seq.py 100 100 100000 0.35 | python3 seqstats.py
Number of sequences: 100
Number of letters: 4957689
Minimum length: 219
Maximum length: 99853
N50: 67081
Composition: A=0.325 C=0.175 G=0.175 T=0.325
"""
