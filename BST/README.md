# Binary Search Tree (BST)

A Binary Search Tree (BST) is a data structure which maintains a set of elements in a way such that the it is **easy and efficient to find an element** given its key. To facilitate this, the BST has a property in which for every node, **all the nodes from the left subtree have keys which are smaller than the key of the node** while **all nodes from the right subtree has keys which are larger than the key of the node.** The elements being maintained must be also be **sortable** and **orderable**.

# BST operations summary

The following table contains the operatations frequently used in a BST data structure. `N` denotes the number of elements in the heap and `h` denotes the height of the tree (**longest path from the root to a leaf**).

|Operation|Description|Time Complexity|
|----------------|-------------------------------|-----------------------------|
`BST()`|![equation](https://latex.codecogs.com/png.latex?O%281%29)|Constructor for BST.
`insert(key)`|![equation](https://latex.codecogs.com/gif.latex?O%28%5Clog%20h%29)|Inserts key into the data structure while maintaining BST property.
`find(key)`|![equation](https://latex.codecogs.com/gif.latex?O%28%5Clog%20h%29)| Finds and returns the specified key. Returns `None` if key is not found.
`get_max/min()`|![equation](https://latex.codecogs.com/gif.latex?O%28%5Clog%20h%29)|Returns the element with the largest/smallest key.
`get_larger/smaller(key)`|![equation](https://latex.codecogs.com/gif.latex?O%28%5Clog%20h%29)|Returns the first key which is **strictly** smaller/larger than the key specified. Returns `None` if there's nothing **strictly** smaller/larger or **if the key specified key is not in BST**.
`get_larger/smaller_than(key)`|![equation](https://latex.codecogs.com/gif.latex?O%28%5Clog%20h%29)|Returns the first key which is **strictly** smaller/larger than the key specified. Returns `None` if there's nothing **strictly** smaller/larger.
`delete(key)`|![equation](https://latex.codecogs.com/gif.latex?O%28%5Clog%20h%29)|Returns and deletes the specified key. Returns `None` if specified key is not found in the BST.
`update(list_of_nodes)`|![equation](https://latex.codecogs.com/gif.latex?O%28%5Clog%20h%29)|A function designed for developers to override when they extend on this BST class. Function is called whenever `insert` and `delete` is called. `list_of_nodes` include a list of nodes which are touched during the insertion or deletion. 
> *It is important to note that even though the Node class exist, the ***user is not expected to touch that class or any object from that class at all***. The interface of all functions of the BST should only involve ***keys***. To use the BST with non-primitive objects, users will need to ***implement their own comparables***.*

# Explanation of BST operations
## Insert

This implementation of *Insert* takes in a **key as parameter**. There is an optional argument of target node which is by default, the root node. There are a total of three possible cases or scenarios in Insert.

1. **The root is empty**. In this case, we replace the root of the BST with a node intialized with the key.
2. **The key is smaller or equal to the key of the target node.** In this case, we check if the left child of the node is empty. If it is, we insert it there, else, we call Insert of the left child of the node.
3. **The key is larger than the key of the target node.** In this case, we check if the right child of the node is empty. If it is, we insert it there, else, we call Insert of the right child of the node.

## Find
The find operation traverses down the BST in binary search fashion and returns the specified key upon finding the key. It returns the first instance of the key found. 

1. The target node starts at the root. 
2. If the key is **smaller** than the target node key, we carry on the search on the **left subtree** of the target node.
3. If the key is **larger** than the target node key, we carry on the search on the **right subtree** of the target node.
4. If **there's no more subtrees** or if the **key equals to the key of the target node**, we return the `None` and the key respectively.

## Get Min/Max
Get min finds the **minimum**/**maximum** key in the BST and returns the key.

1. In Get Min, the algorithms keeps **shifting towards the left child** until it can no longer shift left. The key it is pointing to at that point will be the minimum key.
2. In Get Max, the algorithms keeps **shifting towards the right child** till it can no longer shift right.

## Get Larger/Smaller
Returns the first key which is **strictly** larger/smaller than the specified key. If the specified key is not in the BST, `None` is returned.

1. If the **right subtree** (left for smaller) **exist**, **we get the minimum(maximum) key of the right(left) subtree**. This key is definitely larger(smaller) than the specified key and smaller(larger) than any of the key from its parent and it's other subtrees if it branched from the left(right).
2. If the **right subtree** (left) **does not exist**, we find the **first ancestor or parent** in which it is a **left (right) child of**.
3. If **none of this exist**, there is no key larger (smaller) than specified key. 


## Get Larger/Smaller Than
Same as above but would not return `None` even if the key is not found. It will assume that a node exist with that key and find the next larger/smaller key in BST. It does this through the following steps.

1. It **searches for the key to see if it exist**. If it does, follow `get_larger/smaller()`. If not, proceed to step 2.
2. It **inserts** a node with specified key and carry out `get_larger/smaller()` on the newly created node.
3. It **deletes** the newly created node and **returns** the larger/smaller key found.

## Delete
It finds, deletes and returns the specified key. If the key does not exist in the BST, it returns `None`. 

1. If a **right subtree exist**, get the minimum key there, swap it with the specified key and delete the minimum element.
2. Else, if  **a left subtree exist**, we can either get the maximum key of that subtree to **replace** the node to be deleted or we can simply **replace** the key to be deleted with the root of the left subtree.
3. Else, since there is **no children**, simply delete the key.

>Remember to handle edge case for deletion of root.

## Update
The `update` function is designed for developers to override, if necessary, when extending the `BST` class. It does nothing in `BST`. The input to this function is a list of nodes, `list_of_nodes` which are traversed during an `insert` or `delete` operation. This function makes it easy for users to alter or write to any special attribute in the node they created. An example use case will be in writing the `AVL`.

```python
def update(self, list_of_nodes=[], reverse=False):
	# reverse means that the last node is the leaf and first node, the root, vice versa.
	for node in list_of_nodes:
		update_height(node)	
```


# Implementational Notes
## Mutable Default Values as an Argument
In the `insert(key)` and `delete(key)` functions, an argument, `list_of_node`  is assigned a default value of an empty list when it is not assigned. And the desired effect is for it to reinitialize an empty list whenever `insert` or `delete` is called. A snippet of the code is shown below

```python
def insert(self, key, list_of_nodes=[], update=True):
	# contains code regarding appending to the list as well as 
	# passing down of this list into insert functions (recursively).
```
The above code will **NOT** achieve the desired effect. The `list_of_nodes` referenced in all insert functions will be referring to the **SAME LIST** and no emptying or reinitializing of the list will happen. List will get infinitely longer than what we expect. To resolve it, we look at the code snippet below.
 
```python
def insert(self, key, list_of_nodes=None, update=True):
	if list_of_nodes is None:
		list_of_nodes = []
	# continue with any code inserted previously.
```
In the above code snippet, we introduce a **Sentinel** value of None to denote the empty list, and then, manually reinitialize the list when necessary. The above achieves our desired effect.

# To-Do
1. Implement a sort or, in-order, pre-order and post-order traversal
2. Visualization tool for the BST
3. Arg parser to make package more professional