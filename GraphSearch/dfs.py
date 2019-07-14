"""
This module allows users to run BFS algorithms on 
Graph structures created in the graph module in the parent directory
"""
import sys
sys.path.append("/Users/tanliangwei/Desktop/Summer 2019/Algorithms 1/python_datastructures/Graph")
from graph import Graph, Vertex
clock = 0

def default_check_function(u, v):
	return False

def default_pre_function(v):
	pass

def default_post_function(v):
	pass

# given a graph and a source vertex, this function performs DFS starting from the source.
def dfs(graph, source, pre_function=default_pre_function, post_function = default_post_function, view_stack=False):
	visited = {source}
	parent = {source: None}
	visit_stack = [[source]]
	while len(visit_stack) > 0:
		current_list_of_child = visit_stack[-1]
		current_vertex = current_list_of_child[-1]
		pre_function(current_vertex)
		list_of_child = []
		for child in graph.get_set_of_children(current_vertex):
			if child not in visited:
				visited.add(child)
				list_of_child.append(child)
		if len(list_of_child) > 0:
			visit_stack.append(list_of_child)
			if view_stack:
				print(visit_stack)
		else:
			# if reached leaf node
			current_list_of_child.pop()
			post_function(current_vertex)
			if view_stack:
				print(visit_stack)
			# if this is the last node of the child list,then pop out the list and also the last node, and repeat this check
			while len(current_list_of_child) == 0:
				visit_stack.pop()
				if view_stack:
					print(visit_stack)
				if len(visit_stack) == 0:
					break
				current_list_of_child = visit_stack[-1]
				current_vertex = current_list_of_child.pop()
				post_function(current_vertex)
				if view_stack:	
					print(visit_stack)

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
	G = Graph(True)
	G.make_graph([1, 2, 3, 4, 5, 6, 7, 8, 9], [(1, 2), (1, 3), (2, 4), (2, 5), (3,6), (3,7), (5,8), (5,9)])
	dfs(G, 1)






