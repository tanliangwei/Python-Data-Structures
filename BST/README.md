# Binary Search Tree (BST)

A Binary Search Tree (BST) is a data structure which maintains a set of elements in a way such that the it is **easy and efficient to find an element** given its key. To facilitate this, the BST has a property in which for every node, **all the nodes from the left subtree have keys which are smaller than the key of the node** while **all nodes from the right subtree has keys which are larger than the key of the node.** The elements being maintained must be also be **sortable** and **orderable**.

# BST operations summary TO-DO

The following table contains the operatations frequently used in a Heap data structure. N denotes the number of elements in the heap.

|Operation|Description|Time Complexity|
|----------------|-------------------------------|-----------------------------|
`BST()`|![equation](https://latex.codecogs.com/png.latex?O%281%29)|Constructor for BST.
`insert(key)`|![equation](https://latex.codecogs.com/png.latex?O%28%5Clog%20n%20%29)|Inserts key into the data structure while maintaining BST property.
`find(key)`|![equation](https://latex.codecogs.com/png.latex?O%28%5Clog%20n%20%29)| Finds and returns the specified key. Returns `None` if key is not found.
`get_max/min()`|![equation](https://latex.codecogs.com/png.latex?O%28%5Clog%20n%20%29)|Returns the element with the largest/smallest key.
`get_larger/smaller(key)`|![equation](https://latex.codecogs.com/png.latex?O%28%5Clog%20n%20%29)|Returns the first key which is **strictly** smaller/larger than the key specified. Returns `None` if there's nothing **strictly** smaller/larger or **if the key specified key is not in BST**.
`get_larger/smaller_than(key)`|![equation](https://latex.codecogs.com/png.latex?O%28%5Clog%20n%20%29)|Returns the first key which is **strictly** smaller/larger than the key specified. Returns `None` if there's nothing **strictly** smaller/larger.

> *It is important to note that even though the Node class exist, the ***user is not expected to touch that class or any object from that class at all***. The interface of all functions of the BST should only involve ***keys***. To use the BST with non-primitive objects, users will need to ***implement their own comparables***.*

# Explanation of BST operations
## Insert

This implementation of *Insert* takes in a **key as parameter**. There is an optional argument of target node which is by default, the root node. There are a total of three possible cases or scenarios in Insert.

1. **The root is empty**. In this case, we replace the root of the BST with a node intialized with the key.
2. **The key is smaller or equal to the key of the target node.** In this case, we check if the left child of the node is empty. If it is, we insert it there, else, we call Insert of the left child of the node.
3. **The key is larger than the key of the target node.** In this case, we check if the right child of the node is empty. If it is, we insert it there, else, we call Insert of the right child of the node.

## Get Min/Max
Get min finds the **minimum**/**maximum** key in the BST and returns the key.

1. In Get Min, the algorithms keeps **shifting towards the left child** until it can no longer shift left. The key it is pointing to at that point will be the minimum key.
2. In Get Max, the algorithms keeps **shifting towards the right child** till it can no longer shift right.
