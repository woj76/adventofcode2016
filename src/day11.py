#!/snap/bin/pypy3

from aoc import repres
from collections import deque

'''
This surely can be optimized, part 2 takes ~3 minutes to solve.
'''

part2 = True

if part2:
	init_state = (0,[set(["EG", "EM", "DG", "DM", "SG", "SM", "PG", "PM"]), set(["RG", "RM", "CG", "CM", "TG"]), set(["TM"]), set()])
	chips = ["EM", "DM", "SM", "PM", "RM", "CM", "TM"]
	generators = ["EG", "DG", "SG", "PG", "RG", "CG", "TG"]
else:
	init_state = (0,[set(["SG", "SM", "PG", "PM"]), set(["RG", "RM", "CG", "CM", "TG"]), set(["TM"]), set()])
	chips = ["SM", "PM", "RM", "CM", "TM"]
	generators = ["SG", "PG", "RG", "CG", "TG"]

##Test data:
#init_state = (0, [set(["HM", "LM"]), set(["HG"]), set(["LG"]), set()])
#chips = ["HM", "LM"]
#generators = ["HG", "LG"]

def format_state(s):
	n, fs = s
	ret = str(n)
	for st in fs:
		ret += '|'
		ret += ','.join(sorted([x for x in st]))
	return ret

def final_state(s):
	n, fs = s
	return n == 3 and fs[3] == (set(chips) | set(generators))

def is_micorchip(i):
	return i[1] == 'M'

def is_generator(i):
	return i[1] == 'G'

def get_generator(i):
	return i[0] + 'G'

def valid_state(s):
	n, fs = s
	for items in fs:
		for i in items:
			if is_micorchip(i) and not get_generator(i) in items and [x for x in generators if x in items and x != get_generator(i)]:
				return False
	return True

def next_states(s):
	n, fs = s
	l = [x for x in fs[n]]
	to_move = [[e] for e in l]
	for x in range(len(l)):
		for y in range(x+1, len(l)):
			to_move.append([l[x],l[y]])
	ret = []
	for m in to_move:
		if n > 0:
			new_state = (n-1, [(fs[ni] - set(m)) if ni == n else (fs[ni] | set(m) if ni == n - 1 else fs[ni] | set()) for ni in range(4)])
			if valid_state(new_state):
				ret.append(new_state)
		if n < 3:
			new_state = (n+1, [(fs[ni] - set(m)) if ni == n else (fs[ni] | set(m) if ni == n + 1 else fs[ni] | set()) for ni in range(4)])
			if valid_state(new_state):
				ret.append(new_state)
	return ret

visited = {}
visited[format_state(init_state)] = 0

q = deque()
q.append((0,init_state))

r = None

while True:
	step, s = q.popleft()
	ns = next_states(s)
	if len([sx for sx in ns if final_state(sx)]) == 1:
		r = step + 1
		break

	for s1 in ns:
		t = format_state(s1)
		if t in visited:
			continue
		q.append((step+1, s1))
		visited[t] = step + 1

repres(r, part2)
