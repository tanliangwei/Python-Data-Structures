"""
Python Heap Implementation using ArrayList
Class contains a list
and
1) build_max_heap
2) max_heapify *remember that this resolves a issue with the subtree starting at the node. it in no way
    affects the parent of the node.
3) insert
4) extract max/pop
5) max
6) heapsort
"""


class Heap:

    def __init__(self, list_of_elements):
        self.heap = list_of_elements
        self.heap_size = len(list_of_elements)

    def get_left_child_index(self, index):
        if index >= self.heap_size or (index*2)+1 >= self.heap_size:
            return None
        return (index*2)+1

    def get_right_child_index(self, index):
        if index >= self.heap_size or (index*2)+2 >= self.heap_size:
            return None
        return (index*2)+2

    def get_parent_index(self, index):
        if index >= self.heap_size or (index-1)/2 < 0:
            return None
        return (index-1)/2

    def max_heapify(self, index):
        if index >= self.heap_size:
            return False
        left_child_index = self.get_left_child_index(index)
        right_child_index = self.get_right_child_index(index)
        max_index = index
        if left_child_index is not None and self.heap[left_child_index] > self.heap[index]:
            max_index = left_child_index
        if right_child_index is not None and self.heap[right_child_index] > self.heap[max_index]:
            max_index = right_child_index
        if max_index != index:
            temp = self.heap[index]
            self.heap[index] = self.heap[max_index]
            self.heap[max_index] = temp
            self.max_heapify(max_index)
            return True
        return False

    def build_max_heap(self):
        # find the depth of the tree first.
        depth = 0
        number_of_nodes = self.heap_size
        while number_of_nodes > 1:
            number_of_nodes = number_of_nodes / 2
            depth += 1
        largest_node_index = 2**depth - 2
        if largest_node_index < 0:
            return False
        for i in range(largest_node_index, -1, -1):
            self.max_heapify(i)
        return True

    def insert(self, key):
        self.heap.append(key)
        self.heap_size+=1
        current_index = self.heap_size-1
        while current_index > 0:
            current_index = int((current_index-1)/2)
            self.max_heapify(current_index)
        return True

    def get_max(self):
        if self.heap_size<=0:
            return None
        return self.heap[0]

    def pop(self, index=0):
        if index >= self.heap_size or index<0:
            return None
        pop_element = self.heap[index]
        self.heap[index]=self.heap[self.heap_size-1]
        self.heap_size-=1
        self.heap.pop()
        self.max_heapify(index)
        return pop_element


heap = Heap([])
heap.build_max_heap()
heap.insert(10)
print(heap.heap)
heap.insert(20)
print(heap.heap)
heap.insert(30)
print(heap.heap)
heap.insert(40)
print(heap.heap)
heap.insert(25)
print(heap.heap)




