# BFS and DFS

'''
	These two algorithms are to achieve the following goals:
	1. Find all vertices in a subject vertices connected component
	2. Return all available paths between two vertices
	3. And in the case of BFS, return th shortest path (length measured by number of path edges)

	DFS :
	1. Mark the current vertex as being visited
	2. Explore each adjacent vertex that is not included in the visited set
	3. In DFS you have to check if node has been visited or not, otherwise infinite loop 

	BFS : 
	1. Find shortest path (or just any path) between two nodes. 
	2. Uses queue 
'''

def dfs (graph, start):
	visited, visited_list,stack = set(), [], [start]
	while stack:
		vertex = stack.pop()
		if vertex not in visited:
			visited.add(vertex) # using set will out of order printing, so we add list
			visited_list.append(vertex)
			stack.extend(graph[vertex] - visited)
	return visited_list

def recursive_dfs (graph, start, visited = None):
	if visited is None:
		visited = set()

	visited.add(start)
	for next in graph[start] - visited:
		dfs(graph, next, visited)
	return visited
	
# similar to dfs, just replace stack with queue
def bfs (graph, start):
	visited, visited_list,queue = set(), [], [start]
	while queue:
		vertex = queue.pop(0)
		if vertex not in visited:
			visited.add(vertex) # using set will out of order printing, so we add list
			visited_list.append(vertex)
			queue.extend(graph[vertex] - visited)
	return visited_list



if __name__ == '__main__':
	graph = {'A': set(['B', 'C']),
         	 'B': set(['A', 'D', 'E']),
         	 'C': set(['A', 'F']),
         	 'D': set(['B']),
         	 'E': set(['B', 'F']),
         	 'F': set(['C', 'E'])}

	print ("This is implementation of DFS: ")
	print (dfs (graph, 'A'))

	print ("This is implementation of BFS: ")
	print (bfs(graph, 'A'))
