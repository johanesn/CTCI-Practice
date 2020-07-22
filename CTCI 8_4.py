'''
	Power Set: Write a method to return all subsest of a set.
'''
import math

def power_set(set_a):
	all_subsets = []

	set_size = len(set_a)
	pow_set_size = (int) (math.pow(2, set_size))

	for counter in range (pow_set_size):
		subset = []
		for j in range (set_size):
			if ((counter & (1 << j)) > 0):
				subset.append(set_a[j])
		all_subsets.append(subset)

	return all_subsets

if __name__ == '__main__':
	set_a = (1, 2, 3, 4)

	my_power_set = power_set(set_a)

	print (my_power_set)