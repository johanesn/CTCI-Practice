'''
	Binary to String: Given a real number between 0 and 1 (e.g., 0.72) that is passed in as a double, print the binary representation. If the number cannot be represented accurately in binary with at most 32 characters, print "ERROR"

'''

def bin_to_string (num):
	if (num >= 1 or num <= 0):
		return "ERROR"

	result = []

	while num and len(result) <= 32:
		num = num * 2

		if num >= 1:
			result.append ('1')
			num = num - 1
		else: 
			result.append('0')

		if (len(result) >= 32):
			raise ValueError ('ERROR Len > 32 bit')

	return '.' + ''.join(result)

if __name__ == '__main__' :
	print ("This is the implementation of Binary to String CTCI 5_2")

	num = 0.3125

	print (bin_to_string(num))