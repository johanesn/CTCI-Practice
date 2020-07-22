'''
	Robot in a Grid : Imagine a robot sitting on the upper left corner of grid with r rows and c columns. The robot can only move in two directions, right and down, but certain cells are "off limits" such that the robot cannot step on them. Design an algorithm to find a path for the robot from the top left to the bottom right.

	o o o o o o o o
	o o o o o o o o
	o o o o o o o o
	o o o o o o o o

	o o 
	o o
'''

# exponential method : complexity O(2^(r+c))
def get_path_exponential(maze):
	if len(maze) == 0 or len(maze[0]) == 0:
		return False
	path = []
	if path_finder_exponential(maze, len(maze) - 1, len(maze[0])-1, path):
		return path

	return None 


def path_finder_exponential(maze, row, col, path):
	# if out of bounds or bot available, return.
	if ((col < 0) or (row < 0) or (not maze[row][col])):
		return False

	is_at_origin = (row == 0) and (col == 0)

	# print ('is_at_origin: ', is_at_origin)

	if is_at_origin or path_finder_exponential(maze, row, col-1, path) or path_finder_exponential(maze, row-1, col, path):
		path.append((row, col))
		return True
	return False


# 0 means the point is blocked, 1 is available
if __name__ == '__main__':
	print ("This is the implementation of Robot in a Grid")

	input_path = [[0, 0, 0, 0, 0, 0, 1],
            	  [0, 1, 1, 0, 1, 1, 0],
                  [0, 0, 1, 0, 0, 0, 0],
                  [1, 1, 0, 0, 0, 1, 0]]

	input_path = [[1, 1, 1, 1, 1, 1],
            	  [0, 1, 1, 1, 0, 0],
                  [0, 0, 1, 1, 0, 0],
                  [0, 0, 0, 1, 1, 1],
                  [0, 0, 1, 0, 1, 1]]

	# print (len(input_path)-1, len(input_path[0]))
	print ("Find Path: ", get_path_exponential(input_path))
