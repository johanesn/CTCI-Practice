# Find Duplicates : You have an array of N numbers, where N is at most 32000. The array may have duplicate entries and you do not know what N is. With only 4 KB of memory available, how would print all duplicate elements in the entry?

# 4 KB = 4 * 8 * 2^10 bits and greater than 32000. we can create a bit with 32000 bits, where each bit represents an integer

class BitArray:
	def __init__ (self, n):

		# Divide by 32. To store n bits, we need n/32+1 integers 
		self.arr = [0] * ((n >> 5)+1)
		# print (self.arr)

	def getValue (self, pos):

		# divide by 32 to find the position of the integer
		self.index = pos >> 5
		# no find bit number in arr[index]
		self.bitNo = pos & 0x1F
		# print (self.arr)
		# find value of given bit number in arr[index]
		return (self.arr[self.index] & (1 << self.bitNo)) != 0

	def setValue (self, pos):
		self.index = pos >> 5
		self.bitNo = pos & 0x1F
		self.arr[self.index] |= (1 << self.bitNo)
		# print (self.arr)
def checkDuplicates (arr):

	# create a bit array with 32000 bits
	bit_array = BitArray (32000)

	# Traverse array elements
	for i in range (len(arr)):
		num = arr[i]

		if bit_array.getValue(num):
			print (num, end = " ")
		else:
			bit_array.setValue(num)

if __name__ == '__main__':

	arr = [1, 5, 1, 10, 12, 10]
	checkDuplicates(arr)

