"""
Implementation of Bellman-Ford Algorithm
1. Can solve any shortest path problem without a negative cycle
2. Will identify the presenece of a negative cycle and inform u

***
"""

import sys
sys.path.append("/Users/tanliangwei/Desktop/Summer 2019/Algorithms 1/python_datastructures/Graph")
from weighted_graph import WeightedGraph

def bellman_ford(weighted_graph, source):
	dist = {}
	for v in weighted_graph.get_vertexes():
		dist[v] = float("inf")
	parent = {source:None}
	dist[source] = 0
	pq = {}
	for v in weighted_graph.get_vertexes():
		pq[v] = dist[v]
	pq.update({source: 0})

	# a helper relax function for relaxing edges
	def relax(edge):
		weight = weighted_graph.W[edge]
		u, v = edge
		if dist[v] > (dist[u] + weight):
			dist[v] = dist[u] + weight
			parent[v] = u
			pq.update({v: dist[v]})

	for i in range(0, len(weighted_graph.get_vertexes())-1):
		for e in weighted_graph.get_edges():
			relax(e)

	for e in weighted_graph.get_edges():
		u, v = e
		if dist[v] > dist[u] + weighted_graph.W[e]:
			print("negative cycle detected")
			return

	print(dist)


if __name__ == "__main__":
	print("====== Testing Weighted Graph =========")
	WG = WeightedGraph(directed = True)

	Vertices = ["a","b", "c", "d", "e"]
	Edges = [(("a", "b"), 19), (("b", "c"), 11), (("b", "d"), 4), (("d", "c"), 15), (("d", "e"), 13), (("c", "e"), 5), (("c", "a"), -31)]
	WG.make_graph(Vertices, Edges)
	# print(WG.W)
	bellman_ford(WG, "a")

