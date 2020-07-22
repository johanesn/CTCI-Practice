

def has_lucky_numbers(nums):
	result = False
	for num in nums:
		if num % 7 == 0:
			result = True

	return result


if __name__ == '__main__':

	nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

	print (has_lucky_numbers (nums))