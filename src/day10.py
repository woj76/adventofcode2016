#!/snap/bin/pypy3

from aoc import repres

file = open("../data/day10.txt", "rt")
data = file.read().strip().split('\n')
file.close()

part2 = True

bots = {}
outputs = {}
rels = {}

for d in data:
	l = d.split(' ')
	if l[0] == "value":
		b = int(l[5])
		v = int(l[1])
		if not b in bots.keys():
			bots[b] = []
		bots[b].append(v)
		bots[b].sort()
	else:
		b = int(l[1])
		t1 = 'b' if l[5] == "bot" else 'o'
		t2 = 'b' if l[10] == "bot" else 'o'
		i1 = int(l[6])
		i2 = int(l[11])
		rels[b] = (t1, i1, t2, i2)

changed = True
r = 0

while changed:
	changed = False
	for b in list(bots.keys()):
		vs = bots[b]
		if not part2 and vs == [17, 61]:
			r = b
			changed = False
			break
		if len(vs) != 2:
			continue
		changed = True
		t1, i1, t2, i2 = rels[b]
		[v1, v2] = vs
		if t1 == 'o':
			outputs[i1] = v1
		else:
			if not i1 in bots.keys():
				bots[i1] = []
			bots[i1].append(v1)
			bots[i1].sort()
		if t2 == 'o':
			outputs[i2] = v2
		else:
			if not i2 in bots.keys():
				bots[i2] = []
			bots[i2].append(v2)
			bots[i2].sort()
		bots[b] = []

if part2:
	r = outputs[0] * outputs[1] * outputs[2]

repres(r, part2)
