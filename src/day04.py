#!/usr/bin/python3

from aoc import repres
from functools import cmp_to_key

file = open("../data/day04.txt", "rt")
data = [x for x in file.read().strip().split('\n')]
file.close()

part2 = True
r  = 0

def cmp(e1, e2):
	(c1,l1) = e1
	(c2,l2) = e2
	if c1 < c2:
		return 1
	if c1 > c2:
		return -1
	if ord(l1) > ord(l2):
		return 1
	if ord(l1) < ord(l2):
		return -1
	return 0

cmp_key = cmp_to_key(cmp)

for x in data:
	[code_id, pattern] = x.split('[')
	pattern = list(pattern[:-1])
	words = code_id.split('-')
	i = int(words[-1])
	word = "-".join(words[:-1])
	counts = []
	for l in set(word) - {'-'}:
		counts.append((word.count(l),l))
	counts.sort(key=cmp_key)
	if [e[1] for e in counts[:5]] == pattern:
		if part2:
			s = [" " if c == '-' else chr((ord(c) - ord('a') + i) % 26 + ord('a')) for c in word]
			if s == list("northpole object storage"):
				r = i
				break
		else:
			r += i

repres(r, part2)
