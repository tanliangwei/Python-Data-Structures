"""
This module contains the Weighted Graphs.
It extends the graph class from graph.py
Users can use this class to make Weighed Graphs
This data structure contains 5 functions on the interface.
1. Add vertice - Basically adding a vertice into the graph
2 & 3. Add directed/undirected edge - adding edges into graph
4. Make graph - makes a graph give 2 sets, V and E
5. get set of children - getting a set of children for the object specified

A vertice can be any object which can be uniquely identified - use addresss
An edge wil be of the following format ((vertice 1, vertice 2), weight)

** take note that we only deal with the objects at the interface. We in no way touch the internal objects such as Vertex.
** Graph weights will be made available from a general dictionary or in the form of a tuple.
"""
from graph import Graph, VertexGraph, Vertex

# extremely lightweight form of graph
class WeightedGraph(Graph):
	def __init__(self, directed=True):
		Graph.__init__(self, directed=directed)
		self.W = {}

	def add_directed_edge(self, weighted_edge):
		edge, weight = weighted_edge
		Graph.add_directed_edge(self, edge)
		assert edge in self.W.keys(), "edge already in W"
		self.W[edge] = weight

	def add_undirected_edge(self, weighted_edge):
		edge, weight = weighted_edge
		Graph.add_undirected_edge(self, edge)
		assert edge in self.W.keys(), "edge already in W"
		self.W[edge] = weight
		reverse_edge = (edge[1], edge[0])
		assert reverse_edge in self.W.keys(), " reverse edge already in W"
		self.W[reverse_edge] = weight

class WeightedVertex(Vertex):
	def __init__(self):
		Vertex.__init__(self)
		self.W = {}

	def add_child(self, child, weight=0):
		Vertex.add_child(self, child)
		self.W[child] = weight

class WeightedVertexGraph(VertexGraph):
	def __init__(self, directed = True):
		VertexGraph.__init__(self, directed)
		self.W = {}

	def add_directed_edge(self, weighted_edge):
		edge, weight = weighted_edge
		VertexGraph.add_directed_edge(self, edge)
		assert edge in self.W.keys(), "edge already in W"
		self.W[edge] = weight
		
	def add_undirected_edge(self, edge):
		edge, weight = weighted_edge
		VertexGraph.add_undirected_edge(self, edge)
		assert edge in self.W.keys(), "edge already in W"
		self.W[edge] = weight
		reverse_edge = (edge[1], edge[0])
		assert reverse_edge in self.W.keys(), "reverse edge already in W"
		self.W[reverse_edge] = weight






		



