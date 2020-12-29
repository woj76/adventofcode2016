#!/snap/bin/pypy3

from aoc import repres

with open("../data/day12.txt", "rt") as file:
	data = file.read().strip().split('\n')

part2 = True

regs = {'a' : 0, 'b' : 0, 'c' : 1 if part2 else 0, 'd' : 0}

ip = 0
while ip < len(data):
	d = data[ip]
	line = d.split(' ')
	if line[0] == "cpy":
		if line[1] in ['a', 'b', 'c', 'd']:
			v = regs[line[1]]
		else:
			v = int(line[1])
		regs[line[2]] = v
		ip += 1
	elif line[0] == "inc":
		regs[line[1]] += 1
		ip += 1
	elif line[0] == "dec":
		regs[line[1]] -= 1
		ip += 1
	else:
		assert line[0] == "jnz"
		if line[1] in ['a', 'b', 'c', 'd']:
			v = regs[line[1]]
		else:
			v = int(line[1])
		if v != 0:
			ip += int(line[2])
		else:
			ip += 1

repres(regs['a'], part2)
