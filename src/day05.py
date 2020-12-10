#!/usr/bin/python3

import hashlib
from aoc import repres

input = 'wtnhxymk'

part2 = True

r = 1
passwd = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
i = 0
while passwd.count(' ') > 0:
	hash = hashlib.md5((input + str(r)).encode())
	hashstr = hash.hexdigest()
	if hashstr[:5] == "00000":
		c = hashstr[5]
		if part2 and c in "01234567":
			i = int(c)
			if passwd[i] == ' ':
				passwd[i] = hashstr[6]
		elif not part2:		
			passwd[i] = c
			i += 1
	r += 1
  
repres("".join(passwd), part2)
