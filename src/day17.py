#!/usr/bin/python3

import hashlib
from collections import deque
from aoc import repres

input = 'pvhmgsws'

part2 = True

def get_steps(p, x, y):
	r = []
	doors = hashlib.md5((input+p).encode()).hexdigest()
	if doors[0] in "bcdef" and y > 0:
		r.append('U')
	if doors[1] in "bcdef" and y < 3:
		r.append('D')
	if doors[2] in "bcdef" and x > 0:
		r.append('L')
	if doors[3] in "bcdef" and x < 3:
		r.append('R')
	return r

q = deque()
q.append((0,0,""))

r = float('-inf') if part2 else None

while len(q) > 0:
	x, y, p = q.popleft()
	path_end = False
	if x == 3 and y == 3:
		if part2:
			r = max(r, len(p))
			path_end = True
		else:
			r = p
			break
	if not path_end:
		dirs = get_steps(p, x, y)
		for d in dirs:
			if d == 'U':
				q.append((x, y-1, p+d))
			elif d == 'D':
				q.append((x, y+1, p+d))
			elif d == 'L':
				q.append((x-1, y, p+d))
			elif d == 'R':
				q.append((x+1, y, p+d))

repres(r, part2)
