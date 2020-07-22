'''
	Recursive Multiply: Write a recursive function to multiply two positive integers without using the * operator. You can use addition, substraction and bit shifting, but you should minimize the number of those operation
'''

def recursive_multiply (a, b):
	print ('a: ', a, ' b: ',b)
	if a < b:
		return recursive_multiply(b,a)

	elif b!=0:
		return (a + recursive_multiply(a, b-1))

	else:
		return 0


if __name__ == '__main__':

	a, b = 10, 20

	result = recursive_multiply (a, b)

	print ('result: ', result)