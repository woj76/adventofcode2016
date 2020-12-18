#!/usr/bin/python3

from aoc import repres

file = open("../data/day09.txt", "rt")
data = file.read().strip()
file.close()

part2 = True

def decomp_len(s):
	result = 0
	i = 0
	while i < len(s):
		c = s[i]
		if c == '(':
			j = s.index(')', i+1)
			marker = s[i+1:j]
			[ml, mr] = [int(x) for x in marker.split('x')]
			i = j + 1
			if part2:
				result += decomp_len(s[i:i+ml]) * mr
			else:
				result += ml * mr
			i += ml
		else:
			result += 1
			i += 1
	return result

repres(decomp_len(data), part2)
