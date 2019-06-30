"""
This File contains the Graph class
Users can use this class to make Graphs
"""

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
		return self.graph

	def get_set_of_children(self, obj):
		assert obj in self.graph.keys(), "vertice is not in the set V"
		return self.graph[obj]



class Vertex:
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

class ObjectGraph:
	def __init__(self, directed=True):
		self.V = {}
		self.directed = directed

	def add_vertice(self, obj):
		assert obj not in self.V
		v = Vertex(obj)
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
		return self.V

	def get_set_of_children(self, obj):
		assert obj in self.V, "vertice is not in the set V"
		return self.V[obj].set_of_children


OG = ObjectGraph(True)
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





		



