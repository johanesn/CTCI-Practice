# Chapter 3 : Stacks Implementation
'''
	pop()       : Remove the top item from stack
	push(item)  : Add an item to the top of the stack
	peek()      : Return the top of the stack
	isEmpty()   : Return true only if the stack is empty

	allow constant time adds and removes
	can be implemented using array or linked list
'''
from sys import maxsize

class Stacks:
	# implement stack using array
	def __init__(self):
		self.stack = []

	def is_empty(self):
		return len(self.stack) == 0

	def push_item(self, item):
		self.stack.append(item)
		print (str(item) + " is pushed to the stack")

	def pop_item(self):
		if (self.is_empty()):
			return str(-maxsize - 1)
		popped_item = self.stack.pop()
		print (str(popped_item) + " is popped from the stack")
		return popped_item

	def peek(self):
		if (self.is_empty()):
			return str(-maxsize-1)

		return self.stack[len(self.stack) - 1]


class StackNode:
	def __init__(self, data):
		self.data = data
		self.next = None
 
class Stacks2:
	# implement stack using linked list

	def __init__(self):
		self.head = None

	def is_empty(self):
		if self.head is None:
			return True
		else:
			return False

	def push_item (self, data):
		new_node = StackNode(data)
		new_node.next = self.head
		self.head = new_node
		print (str(data) + " is pushed to the stack")

	def pop_item(self):
		if (self.is_empty()):
			return float("-inf")

		popped_item = self.head.data 
		temp = self.head.next
		self.head = temp

		print (str(popped_item) + " is popped from the stack")

	def peek (self):
		if (self.is_empty()):
			return float("-inf")
		return self.head.data 


if __name__ == '__main__':
	print ("This is chapter 3 implementation of Cracking The Coding Interview\n")

	print ("1st : Implementation using array ")
	MyStack = Stacks()
	MyStack.push_item(10)
	MyStack.push_item(20)
	MyStack.push_item(30)
	MyStack.push_item(40)

	MyStack.pop_item()
	MyStack.pop_item()
	peeked_item = MyStack.peek()
	print (str(peeked_item) + " is peeked from the stack")

	# ================================================================================== #
	print ("\nImplementation using linked list\n")

	MyStack2 = Stacks2()
	MyStack2.push_item(10)
	MyStack2.push_item(20)
	MyStack2.push_item(30)
	MyStack2.push_item(40)

	MyStack2.pop_item()
	MyStack2.pop_item()
	MyStack2.pop_item()

	MyStack2.push_item(50)
	MyStack2.push_item(60)

	MyStack2.pop_item()
	MyStack2.pop_item()

	peeked_item = MyStack2.peek()

	print (str(peeked_item) + " is peeked from the stack")



