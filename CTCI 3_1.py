# 3.1. Describe how you could use a single array to implement three stacks 

class MultiStack:
	def __init__(self):
		self.array = [None, None, None]
		self.current = [0, 1, 2]

	def push_item (self, item, stack_number):
		if not stack_number in [0, 1, 2]:
			raise Exception("Bad stack number")

		while (len(self.array) <= self.current[stack_number]):
			self.array += [None] * len(self.array)
		self.array[self.current[stack_number]] = item
		self.current[stack_number] += 3

	def pop_item (self, stack_number):
		if not stack_number in [0, 1, 2]:
			raise Exception ("Bad stack number")
		if self.current [stack_number] > 3 : 
			self.current [stack_number] -= 3
		item = self.array [self.current[stack_number]]
		self.array[self.current[stack_number]] = None

		return item
	def print_stack (self):
		print (self.array)
		print (self.current)

if __name__ == '__main__':
	print ("Implementation of 3_1 of CTCI")

	MultiStackObject = MultiStack()
	MultiStackObject.push_item(101, 0)
	MultiStackObject.push_item(102, 0)
	MultiStackObject.push_item(103, 0)
	MultiStackObject.push_item(104, 0)

	MultiStackObject.push_item(201, 1)
	MultiStackObject.push_item(202, 1)
	MultiStackObject.push_item(203, 1)
	MultiStackObject.push_item(204, 1)

	MultiStackObject.push_item(301, 2)
	MultiStackObject.push_item(302, 2)
	MultiStackObject.push_item(303, 2)
	MultiStackObject.push_item(304, 2)
	# MultiStackObject.push_item(401, 3)
	MultiStackObject.print_stack()

	MultiStackObject.pop_item(0)
	MultiStackObject.print_stack()