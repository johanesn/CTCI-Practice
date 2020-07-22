# Implementation of Tries 

'''
	If we store keys in BST, a well balanced BST will need time proportional o M * log N where M is 
	maximum string length and N is the number of keys in tree.

	Using Trie, we can search the key in O(M) time. 

	Why using trie? 
	1. We can insert and find strings in O(L) time where L represent the length of single word.
	Faster than BST and hashing because of the way it is implemented. We do not need to compute
	any hash function. No collision handling is required (like open addressing and separate chain)
	
	2. Easily print all words in alphabetical order (not possible with hashing)
	3. We can efficiently do prefix search 

	Disadvantage?
	They need a lot memory for storing strings. 
'''

ALPHABET_SIZE = 26

class TrieNode : 
	def __init__ (self):
		self.children = [None] *26
		self.isEndOfWord = False

class Trie:
	def __init__(self):
		self.root = TrieNode()

	def get_node(self):
		return TrieNode()

	def char_to_index (self, ch):
		return ord (ch) - ord('a')

	def insert (self, key):
		curr = self.root 
		length = len(key)

		for level in range (length):
			index = self.char_to_index (key[level])

			# if current character is not present
			if not curr.children[index]:
				curr.children[index] = self.get_node()
			curr = curr.children[index]

		# mark last node as leaf
		curr.isEndOfWord = True


	def search (self, key):
		curr = self.root
		length = len(key)

		for level in range (length):
			index = self.char_to_index(key[level])

			if not curr.children[index]:
				return False
			curr = curr.children[index]

		return curr != None and curr.isEndOfWord 

	def find_prefix (self):
		# to do later
		pass

	def print_trie (self):
		# to do later
		pass
if __name__ == '__main__':
	print ("This is the implementation of Trie")

	keys = ["the", "a", "there", "anaswe", "any", "by", "their"]

	MyTrie = Trie()

	# insert
	for key in keys: 
		MyTrie.insert(key)


	# search 
	print ("{} ---- {}".format("the", MyTrie.search("the")))
	print ("{} ---- {}".format("the", MyTrie.search("there")))
	print ("{} ---- {}".format("the", MyTrie.search("their")))
	print ("{} ---- {}".format("the", MyTrie.search("answer")))


