#!/snap/bin/pypy3

from aoc import repres

with open("../data/day21.txt", "rt") as file:
	data = file.read().strip().split('\n')

part2 = True

sl = list("fbgdceah" if part2 else "abcdefgh")

for idx in range(len(data)):
	d = data[len(data) - idx - 1 if part2 else idx].split(' ')
	if d[0] == "swap":
		if d[1] == "position":
			p1,p2 = int(d[2]), int(d[5])
		elif d[1] == "letter":
			p1,p2 = sl.index(d[2]), sl.index(d[5])
		sl[p1], sl[p2] = sl[p2], sl[p1]
	elif d[0] == "rotate":
		if d[1] == "based":
			i = sl.index(d[6])
			if part2:
				i = [-9, -1, -6, -2, -7, -3, -8, -4][i]
			else:
				i = i + (2 if i >= 4 else 1)
		elif d[1] == "left" or d[1] == "right":
			i = int(d[2])
			if (not part2 and d[1] == "left") or (part2 and d[1] == "right"):
				i = -i
		sl = [sl[(x-i) % len(sl)] for x in range(len(sl))]
	elif d[0] == "reverse":
		p1, p2 = int(d[2]), int(d[4])
		sl = [sl[p2 - (x - p1) if p1 <= x <= p2 else x] for x in range(len(sl))]
	elif d[0] == "move":
		p1, p2 = int(d[2]), int(d[5])
		if part2:
			p1, p2 = p2, p1
		l = sl[p1]
		del sl[p1]
		sl.insert(p2, l)

repres("".join(sl), part2)
