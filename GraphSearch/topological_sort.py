from dfs import DFS
import sys
sys.path.append("/Users/tanliangwei/Desktop/Summer 2019/Algorithms 1/python_datastructures/Graph")
from graph import Graph, Vertex

# important to note that graph must be a dag.
def topological_sort(graph):
	finishing_list =[]
	def pos_function(vertex):
		finishing_list.append(vertex)
	DFS(graph, pos_function=pos_function)
	finishing_list.reverse()
	return finishing_list





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
	OG.make_graph([a, b, c, d, e, f], [(a, b), (a, e), (f, d), (c, e)])
	print(topological_sort(OG))