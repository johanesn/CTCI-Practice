'''
	Triple Step: A child is running up a staircase with n steps and can hop either 1 step, 2 steps or 3 steps at a time. Implement a method to count how many possible ways the child can run up the stairs.

	n == 1 --> (1) --> 1
	n == 2 --> (1,1),(2) --> 2
	n == 3 --> (1,1,1), (1,2), (2,1), (3) --> 4
	n == 4 --> (1,1,1,1), (1,2,1),(1,1,2),(2,1,1), (2,2), (3,1), (1,3), (4) --> 7
'''



def TripleStepRecursive (n):
	if (n == 1 or n ==0):
		return 1
	elif n == 2:
		return 2
	else:
		return TripleStepRecursive(n-3) + TripleStepRecursive(n-2) + TripleStepRecursive(n-1)

def TripleStepDP (n):
	step = [0] * (n+1)
	step[0] = 1
	step[1] = 1
	step[2] = 2

	for i in range (3, n+1):
		step[i] = step[i-1] + step[i-2] + step[i-3]

	return step[n]

if __name__ == '__main__':
	print ("This is the implementation of CTCI 8_1: Triple Step")

	n_steps = 4

	print ("Find Steps: ", TripleStepRecursive(n_steps))

	print ("Find steps: ", TripleStepDP(n_steps))