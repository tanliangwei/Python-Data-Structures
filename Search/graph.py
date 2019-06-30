"""
This module contains the Graph class
Users can use this class to make Graphs
This data structure contains 5 functions on the interface.
1. Add vertice - Basically adding a vertice into the graph
2 & 3. Add directed/undirected edge - adding edges into graph
4. Make graph - makes a graph give 2 sets, V and E
5. get set of children - getting a set of children for the object specified

** take note that we only deal with the objects at the interface. We in no way touch the internal objects such as Vertex.
"""

# extremely lightweight form of graph
class DictGraph:
	def __init__(self, directed=True):
		self.graph = {}
		self.directed = directed

	def add_vertice(self, obj):
		assert obj not in self.graph.keys(), "vertice is already in key"
		self.graph[obj] = set()

	def __contains__(self, obj):
		return obj in self.graph.keys()

	def add_directed_edge(self, edge):
		from_object, to_object = edge
		assert from_object in self.graph.keys(), "u is not in the set V"
		assert to_object in self.graph.keys(), "v is not in the set V"
		self.graph[from_object].add(to_object)

	def add_undirected_edge(self, edge):
		from_object, to_object = edge
		assert from_object in self.graph.keys(), "u is not in the set V"
		assert to_object in self.graph.keys(), "v is not in the set V"
		self.graph[from_object].add(to_object)
		self.graph[to_object].add(from_object)

	def make_graph(self, V, E):
		self.graph = {}
		for v in V:
			self.add_vertice(v)
		if self.directed:
			for e in E:
				self.add_directed_edge(e)
		else:
			for e in E:
				self.add_undirected_edge(e)

	def get_set_of_children(self, obj):
		assert obj in self.graph.keys(), "vertice is not in the set V"
		return self.graph[obj]

class Vertex:
	def __init__(self):
		self.set_of_children = set()

	def get_set_of_children(self):
		return self.set_of_children

	def add_child(self, child):
		self.set_of_children.add(child)

class VertexGraph:
	def __init__(self, directed = True):
		self.V = set()
		self.E = set()

	def add_vertice(self, obj):
		assert obj not in self.V, "vertice is already in Graph"
		self.V.add(obj)

	def add_directed_edge(self, edge):
		assert edge not in E, "edge already in Graph"
		from_obj, to_obj = edge
		assert from_obj in V, "u of (u,v) not in V"
		assert to_obj in V, "v of (u,v) not in V"
		self.E.add(edge)
		from_obj.add_child(to_object)

	def add_undirected_edge(self, edge):
		assert edge not in E, "edge already in Graph"
		from_obj, to_obj = edge
		assert from_obj in V, "u of (u,v) not in V"
		assert to_obj in V, "v of (u,v) not in V"
		self.E.add(edge)
		from_obj.add_child(to_object)
		to_obj.add_child(from_object)

	def make_graph(self, V, E):
		self.V = set()
		self.E = set()
		for v in V:
			add_vertice(v)
		if self.directed:
			for e in E:
				self.add_directed_edge(e)
		else:
			for e in E:
				self.add_undirected_edge(e)

	def get_set_of_children(self, obj):
		assert obj in self.V, "vertice is not in the set V"
		return obj.get_set_of_children()





# not as light weight. Currenly can't think of any reason to use this.
class Node:
	def __init__(self, obj):
		self.obj = obj
		self.set_of_children = set()

	# so that when u compare two vertex with the same object, 
	# it will return true.
	def __eq__(self, other):
		return self.obj == other

	# so that it will use the obj when hashing in the value
	def __hash__(self):
	    # :nodoc: Delegate comparison to keys.
	    return hash(self.obj)

	def add_child(self, obj):
		self.set_of_children.add(obj)

class NodeGraph:
	def __init__(self, directed=True):
		self.V = {}
		self.directed = directed

	def add_vertice(self, obj):
		assert obj not in self.V
		v = Node(obj)
		self.V[v]=v

	def add_directed_edge(self, edge):
		from_object, to_object = edge
		assert from_object in self.V, "u is not in the set V"
		assert to_object in self.V, "v is not in the set V"
		self.V[from_object].add_child(to_object)

	def add_undirected_edge(self, edge):
		from_object, to_object = edge
		assert from_object in self.V, "u is not in the set V"
		assert to_object in self.V, "v is not in the set V"
		self.V[from_object].add_child(to_object)
		self.V[to_object].add_child(from_object)

	def make_graph(self, V, E):
		self.V = {}
		for v in V:
			self.add_vertice(v)
		if self.directed:
			for e in E:
				self.add_directed_edge(e)
		else:
			for e in E:
				self.add_undirected_edge(e)

	def get_set_of_children(self, obj):
		assert obj in self.V, "vertice is not in the set V"
		return self.V[obj].set_of_children





OG = NodeGraph(True)
OG.make_graph([1,2,3,4,5,6], [(1,2), (1,3), (6,4), (3,5)])
visited = set()

queue = [1]
while len(queue)>0:
	current_obj = queue.pop()
	if current_obj not in visited:
		visited.add(current_obj)
		for e in OG.get_set_of_children(current_obj):
			if e not in visited:
				queue.append(e)

print(visited)





		



