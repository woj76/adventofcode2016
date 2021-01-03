#!/snap/bin/pypy3

from aoc import repres

with open("../data/day15.txt", "rt") as file:
	data = [[int(y[:-1] if i == 11 else y) for (i,y) in enumerate(x.split(' ')) if i in [3, 11]] for x in file.read().strip().split('\n')]

part2 = True

if part2:
	data.append((11,0))

t = 0
while True:
	slots = []
	for (i,d) in enumerate(data):
		slots.append((d[1]+t+i+1) % d[0])
	if sum(slots) == 0:
		break
	t += 1

repres(t, part2)
