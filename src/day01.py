#!/usr/bin/python3

from aoc import tadd, repres, loopbreak

file = open("../data/day01.txt", "rt")
data = [(x[:1],int(x[1:])) for x in file.readline().strip().split(', ')]
file.close()

part2 = True

r  = 0
#         U      R       D        L
dirs = [ (0,1), (1, 0), (0, -1), (-1, 0) ]
i = 0
p = (0,0)

visited = []

try:
	for d,s in data:
		i += 1 if d == 'R' else -1
		i %= 4
		while s > 0:
			p = tadd(p, dirs[i])
			if part2 and p in visited:
				raise loopbreak()
			visited.append(p)
			s -= 1
except loopbreak:
	pass

r = abs(p[0]) + abs(p[1])

repres(r, part2)