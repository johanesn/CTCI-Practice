# Queue via Stacks : Implement MyQueue class which implements a queue using two stacks

''' 
	Can be done using two methods 
		1. By making enqueue operation costly --> O(n) but dequeu cheap or
		2. By making dequeue operation costly --> O(n) but enqueue cheap

		In here, we implement the first method

		enqueue (self, item):
			- while first_stack is not empty, push everything from first_stack to second_stack
			- push item to first_stack 
			- push everything back to first_stack
			- O(n) complexity

		dequeue(self):
			- if first_stack empty, raise exception
			- pop an item from first_stack
			- O(1) complexity


'''

from Stacks import Stacks 

class MyQueue:
	def __init__(self):
		self.first_stack = Stacks() # push item
		self.second_stack = Stacks() 

	# expensive enqueue operation 
	def enqueue (self, item):
		while len (self.first_stack.stack) != 0:
			self.second_stack.push_item(self.first_stack.stack[-1])
			self.first_stack.pop_item()

		self.first_stack.push_item(item)

		while len(self.second_stack.stack) != 0:
			self.first_stack.push_item(self.second_stack.stack[-1])
			self.second_stack.pop_item()

	# cheap dequeue operation 
	def dequeue (self):
		if (self.first_stack.is_empty()):
			raise Exception ("This stack is empty, bad dequeue operation")

		dequeue_item = self.first_stack.stack[-1]

		self.first_stack.pop_item()
		return dequeue_item

if __name__ == '__main__':
	print ("This is implementation of CTCI 3_4")

	QueueObject = MyQueue()
	QueueObject.enqueue(10)
	QueueObject.enqueue(20)
	QueueObject.enqueue(30)

	print (QueueObject.first_stack.stack)

	print ("Dequeue item: ",QueueObject.dequeue())
	print ("Dequeue item: ",QueueObject.dequeue())

