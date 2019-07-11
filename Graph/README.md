# Graphs
Graphs are data structures which maintains a set of Vertexes (**V**) and a set of Edges(**E**) and optionally in a weighted graph, a map `weight(u,v)` which maps every edge to a weight. Vertex are nodes in the graph, each containing information for modelling the user's application. The edges tells us how the vertex are connected to one another with the weights indicating the cost/benefit of traversing the edge. In an unweighted graph, all weights are defaulted to a cost of 1. This module contain 2 weighted and 2 unweighted graphs.

1. `Graph` - A graph built using a **Hashtable**, otherwise known as Dictionary in python.
2. `VertexGraph` - An **object oriented** graph built using a Vertex datastructure and sets **V**.
3. `WeightedGraph` - An extention of (1), but have another **Hashtable** to map edges to weights.
4. `WeightedVertexGraph` - An extention of (2), but every `WeightedVertex` object contains a **Hashtable** to map its edges to weights.

# Graph Operations Summary
To maintain simplicity when using this module, the interface and methods of all 4 graphs data structure are the same with the exception of the definition of edge.

> For an **unweighted graph**, an edge is of this format `(from_vertex,to_vertex)`. For a **weighted graph**, it is `((from_vertex,to_vertex), weight)`, 

|Operation|Description|Time Complexity|
|----------------|-------------------------------|-----------------------------|
`Graph/VertexGraph(directed)`|![equation](https://latex.codecogs.com/png.latex?O%281%29)|Constructor for the Graph. `directed` allows you to specify whether the graph is directed or undirected. Default value for `directed` is `True`.
`add_vertex(vertex)`|![equation](https://latex.codecogs.com/png.latex?O%281%29)|Inserts a vertex into the Graph. This is **needed** before edges concerning it can be added in. Throws an error if the vertice is already in the graph.
`add_directed_edge(edge)`|![equation](https://latex.codecogs.com/png.latex?O%281%29)|Inserts the specified edge into the Graph as a **directed** edge. Throws an error if the vertices in the edge is not in the graph.
`add_undirected_edge(edge)`|![equation](https://latex.codecogs.com/png.latex?O%281%29)|Inserts the specified edge into the Graph as a **undirected** edge. Throws an error if the vertices in the edge is not in the graph.
`make_graph(V, E)`|![equation](https://latex.codecogs.com/png.latex?O%28%7CV%7C&plus;%7CE%7C%29)|Constructs the graph with the given sets of Vertexes **V** and Edges **E**.
`get_set_of_children(vertex)`|![equation](https://latex.codecogs.com/png.latex?O%281%29)|Returns the set of children of the specified vertex. Throws an error if the vertex is not in the graph. 
`get_vertexes()`|![equation](https://latex.codecogs.com/gif.latex?O(|V|))|Returns the set of vertex **V**.
`get_edges()`|![equation](https://latex.codecogs.com/gif.latex?O(|E| + |V|))|Returns the set of edges **E**.



## The (Weighted) Vertex Graph Structure
The `(Weighted)VertexGraph` is build using a `(Weighted)Vertex` data structure and the `(Weighted)VertexGraph` graph datatype. All the vertexes added into the `(Weighted)VertexGraph` must be of the `(Weighted)Vertex` datas structure. To use `(Weighted)VertexGraph`, users will have to import the `(Weighted)Vertex` data structure and specialize (inherit from) it to suit their needs.

***The `(Weighted)VertexGraph` might be chosen over the `Graph` in the scenario when the use case involves many different states which the users intend to model with vertexes. In such a case, it might be better to generate the children in dynamically instead of loading the whole graph into memory.***

When inheriting from the `(Weighted)Vertex` data structure, it is **not** necessary to override any of the functions. One can just add in attributes or methods to suit their needs. ***However, to model the above mentioned use case, you will need to override either the `get_set_of_children()` or the `add_child(vertex)` method or both.*** The points below describe the interface of the two methods mentioned.

1. `get_set_of_children()` - takes in **no** parameters and returns a set of `Vertex`es or objects from a subclass of `Vertex`.
2. `add_child(vertex)` - takes in a `Vertex` or an object from a subclass of `Vertex` and adds it into the `set_of_children` attribute of `Vertex`.

## The (normal) Graph Structure
The normal graph structure is a graph built using a Dictionary (`dict`), otherwise known as a Hashtable. It is extremely lightweight and can be used in almost all applications of graphs. 

## TO-DO

1. Give some example codes.
2. Maybe allow for different set of edges for the same set of vertices. To model  lets say different timings of roads
3. weigted graphs. 
4. Should i create a generator version of get vertex and get edges?


