
# Insertion sort
'''
	1. involves the comparison of element with its adjacent element
	2. if can be swap, then swap
	3. repeated until all element in the array is at position
'''

# Bucket Sort(Radix Sort)
# to sort large set of floating point numbers
'''
	Algorithm :
	1. Create n empty buckets (or lists)
	2. Do the following for every array element arr[i]
		a) Insert arr[i] into bucket [n * arr[i]]
	3. Sort individual buckets using insertion sort 
	4. Concatenate all sorted buckets 
'''

def insertion_sort (arr):
	for i in range (1, len(arr)):	
		key = arr[i]
		j = i-1
		while j>=0 and arr[j] > key:
			arr[j+1] = arr[j]
			j = j-1
		arr[j+1] = key
	return arr 

def bucket_sort (arr):
	arr_bucket = []
	slot_num = 10

	for i in range (slot_num):
		arr_bucket.append([])

	# put array elements in different buckets
	for j in arr:
		index_arr = int(slot_num * j)
		arr_bucket[index_arr].append(j)

	# sort each bucket
	for i in range (slot_num):
		arr_bucket[i] = insertion_sort(arr_bucket[i])

	# concatenate
	k = 0
	for i in range (slot_num):
		for j in range (len(arr_bucket[i])):
			arr[k] = arr_bucket[i][j]
			k = k+1

	return arr


if __name__ == '__main__':
	print ("This is the implementation of bucket sort")

	arr = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]

	print("Sorted array is: ", bucket_sort(arr))