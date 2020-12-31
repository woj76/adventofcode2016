#!/snap/bin/pypy3

from aoc import repres
from collections import deque

input = 1350

grid = {}

def get_xy(x,y):
	if x < 0 or y < 0:
		return None
	if (x,y) in grid:
		return grid[(x,y)]
	ones = "{0:b}".format(x*x + 3*x + 2*x*y + y + y*y + input).count('1')
	if ones % 2 == 0:
		v = '.'
	else:
		v = '#'
	grid[(x,y)] = v
	return v

def neighbours(x,y):
	ret = []
	for (nx,ny) in [(x+1,y), (x-1, y), (x, y+1), (x, y-1)]:
		if nx < 0 or ny < 0:
			continue
		if get_xy(nx, ny) == '.':
			ret.append((nx,ny))
	return ret

def get_dist(x,y):
	if (x,y) in dist:
		return dist[(x,y)]
	return float('inf')

tx, ty = 31, 39

q = deque()
dist = {}
prev = {}

dist[(1,1)] = 0
q.append((1,1))

while len(q) > 0:
	ux, uy = q.popleft()
	if (ux, uy) == (tx, ty):
		break
	for v in neighbours(ux, uy):
		alt = get_dist(ux,uy) + 1
		if alt < get_dist(v[0], v[1]):
			dist[v] = alt
			prev[v] = (ux,uy)
			q.append(v)

r = dist[(tx,ty)]

repres(r, False)

visited = {}

def dfs(d,p):
	if d == 51:
		return
	if (d,p) in visited:
		return
	visited[(d,p)] = True
	for v in neighbours(p[0], p[1]):
		dfs(d+1, v)

dfs(0, (1,1))

r = len(set([p for d,p in visited]))

repres(r, True)
