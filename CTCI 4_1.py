'''
	Routes Between Nodes: Given a directed Graph, design an algorithm to find out whether there is route between nodes

	This can be solved by using BFS or DFS. Talking to the interviewer about both pros and cons
	might add more points

'''

def path_bfs(start, end, graph):
	path, visited = [start], [start]

	while path:
		current_node = path.pop(0)
		for child in graph.get(current_node, []):
			if child == end:
				return True
			if not child in visited:
				visited.append(child)
				path.append(child)
	return False

def path_dfs (start, end, graph):
	path = [start]
	visited = [start]

	while path : 
		current_node = path.pop()
		for child in graph.get(current_node, []):
			if child == end:
				return True

			if not child in visited:
				visited.append(child)
				path.append(child)
	return False

if __name__ == '__main__':
	print ("This is implementation of CTCI 4_1, Routes Between Nodes")

	graph = {'A': ['B', 'C'],
         	 'B': ['A', 'D', 'E'],
         	 'C': ['A', 'F'],
         	 'D': ['B'],
         	 'E': ['B', 'F'],
         	 'F': ['C', 'E'],
         	 'G': []}

	print (path_dfs('A','F', graph))
	print (path_bfs('A','F', graph))