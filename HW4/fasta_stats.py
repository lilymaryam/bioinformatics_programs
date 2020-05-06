#!/usr/bin/env python3

import gzip
import sys

# Write a program that computes typical stats for sequence files
# Command line:
#	python3 fasta_stats.py transcripts.fasta.gz
# Output:
#	See below
import gzip

def read_fasta(filename):
	name = None
	seqs = []
	
	fp = None
	if filename == '-':
		fp = sys.stdin
	elif filename.endswith('.gz'):
		fp = gzip.open(filename, 'rt')
	else:
		fp = open(filename)

	for line in fp.readlines():
		line = line.rstrip()
		if line.startswith('>'):
			if len(seqs) > 0:
				seq = ''.join(seqs)
				yield(name, seq)
				name = line[1:]
				seqs = []
			else:
				name = line[1:]
		else:
			seqs.append(line)
	yield(name, ''.join(seqs))
	fp.close()



for name, seq in read_fasta('proteins.fasta.gz'):
	print(name, len(seq))


"""
python3 fasta_stats.py transcripts.fasta.gz
Count: 232
Total: 278793
Min: 603
Max: 1991
Mean: 1201.7
NTs: 0.291 0.218 0.210 0.281
"""
