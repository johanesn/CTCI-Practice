'''
	Coins : Given an infinite number of quarters (25 cents), dimes (10 cents), nickels (5 cents), and pennies (1 cent), write code to calculate the number of ways of representing n cents.
'''

# geeksforgeeks method 

def coins (arr, m, n):
	if (n == 0):
		return 1

	if (n < 0): 
		return 0

	if (m <= 0 and n >= 1):
		return 0

	return coins(arr, m-1, n) + coins(arr, m, n-arr[m-1])

if __name__ == '__main__':
	arr = [25, 10, 5, 1]
	n = 25
	m = len(arr)
	result = coins (arr, m, n)

	print ('result: ', result)