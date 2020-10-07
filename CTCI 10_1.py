# Sorted Merge: You are given two sorted arrays, A and B, where A has a large enough buffer at the end to hold B. Write a method to merge B into A in sorted order.

def sortedMerge (arr1, arr2):
	arr = arr1+arr2
	arr.sort()

	return arr

if __name__ == '__main__': 
	print ("This is implementation of Sorted Merge")

	arr1 = [ 8, 23, 10,  1,  9, 25,  3, 19,  5,  4]

	arr2 = [95, 16,  5, 33, 43] 

	print (sortedMerge (arr1, arr2))