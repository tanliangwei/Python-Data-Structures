"""
This module allows users to run BFS algorithms on 
Graph structures created in the graph module in the parent directory
"""
import sys
sys.path.append("/Users/tanliangwei/Desktop/Summer 2019/Algorithms 1/python_datastructures/Graph")
from graph import Graph, Vertex

def default_check_function(u, v):
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
	terminate = False
	if root is not None:
		parent[root] = None
		stack = [root]
		while len(stack) > 0:
			print(stack)
			u = stack[-1]
			if u in visited:
				u = stack.pop()
				pos_function(u)
				continue
			pre_function(u)
			for v in graph.get_set_of_children(u):
				if v not in parent:
					parent[v] = u
					stack.append(v)
				if check_terminate(u, v):
					terminate = True
				if terminate:
					break
			visited.add(u)
			if terminate:
				break
		return parent
	if root is None:
		for v in graph.get_vertexes():
			if v not in parent:
				DFS(graph, v, check_terminate, pre_function, pos_function, visited, parent)
		return parent

def check_cycle(graph):
	visited = set()
	for v in graph.get_vertexes():
		if v not in visited:
			cycle = check_cycle_1(graph, v, visited)
			if cycle:
				return True
	return False


def check_cycle_1(graph, vertex, visited = None, visit_stack=None):
	if visit_stack is None:
		visit_stack = set()
	if visited is None:
		visited = set()
	visit_stack.add(vertex)
	visited.add(vertex)
	for child in graph.get_set_of_children(vertex):
		if child in visit_stack:
			return True
		if child not in visited:
			cycle = check_cycle_1(graph, child, visited, visit_stack)
			if cycle:
				return True
	visit_stack.remove(vertex)
	return False





			





if __name__ == "__main__":
	OG = Graph(True)
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






