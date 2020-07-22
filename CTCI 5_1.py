'''
	Insertion : You are given two 32-bit numbers, N and M and two bit positions, i and j. Write a method to insert M into N such that M starts at bit j and ends at bit i. You can assume that bits j through i have enough space to fit all of M. That is if M = 10011, you can assume that there are at least 5 bits between j and i. You would not for example, have j=3 and i=2, because M could not fully fit between bit 3 and bit 2.

	Example:
	Input  : N = 10000000000, M = 10011, i  = 2, j = 6
	Output : N = 10001001100 

	Solution:
	1. Clear the bits j through i in N
	2. Shift M so that it lines up with bits j through i
	3. Merge M and N
'''

def bit_insertion(n, m, i, j):
	m = int(m, 2)
	n = int(n, 2) 

	# This can specify how many bits
	allones = ~0

	# for example i = 2, j = 4
	# 1s before position j, then 0s. left = 11100000
	left_mask = (allones << (j+1))

	# 1s after position i. right = 11100011
	right_mask = ((1 << i) - 1)

	# Combine both mask
	mask = left_mask | right_mask

	# Clear bits j through i then put m in there
	n_cleared = n & mask

	m_shifted = m << i

	result = n_cleared | m_shifted

	# convert binary to string
	return bin(result)[2:] 

if __name__ == '__main__':
	print ("This is the implementation of bit insertion CTCI 5_1")

	N = '10000000000'
	M = '10011'
	i = 2
	j = 6

	result = bit_insertion(N, M, i, j)

	print (result)
