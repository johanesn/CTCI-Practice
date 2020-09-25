# Bubble Sort; Runtime: O(n^2) average and worst case ; Memory: O(1)

def bubble_sort (arr):

	for i in range (len(arr)-1):
		for j in range (len(arr) - i - 1):	
			if (arr[j+1] < arr[j]):
				arr[j], arr[j+1] = arr[j+1], arr[j]
	return arr 
if __name__ == '__main__':
	print ("This is the implementation of bubble sort")

	arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 100]

	print(bubble_sort(arr))