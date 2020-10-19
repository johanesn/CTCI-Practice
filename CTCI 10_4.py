# Sorted Search, No Size: You are given an array-like data structure Listy which lacks a size method. It does, however, have an elementAt(i) method that returns the element at index i in O(1) time. If i is beyond the bounds of the data structure, it returns -1 (for this reason, the data structure only supports positive integers). Given a Listy which contains sorted, positive integers, find the index at which an element x occurs. if x occurs multiple times, you may return any index. 

# It seems not knowing the length of the array does not really impact our time complexity because, findPos at O (log n) and binary search done in O (log n)
def binarySearch (arr, left, right, x):
	if right >= left:
		mid = int (left + (right-left)/2)

		if (arr[mid] == x):
			return mid

		if arr[mid] == x:
			return (arr, left, mid-1, x)

		return binarySearch(arr, mid+1, right, x)

	return -1

def findPos (arr, x):
	low, high, val = 0, 1, arr[0]

	# this is for finding the position first 
	# has two pointer and update two pointer 2*low because to simplification the speed O(log n)
	while val < x:
		low = high
		high = 2 * high 
		val = arr[high]

	return binarySearch (arr, low, high, x)

if __name__ == '__main__':	
	arr = [3, 5, 7, 9, 10, 90, 100, 130, 140, 160, 170]
	res = findPos (arr, 10)

	if res == -1:
		print ("Element not found")

	else:
		print ("Element found at index: ", res)
