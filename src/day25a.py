#!/snap/bin/pypy3

from aoc import repres

const = 7 * 365 # from user input

num = 1
while True:
	num *= 2
	if num > const:
		break
	num *= 2
	if num > const:
		break
	num += 1
	if num > const:
		break

repres(num - const, False)
