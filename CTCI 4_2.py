'''
	Minimal Tree: Given a sorted (increasing order) array with unique integer elements, write an 
	algorithm to create a binary search tree with minimal height

	Solution: 

	We need to match number of nodes in left subtree to the number of nodes in right 
	subtree as much as possible.

	1. Insert into the tree middle elemnt of the array 

	2. Insert (into the left subtree) the left subarray elements

	3. Insert (into the right subtree) the right subarray elements

	4. Recurse
'''

import unittest

def create_minimal_bst(input_array):
	if not input_array:
		return None

	elif len(input_array) == 1:
		return TreeNode(input_array[0])

	n = len(input_array)
	mid = int(n/2)

	head = TreeNode(input_array[mid])
	left = create_minimal_bst (input_array[:mid])
	right = create_minimal_bst (input_array[mid+1:])

	head.left = left 
	head.right = right

	return head

class Test(unittest.TestCase):

	def test_create_bst(self):
		bst = create_minimal_bst([2,3,4,5,6,7])
		self.assertEqual(bst.value, 5)
		self.assertEqual(bst.left.value, 3)
		self.assertEqual(bst.left.left.value, 2)
		self.assertEqual(bst.left.right.value, 4)
		self.assertEqual(bst.right.value, 7)
		self.assertEqual(bst.right.left.value, 6)

class TreeNode:
	def __init__(self, value, left = None, right = None):
		self.value = value
		self.left = left
		self.right = right

if __name__ == '__main__':
	print ("This is the implementation of Minimal Tree")

	unittest.main(exit=False)

