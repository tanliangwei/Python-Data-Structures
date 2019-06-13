# Heap

A heap is a data structure which maintains a set of elements in a way such that the element having **maximum/minimum** key can be easily obtained. To facilitate this, all Heaps has a property known as the **Min/Max-Heap property** in which **for all nodes, all of the nodes from its subtree have keys which are smaller than the target node.** Elements can also be **added or removed** from this data structure at **fast speeds** while maintaining the above property. The heap implemented in our case is a ***Max-Heap***.

# Heap operations summary

The following table contains the operatations frequently used in a Heap data structure. N denotes the number of elements in the heap.

|Operation|Description|Time Complexity|
|----------------|-------------------------------|-----------------------------|
`Heap(list)`|![equation](https://latex.codecogs.com/png.latex?O%281%29)|Constructor for heap.
`insert(key)`|![equation](https://latex.codecogs.com/png.latex?O%28%5Clog%20n%20%29)|Inserts *key* into the data structure while maintaining max-heap property.
`pop(index)`|![equation](https://latex.codecogs.com/png.latex?O%28%5Clog%20n%20%29)|Returns and removes the element at the specified index while maintaining max-heap property. *Default value (if not specified) for index is 0 which points to the largest element in Heap.*
`get_max()`|![equation](https://latex.codecogs.com/png.latex?O%281%29)|Returns the element with the largest key.
`build_max_heap()`|![equation](https://latex.codecogs.com/png.latex?O%28n%20%29)|Creates a list with max-heap property with a list of unordered elements.

# Explanation of methods

## Max Heapify
This method takes in a target node and corrects a **single violation** of Max-Heap property at that target node. The assumption is that the left and right subtrees of the target node fulfils the Max-Heap property. So, these are the steps taken by Max Heapify.

1. It retrieves the keys of the child nodes and **compare them** to get the node of the child with the **higher key**. We call that child, "**higher-child**".
2. It compares the key of the target node with the key of the **higher-child**. If **higher-child** is larger, we swap **higher-child** with the target node and continue Max-Heapify at the new position of target node. (*Max-Heap property might still be violated there.*)
3. Else, we do nothing and return.

***Edge cases:***

* If there are no children, we can return `False` immediately. There is no error to begin with.
* If the target node is `None` or if its index is larger than the heap size, we can return `False` immediately. There is no tree and thus no error to begin with.

Max Heapify will return `True` if at least one swap occured and `False` if no swap occured at all - *no error to begin with*.

## Build Max Heap


# TO-DO
1. Comparison between Heap and BSTs.
2. Implement visualization for Heap and BSTs.
3. Implement Heapsort