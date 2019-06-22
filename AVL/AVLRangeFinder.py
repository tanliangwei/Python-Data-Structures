from AVL import AVL, AVLNode

class AVLRangeFinderNode(AVLNode):
	def __init__(self, key, parent=None, left=None, right=None, height=0, count=1):
		AVLNode.__init__(self, key=key, parent=parent, left=left, right=right, height=height)
		self.count=count

class AVLRangeFinder(AVL):
	def __init__(self, root=None, node_type=AVL_count_node):
		AVL.__init__(self, root, node_type)

	def get_count(self, node):
		if node is None:
			return 0
		return node.count

	def update_count(self, node):
		if node is None:
			return
		node.count = self.get_count(node.left) + self.get_count(node.right) + 1

	def rotate_left(self, node):
		AVL.rotate_left(self, node)
		self.update_count(node)
		self.update_count(node.right)

	def rotate_right(self, node):
		AVL.rotate_right(self, node)
		self.update_count(node)
		self.update_count(node.left)

	def rank(self, key):
		count = 0
		current_node =self.root
		while current_node is not None:
			if key >= current_node.key:
				count += self.get_count(current_node.left) + 1
				current_node = current_node.right
				continue
			if key < current_node.key:
				current_node = current_node.left
				continue
		return count

	def range_count(self, l, r):
		if self.find(l) is not None:
			return self.rank(r) - self.rank(l) + 1
		return self.rank(r) - self.rank(l)

	def list(self, l, r):
		node = self.lca(l, r)
		return_list = self.range_list(l, r, node)
		return return_list

	def lca(self, l, r):
		current_node = self.root
		while current_node is not None:
			if l<=current_node.key and current_node.key<=r:
				return current_node
			elif l<=current_node.key:
				current_node = current_node.left
			else:
				current_node = current_node.right
		return current_node

	def range_list(self, l, r, node, return_list=None):
		if return_list is None:
			return_list=[]
		if node is None:
			return return_list
		if node.key>=l and node.key<=r:
			return_list.append(node.key)
		if node.key>l:
			self.range_list(l, r, node.left, return_list)
		if node.key<r:
			self.range_list(l, r, node.right, return_list)
		return return_list





