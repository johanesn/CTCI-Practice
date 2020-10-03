# selection sort 

'''
	arr[] = 64 25 12 22 11

	1. find the minimum element in arr[0..4] and place it in the beginning
	11 25 12 22 64

	repeat until finish 
'''
def selection_sort(arr):
	for i in range (len(arr)):
		min_idx = i
		for j in range (i+1, len(arr)):
			if arr[j] < arr[min_idx]:
				min_idx = j

		arr[i], arr[min_idx] = arr[min_idx], arr[i]

	return arr   


if __name__ == '__main__':
	print ("This is the implementation of selection sort")

	arr = [10, 9, 8, 7, 1, 5, 100, 99, 0, 20, 3]

	print (selection_sort (arr))