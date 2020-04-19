#!/usr/bin/env python3

# Write a program that computes the GC fraction of a DNA sequence in a window
# Window size is 11 nt
# Output with 4 significant figures using whichever method you prefer
# Use no nested loops
# Describe the pros/cons of this algorith vs. nested loops

seq = 'ACGACGCAGGAGGAGAGTTTCAGAGATCACGAATACATCCATATTACCCAGAGAGAG'
w = 11
gc = 0
for i in range(0,w):
	if seq[i] == "G" or seq[i] == "C":
		gc += 1 
print(0,seq[0:w],f'{gc/w:.4f}')
	
for i in range(1, len(seq)-(w-1)): 
	prev_nt = seq[i-1]
	next_nt = seq[i+w-1]
	if prev_nt == 'G' or prev_nt == "C": gc -= 1
	if next_nt == 'G' or next_nt == "C": gc += 1
	print(i,seq[i:i+w],f'{gc/w:.4f}')
	
"""
The nested loop algorithm individually calculates the GC content for each window. This
takes a lot of computing power when each window has only a single letter difference from
the previous window. The separate loops algorithm save computing power by sliding the 
window along the sequence and adding and/or subtracting the Gs and Cs from the existing 
fraction as they enter and leave the window. Separate loops are much faster for long 
windows.

The cons of using the separate loops algorithm is that it takes longer to reprogram the 
code if the windows are more than 1 base pair apart. In the nested loop algorithm, the 
range in the outer loop can be changed to index a different window from the sequence. 
In the separate loop algorithm, the prev and next variables have to become sequences
and the GC content of these variables has to be counted and deleted from the existing 
fraction to get the right answer. This takes longer to re-program than the nested loop 
algorithm.  
"""
	
	

"""
0 ACGACGCAGGA 0.6364
1 CGACGCAGGAG 0.7273
2 GACGCAGGAGG 0.7273
3 ACGCAGGAGGA 0.6364
4 CGCAGGAGGAG 0.7273
5 GCAGGAGGAGA 0.6364
6 CAGGAGGAGAG 0.6364
7 AGGAGGAGAGT 0.5455
8 GGAGGAGAGTT 0.5455
9 GAGGAGAGTTT 0.4545
10 AGGAGAGTTTC 0.4545
11 GGAGAGTTTCA 0.4545
12 GAGAGTTTCAG 0.4545
13 AGAGTTTCAGA 0.3636
14 GAGTTTCAGAG 0.4545
15 AGTTTCAGAGA 0.3636
16 GTTTCAGAGAT 0.3636
17 TTTCAGAGATC 0.3636
18 TTCAGAGATCA 0.3636
19 TCAGAGATCAC 0.4545
20 CAGAGATCACG 0.5455
21 AGAGATCACGA 0.4545
22 GAGATCACGAA 0.4545
23 AGATCACGAAT 0.3636
24 GATCACGAATA 0.3636
25 ATCACGAATAC 0.3636
26 TCACGAATACA 0.3636
27 CACGAATACAT 0.3636
28 ACGAATACATC 0.3636
29 CGAATACATCC 0.4545
30 GAATACATCCA 0.3636
31 AATACATCCAT 0.2727
32 ATACATCCATA 0.2727
33 TACATCCATAT 0.2727
34 ACATCCATATT 0.2727
35 CATCCATATTA 0.2727
36 ATCCATATTAC 0.2727
37 TCCATATTACC 0.3636
38 CCATATTACCC 0.4545
39 CATATTACCCA 0.3636
40 ATATTACCCAG 0.3636
41 TATTACCCAGA 0.3636
42 ATTACCCAGAG 0.4545
43 TTACCCAGAGA 0.4545
44 TACCCAGAGAG 0.5455
45 ACCCAGAGAGA 0.5455
46 CCCAGAGAGAG 0.6364
"""
