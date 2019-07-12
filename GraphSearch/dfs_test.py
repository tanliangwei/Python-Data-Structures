import sys
sys.path.append("/Users/tanliangwei/Desktop/Summer 2019/Algorithms 1/python_datastructures/Graph")
from dfs import DFS, check_cycle
from graph import Graph, VertexGraph, Vertex

V = {"Singapore", "Tokyo", "Shanghai", "Kualar Lumpur", "Hong Kong", "Seoul", 
	"Mumbai", "London", "Paris", "San Francisco", "Iceland", "New York",
	"Boston"}


E = {("Singapore", "Tokyo"), ("Singapore", "Shanghai"), ("Tokyo", "Shanghai"), ("Singapore", "Kualar Lumpur"),
	("Singapore", "Mumbai"), ("Kualar Lumpur", "Hong Kong"), ("Hong Kong", "San Francisco"), ("Tokyo", "Kualar Lumpur"),
	("Tokyo", "Seoul"), ("Tokyo", "San Francisco"), ("Shanghai", "San Francisco"), ("San Francisco", "Boston"),
	("San Francisco", "New York"), ("Singapore", "Hong Kong"), ("Mumbai", "Paris"), ("Mumbai", "London"),
	("Boston", "Iceland"), ("New York", "Iceland"), ("Boston", "London"), ("Boston", "Paris"), ("New York", "Boston"),
	("New York", "Paris"), ("Paris", "Iceland"), ("London", "Iceland")};

country_dict = {}

class Country(Vertex):
	def __init__(self, name=None):
		Vertex.__init__(self)
		self.name = name

	def __repr__(self):
		return repr(self.name)

def create_graphs(V, E):
	graph = Graph(directed = True)
	vertex_graph = VertexGraph(directed = True)
	set_of_country = set()
	set_of_edge = set()
	for v in V:
		temp_country = Country(v)
		set_of_country.add(temp_country)
		country_dict[v] = temp_country
	for e in E:
		u, v = e
		temp_edge = (country_dict[u], country_dict[v])
		set_of_edge.add(temp_edge)
	graph.make_graph(V, E)
	vertex_graph.make_graph(set_of_country, set_of_edge)
	return graph, vertex_graph

def find_path(source, target, graph):
	def target_check(u, v):
		return v==target
	parent = DFS(graph = graph, root = source, check_terminate = target_check)
	print("Parent: ", parent)
	path = [target]
	cur_country = target
	while parent[cur_country] is not None:
		parent_country = parent[cur_country]
		path.append(parent_country)
		cur_country = parent_country
	path.reverse()
	return path

def test_dfs(graph1, graph2, source, target):
	path_1 = find_path(source, target, graph1) 
	path_2 = find_path(country_dict[source], country_dict[target], graph2)



graph, vertex_graph = create_graphs(V, E)
# test_dfs(graph, vertex_graph, "Singapore", "Iceland")
print(check_cycle(graph))



