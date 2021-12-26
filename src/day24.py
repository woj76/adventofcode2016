#!/usr/bin/python3

from aoc import repres

import heapq
from collections import defaultdict

file = open("../data/day24.txt", "rt")
data = [x for x in file.read().strip().split('\n') if x != '']
file.close()

part2 = True
r  = 0

plane = {}
positions = []

y = 0
for d in data:
	x = 0
	for c in d:
		if c != '#':
			plane[(x,y)] = True
			if c == '0':
				zero_pos = (x,y)
			elif c != '.':
				positions.append((x,y))
		x += 1
	y += 1

positions = [zero_pos] + positions

def dijkstra(src,tgt):
	visited = set()
	q = []
	dist = defaultdict(lambda : float('inf'))
	dist[src] = 0

	heapq.heappush(q, (0, src))

	while q:
		cst, u = heapq.heappop(q)
		visited.add(u)
		if u == tgt:
			return cst
		ux,uy = u
		for v in [(x,y) for x,y in [(ux+1,uy), (ux,uy+1), (ux-1,uy), (ux,uy-1)] if (x,y) in plane and (x,y) not in visited]:
			alt = dist[u] + 1
			if alt < dist[v]:
				dist[v] = alt
				heapq.heappush(q, (alt, v))

distances = {}

for i in range(len(positions)):
	for j in range(i+1,len(positions)):
		d = dijkstra(positions[i], positions[j])
		if d < float('inf'):
			distances[(i,j)] = distances[(j,i)] = d

r = float('inf')

def find_shortest(considered,cst):
	global r
	if len(considered) == len(positions):
		if part2:
			cst = cst + distances[(considered[-1],0)]
		if cst < r:
			r = cst
		return
	curr = considered[-1]
	for p in [n for n in range(len(positions)) if n not in considered]:
		if (curr,p) in distances:
			find_shortest(considered+[p], cst+distances[(curr,p)])

find_shortest([0],0)

repres(r, part2)
