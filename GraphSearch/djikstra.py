"""
Implementation from the Djikstra's Algorithm
**Note that you cannot have ANY negative weight for this algorithm
lets use a dict implementation of PQ
"""
import sys
sys.path.append("/Users/tanliangwei/Desktop/Summer 2019/Algorithms 1/python_datastructures/Graph")
sys.path.append("/Users/tanliangwei/Desktop/Summer 2019/Algorithms 1/python_datastructures/DFS")
from weighted_graph import WeightedGraph, WeightedVertexGraph, WeightedIntVertex
from topological_sort import topological_sort

def djikstra(weighted_graph, source):
	# initialization a dictionry for dist
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

	def key_function(key):
		return pq[key]

	while len(pq)>0:
		u = min(pq, key = key_function)
		pq.pop(u)
		for v in weighted_graph.get_set_of_children(u):
			relax((u, v))

	print(dist)

def DAG_shortest_path(weighted_graph, source):
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
	topo_sorted_vertexes = topological_sort(weighted_graph)
	for v in topo_sorted_vertexes:
		for e in weighted_graph.get_set_of_children(v):
			relax((v,e))

	print(dist)





if __name__ == "__main__":
	print("====== Testing Weighted Graph =========")
	WG = WeightedGraph(directed = True)

	Vertices = ["a","b", "c", "d", "e"]
	Edges = [(("a", "b"), 19), (("a", "c"), 7), (("b", "c"), 11), (("b", "d"), 4), (("d", "c"), 15), (("d", "e"), 13), (("c", "e"), 5)]
	WG.make_graph(Vertices, Edges)
	print(WG.W)
	djikstra(WG, "a")
	DAG_shortest_path(WG, "a")



