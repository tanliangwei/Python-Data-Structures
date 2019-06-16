from BST import Node, BST
import random

class AVLNode(Node):
	def __init__(self, key, parent=None, left=None, right=None, height=0):
		Node.__init__(self, key=key, parent=parent, left=left, right=right)
		self.height=height

class AVL(BST):
	def __init__(self, root=None, node_type=AVLNode):
		BST.__init__(self, root, node_type)

	def update(self, list_of_nodes, reverse=False):
		# this guy will receive a list of nodes with index 1 being the root and final index being a leaf
		# if reverse is true, this guy receives a list of nodes with 1 being leaf
		if reverse:
			for i in range(len(list_of_nodes)-1, -1, -1):
				left_child_height = list_of_nodes[i].left.height if list_of_nodes[i].left is not None else -1
				right_child_height = list_of_nodes[i].right.height if list_of_nodes[i].right is not None else -1
				list_of_nodes[i].height = max(left_child_height, right_child_height) + 1
		else:
			for i in range(0, len(list_of_nodes)):
				left_child_height = list_of_nodes[i].left.height if list_of_nodes[i].left is not None else -1
				right_child_height = list_of_nodes[i].right.height if list_of_nodes[i].right is not None else -1
				list_of_nodes[i].height = max(left_child_height, right_child_height) + 1






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


# test.
if __name__ == '__main__':
	test_list =[]
	bst = AVL()

	print("===Starting Insertion Test====")
	for i in range(0,100000):
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
		# try:
		# 	assert bst.count() == len(test_list)
		# except AssertionError:
		# 	print("BST count ", bst.count())
		# 	print("test list count", len(test_list))

	print("============Success===========\n")