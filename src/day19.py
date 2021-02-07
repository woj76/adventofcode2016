#!/snap/bin/pypy3

from aoc import repres

part2 = True

input = 3012210

class Node:
	def __init__(self, n):
		self.n = n
		self.v = 1
		self.next = self
	def append(self, n):
		nn = Node(n)
		after = self.next
		self.next = nn
		nn.next = after
		return nn

lst = Node(1)
for i in range(1,input):
	lst = lst.append(i+1)
lst = lst.next

steal_elf = lst
for _ in range((input // 2)-1 if part2 else 0):
	steal_elf = steal_elf.next

while input > 1:
	steal_elf.next = steal_elf.next.next
	if input % 2 == 1 or not part2:
		steal_elf = steal_elf.next
	lst = lst.next
	input -= 1

repres(lst.n, part2)
