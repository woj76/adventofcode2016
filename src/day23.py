#!/snap/bin/pypy3

from aoc import repres

with open("../data/day23.txt", "rt") as file:
	data = file.read().strip().split('\n')

part2 = True

regs = {'a' : 12 if part2 else 7, 'b' : 0, 'c' : 0, 'd' : 0}

ip = 0
while ip < len(data):
	d = data[ip]
	line = d.split(' ')
	if line[0] == "cpy":
		if line[1] in regs:
			v = regs[line[1]]
		else:
			v = int(line[1])
		if line[2] in regs:
			regs[line[2]] = v
		ip += 1
	elif line[0] == "inc":
		if line[1] in regs:
			regs[line[1]] += 1
		ip += 1
	elif line[0] == "dec":
		if line[1] in regs:
			regs[line[1]] -= 1
		ip += 1
	elif line[0] == "jnz":
		if line[1] in regs:
			v = regs[line[1]]
		else:
			v = int(line[1])
		if v != 0:
			if line[2] in regs:
				ip += regs[line[2]]
			else:
				ip += int(line[2])
		else:
			ip += 1
	else:
		assert line[0] == "tgl"
		v = ip
		if line[1] in regs:
			v += regs[line[1]]
		else:
			v += int(line[1])
		if 0 <= v < len(data):
			line = data[v]
			ins = line[:3]
			args = line[3:]
			if ins == "inc":
				line = "dec" + args
			elif ins == "dec" or ins == "tgl":
				line = "inc" + args
			elif ins == "jnz":
				line = "cpy" + args
			else:
				line = "jnz" + args
			data[v] = line
		ip += 1

repres(regs['a'], part2)
