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

    def get_left_child(self, index):
        if index >= self.heap_size or (index*2)+1 >= self.heap_size:
            return None
        return self.heap[(index*2)+1]

    def get_right_child(self, index):
        if index >= self.heap_size or (index*2)+2 >= self.heap_size:
            return None
        return self.heap[(index*2)+2]

    def get_parent(self, index):
        if index >= self.heap_size or (index-1)/2 < 0:
            return None
        return self.heap[(index-1)/2]

    def max_heapify(self, index):
        if index >= self.heap_size:
            return
        left_child = self.get_left_child(index)
        right_child = self.get_right_child(index)
        if left_child is not None and right_child is not None:
            if left_child >= right_child:
                max_child = left_child
                max_index = (index*2)+1
            else:
                max_child = right_child
                max_index = (index * 2) + 2
            if self.heap[index] >= max_child:
                return False
            else:
                temp = self.heap[index]
                self.heap[index] = self.heap[max_index]
                self.heap[max_index] = temp
                return True
        if left_child is not None and right_child is None:
            max_child = left_child
            max_index = (index * 2) + 1
            if self.heap[index] >= max_child:
                return False
            else:
                temp = self.heap[index]
                self.heap[index] = self.heap[max_index]
                self.heap[max_index] = temp
                return True
        if left_child is None and right_child is not None:
            max_child = right_child
            max_index = (index * 2) + 2
            if self.heap[index] >= max_child:
                return False
            else:
                temp = self.heap[index]
                self.heap[index] = self.heap[max_index]
                self.heap[max_index] = temp
                return True
        return False

    


