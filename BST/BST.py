"""
This file contains the BST data structure. It consist of 2 classes
1. Node
2. BST
"""

class Node:
	def __init__(self, left_child=None, right_child=None, parent=None, key=None):
		self.left_child=left_child
		self.right_child=right_child
		self.parent=parent
		self.key=key


node =Node()