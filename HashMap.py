# Chapter 1 : Hash Map Implementation 

class Node:
	def __init__(self, key, value):
		self.key = key
		self.value = value
		self.next = None

	def __str__(self):
		return "<Node: (%s, %s), next: %s>" % (self.key, self.value, self.next != None)
	def __repr__(self):
		return str(self)


class HashTable:
	def __init__(self):
		self.size = 10
		self.array = [None] * self.size

	def hash_function(self, key):
		hashsum = 0

		for idx, c in enumerate (key):
			hashsum = hashsum + ((idx + len(key)) ** ord(c))
			hashsum = hashsum % self.size

		return hashsum

	def insert (self, key, value):
		# using chaining 
		index = self.hash_function (key)
		print ("Index: ", index)
		node = self.array[index]

		if node is None :
			self.array[index] = Node(key, value)
			# print(self.array[index])
			return 

		while node is not None:
			prev = node
			node = node.next

		prev.next = Node (key,value) 

	def find (self, key):
		index = self.hash_function(key)

		node = self.array[index]

		while node is not None and node.key != key:
			node = node.next

		if  node is None:
			# Not found
			print ("That thing does not exist here")

		else:
			print ("The item is found with value ", node.value)

	def remove(self, key):
		index = self.hash_function(key)

		node = self.array[index]
		prev = None

		while node is not None and node.key != key:
			prev = node
			node = node.next
		if node is None:
			# Key not found
			print ("Key not found")
		else:
			result = node.value
			if prev is None:
				self.array[index] = node.next
			else:
				prev.next = prev.next.next


	def print_hashtable(self):
		for i in range (self.size):
			curr = self.array[i]
			while curr is not None:
				print (curr)
				curr = curr.next

if __name__ == '__main__':

	print ("This is hash table implementation")

	HashTableObject = HashTable()

	HashTableObject.insert("Monday"   , 1)
	HashTableObject.insert("Tuesday"  , 2)
	HashTableObject.insert("Wednesday", 3)
	HashTableObject.insert("Thursday" , 4)
	HashTableObject.insert("Friday"   , 5)

	HashTableObject.find("Monday")
	HashTableObject.remove("Monday")
	HashTableObject.find("Monday")
	
	HashTableObject.find("Tuesday")
	HashTableObject.find("Wednesday")
	HashTableObject.find("Thursday")
	HashTableObject.find("Friday")

	HashTableObject.insert("Monday", 1)
	HashTableObject.insert("Saturday", 6)
	HashTableObject.insert("Sunday", 7)

	HashTableObject.print_hashtable()

