'''
	Magic Index : A magic index in an array A[1 ... n-1] is defined to be an index such that A[i] = i. Given a sorted array of distinct integers, write a method to find a magic index, if one exists in an array A. 

	Follow Up : What if the values are not distinct 
'''

# What if elements are not distinct? 
def magic_index_fast2(arr, start, end):
	# print ('end: ', end, ' start: ', start)
	if (end < start):
		return -1

	mid_index = int((start + end) / 2)
	mid_value = arr[mid_index]
	if (mid_value == mid_index):
		return mid_index

	# Search left 
	left_index = min(mid_index - 1, mid_value)
	left = magic_index_fast2(arr, start, left_index)
	# print ("left: ", left)
	if (left >= 0):
		return left

	# Search right
	right_index = max(mid_index+1, mid_value)
	right = magic_index_fast2(arr, right_index, end)
	if (right >= 0):
		return right

# classic binary search problem
def magic_index_fast(arr, start, end):

	# this method must assume that array is sorted 
	
	mid = int((start + end) / 2)

	if (end < start):
		return None

	if (arr[mid] == mid):
		return mid
	elif (arr[mid] > mid):
		return magic_index_fast(arr, 0, mid - 1)
	else:
		return magic_index_fast(arr, mid+1, end)

# brute force 
def magic_index_slow(arr):
	for i in range (len(arr)):
		if (arr[i] == i):
			return i

	return None

def check_exist(ret_val):
	print ("ret_val: ",ret_val)
	if ret_val == None:
		print ("magic index does not exist !!!")

	else:
		print ("magic index does exist !!! ")


if __name__ == '__main__':

	arr = [-40, -20, -1, 1, 2, 3, 5, 7, 9, 12, 13]

	magic_index_exist1 = magic_index_slow(arr)
	check_exist(magic_index_exist1)

	arr.sort()

	magic_index_exist2 = magic_index_fast(arr, 0, len(arr)-1)
	check_exist(magic_index_exist2)

	arr_not_distinct = [-1, -1, 2, 2, 2, 4, 5, 7, 9, 12]

	arr_not_distinct.sort()

	magic_index_exist3 = magic_index_fast2(arr_not_distinct, 0, len(arr_not_distinct) - 1)
	check_exist(magic_index_exist3)
