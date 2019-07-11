# Graphs
Graphs are data structures which maintains a set of Vertexes (**V**) and a set of Edges(**E**). Vertex are nodes in the graph, each containing information for modelling the user's application. The edges tells us how the vertex are connected to one another. There are several ways of representing this information. In this package, two ways will be introduced. 

1. DictGraph - A graph built using a **Hashtable**, otherwise known as Dictionary in python.
2. VertexGraph - An **object oriented** graph built using a Vertex datastructure and sets **V** and **E**.

# Graph Operations Summary
The table belows shows the operations of the Graph. This is applicable to both the Dict and Vertex Graphs. 

|Operation|Description|Time Complexity|
|----------------|-------------------------------|-----------------------------|
`Graph/VertexGraph(directed)`|![equation](https://latex.codecogs.com/png.latex?O%281%29)|Constructor for the Graph. `directed` allows you to specify whether the graph is directed or undirected. Default value for `directed` is `True`.
`add_vertex(vertex)`|![equation](https://latex.codecogs.com/png.latex?O%281%29)|Inserts a vertex into the Graph. This is **needed** before edges concerning it can be added in. Throws an error if the vertice is already in the graph.
`add_directed_edge(edge)`|![equation](https://latex.codecogs.com/png.latex?O%281%29)|Inserts the specified edge into the Graph as a **directed** edge. Throws an error if the vertices in the edge is not in the graph.
`add_undirected_edge(edge)`|![equation](https://latex.codecogs.com/png.latex?O%281%29)|Inserts the specified edge into the Graph as a **undirected** edge. Throws an error if the vertices in the edge is not in the graph.
`make_graph(V, E)`|![equation](https://latex.codecogs.com/png.latex?O%28%7CV%7C&plus;%7CE%7C%29)|Constructs the graph with the given sets of Vertexes **V** and Edges **E**.
`get_set_of_children(vertex)`|![equation](https://latex.codecogs.com/png.latex?O%281%29)|Returns the set of children of the specified vertex. Throws an error if the vertex is not in the graph. 
`get_vertexes()`|![equation](https://latex.codecogs.com/gif.latex?O(|V|))|Returns the set of vertex **V**.
`get_edges()`|![equation](https://latex.codecogs.com/gif.latex?O(|E|))|Returns the set of edges **E**.

## The Vertex Graph Structure
The `VertexGraph` is build using a `Vertex` data structure and the `VertexGraph` graph datatype. All the vertexes added into the `VertexGraph` must be of the `Vertex` datas structure. To use `VertexGraph`, users will have to import the `Vertex` data structure and specialize (inherit from) it to suit their needs.

***The `VertexGraph` might be chosen over the `DictGraph` in the scenario when the use case involves many different states which the users intend to model with vertexes. In such a case, it might be better to generate the children in dynamically instead of loading the whole graph into memory.***

When inheriting from the `Vertex` data structure, it is **not** necessary to override any of the functions. One can just add in attributes or methods to suit their needs. ***However, to model the above mentioned use case, you will need to override either the `get_set_of_children()` or the `add_child(vertex)` method or both.*** The points below describe the interface of the two methods mentioned.

1. `get_set_of_children()` - takes in **no** parameters and returns a set of `Vertex`es or objects from a subclass of `Vertex`.
2. `add_child(vertex)` - takes in a `Vertex` or an object from a subclass of `Vertex` and adds it into the `set_of_children` attribute of `Vertex`.

## The (normal) Graph Structure
The normal graph structure is a graph built using a Dictionary (`dict`), otherwise known as a Hashtable. It is extremely lightweight and can be used in almost all applications of graphs. 

## TO-DO

1. Give some example codes.
2. Maybe allow for different set of edges for the same set of vertices. To model  lets say different timings of roads
3. weigted graphs. 
4. Should i create a generator version of get vertex and get edges?


