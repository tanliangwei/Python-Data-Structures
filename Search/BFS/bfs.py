"""
This module allows users to run BFS algorithms on 
Graph structures created in the graph module in the same directory
"""

def default_check_function(v):
	return False

def BFS(graph, root, check_terminate = default_check_function):
	level = {root: 0}
	parent = {root: None}
	i = 1
	frontier = {root}
	terminate = False
	while len(frontier) > 0:
		next_set = set()
		for u in frontier:
			for v in graph.get_set_of_children(u):
				if v not in level:
					if check_terminate(v):
						terminate = True
					level[v] = i
					parent[v] = u
					next_set.add(v)
				if terminate:
					break
			if terminate:
				break
		if terminate:
			break
		frontier = next_set
		i += 1
	return parent, level

if __name__ == "__main__":
	import sys
	sys.path.append("/Users/tanliangwei/Desktop/Summer 2019/Algorithms 1/python_datastructures/Search")
	print(sys.path)
	from graph import VertexGraph, DictGraph, Vertex

	def check(v):
		if v==v:
			return True
		return False

	OG = DictGraph(True)
	a = Vertex()
	b = Vertex() 
	c = Vertex() 
	d = Vertex() 
	e = Vertex() 
	f = Vertex() 
	OG.make_graph([a, b, c, d, e, f], [(a, b), (a, c), (f, d), (c, e), (e, f)])
	print(BFS(OG, a, check))



