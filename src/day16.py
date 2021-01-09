#!/snap/bin/pypy3

from aoc import repres

part2 = True

input = list("01000100010010111")

disk_size = 35651584 if part2 else 272

while len(input) < disk_size:
	input.append('0')
	for i in range(len(input)-2, -1, -1):
		input.append('1' if input[i] == '0' else '0')
		if len(input) == disk_size:
			break

while len(input) % 2 == 0:
	input = ['1' if input[i] == input[i+1] else '0' for i in range(0, len(input), 2)]

r = "".join(input)

repres(r, part2)
