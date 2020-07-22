# Chapter 3 : Queue Implementation
'''
	add(item) : Add an item to the end of the list
	remove()  : Remove the first item in the list
	peek()    : Return to the top of the queue
	isEmpty() : Return true if and only if the queue is empty

	Implementation in BFS or cache
'''

class QueueNode:
	def __init__(self, data):
		self.data = data
		self.next = None 

class Queues:
	def __init__ (self):
		self.front = self.rear = None

	def enqueue (self, item):
		new_node = QueueNode(item)

		if self.rear == None:
			self.front = self.rear = new_node
		self.rear.next = new_node
		self.rear = new_node 

	def dequeue (self):
		if self.is_empty():
			return

		temp = self.front 
		self.front = temp.next

		if (self.front == None):
			self.rear = None

	def peek(self):
		return self.rear.data 

	def is_empty(self):
		return self.front == None
if __name__ == '__main__':
	print ("Implementation of Queues")

	QueueObject = Queues ()

	QueueObject.enqueue(10)
	QueueObject.enqueue(20)
	QueueObject.enqueue(30)

	QueueObject.dequeue()
	print ("Queue front: ", str(QueueObject.front.data))
	print ("Queue rear: ", str(QueueObject.rear.data))

	peek_value = QueueObject.peek()
	print (peek_value)