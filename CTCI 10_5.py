# Sparse Search: Given a sorted array of strings that is interspersed with empty strings, write a method to find the location of a given string.

def sparseSearch (arr, key, low, high):
	while low <= high:
		mid = int(low + (high-low)/2)

		if arr[mid] == '':
			left = mid-1
			right = mid+1

			while True:
				print ("inside inf loop")
				# out of bounds check
				if left < low and right > high:
					return -1

				elif left >= low and arr[left] != '':
					# search left
					mid = left
					break
				elif right <= high and arr[right] != '':
					# search right
					mid = right
					break
				left = left - 1
				right = right + 1

		if arr[mid] == key:
			return mid 

		elif arr[mid] > key:
			# search left
			high = mid-1 

		elif arr[mid] < key:
			low = mid+1


	return -1

if __name__ == '__main__':

	arr = ["at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""]
	res = sparseSearch (arr, "ball", 0, len(arr)-1)

	if (res == -1):
		print ("Element not found!")

	else:
		print ("Element found at index: ", res)

