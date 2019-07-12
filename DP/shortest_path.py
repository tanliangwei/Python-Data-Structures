"""
DP Shortest Path Algorithm using the following recurrence
δk(s, v) = min{w(u, v) + δk-1(s, u) (u, v) ∈ E}
where δk(s, v) is the shortest path from s to v using k or less steps

** Bellman Ford in disguise

memo format = [{k=0 dict}, {k=1 dict}, {}]
"""

import sys
sys.path.append("/Users/tanliangwei/Desktop/Summer 2019/Algorithms 1/python_datastructures/Graph")
from weighted_graph import WeightedGraph, WeightedVertexGraph, WeightedVertex

def shortest_path(graph, source, memo):
	memo = []
	parent = {source:None}
	for a in range(0, len(graph.get_vertexes())):
		d = {}
		for v in graph.get_vertexes():
			d[v] = float("inf")
			if v == source:
				d[v] = 0
		memo.append(d)

	for i in range(1, len(graph.get_vertexes())):
		current_dict = memo[i]
		previous_dict = memo[i-1]
		for u in graph.get_vertexes():
			if u == source:
				current_dict[u] = 0
			for v in graph.get_set_of_children(u):
				if graph.W[(u, v)]+previous_dict[u] < current_dict[v]:
					current_dict[v] = graph.W[(u, v)]+previous_dict[u]
					parent[v] = u
	return parent, memo

if __name__ == "__main__":
	s = "s"
	a = "a"
	b = "b"
	c = "c"
	d = "d"
	e = "e"
	f = "f"
	g = "g"
	V = [s, a, b, c, d, e, f, g]
	E = [((s, a), 10), ((s,g), 8), ((a, e), 2), ((b, a), 1), ((b, c), 1), ((c, d), 3), ((d, e), -1), ((e, b), -2), 
		((f, e), -1), ((f, a), -4), ((g, f), 1)]
	WG = WeightedGraph()
	WG.make_graph(V, E)
	a, b = shortest_path(WG, s, [])
	print(a)
	print(b[len(WG.get_vertexes())-1])




