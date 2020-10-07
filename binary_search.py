# Binary Search

'''
	Ignore half of the elements after just one comparison

	1. Compare x with middle element
	2. If x matches with middle element, we return the mid index
	3. Else if x is greater, then x can only lie in the right half subarray
	4. Else (x is smaller), recur for left half.
'''

def binarySearch (arr, left, right, x):
	while left <= right:
		mid = int( left + (right - left) / 2) # to avoid overflow

		if arr[mid] == x:
			return mid

		elif arr[mid] <= x:
			left = mid+1

		else:
			right = mid - 1

	return -1



if __name__ == '__main__':
	arr = [2, 3, 4, 10, 40]

	x = 10 # item that we need to find

	result = binarySearch(arr, 0, len(arr)-1, x)

	print (result)