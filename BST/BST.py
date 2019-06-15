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

	def __repr__(self):
		return repr(self.key)

	def __str__(self):
		return str(self.key)

class BST:
	def __init__(self, root=None):
		self.root=root

	def insert(self, key, node=None):
		temp_node=node
		if node is None:
			temp_node=self.root
		if temp_node is None:
			self.root=Node(key=key)
		elif key<=temp_node.key:
			if temp_node.left is None:
				temp_node.left=Node(key=key, parent=temp_node)
			else:
				self.insert(key, temp_node.left)			
		elif key>temp_node.key:
			if temp_node.right is None:
				temp_node.right=Node(key=key, parent=temp_node)
			else:
				self.insert(key, temp_node.right)

	def get_min(self, node=None):
		current_node=node
		if current_node is None:
			current_node=self.root
		if current_node is None:
			return None
		if current_node.left is None:
			return current_node.key
		return self.get_min(current_node.left)

	def get_max(self, node=None):
		current_node=node
		if current_node is None:
			current_node=self.root
		if current_node is None:
			return None
		if current_node.right is None:
			return current_node.key
		return self.get_max(current_node.right)

	def find(self, key, node=None):
		temp_node=node
		if node is None:
			temp_node=self.root
		if self.root is None:
			return None
		if key == temp_node.key:
			return temp_node.key
		elif key<temp_node.key:
			if temp_node.left is None:
				return None
			return self.find(key, temp_node.left)
		elif key>temp_node.key:
			if temp_node.right is None:
				return None
			return self.find(key, temp_node.right)


	# def get_larger(self, node):
	# 	if node.right is not None:
	# 		return self.get_min(node.right)
	# 	while node.parent is not None:
	# 		if node.parent.right is node:
	# 			node = node.parent
	# 		else:
	# 			return node.parent
	# 	return node





# Node test 

bst = BST()
bst.insert(10)
bst.insert(100)
bst.insert(750)
bst.insert(75)
bst.insert(175)
print(bst.find(175))
print(bst.find(176))



# Insert Test