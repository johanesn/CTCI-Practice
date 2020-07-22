# Binary Heap

'''
	1) It is a complete tree (all levels are completely filled except possibly the last level and last level has all keys as left as possible)
	2) Binary Heap is either a Min Heap or Max Heap. 

	These properties makes them suitable to be stored in an array

	Applications of Heaps:
	1) Heap Sort : uses binary heap to sort array in O (n log n) time
	2) Priority Queue 
	3) Graph Allgorithms : Djikstra Shortest Path and Prim's Minimum Spanning Tree
	4) Problems like K'th Largest Element in Array, Sort an Almost Sorted Array, Merge K Sorted Arrays

'''


''' 
Operations on Min Heap:
	1) get_minimum() : returns the root element of Min Heap, Time Complexity O(1)
	2) extract_minimum() : removes the minimum element from Min Heap ; O (log n), need to maintain heap property by calling heapify()
	3) decrease_key() : decreases value of key. the time complexity of this operation is O(logn)
	4) insert_key() : inserting a new key takes O(logn) time. We add new key at the end of the tree. If new key is greater than its parent, 
				  we don't need to do anything. Otherwise, we need to travse up to fix violated heap
	5) delete_key() : deleting a ey also takes O(logn) time. 

'''

from heapq import heappush, heappop, heapify

class MinHeap:
	def __init__(self):
		self.heap = []

	def parent(self, i):
		return int ((i-1)/2)

	def extract_min(self):
		return heappop (self.heap)

	def decrease_key(self, i, new_val):
		# decrease value at index 'i' to new_val (assuming new_val is smaller than heap[i])
		self.heap[i] = new_val
		while (i != 0 and self.heap[self.parent(i)] > self.heap[i]):
			self.heap[i], self.heap[self.parent(i)] = (self.heap[self.parent(i)], self.heap[i])
			i = self.parent(i)

	def insert_key(self, k):
		heappush (self.heap, k)

	def delete_key(self, i):
		# to delete key at index i, first reduce value to minus infinite and calls extractmin
		self.decrease_key (i, float("-inf"))
		self.extract_min()

	def get_min(self):
		return self.heap[0]

if __name__ == '__main__':
	MinHeapObject = MinHeap()

	MinHeapObject.insert_key(3)
	MinHeapObject.insert_key(2)
	MinHeapObject.delete_key(1)
	MinHeapObject.insert_key(15)
	MinHeapObject.insert_key(5)
	MinHeapObject.insert_key(4)
	MinHeapObject.insert_key(45)

	print (MinHeapObject.extract_min())
	print (MinHeapObject.get_min())
	MinHeapObject.decrease_key(2,1)
	print (MinHeapObject.get_min())
