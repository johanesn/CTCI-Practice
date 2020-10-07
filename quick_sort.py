# Quick Sort | Runtime: O(n log n) average O(n^2) and memory: O(logn)

# use divide and conquer like merge sort but without additional storage

# trade off is if the list is not divided as half, the advantage is diminished

'''
	1. selects a value, which is called the pivot value (many methods), use first item here
	2. has leftmark and rightmark
	3. leftmark will move to scanning right until it finds a value > pivot value.
	4. rightmark will move to scanning left until it finds a value < pivot value.
'''

def quickSort (arr):
	quickSortHelper (arr, 0, len(arr)-1)

def quickSortHelper (arr, first, last):
	if first < last:
		split_point = partition (arr, first, last)
		# print('split_point: ', split_point)
		quickSortHelper(arr, first, split_point-1)
		quickSortHelper(arr, split_point+1, last)

def partition (arr, first, last):
	pivot_value = arr[first]

	left_mark = first+1
	right_mark = last

	done = False
	while not done:
		while left_mark <= right_mark and arr[left_mark] <= pivot_value:
			left_mark = left_mark + 1
		while right_mark >= left_mark and arr[right_mark] >= pivot_value:
			right_mark = right_mark -1

		if right_mark < left_mark:
			done = True
		else:
			temp = arr[left_mark]
			arr[left_mark] = arr[right_mark]
			arr[right_mark] = temp

	temp = arr[first]
	arr[first] = arr[right_mark]
	arr[right_mark] = temp

	return right_mark

if __name__ == '__main__':
	arr = [54, 26, 93, 17, 77, 31, 44, 55, 20]

	quickSort(arr)
	print(arr)