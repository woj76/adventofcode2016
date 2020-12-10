#!/usr/bin/python3

from aoc import repres

file = open("../data/day06.txt", "rt")
data = [x for x in file.read().strip().split('\n')]
file.close()

part2 = True
r  = ""

l = len(data[0])

for col in range(0, l):
	counts = {}
	for c in range(ord('a'), ord('z') + 1):
		counts[chr(c)] = 0
	for x in data:
		counts[x[col]] += 1
	d = []
	for c in counts:
		d.append((counts[c], c))
	d.sort()
	r += d[0 if part2 else -1][1]

repres(r, part2)

