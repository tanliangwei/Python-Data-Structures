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
The `update` function receives a `list_of_nodes` parameter which contains the list of updated nodes. Update will check and rebalance each node (subtree) starting from the leaf up to the root via `check_and_rebalance` while updating the height via `update_height` simultaneously after every check or rebalance. This is responsible for maintaining the *AVL Property* of the `AVL`  

## Rotate Right/Left

1. If everything is present, cool, as per normal.
2. If there's no left subtree for x, we can just exit.
3. If x is the root, we need to update root too and when we update the left node's parent, make it none. since x got no parent too.
4. If left subtree got no right subtree that's OK, just attach nothing to x's left subtree.




