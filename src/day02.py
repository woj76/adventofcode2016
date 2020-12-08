#!/usr/bin/python3

from aoc import repres

file = open("../data/day02.txt", "rt")
data = [x for x in file.read().strip().split('\n')]
file.close()

part2 = True

r  = ""
if part2:
	keypad = [ "       ", "   1   ", "  234  ", " 56789 ", "  ABC  ", "   D   ", "       " ]
	x, y = 1, 3
else:
	keypad = [ "     ", " 123 ", " 456 ", " 789 ", "     " ]
	x = y = 2

for d in data:
	for c in d:
		if c == 'L':
			mx, my = -1, 0
		elif c == 'R':
			mx, my = 1, 0
		elif c == 'U':
			mx, my = 0, -1
		elif c == 'D':
			mx, my = 0, 1
		nx, ny = x + mx, y + my
		if keypad[ny][nx] != ' ':
			x, y = nx, ny
	r += keypad[y][x]

repres(r, part2)

