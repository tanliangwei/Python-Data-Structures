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



# Node test 

# Insert Test