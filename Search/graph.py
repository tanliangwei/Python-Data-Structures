"""
This File contains the Graph class
Users can use this class to make Graphs
"""

class DummyObject:
	def __init__(self, x=None, y=None):
		self.x = x
		self.y = y

class Graph:
	def __init__(self, directed=True):
		self.graph = {}
		self.directed = directed

	def add_vertice(self, obj):
		assert obj not in self.graph.keys(), "vertice is already in key"
		self.graph[obj] = []

	def __contains__(self, key):
		return key in self.graph.keys()

	def add_directed_edge(self, edge):
		from_object, to_object = edge
		assert from_object in self.graph.keys(), "u is not in the set V"
		assert to_object in self.graph.keys(), "v is not in the set V"
		self.graph[from_object].append(to_object)

	def add_undirected_edge(self, edge):
		from_object, to_object = edge
		assert from_object in self.graph.keys(), "u is not in the set V"
		assert to_object in self.graph.keys(), "v is not in the set V"
		self.graph[from_object].append(to_object)
		self.graph[to_object].append(from_object)

	def make_graph(self, V, E):
		self.graph = {}
		for v in V:
			self.add_vertice(v)
		if directed:
			for e in E:
				self.add_directed_edge(e)
		else:
			for e in E:
				self.add_undirected_edge(e)
		return self.graph




		



