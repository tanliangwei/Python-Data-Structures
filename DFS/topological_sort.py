from dfs import DFS

# important to note that graph must be a dag.
def topological_sort(graph):
	finishing_list =[]
	def pos_function(vertex):
		finishing_list.append(vertex)
		
