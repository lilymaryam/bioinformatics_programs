#!/usr/bin/env python3

# Write a program that prints out the position, frame, and letter of the DNA
# Try coding this with a single loop
# Try coding this with nested loops

dna = 'ATGGCCTTT'

print("Single Loop")
for i in range (0,len(dna)):
	f = i%3
	l= dna[i]
	print(i,f,l)
	
print("Nested Loops")
for i in range (0,len(dna)-2,3):
	frame = 0
	for j in range (i,i+3):
		print(j,frame,dna[j])
		frame += 1
	

		
	


"""
0 0 A
1 1 T
2 2 G
3 0 G
4 1 C
5 2 C
6 0 T
7 1 T
8 2 T
"""
