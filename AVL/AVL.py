from BST import Node, BST
import random
import cProfile

class AVLNode(Node):
	def __init__(self, key, parent=None, left=None, right=None, height=0):
		Node.__init__(self, key=key, parent=parent, left=left, right=right)
		self.height=height

class AVL(BST):
	def __init__(self, root=None, node_type=AVLNode):
		BST.__init__(self, root, node_type)


	def update_height(self, node):
		node.height = max(self.get_node_height(node.left),self.get_node_height(node.right)) + 1

	def get_node_height(self, node):
		if node is None:
			return -1
		return node.height

	def update(self, list_of_nodes, reverse=False):
		if not reverse:
			for i in range(len(list_of_nodes)-1, -1, -1):
				self.update_height(list_of_nodes[i])
				self.check_and_rebalance(list_of_nodes[i])
		else:
			for i in range(0, len(list_of_nodes)):
				self.update_height(list_of_nodes[i])
				self.check_and_rebalance(list_of_nodes[i])

	def rotate_right(self, node):
		if node.left is None:
			return
		node_left = node.left
		if node is self.root:
			self.root = node_left
			node_left.parent = None
		else:
			node_left.parent = node.parent
			if node.parent.right is node:
				node.parent.right = node_left
			else:
				node.parent.left = node_left
		node.left = node_left.right
		if node_left.right is not None:
			node_left.right.parent = node
		node_left.right = node
		node.parent = node_left
		self.update_height(node)
		self.update_height(node_left)

	def rotate_left(self, node):
		if node.right is None:
			return
		node_right = node.right
		if node is self.root:
			self.root = node_right
			node_right.parent = None
		else:
			node_right.parent = node.parent
			if node.parent.right is node:
				node.parent.right = node_right
			else:
				node.parent.left = node_right
		# step 2 
		node.right = node_right.left
		if node_right.left is not None:
			node_right.left.parent = node
		# step 3
		node_right.left = node
		node.parent = node_right
		self.update_height(node)
		self.update_height(node_right)

	def check_and_rebalance(self, node):
		# first we check if it is balanced
		left_child_height = node.left.height if node.left is not None else -1
		right_child_height = node.right.height if node.right is not None else -1
		if abs(left_child_height - right_child_height)<=1:
			return
		if right_child_height>left_child_height:
			# right heavy
			right_child = node.right
			if right_child is None:
				return
			right_child_right_child_height = right_child.right.height if right_child.right is not None else -1
			right_child_left_child_height = right_child.left.height if right_child.left is not None else -1
			if (right_child_right_child_height - right_child_left_child_height) >=0 :
				# right - right heavy
				self.rotate_left(node)
				return
			else:
				self.rotate_right(right_child)
				self.rotate_left(node)
				return 
		else:
			# left heavy
			left_child = node.left
			if left_child is None:
				return
			left_child_right_child_height = left_child.right.height if left_child.right is not None else -1
			left_child_left_child_height = left_child.left.height if left_child.left is not None else -1
			if (left_child_left_child_height - left_child_right_child_height) >=0 :
				# left - left heavy
				self.rotate_right(node)
				return
			else:
				self.rotate_left(left_child)
				self.rotate_right(node)
				return

	def check_avl(self):
		if self.root is None:
			return True
		return self.check_avl_2(self.root.left) and self.check_avl_2(self.root.right) and (max(self.get_node_height(self.root.left),self.get_node_height(self.root.right))+1)==self.get_node_height(self.root)


	def check_avl_2(self, node):
		if node is None:
			return True
		return self.check_avl_2(node.left) and self.check_avl_2(node.right) and (max(self.get_node_height(node.left),self.get_node_height(node.right))+1)==self.get_node_height(node)











if __name__ == '__main__': 
	def append(x, y, key, index):
		x.append(key)
		y.insert(key)
		if index % 1000==0:
			print("......")

	def get_next_larger_test(x, y, key, index):
		larger_key = None
		min_diff = None
		for i in x:
			diff = i-key
			if diff>0 and (min_diff is None or diff<min_diff):
				min_diff=diff
				larger_key=i
		assert larger_key==y.get_larger_than(key)
		if index % 500==0:
			print("......")

	def get_next_smaller_test(x, y, key, index):
		smaller_key = None
		min_diff = None
		for i in x:
			diff = key-i
			if diff>0 and (min_diff is None or diff<min_diff):
				min_diff=diff
				smaller_key=i
		assert smaller_key==y.get_smaller_than(key)
		if index % 500==0:
			print("......")

	def delete_on_list(x, key):
		try:
			x.remove(key)
			return key
		except ValueError:
			return None

	def find_on_list(x, key):
		try:
			ind = x.index(key)
			return x[ind]
		except ValueError:
			return None

	def delete_test(x, y, key, index):
		assert delete_on_list(x, key) == y.delete(key)
		try:
			assert find_on_list(x, key) == y.find(key)
		except AssertionError:
			print(find_on_list(x, key))
			print(y.find(key))
			print(key)
		if index % 10000==0:
			print("......")

	def slow_function():
	    avl = AVL()
	    for i in range(0,100000):
	        if i % 10000==0:
	            print("......")
	        avl.insert(random.randint(1,10001))
	    print(avl.check_avl())

	# import cProfile
	# cProfile.run('slow_function()')
	test_list =[]
	bst = AVL()

	print("===Starting Insertion Test====")
	for i in range(0,10000):
		append(test_list, bst, random.randint(1,10001), i)

	for i in test_list:
		assert bst.find(i)==i

	print("============Success==========\n")

	print("==Starting Get Max/Min Test===\n")
	assert max(test_list) == bst.get_max()
	assert min(test_list) == bst.get_min()
	print("============Success===========\n")

	print("==Starting Get Larger Than Test==")
	for i in range(0,150):
		get_next_larger_test(test_list, bst, random.randint(1,1000001), i)
	print("==Starting Get Smaller Than Test==")
	for i in range(0,150):
		get_next_smaller_test(test_list, bst, random.randint(1,1000001), i)
	print("============Success===========\n")

	print("=====Starting Delete Test========")
	for i in range(0,100000):
		delete_test(test_list, bst, random.randint(1,10001), i)
		try:
			assert bst.count() == len(test_list)
		except AssertionError:
			print("BST count ", bst.count())
			print("test list count", len(test_list))


	print("============Success===========\n")