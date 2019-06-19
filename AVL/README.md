# Adelson-Velsky and Landis (AVL) Tree
An AVL Tree (AVL) is a Binary Search Tree (BST) which is self balancing. What this means that it will always ensure that for **EVERY** node, the height of its two subtree differs by at most 1. Everytime after an `insert` or `delete`, it will carry out **self-balancing** procedures, to ensure the above property (**AVL property**) holds. This ensures that the height of the tree is:

![equation](https://latex.codecogs.com/gif.latex?height%3DO%28%5Clog%20n%29)

## Update
when supplied a list of nodes which was touched during an insert or delete, we traverse through it and update the height of everything. Might insert fix/rebalancing inside instead of waiting till the end.

## Rotate Right/Left

1. If everything is present, cool, as per normal.
2. If there's no left subtree for x, we can just exit.
3. If x is the root, we need to update root too and when we update the left node's parent, make it none. since x got no parent too.
4. If left subtree got no right subtree that's OK, just attach nothing to x's left subtree.




