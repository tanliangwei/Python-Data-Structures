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

	def insert(self, key, node=None, list_of_nodes=[], update=True):
		temp_node=node
		if node is None:
			temp_node=self.root
		if temp_node is None:
			self.root=Node(key=key)
			temp_node=self.root
		list_of_nodes.append(temp_node)
		elif key<=temp_node.key:
			if temp_node.left is None:
				temp_node.left=Node(key=key, parent=temp_node)
				list_of_nodes.append(temp_node.left)
				if update:
					self.update_attribute(list_of_nodes)
			else:
				self.insert(key, temp_node.left, list_of_nodes, update)			
		elif key>temp_node.key:
			if temp_node.right is None:
				temp_node.right=Node(key=key, parent=temp_node)
				list_of_nodes.append(temp_node.right)
				if update:
					self.update_attribute(list_of_nodes)
			else:
				self.insert(key, temp_node.right, list_of_nodes, update)

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

	def get_larger(self, key, node=None, strict=True):
		temp_node=node
		if node is None:
			temp_node=self.root
		if self.root is None:
			return None
		select_node = self.find_node(key, temp_node)
		if select_node is None:
			return None
		if select_node.right is not None:
			min_node = self.get_min_node(select_node.right)
			if min_node.key>key:
				return min_node.key
			return self.get_larger(key, min_node)
		while select_node.parent is not None:
			if select_node.parent.right is select_node:
				select_node = select_node.parent
			else:
				if select_node.parent.key>key:
					return select_node.parent.key
				return self.get_larger(key, select_node.parent)
		return None

	def get_smaller(self, key, node=None, strict=True):
		temp_node=node
		if node is None:
			temp_node=self.root
		if self.root is None:
			return None
		select_node = self.find_node(key, temp_node)
		if select_node is None:
			return None
		if select_node.left is not None:
			max_node = self.get_max_node(select_node.left)
			if max_node.key<key:
				return max_node.key
			return self.get_smaller(key, max_node)
		while select_node.parent is not None:
			if select_node.parent.left is select_node:
				select_node = select_node.parent
			else:
				if select_node.parent.key<key:
					return select_node.parent.key
				return self.get_smaller(key, select_node.parent)
		return None

	def get_larger_than(self, key):
		if self.find(key) is not None:
			return self.get_larger(key)
		self.insert(key, update=False)
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
		self.insert(key, update=False)
		node = self.find_node(key)
		smaller = self.get_smaller(key)
		if node is node.parent.left:
			node.parent.left = None
			node.parent = None
		else:
			node.parent.right = None
			node.parent = None
		return smaller

	def delete(self, key):
		node = self.find_node(key)
		if node is None:
			return None
		if node.left is not None:
			current_node = node.left
			while current_node.right is not None:
				current_node = current_node.right
		elif node.right is not None:
			current_node = node.right
			while current_node.left is not None:
				current_node = current_node.left
		else:
			current_node = node
		temp = node.key
		node.key = current_node.key
		if current_node.parent.right is current_node:
			current_node.parent.right = current_node.left or current_node.right
			current_node.parent = None
		else:
			current_node.parent.left = current_node.right or current_node.left
			current_node.parent = None
		return temp

	def update_attribute(self, list_of_nodes):
		# this guy will receive a list of nodes with index 1 being the root and final index being a leaf
		pass





# test.
if __name__ == '__main__':
	bst = BST()
	bst.insert(10)
	bst.insert(15)
	bst.insert(100)
	bst.insert(750)
	bst.insert(75)
	bst.insert(175)
	bst.delete(175)
	print(bst.delete(76))
	print(bst.find(100))
	print(bst.get_smaller_than(10))
	print(bst.get_smaller_than(15))
	print(bst.get_smaller_than(750))
	print(bst.get_smaller(100))