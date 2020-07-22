'''
	This method is highly efficient way to generate list of primes. It works by recognizing that all non-prime numbers are divisible by a prime number
'''

import math

def sieve_of_eratosthenes(max_num):

	flags = [True for i in range (max_num+1)]

	prime = 2

	flags[0] = False
	flags[1] = False

	while (prime <= math.sqrt(max_num)):

		if (flags[prime] == True):
			for i in range (prime * 2, max_num+1, prime):
				flags[i] = False

		prime = prime + 1

	for i in range (max_num + 1):
		if flags[i]:
			print (i, end = " "),

if __name__ == '__main__':

	print ("This is a method to generate list of primes")

	max_num = 100

	sieve_of_eratosthenes(max_num)