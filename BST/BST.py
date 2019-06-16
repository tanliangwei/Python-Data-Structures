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

	def get_min(self):
		node = self.get_min_node()
		if node is None:
			return None
		return node.key
	
	def get_min_node(self, node=None):
		current_node=node
		if current_node is None:
			current_node=self.root
		if current_node is None:
			return None
		if current_node.left is None:
			return current_node
		return self.get_min_node(current_node.left)

	def get_max(self):
		node = self.get_max_node()
		if node is None:
			return None
		return node.key

	def get_max_node(self, node=None):
		current_node=node
		if current_node is None:
			current_node=self.root
		if current_node is None:
			return None
		if current_node.right is None:
			return current_node
		return self.get_max_node(current_node.right)

	def find(self, key):
		node = self.find_node(key)
		if node is None:
			return None
		return node.key

	def find_node(self, key, node=None):
		temp_node=node
		if node is None:
			temp_node=self.root
		if self.root is None:
			return None
		if key == temp_node.key:
			return temp_node
		elif key<temp_node.key:
			if temp_node.left is None:
				return None
			return self.find_node(key, temp_node.left)
		elif key>temp_node.key:
			if temp_node.right is None:
				return None
			return self.find_node(key, temp_node.right)

	def get_larger(self, key):
		node = self.find_node(key)
		if node is None:
			return None
		if node.right is not None:
			return self.get_min_node(node.right).key
		while node.parent is not None:
			if node.parent.right is node:
				node = node.parent
			else:
				return node.parent
		return None

	def get_smaller(self, key):
		node = self.find_node(key)
		if node is None:
			return None
		if node.left is not None:
			return self.get_max_node(node.left).key
		while node.parent is not None:
			if node.parent.left is node:
				node = node.parent
			else:
				return node.parent
		return None

	def get_larger_than(self, key):
		if self.find(key) is not None:
			return self.get_larger(key)
		self.insert(key)
		node = self.find_node(key)
		larger = self.get_larger(key)
		if node is node.parent.left:
			node.parent.left = None
			node.parent = None
		else:
			node.parent.right = None
			node.parent = None
		return larger

	def get_smaller_than(self, key):
		if self.find(key) is not None:
			return self.get_smaller(key)
		self.insert(key)
		node = self.find_node(key)
		smaller = self.get_smaller(key)
		if node is node.parent.left:
			node.parent.left = None
			node.parent = None
		else:
			node.parent.right = None
			node.parent = None
		return smaller




# Node test 

bst = BST()
bst.insert(10)
bst.insert(100)
bst.insert(750)
bst.insert(75)
bst.insert(175)
print(bst.find(175))
print(bst.find(176))
print(bst.get_smaller_than(10))
print(bst.get_smaller_than(15))
print(bst.find(15))
print(bst.get_smaller_than(750))
print(bst.get_smaller_than(100))



# Insert Test