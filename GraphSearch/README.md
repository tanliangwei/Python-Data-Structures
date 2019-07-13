# Graph Search Algorithms
Graph search algorithms traverse through the graph in search of objectives or solutions defined by the user. The end result could be a table of solutions, path traversed to reach an objective or even a simple yes or no. In this package, 4 basic graph search algorithms will be elaborated with others being an extention of these 4 basic graph search algorithms. 

1. `bfs`(Breath First Search) traverses an **unweighted graph** layer by layer from the **shallowest to the deepest** layer.
2. `dfs`(Depth First Search) explores the deepest nodes of an **unweighted graph** as quickly as possible.
3. `djikstra` (Djikstra's Algorithm) is a shortest simple path algorithm for **weighted graphs** with only **non negative edges**.
4. `bellman_ford` (Bellman-Ford Algorithm) is the most general shortest simple path algorithms for all **weighted-graphs**. 

>In the presenece of a **negative cycle**, the Bellman-Ford Algorithm will detect the cycle but becomes incapable of finding shortest path.

# Graph Search Summary

|Operation|Time Complexity
|----------------|-------------------------------|
`bfs(graph,source,check_terminate)`|![equation](https://latex.codecogs.com/gif.latex?O%28%7CV%7C&plus;%7CE%7C%29)
`dfs(graph)`|![equation](https://latex.codecogs.com/gif.latex?O%28%7CV%7C&plus;%7CE%7C%29)
`djikstra(edge)`|![equation](https://latex.codecogs.com/gif.latex?O%28%7CV%7C%5Clg%20%7CV%7C&plus;%7CE%7C%29)
`bellman_ford(edge)`|![equation](https://latex.codecogs.com/gif.latex?O%28%7CV%7C%7CE%7C%29)

## Breath First Search
The Breath First Search (BFS) algorithm explores a graph from the nodes nearest to the source to the nodes furthest away. It is used in finding the shortest path for applications in which the **cost/benefit of each step is constant** throughout the whole graph. We can use this to find the best solution out of a maze or many other single agent games. 

### Using `bfs`
`bfs` takes in **3** input parameters and returns **2** outputs.
Most markdown syntaxes work inside block quotes.

* Inputs
	1. `graph` - The target graph. **Graph must share the same interface as the `Graph` in the `Graph` module**
	2. `source` - The source vertex.
	3. `check_terminate(u, v)` *(optional)* - We can pass in a function to determine when the `bfs` terminates based on the edge `(u, v)` which `bfs` is currently traversing. Function must return `True` to terminate. Default `check_terminate` function always returns `False`.

* Outputs
	
	1. `parent` -Contains a `dict` which shows the parent vertex of every vertex in the shortest paths computed. We can use it to derive the shortest path to every reachable vertex.
	2. `level` - Contains a `dict` which stores information regarding the number of edges required to reach a certain vertex from the `source` specified. 

### Example
~~~python
"""
An example application to find the shortest path from California to New York
"""

# bfs will terminate once we find "California"
def check_terminate(u, v):
	return v=="California"

# Call bfs over here
parent, level = bfs(graph, "New York", check_terminate) 

# Parent will be have such a format : 
# {"New York": "Utah", "Utah":"California", "Boston":"Utah", "California": None}
# Level will have the following format
# {"California": 0, "Utah": 1, "Boston": 2, "New York": 2}
~~~


### Time Complexity
The time complexity of BFS is \\(O(|V|+|E|) \\) which is also equal to \\(O(b^d) \\) where b is the branching factor and d is the depth of the graph.

### Space Complexity
On top of the space required for the graph, BFS further requires \\(O(b^d) \\) or \\(O(|V|) \\) in the worst case which is the space required to store all the vertexes at one layer.

#### Questions

1. Should we include a BFS which takes in no source and will run through the entire graph? Is it meaningful?

## Depth First Search


