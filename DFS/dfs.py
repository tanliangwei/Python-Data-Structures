"""
This module allows users to run BFS algorithms on 
Graph structures created in the graph module in the parent directory
"""
import sys
sys.path.append("/Users/tanliangwei/Desktop/Summer 2019/Algorithms 1/python_datastructures/Graph")
from graph import DictGraph, Vertex

def default_check_function(v):
	return False

def DFS(graph, root=None, check_terminate = default_check_function, finished_visiting=None, parent=None):
	if parent is None:
		parent = {}
	if finished_visiting is None:
		finished_visiting = set()
	if root is not None:
		parent[root] = None
		stack = [root]
		terminate = False
		while len(stack) > 0:
			u = stack[-1]
			if u in finished_visiting:
				stack.pop()
				continue
			for v in graph.get_set_of_children(u):
				if v not in parent:
					if check_terminate(v):
						terminate = True
					parent[v] = u
					stack.append(v)
				if terminate:
					break
			finished_visiting.add(u)
			if terminate:
				break
		return
	if root is None:
		for v in graph.get_vertexes():
			if v not in parent:
				DFS(graph, v, check_terminate, finished_visiting, parent)
		return parent


OG = DictGraph(True)
a = Vertex()
b = Vertex() 
c = Vertex() 
d = Vertex() 
e = Vertex() 
f = Vertex() 
OG.make_graph([a, b, c, d, e, f], [(a, b), (a, c), (f, d), (c, e)])
print(DFS(OG))






