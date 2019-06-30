"""
This module allows users to create Graphs and run the BFS algorithm on the Graph
"""

# this takes in an input of set of edges and a set of vertices and generates a hash table =/
# adjacency list graph structure
def generate_directed_graph(vertices, edges):
	vertices = set(vertices)
	edges = set(edges)
	graph = {}
	for v in vertices:
		graph[v] = []
	for e in edges:
		u, v = e
		graph[u].append(e)
	return graph

def generate_undirected_graph(vertices, edges):
	vertices = set(vertices)
	edges = set(edges)
	graph = {}
	for v in vertices:
		graph[v] = []
	for e in edges:
		u, v = e
		graph[u].append(v)
		graph[v].append(u)
	return graph

