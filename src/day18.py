#!/snap/bin/pypy3

from aoc import repres

with open("../data/day18.txt", "rt") as file:
	data = [['.'] + list(file.read().strip()) + ['.']]

part2 = True

total_rows = 400000 if part2 else 40

last_row = data[0]

for _ in range(total_rows - 1):
	new_row = ['.'] * len(last_row)
	for i in range(1, len(new_row)-1):
		if "".join(last_row[i-1:i+2]) in ["^^.", ".^^", "^..", "..^"]:
			new_row[i] = '^'
	data.append(new_row)
	last_row = new_row

repres(sum([r.count('.') for r in data]) - 2*total_rows, part2)
