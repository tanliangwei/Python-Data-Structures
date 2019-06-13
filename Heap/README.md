# Heap

A heap is a data structure which maintains a set of elements in a way such that the element having ***maximum/minimum*** key can be easily obtained. Elements can also be added or removed from this data structure at fast speeds while maintaining the above property. This property is known as the ***Max/Min-Heap*** property. The heap implemented in our case is a ***Max-Heap***.

# Heap operations summary

The following table contains the operatations frequently used in a Heap data structure. N denotes the number of elements in the heap.

|Operation|Description|Time Complexity|
|----------------|-------------------------------|-----------------------------|
`Heap(list)`|![equation](https://latex.codecogs.com/png.latex?O%281%29)|Constructor for heap.
`insert(key)`|![equation](https://latex.codecogs.com/png.latex?O%28%5Clog%20n%20%29)|Inserts *key* into the data structure while maintaining max-heap property.
`pop(index)`|![equation](https://latex.codecogs.com/png.latex?O%28%5Clog%20n%20%29)|Returns and removes the element at the specified index while maintaining max-heap property. *Default value (if not specified) for index is 0 which points to the largest element in Heap.*
`get_max()`|![equation](https://latex.codecogs.com/png.latex?O%281%29)|Returns the element with the largest key.
`build_max_heap()`|![equation](https://latex.codecogs.com/png.latex?O%28n%20%29)|Creates a list with max-heap property with a list of unordered elements.

# TO-DO
1. Comparison between Heap and BSTs.
2. Implement visualization for Heap and BSTs.