# Chapter 2 : Linked List Implementation 

# Linked list does not provide constant time access to a particular index, you have to traverse

# The benefit is that you can add and remove items from the beginning of the list in constant time

class Node:

	def __init__ (self, data):
		self.data = data
		self.next = None

	def __str__(self):
		return "<Node: (data is %s), next: %s>" % (self.data, self.next != None)
	def __repr__(self):
		return str(self)


class LinkedList:

	def __init__(self):
		self.head = None

	def insert_head_node(self, data):
		print ("Insert head node operation")
		new_node = Node(data)

		if self.head is None:
			self.head = new_node
			return 

		new_node.next = self.head
		self.head = new_head

	def insert_tail_node (self, data):
		print ("Insert tail node operation")
		new_node = Node(data)

		if self.head is None:
			self.head = new_node
			return 

		# traverse to the end of the node
		curr = self.head
		while curr.next:
			curr = curr.next

		curr.next = new_node

	def insert_after (self, prev, data):
		if prev is None:
			print ("The given previous node must inline")
			return

		new_node = Node(data)
		new_node.next = prev.next
		prev.next = new_node

	# 2.3 Delete middle node (similar but input is key, so need to traverse)
	def delete_node (self, key):
		print ("Delete node operation")
		curr = self.head

		if (curr is not None):
			if (curr.data == key):
				self.head = curr.next
				curr = None
				return

		while (curr is not None):
			if curr.data == key:
				break
			prev = curr 
			curr = curr.next

		# key is not present on the linked list
		if curr is None:
			print ("That item does not exist")
			return

		prev.next = curr.next

		curr = None



	# 2.1 Write code to remove duplicates from unsorted linked list 
	def remove_duplicates (self, WITH_BUFFER = 1):
		prev = None
		curr = self.head
		if WITH_BUFFER: 
			# use a hash table which is a dict in python
			temp_list = []
			print ("Remove duplicates using additional buffer")
			while curr is not None:
				if curr.data in temp_list:
					prev.next = curr.next
				else:
					temp_list.append(curr.data)
					prev = curr
				curr = curr.next
		else: 
			# use two pointers
			pass

	# 2.2 Return K-th to last : Implement algorithm to find the K-th to last element of singly linked list
	def return_kth_to_last(self, k, OPTIONS = 2):
		# solution 1 : using known linked list size
		if OPTIONS == 1:
			# passed because too trivial just return lenght - K element
			pass

		# solution 2 : using iterative method, two pointers
		elif OPTIONS == 2:
			p1, p2 = self.head, self.head

			for i in range (k):
				if not p1:
					return
				p1 = p1.next
			while p1 is not None:
				p1, p2 = p1.next, p2.next

			return p2.data


	def print_linked_list(self):
		print ("\nPrint linked list content operation")
		curr = self.head
		while (curr):
			print (curr.data, end = ' ')
			curr = curr.next
		print ('\n')
if __name__ == '__main__':

	LinkedListObject = LinkedList()

	LinkedListObject.insert_tail_node (1)
	LinkedListObject.insert_tail_node (2)
	LinkedListObject.insert_tail_node (3)
	LinkedListObject.insert_tail_node (4)
	LinkedListObject.insert_tail_node (5)
	LinkedListObject.insert_tail_node (6)
	LinkedListObject.insert_tail_node (7)

	LinkedListObject.print_linked_list()

	# test delete middle node
	LinkedListObject.delete_node(5)
	LinkedListObject.delete_node(8)
	LinkedListObject.print_linked_list()

	# test remove duplicates
	LinkedListObject.insert_tail_node(1)
	LinkedListObject.insert_tail_node(2)
	LinkedListObject.insert_tail_node(7)
	LinkedListObject.insert_tail_node(8)
	LinkedListObject.remove_duplicates()
	LinkedListObject.print_linked_list()

	# test return kth elements from last 
	kth_element = LinkedListObject.return_kth_to_last(1)
	print ("The kth element from last of single linked list is: ", kth_element)
