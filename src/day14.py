#!/usr/bin/python3
# Weirdly, hashlib seems to be way faster with the original Python interpreter

import hashlib
from aoc import repres

input = 'zpqevtbw'

part2 = True

def compute_hash(s):
	for _ in range(2017 if part2 else 1):
		s = hashlib.md5(s.encode()).hexdigest()
	return s

hashes = []
for index in range(1001):
	hashes.append(compute_hash(input + str(index)))

num_keys = 0
index = 0

while num_keys < 64:
	h = hashes[0]
	hashes = hashes[1:]
	triple_char = None
	for j in range(len(h)-2):
		if h[j] == h[j+1] == h[j+2]:
			triple_char = h[j]
			break
	if triple_char != None:
		fivelet = triple_char * 5
		for oh in hashes:
			if fivelet in oh:
				num_keys += 1
				break
	hashes.append(compute_hash(input + str(index+1001)))
	index += 1

repres(index-1, part2)
