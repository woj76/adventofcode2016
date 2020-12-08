#!/usr/bin/python3

from aoc import repres

file = open("../data/day03.txt", "rt")
data = [[int(y) for y in x.strip().split('  ') if y != ''] for x in file.read().strip().split('\n')]
file.close()

part2 = True
r  = 0

def check_triangle(x, y, z):
	return 1 if x + y > z and x + z > y and y + z > x else 0

if part2:
	for i in range(3):
		for j in range(0, len(data), 3):
			x = data[j][i]
			y = data[j+1][i]
			z = data[j+2][i]
			r += check_triangle(x, y, z)
else:
	for [x, y, z] in data:
		r += check_triangle(x, y, z)

repres(r, part2)
