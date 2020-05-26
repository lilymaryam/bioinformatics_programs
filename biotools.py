#!/usr/bin/env python3

import sys
import gzip
import math

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

def entropy(p):
	h = 0
	sum = 0
	for pi in p:
		assert(pi != 0)
		h -= pi*math.log2(pi)
		sum += pi
	assert(math.isclose(sum, 1))
	return h
	
def seqentropy(seq):
	a,c,g,t = 0,0,0,0
	for nt in seq:
		if nt == 'A': a += 1
		elif nt == 'C': c += 1
		elif nt == 'G': g += 1
		elif nt == 'T': t += 1
	total = a + c + g + t
	if total == 0: return None
	fd = []
	if a != 0: fd.append(a/total)
	if c != 0: fd.append(c/total)
	if g != 0: fd.append(g/total)
	if t != 0: fd.append(t/total)
	return entropy(fd)