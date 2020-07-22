# Tree Traversal (Inorder, Preorder and Postorder)

'''
			  1
			/  \				
		  2      3
        /    \
       4      5 

     (a) Inorder (Left, Root, Right)   : 4 2 5 1 3
     	 > In case of BST, inorder traversal gives nodes in non-decreasing order

     (b) Preorder (Root, Left, Right)  : 1 2 4 5 3 
     	 > Used to create a copy oof the tree. 
     	 > Can also be used to get prefix expression on of an expression tree

     (c) Postorder (Left, Right, Root) : 4 5 2 3 1
     	 > Used to delete the tree
     	 > Also useful to get the postfix expression of an expression tree
'''

class TreeNode: 
	def __init__(self, key):
		self.left = self.right = None
		self.val = key

def print_inorder(root):
	if root : 
		print_inorder(root.left)

		print (root.val, end = " ")

		print_inorder(root.right)

def print_preorder(root):
	if root :
		print (root.val, end = " ")

		print_preorder(root.left)

		print_preorder (root.right)

def print_postorder(root):
	if root : 
		print_postorder(root.left)

		print_postorder(root.right)

		print (root.val, end = " ")

if __name__ == '__main__':

	print ("This is implementation of tree traversal")

	root = TreeNode (25)

	root.left = TreeNode(15)
	root.right = TreeNode(50)

	root.left.left = TreeNode(10)
	root.left.right = TreeNode(22)
	root.right.left = TreeNode(35)
	root.right.right = TreeNode(70)

	root.left.left.left = TreeNode (4)
	root.left.left.right = TreeNode(12)
	root.left.right.left = TreeNode(18)
	root.left.right.right = TreeNode(24)
	root.right.left.left = TreeNode(31)
	root.right.left.right = TreeNode(44)
	root.right.right.left = TreeNode(66)
	root.right.right.right = TreeNode(90)

	print ("Inorder traversal of binary tree is")
	print_inorder(root)
	print ('\n')

	print ("Preorder traversal of binary tree is")
	print_preorder(root)
	print ('\n')

	print ("Postorder traversal of binary tree is")
	print_postorder(root)
	print ('\n')




