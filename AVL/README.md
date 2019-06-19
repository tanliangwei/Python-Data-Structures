# Adelson-Velsky and Landis (AVL) Tree
An `AVL` Tree (AVL) is a Binary Search Tree (BST) which is self balancing. What this means that it will always ensure that for **EVERY** node, the height of its two subtree differs by at most 1. Everytime after an `insert` or `delete`, it will carry out **self-balancing** procedures, to ensure the above property (**AVL property**) holds. This ensures that the height of the tree is:

![equation](https://latex.codecogs.com/gif.latex?height%3DO%28%5Clog%20n%29)

This ensures that `insert` and `delete` operations can be carried out in `O(height), height = O(logn)` time (*n is the number of elements*) in the worst case **INSTEAD** of `O(height), height = O(n)` time in the worst case in a badly balanced `BST`. The result is a `BST` with a much insertions and deletions which operates in **logarithmic time** in the worst case.

# AVL operations summary
An AVL is a BST and it contains the same operations as a BST. The difference is that it has a much better guranteed (worst case) time for most operations. `N` denotes the number of elements in the heap and `h` denotes the height of the tree (**longest path from the root to a leaf**).

|Operation|Description|Time Complexity|
|----------------|-------------------------------|-----------------------------|
`AVL()`|![equation](https://latex.codecogs.com/png.latex?O%281%29)|Constructor for `AVL`.
`insert(key)`|![equation](https://latex.codecogs.com/gif.latex?O%28%5Clog%20n%29)|Inserts key into the data structure while maintaining AVL property.
`find(key)`|![equation](https://latex.codecogs.com/gif.latex?O%28%5Clog%20n%29)| Finds and returns the specified key. Returns `None` if key is not found.
`get_max/min()`|![equation](https://latex.codecogs.com/gif.latex?O%28%5Clog%20n%29)|Returns the element with the largest/smallest key.
`get_larger/smaller(key)`|![equation](https://latex.codecogs.com/gif.latex?O%28%5Clog%20n%29)|Returns the first key which is **strictly** smaller/larger than the key specified. Returns `None` if there's nothing **strictly** smaller/larger or **if the key specified key is not in `AVL`**.
`get_larger/smaller_than(key)`|![equation](https://latex.codecogs.com/gif.latex?O%28%5Clog%20n%29)|Returns the first key which is **strictly** smaller/larger than the key specified. Returns `None` if there's nothing **strictly** smaller/larger.
`delete(key)`|![equation](https://latex.codecogs.com/gif.latex?O%28%5Clog%20n%29)|Returns and deletes the specified key. Returns `None` if specified key is not found in the `AVL`.

# Explanation of AVL operations
This `AVL` is created by extending the `BST` class and making changes to the `insert`, `delete` and `update` operations of the original `BST`.

## AVL Node Class
The implementing of an `AVL` also require an additional `AVL_node` Class. This class contains an additional `height` attribute which is used in balancing the `AVL`

## Insert
The `insert` operation of an `AVL` calls the standard `insert` operation of the `BST` but calls a **overriden** `update` function which rebalances the trees and updates the `height` of the nodes.

## Delete
The `delete` operation of an `AVL` calls the standard `delete` operation of the `BST` but calls an **overriden** `update` function which rebalances the trees and updates the `height` of the nodes.

## Update
The `update` function receives a `list_of_nodes` parameter which contains the list of updated nodes. Update will check and rebalance each node (subtree) starting from the leaf up to the root via `check_and_rebalance` while updating the height via `update_height` simultaneously after every check or rebalance. This is responsible for maintaining the *AVL Property* of the `AVL`.

## Check and Rebalance
This function corrects a **SINGLE** violation of *AVL Property* at a certain node. *AVL Property* of the subtrees of the node must **NOT** be violated. This function checks and rebalance the imbalances of the subtree at the node. The result is a balanced subtree fulfilling the *AVL Property* There are 4 cases to consider in this function.

1. The violating node is **right heavy**. Its right child fulfills the *AVL Property but is **right heavy or balanced**. We call this **right-right heavy**. To remedy this, we call `rotate_left` on the node itself. 
2. The violating node is **right heavy**. Its right child fulfills the *AVL Property but is **left heavy**. We call this **right-left heavy**. To remedy this, we call `rotate_right` on the right child, followed by `rotate_left` on the node itself.
3. For **left-left heavy** violations, we call `rotate_right` on the node itself. 
4. For **left-right heavy** violations, we call `rotate_left` on the left child, followed by `rotate_right` on the node itself.

> **Right heavy** is, a property used to describe nodes in which their right child has a greater `height` than their left child. Vice versa for **left heavy**. **Balance** suggest equal `height` for both right and left children.

## Rotate Right/Left

`rotate_left` involves the movements of the node, it's right child and their subtrees. There is also a change of child for the parent of the node to the right child. Vice versa for left. The following describes the operation of `rotate_left`. Vice versa for `rotate_right`. In the end, we update the `height`s of both nodes.

1. We make the right child the parent of the node.
2. We connect the left subtree of the right child to the right child of the node.
3. We make the node the left child of the right child. 
4. We make the original parent of the node the parent of the right child.
5. Update the `height`s of both nodes via `update_height`.

> **Implementational Details**: The following pointers have to be adjusted. The *left/right pointer of the parent* of the node. The *parent pointers* of the node and the right child. The *parent pointer* of the left subtree of the right child. The *right pointer* of the node and the *left pointer* of right child. **A total of 6 pointers in total**.


# TO-DO

1. Insert some visuals for the rebalancing operations
2. Maybe try to implemement a range finder in this file.




