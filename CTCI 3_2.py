# 3.2 Stack Min : How would you design a stack which, in addition to push and pop, has a function min which returns the min element

'''
	Can be easily done if we keep track of the minimum value at each operation (push and pop)
	Probem 
'''

# from sys import maxsize

class StackMin():
	def __init__(self):
		self.stack = []
		self.min = float('inf')

	def push_item (self, item):
		if item < self.min:
			# self.stack.append (self.min)
			self.min = item
		self.stack.append(item)

	def pop_item (self):
		temp = self.stack[-1]
		self.stack.pop()

		if temp == self.min:
			self.min = self.stack[-1]
			self.stack.pop()

	def get_min(self):
		return self.min


if __name__ == '__main__':
	print ("Implementation of 3_2 of CTCI")

	StackMinObject = StackMin()

	StackMinObject.push_item(40)
	StackMinObject.push_item(50)
	StackMinObject.push_item(10)
	StackMinObject.push_item(20)
	StackMinObject.push_item(30)

	print (StackMinObject.stack)
	min_item = StackMinObject.get_min()
	print ('Minimum value: ', min_item)

	StackMinObject.pop_item()
	StackMinObject.pop_item()
	StackMinObject.pop_item()

	print (StackMinObject.stack)
	min_item = StackMinObject.get_min()
	print ('Minimum value: ', min_item)

