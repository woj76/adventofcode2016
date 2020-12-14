#!/usr/bin/python3

from aoc import repres

file = open("../data/day07.txt", "rt")
data = [x + '\n' for x in file.read().strip().split('\n')]
file.close()

part2 = True
r  = 0

def abba(str):
	for i in range(len(str)-3):
		if str[i] != str[i+1] and str[i] == str[i+3] and str[i+1] == str[i+2]:
			return True
	return False


for d in data:
	s = ""
	strings_in = []
	strings_out = []
	for c in d:
		if c == '[' or c == '\n':
			strings_out.append(s)
			s = ""
		elif c == ']':
			strings_in.append(s)
			s = ""
		else:
			s += c			
	if part2:
		babs = []
		for s in strings_out:
			for i in range(len(s) - 2):
				aba = list(s[i:i+3])
				if aba[0] != aba[1] and aba[0] == aba[2]:
					babs.append(aba[1]+aba[0]+aba[1])
		if len([True for x in babs for y in strings_in if x in y]) > 0:
			r += 1
	else:
		abba_out = False
		abba_in = False
		for s in strings_out:
			abba_out = abba_out or abba(s)
		for s in strings_in:
			abba_in = abba_in or abba(s)
		if abba_out and not abba_in:
			r += 1

repres(r, part2)

