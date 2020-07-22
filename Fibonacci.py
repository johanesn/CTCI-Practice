# Test Fibonacci for recursion and dynammic programming

'''
	Dynamic programming is an algorithmic paradigm that solves a given complex problem by breaking it into subproblems and stores the results of subproblems to avoid computing the same results again.

	Two main properties : Overlapping Subproblems and Optimal Substructure
'''

# top down method, first search at look_up array to find the solution 
def fib_memoization (n, look_up):
	if n == 0 or n == 1:
		look_up[n] = n

	else:
		look_up[n] = fib_memoization(n-1, look_up) + fib_memoization(n-2, look_up)

	return look_up[n]

# bottom up method, literally build the solution bottom up
def fib_tabulation(n):
	fib = [0] * (n+1)

	fib[1] = 1

	for i in range(2, n+1):
		fib[i] = fib[i-1] + fib[i-2]

	return fib[n]

if __name__ == '__main__' :

	print ("This is the implementation of Fibonacci")

	n = 10

	print ("========= Top Down / Memoization Method ======== ")

	look_up = [None] * (101)

	print ("Fibonacci number is : ", fib_memoization(n, look_up))

	print ("========= Bottom Up / Tabulation Method ======== ")

	print ("Fibonacci number is : ", fib_tabulation(n))
