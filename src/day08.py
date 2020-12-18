#!/usr/bin/python3

from aoc import repres

file = open("../data/day08.txt", "rt")
data = [x for x in file.read().strip().split('\n')]
file.close()

part2 = True

x_max = 50
y_max = 6

display = [[0]*x_max for _ in range(y_max)]

for d in data:
	if d[:4] == "rect":
		[w,h] = [int(xy) for xy in d[5:].split('x')]
		for x in range(w):
			for y in range(h):
				display[y][x] = 1
	else:
		dd = d.split(' ')
		rot_xy = int(dd[2][2:])
		rot_n = int(dd[4])
		if dd[1] == "row":
			for _ in range(rot_n):
				last = display[rot_xy][-1]
				for i in range(x_max-1, 0, -1):
					display[rot_xy][i] = display[rot_xy][i-1]
				display[rot_xy][0] = last
		else:
			assert dd[1] == "column"
			for _ in range(rot_n):
				last = display[-1][rot_xy]
				for j in range(y_max-1, 0, -1):
					display[j][rot_xy] = display[j-1][rot_xy]
				display[0][rot_xy] = last

if part2:
	print("Part 2:\n")
	for row in display:
		print("".join([('#' if x == 1 else '.') for x in row]))
	print()
else:
	repres(sum([sum(row) for row in display]), False)
