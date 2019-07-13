"""
This module allows users to run BFS algorithms on 
Graph structures created in the graph module in the parent directory
"""
import sys
sys.path.append("/Users/tanliangwei/Desktop/Summer 2019/Algorithms 1/python_datastructures/Graph")

def default_check_function(u, v):
	return False

def BFS(graph, source, check_terminate = default_check_function):
	level = {source: 0}
	parent = {source: None}
	i = 1
	frontier = {source}
	terminate = False
	while len(frontier) > 0:
		next_set = set()
		for u in frontier:
			for v in graph.get_set_of_children(u):
				if check_terminate(u, v):
						terminate = True
				if v not in level:
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
	print(sys.path)
	from graph import VertexGraph, Graph, IntVertex

	def check(v):
		if v==v:
			return True
		return False

	OG = VertexGraph(True)
	a = IntVertex(0)
	b = IntVertex(1) 
	c = IntVertex(2) 
	d = IntVertex(3) 
	e = IntVertex(4) 
	f = IntVertex(5) 
	OG.make_graph([a, b, c, d, e, f], [(a, b), (a, c), (f, d), (c, e), (e, f)])
	print(BFS(OG, a, check))



