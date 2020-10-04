# Merge Sort O(nlogn) average and worst case. Memory: depends 			

def mergeSort (arr):
	print ("Splittig ", arr)

	if len(arr) > 1:
		mid = int(len(arr) / 2)
		left_half = arr[:mid]
		right_half = arr[mid:]

		mergeSort(left_half)
		mergeSort(right_half)

		i, j, k = 0, 0, 0

		# traverse both lists and each iteration and add smaller of both elements 
		while ((i < len(left_half)) and (j < len(right_half))):
			if left_half[i] < right_half[j]:
				arr[k] = left_half[i]
				i = i+1
			else:
				arr[k] = right_half[j]
				j = j+1

			k = k+1

		# add remaining elements on half left
		while (i < len(left_half)):
			arr[k] = left_half[i]
			i = i+1
			k = k+1

		# add remaining elements of half right
		while (j < len(right_half)):
			arr[k] = right_half[j]
			j = j+1
			k = k+1

		print ("Merging ", arr)

if __name__ == '__main__':
	print ("This is the implementation of merge sort")

	arr = [14, 7, 3, 12, 9, 11, 6, 2]
	print (mergeSort (arr))

