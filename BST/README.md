# Binary Search Tree (BST)

A Binary Search Tree (BST) is a data structure which maintains a set of elements in a way such that the it is **easy and efficient to find an element** given its key. To facilitate this, the BST has a property in which for every node, **all the nodes from the left subtree have keys which are smaller than the key of the node** while **all nodes from the right subtree has keys which are larger than the key of the node.** The elements being maintained must be also be **sortable** and **orderable**.

# BST operations summary TO-DO

The following table contains the operatations frequently used in a Heap data structure. N denotes the number of elements in the heap.

|Operation|Description|Time Complexity|
|----------------|-------------------------------|-----------------------------|
`Heap(list)`|![equation](https://latex.codecogs.com/png.latex?O%281%29)|Constructor for heap.
`insert(key)`|![equation](https://latex.codecogs.com/png.latex?O%28%5Clog%20n%20%29)|Inserts *key* into the data structure while maintaining max-heap property.
`pop(index)`|![equation](https://latex.codecogs.com/png.latex?O%28%5Clog%20n%20%29)|Returns and removes the element at the specified index while maintaining max-heap property. *Default value (if not specified) for index is 0 which points to the largest element in Heap.*
`get_max()`|![equation](https://latex.codecogs.com/png.latex?O%281%29)|Returns the element with the largest key.
`build_max_heap()`|![equation](https://latex.codecogs.com/png.latex?O%28n%20%29)|Creates a list with max-heap property with a list of unordered elements.

## Insert

This implementation of Insert takes in a target node and a key. By default, the target node will be the root node. There are a total of three possible cases or scenarios in Insert.

1. **The root is empty**. In this case, we replace the root of the BST with a node intialized with the key.
2. **The key is smaller or equal to the key of the target node.** In this case, we check if the left child of the node is empty. If it is, we insert it there, else, we call Insert of the left child of the node.
3. **The key is larger than the key of the target node.** In this case, we check if the right child of the node is empty. If it is, we insert it there, else, we call Insert of the right child of the node.