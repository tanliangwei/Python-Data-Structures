"""
This module allows users to run BFS algorithms on 
Graph structures created in the graph module in the parent directory
"""
import sys
sys.path.append("/Users/tanliangwei/Desktop/Summer 2019/Algorithms 1/python_datastructures/Graph")
from graph import DictGraph, Vertex

def default_check_function(v):
	return False

def default_pre_function(v):
	pass

def default_pos_function(v):
	pass

def DFS(graph, 
		root=None, 
		check_terminate = default_check_function, 
		pre_function = default_pre_function, 
		pos_function = default_pos_function, 
		visited = None, 
		parent = None):
	if parent is None:
		parent = {}
	if visited is None:
		visited = set()
	if root is not None:
		parent[root] = None
		stack = [root]
		terminate = False
		while len(stack) > 0:
			u = stack[-1]
			pre_function(u)
			if u in visited:
				u = stack.pop()
				pos_function(u)
				continue
			for v in graph.get_set_of_children(u):
				if v not in parent:
					if check_terminate(v):
						terminate = True
					parent[v] = u
					stack.append(v)
				if terminate:
					break
			visited.add(u)
			if terminate:
				break
		return
	if root is None:
		for v in graph.get_vertexes():
			if v not in parent:
				DFS(graph, v, check_terminate, pre_function, pos_function, visited, parent)
		return parent

if __name__ == "__main__":
	OG = DictGraph(True)
	# a = Vertex()
	# b = Vertex() 
	# c = Vertex() 
	# d = Vertex() 
	# e = Vertex() 
	# f = Vertex() 
	a = 1
	b = 2
	c = 3
	d = 4
	e = 5
	f = 6 
	OG.make_graph([a, b, c, d, e, f], [(a, b), (a, c), (f, d), (c, e)])
	print(DFS(OG))






