"""
This module allows users to run BFS algorithms on 
Graph structures created in the graph module in the parent directory
"""
import sys
sys.path.append("/Users/tanliangwei/Desktop/Summer 2019/Algorithms 1/python_datastructures/Graph")
from graph import Graph, Vertex
clock = 0

def default_terminate_function(u, v, list_of_child, visit_stack, parent):
	return False

def default_pre_function(v):
	pass

def default_post_function(v):
	pass

def dfs(graph, pre_function = default_pre_function, 
		post_function = default_post_function,
		terminate_function = default_terminate_function,
		view_stack = False):
	parent = {}
	terminate = False
	for v in graph.get_vertexes():
		if v not in parent:
			parent, terminate = dfs_util(graph, v, parent, pre_function, post_function, terminate_function, view_stack)
		if terminate:
			break
	return parent, terminate


# given a graph and a source vertex, this function performs DFS starting from the source.
def dfs_util(graph, source, parent,
		pre_function = default_pre_function, 
		post_function = default_post_function, 
		terminate_function = default_terminate_function,
		view_stack = False):
	parent[source] = None
	visit_stack = [[source]]
	terminate = False
	while len(visit_stack) > 0:
		current_list_of_child = visit_stack[-1]
		current_vertex = current_list_of_child[-1]
		pre_function(current_vertex)
		list_of_child = []
		for child in graph.get_set_of_children(current_vertex):
			if terminate_function(current_vertex, child, list_of_child, visit_stack, parent):
				terminate = True
				break
			if child not in parent:
				parent[child] = current_vertex
				list_of_child.append(child)
		if terminate:
			break
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
	return parent, terminate

def check_cycle(graph):
	def cycle_terminate_function(u, v, list_of_child, visit_stack, parent):
		for visiting in visit_stack:
			if visiting[-1] == v:
				print("cycle detected")
				return True
	parent, terminate = dfs(graph, terminate_function = cycle_terminate_function)

	return parent, terminate

def check_cycle_2(graph):
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
	G.make_graph([1, 2, 3, 4, 5, 6, 7, 8, 9], [(1, 2), (1, 3), (2, 4), (2, 5), (3,6), (3,7), (5,8), (5,9), (1, 9)])
	print(check_cycle(G))






