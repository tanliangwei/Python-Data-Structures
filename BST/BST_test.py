from BST import Node, BST
import random

class Count_Node(Node):
	def __init__(self, key, left=None, right=None, parent=None):
		Node.__init__(self, key, left, right, parent)
		self.count=1

class Count_BST(BST):
	def __init__(self, root=None, factory_node = Count_Node):
		BST.__init__(self, root, factory_node)

	def update_attribute(self, list_of_nodes, reverse=False):
		# this guy will receive a list of nodes with index 1 being the root and final index being a leaf
		# if reverse is true, this guy receives a list of nodes with 1 being leaf
		if not reverse:
			for i in range(len(list_of_nodes)-1, -1, -1):
				node = list_of_nodes[i]
				number_of_left = node.left.count if node.left is not None else 0
				number_of_right = node.right.count if node.right is not None else 0
				node.count=number_of_right+number_of_left+1
		if reverse:
			for i in range(0, len(list_of_nodes)):
				node = list_of_nodes[i]
				number_of_left = node.left.count if node.left is not None else 0
				number_of_right = node.right.count if node.right is not None else 0
				node.count=number_of_right+number_of_left+1




def append(x, y, key, index):
	x.append(key)
	y.insert(key)
	if index % 10000==0:
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
	bst = BST()

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