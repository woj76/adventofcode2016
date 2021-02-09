#!/snap/bin/pypy3

from aoc import repres

with open("../data/day20.txt", "rt") as file:
	data = []
	for x in file.read().strip().split('\n'):
		data.append(tuple([int(y) for y in x.split('-')]))

part2 = True

lowest = 0
total = 4294967296

for _ in range(5):
	for i in range(len(data)):
		r1, r2 = data[i]
		for j in range(i+1, len(data)):
			s1, s2 = data[j]
			if s1 <= r1 and r1 <= s2 <= r2:
				data[j] = (s1, r1-1)
			elif r1 <= s1 <= r2 and s2 >= r2:
				data[j] = (r2+1, s2)

for i in range(len(data)):
	if data[i] == None:
		continue
	r1, r2 = data[i]
	to_remove = []
	for j in range(i+1, len(data)):
		if data[j] == None:
			continue
		s1, s2 = data[j]
		if r1 <= s1 and s2 <= r2:
			to_remove.append(j)
		if s1 <= r1 and r2 <= s2:
			to_remove.append(i)
	for j in to_remove:
		data[j] = None

if part2:
	for r1,r2 in [x for x in data if x != None]:
		total -= (r2-r1+1)
	r = total
else:
	for _ in range(5):
		for r1,r2 in [x for x in data if x != None]:
			if r1 <= lowest and r2 > lowest:
				lowest = r2 + 1
	r = lowest

repres(r, part2)
