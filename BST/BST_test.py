import BST

class 




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
	print(bst.delete(75))
	print(bst.find(100))
	print(bst.get_smaller_than(10))
	print(bst.get_smaller_than(15))
	print(bst.get_smaller_than(750))
	print(bst.get_smaller(100))