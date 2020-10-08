# Search in Rotated Array: Given a sorted array of n integers that has been reotated an unknown number of times, write code to find an element in the array. You may assume that the array was originally sorted in increasing order.

# need to find it in O(logn)

'''
	1. The idea is to find the pivot point (which is next element to it is smaller than it)
	2. Use binary search 
	3. After finding pivot, divide the array into two sub arrays
	4. Now the individual sub - arrays are sorted so the element can be searched using Binary Search
'''

def search (arr, left, right, x):
	mid = int(left + (right-left)/2)
	if x == arr[mid]:
		return mid
	if (right < left):
		return -1

	if (arr[left] < arr[mid]):
		if (x >= arr[left] and x < arr[mid]):	
			return search (arr, left, mid-1, x)
		else:
			return search (arr, mid+1, right, x)

	elif (arr[mid] < arr[right]):
		if (x > arr[mid] and x <= arr[right]):
			return search (arr, mid+1, right, x)
		else:
			return search (arr, left, mid-1, x)

	# left or right half is all repeats
	elif (arr[left] == arr[mid]):
		return search (arr, mid+1, right, x)
	else:
		result = search (arr, left, mid-1, x)

		if (result == -1):
			return search (arr, mid+1, right, x)
		else:
			return result

	return -1

if __name__ == '__main__':
	print ("This is the implementation of Search in Rotated Array")

	arr = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]
	x = 25

	print(search(arr, 0, len(arr)-1, x))