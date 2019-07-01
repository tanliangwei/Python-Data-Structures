# Sorting
Sorting is a process in which a sequence of objects are arranged in order. The way the objects are sorted are determined by **comparator functions**. Intuitively, **comparator functions** contain instructions for determining if an object is *larger than*, *smaller than* or *equal* to the object it is being compared to. The input to a **Sort Function** is an unsorted sequence of objects. The output of a **Sort Function** is a sorted sequence of the objects supplied. Default comparator functions already exist for all primitive objects like `int` , `str` ,`float` and more and will be used if another comparator function is not supplied. 

# Comparison of Sorts
## General Sorts
| Name | Time Complexity | Description |
|----------------|-------------------------------|-----------------------------|
`countsort(arr)`|![equation](https://latex.codecogs.com/png.latex?O(n&plus;m))| Sorts a sequence of **integers** or objects whose sort depends on a single **integer attribute**.
`radixsort(arr)`|![equation](https://latex.codecogs.com/png.latex?O(n\log&space;_{n}k))| Sorts a sequence of **postive integers** or objects whose sort depends on a single **positive integer attribute**. 
## Integer Sorts
| Name | Time Complexity | Description |
|----------------|-------------------------------|-----------------------------|
`countsort(arr)`|![equation](https://latex.codecogs.com/png.latex?O(n&plus;m))| Sorts a sequence of **integers** or objects whose sort depends on a single **integer attribute**.
`radixsort(arr)`|![equation](https://latex.codecogs.com/png.latex?O(n\log&space;_{n}k))| Sorts a sequence of **postive integers** or objects whose sort depends on a single **positive integer attribute**. 

## Count Sort 
Count sort takes in an list of integers and sorts it. If you wish to sort a list of objects **via a certain integer attribute**, you will need to supply a `key_function`.

Basic use case: 

```python
from countsort import countsort

list_of_number = [9, 5, 6, 2, 7, 11]
countsort(list_of_number) # list_of_number will be [2, 5, 6, 7, 9, 11] after call
```

To reverse the sorting order:

```python
list_of_number = [9, 5, 6, 2, 7, 11]
countsort(list_of_number, reverse=True) # list_of_number will be [11, 9, 7, 6, 5, 2] after call
```

To sort objects defined by us:

```python
# a certain object which we wish to sort via a single integer attribute
class people:
	def __init__(self, name, id):
		self.name=name
		self.id=id # where id is an integer

# define the key_function whose interface is a object input and strictly an integer output
def key_function(people):
	return people.id # returns an integer key used in sorting

...
# initialize the people objects
...

list_of_people = [p1, p2, p3, p4, p5, p6] # list of people objects
countsort(list_of_number, key_function=key_function) # list_of_people will be sorted based on their ids.
```