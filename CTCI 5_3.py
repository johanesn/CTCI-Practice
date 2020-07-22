'''
	Flip Bit to Win : You have an integer and you can flip exactly one bit from a 0 to a 1. Write code to find the length of the longest sequence of 1s you could create.
'''

def longest_sequence (n):

	if (~n == 0):
		return 8 * sizeof()

	currLen, prevLen, maxLen = 0, 0, 0

	while (n > 0):
		if ((n & 1) == 1):
			currLen += 1
		elif ((n & 1) == 0):
			if ((n & 2) == 0):
				prevLen = 0
			else:
				prevLen = currLen

			currLen = 0

		maxLen = max (prevLen + currLen, maxLen)

		n >>= 1

	return maxLen + 1

if __name__ == '__main__':
	print ("This is the implementation of Flip Bit to Win CTCI 5_3")

	n = 1775 

	print (longest_sequence(n))

