#!/usr/bin/env python3

from math import sqrt
import fileinput

# Write a program that computes typical stats
# Count, Min, Max, Mean, Std. Dev, Median
# No, you cannot import any other modules!

#assert(len(sys.argv)== 2)
#sys.argv[2] == textfile

numbers = []
sum = 0
for line in fileinput.input():
	if line[0] == '#': continue
	line = line.rstrip()
	numbers.append(float(line))
	sum += float(line)
numbers.sort()
if len(numbers)%2 != 0:
	median = numbers[((len(numbers)-1)/2)]
else: 
	median = (numbers[int((len(numbers))/2)] + numbers[int(((len(numbers))/2)-1)])/2

mean = sum/len(numbers)
sumstdev = 0
for i in range(len(numbers)):
	stdev = (numbers[i]-mean)**2
	sumstdev += stdev
stddev = sqrt(sumstdev/len(numbers))
	
print(f'Count: {len(numbers)}')
print(f'Minimum: {numbers[0]}')
print(f'Maximum: {numbers[-1]}')
print(f'Mean: {mean}')
print(f'Std. dev: {stddev:.3f}')
print(f'Median: {median}')
 

"""
python3 stats.py numbers.txt
Count: 10
Minimum: -1.0
Maximum: 256.0
Mean: 29.147789999999997
Std. dev: 75.777
Median 2.35914
"""
