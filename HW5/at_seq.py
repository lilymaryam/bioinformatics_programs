#!/usr/bin/env python3

import random
random.seed(1) # comment-out this line to change sequence each time

# Write a program that stores random DNA sequence in a string
# The sequence should be 30 nt long
# On average, the sequence should be 60% AT
# Calculate the actual AT fraction while generating the sequence
# Report the length, AT fraction, and sequence

DNA = ''
at  = 0 
length = 30
for nt in range(length):
	r = random.random()
	if r < .6:
		at += 1
		r = random.random()
		if r > .5:  DNA += 'A'
		else:       DNA += 'T'
	else:
		r = random.random()
		if r > .5:  DNA += 'G'
		else:       DNA += 'C'
print(length, at/length, DNA)
		


"""
30 0.6666666666666666 ATTACCGTAATCTACTATTAAGTCACAACC
"""
