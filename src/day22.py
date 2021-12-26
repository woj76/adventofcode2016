#!/snap/bin/pypy3

from aoc import repres

part2 = True
r = 0

nodes = {}

max_x, max_y = 0, 0

with open("../data/day22.txt", "rt") as file:
	for d in file.read().strip().split('\n'):
		if d[:4] != "/dev":
			continue
		while '  ' in d:
			d = d.replace('  ', ' ')
		[n, s, u, a, p] = d.split(' ')
		[x, y] = [int(z) for z in n[16:].split('-y')]
		max_x = max(x, max_x)
		max_y = max(y, max_y)
		nodes[(x,y)] = (int(s[:-1]), int(u[:-1]))

max_x += 1
max_y += 1


def nodes_to_state(nds):
	r = ""
	for k in sorted(nds.keys()):
		r += str(nds[k])
	return r

min_cost = float('inf')
visited = {}

def final_state(nds):
	return nds[(0,0)][1]

if part2:
	found = False
	for y in range(max_y):
		for x in range(max_x):
			if nodes[(x,y)][1] == 0:
				zero_x = x
				zero_y = y
				found = True
				break
		if found:
			break
	# Should use shortest path, but the problem has specific shape
	x = zero_x
	y = zero_y
	steps = 0
	zero_size = nodes[(zero_x,zero_y)][0]
	while x != max_x-1 or y != 0:
		if y == 0:
			x += 1
		else:
			if nodes[(x,y-1)][0] > zero_size:
				x -= 1
			else:
				y -= 1
		steps += 1
	r = steps + (max_x-2)*5
else:
	for (x,y) in nodes:
		if nodes[(x,y)][1] == 0:
			continue
		for (x1, y1) in nodes:
			if (x, y) == (x1, y1):
				continue
			if nodes[(x,y)][1] <= nodes[(x1,y1)][0]-nodes[(x1,y1)][1]:
				r += 1

repres(r, part2)
