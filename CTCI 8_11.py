'''
	Coins : Given an infinite number of quarters (25 cents), dimes (10 cents), nickels (5 cents), and pennies (1 cent), write code to calculate the number of ways of representing n cents.
'''

def coins (n,):
	if n == 0:
		return 1

	if n < 0:
		return 0:


if __name__ == '__main__':
	n = [25, 10, 5, 1]

	result = coins (n)

	print ('result: ', result)