from countsort import countsort
from radixsort import radixsort

class node:
	def __init__(self, num):
		self.num = num
	def __lt__(self, other):
		return self.num < other
	def __gt__(self, other):
		return self.num > other
	def __eq__(self, other):
		return self.num == other
	def __le__(self, other):
		return self.num <= other
	def __ge__(self, other):
		return self.num >= other
	def __ne__(self, other):
		return self.num != other


def key_func(obj):
	return obj.num

q = node(1)
w = node(1)
e = node(2)
r = node(2)
t = node(3)
y = node(3)
u = node(-10)
i = node(100)
o = node(7)

temp_list = [y,t,r,e,w,q,u,i,o]
countsort(temp_list, key_function=key_func, reverse=False)
print(list(map(key_func, temp_list)))


print(q>w)
print(q>=w)
print(q<y)
print(q==1)
print(y < 2)
print(y > q)
