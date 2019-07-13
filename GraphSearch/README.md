# Graph Search Algorithms
Graph search algorithms traverse through the graph in search of objectives or solutions defined by the user. The end result could be a table of solutions, path traversed to reach an objective or even a simple yes or no. In this package, 4 basic graph search algorithms will be elaborated with others being an extention of these 4 basic graph search algorithms. 

1. `bfs`(Breath First Search) traverses an **unweighted graph** layer by layer from the **shallowest to the deepest** layer.
2. `dfs`(Depth First Search) explores the deepest nodes of an **unweighted graph** as quickly as possible.
3. `djikstra` (Djikstra's Algorithm) is a shortest simple path algorithm for **weighted graphs** with only **non negative edges**.
4. `bellman_ford` (Bellman-Ford Algorithm) is the most general shortest simple path algorithms for all **weighted-graphs**. 

>In the presenece of a **negative cycle**, the Bellman-Ford Algorithm will detect the cycle but becomes incapable of finding shortest path.

## Graph Search Summary

|Operation|Time Complexity
|----------------|-------------------------------|
`bfs(graph,source,check_terminate)`|![equation](https://latex.codecogs.com/gif.latex?O%28%7CV%7C&plus;%7CE%7C%29)
`dfs(graph)`|![equation](https://latex.codecogs.com/gif.latex?O%28%7CV%7C&plus;%7CE%7C%29)
`djikstra(edge)`|![equation](https://latex.codecogs.com/gif.latex?O%28%7CV%7C%5Clg%20%7CV%7C&plus;%7CE%7C%29)
`bellman_ford(edge)`|![equation](https://latex.codecogs.com/gif.latex?O%28%7CV%7C%7CE%7C%29)

## Breath First Search

