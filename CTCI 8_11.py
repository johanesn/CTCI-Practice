'''
	Coins : Given an infinite number of quarters (25 cents), dimes (10 cents), nickels (5 cents), and pennies (1 cent), write code to calculate the number of ways of representing n cents.
'''

# bottom up solution because there is overlapping subproblem
# solutions from tutorial point
def count(S, m, n):
   	# base case
	table = [[0 for x in range(m)] for x in range(n+1)]
  
	# for n = 0
	for i in range(m):
		table[0][i] = 1

	# rest values are filled in bottom up manner
	for i in range(1, n+1):
		for j in range(m):
			# solutions including S[j]
			x = table[i - S[j]][j] if i-S[j] >= 0 else 0
			# solutions excluding S[j]
			y = table[i][j-1] if j >= 1 else 0
			# total
			table[i][j] = x + y
		# print (table)
		# print (i, " ", j, ": ", table[i][j])

	return table[n][m-1]

if __name__ == "__main__":
	arr = [1, 5, 10]
	m = len(arr)
	n = 10
	print("Number of coins: ",end="")
	print(count(arr, m, n))