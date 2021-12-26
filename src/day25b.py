#!/snap/bin/pypy3

from aoc import repres

with open("../data/day25.txt", "rt") as file:
	data = file.read().strip().split('\n')

part2 = True
r = 0

def run(a):
	regs = {'a' : a, 'b' : 0, 'c' : 0, 'd' : 0}
	ip = 0
	output = ""
	steps = 0
	while steps < 30:
		d = data[ip]
		line = d.split(' ')
		if line[0] == "cpy":
			if line[1] in ['a', 'b', 'c', 'd']:
				v = regs[line[1]]
			else:
				v = int(line[1])
			regs[line[2]] = v
			ip += 1
		elif line[0] == "out":
			out = regs[line[1]]
			output += str(out)
			steps += 1
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
	if output == "01" * 15:
		return a
	return None

a = 0
while True:
	r = run(a)
	if r != None:
		break
	a += 1

repres(r, part2)
