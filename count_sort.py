# Counting Sort

# Time and space complexity O(n+k)
def count_sort(arr):
	output = [0 for i in range (len(arr))]
	# print("output: ", output)

	count = [0 for i in range(256)]
	# print("count: ", count)

	ans = ["" for i in arr]
	# print("ans: ", ans)

	for i in arr:
		count[ord(i)] += 1

	for i in range(256):
		count[i] = count[i] + count[i-1]

    # Build the output character array 
	for i in range(len(arr)): 
		output[count[ord(arr[i])]-1] = arr[i] 
		count[ord(arr[i])] -= 1
  
    # Copy the output array to arr, so that arr now 
    # contains sorted characters 
	for i in range(len(arr)): 
		ans[i] = output[i]  

	return ans

def count_sort2(arr):
    max_element = int(max(arr)) 
    min_element = int(min(arr)) 
    range_of_elements = max_element - min_element + 1
    # Create a count array to store count of individual 
    # elements and initialize count array as 0 
    count_arr = [0 for _ in range(range_of_elements)] 
    output_arr = [0 for _ in range(len(arr))] 
  
    # Store count of each character 
    for i in range(0, len(arr)): 
        count_arr[arr[i]-min_element] += 1
  
    # Change count_arr[i] so that count_arr[i] now contains actual 
    # position of this element in output array 
    for i in range(1, len(count_arr)): 
        count_arr[i] += count_arr[i-1] 
  
    # Build the output character array 
    for i in range(len(arr)-1, -1, -1): 
        output_arr[count_arr[arr[i] - min_element] - 1] = arr[i] 
        count_arr[arr[i] - min_element] -= 1
  
    # Copy the output array to arr, so that arr now 
    # contains sorted characters 
    for i in range(0, len(arr)): 
        arr[i] = output_arr[i] 
  
    return arr 
if __name__ == '__main__':
	
	print("This is the implementation of count sort ")

	arr = "geeksforgeeks"
	# only can sort char and no negative numbers 
	ans = count_sort(arr)
	print("Sorted character array is % s" %("".join(ans))) 

	arr = [10, 9, 8, 7, 20, 30, 1, 0]
	ans = count_sort2 (arr)
	print("Sorted character array is " + str(ans)) 