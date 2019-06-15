"""
This file contains the BST data structure. It consist of 2 classes
1. Node
2. BST
"""

class Node:
	def __init__(self, key, left=None, right=None, parent=None):
		self.left=left
		self.right=right
		self.parent=parent
		self.key=key

	# def __repr__(self):
	# 	return str(self.key)

	# def __str__(self):
	# 	return str(self.key)


x = []
a = Node(10)
b = Node(20)
c = Node(30)
x.append(a)

x.append(b)

x.append(c)
# x.sort()
print(x)

# Insert Test