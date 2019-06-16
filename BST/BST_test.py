from BST import Node, BST

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






# test.
if __name__ == '__main__':
	count_bst = Count_BST()
	print(count_bst.Node)
	count_bst = BST()
	count_bst.insert(10)
	count_bst.insert(15)
	count_bst.insert(100)
	count_bst.insert(750)
	count_bst.insert(75)
	count_bst.insert(175)
	# count_bst.delete(175)
	print(count_bst.delete(75))
	print(count_bst.find(100))
	print(count_bst.get_smaller_than(10))
	print(count_bst.get_smaller_than(15))
	print(count_bst.get_smaller_than(750))
	print(count_bst.get_smaller(100))