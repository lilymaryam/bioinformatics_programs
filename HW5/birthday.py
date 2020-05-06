#!/usr/bin/env python3

# You are probably well aware of the 'birthday paradox'
# https://en.wikipedia.org/wiki/Birthday_problem
# Let's try simulating it
# We will have a variable number of bins (can be months or days)
# And some number of trials for the simulation
# And some number of people whose have random birthdays
# Use assert() to check parameters
# On the command line:
#	python3 birthday.py <bins> <trials> <people>

import sys
import random

assert(len(sys.argv)==4)
bins = int(sys.argv[1])
trials = int(sys.argv[2])
people = int(sys.argv[3])

twobdays = 0
for t in range(trials):
	calendar = [0]*bins
	for p in range(people):
		r = random.randint(0,bins-1)
		calendar[r] += 1
	for day in calendar:
		if day > 1: 
			twobdays += 1
			break
print(f'{twobdays/trials:.3f}')

"""
python3 birthday.py 365 1000 23
0.520
"""

