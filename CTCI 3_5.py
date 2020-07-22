'''
	Sort Stack : Write a program to sort a stack such that smallest items are on the top. 
	You can use an additional temporary stack, but you may not copy the elements into any other data structure.
	The stack supports the following operations: push, pop, peek and isEmpty

'''

from Stacks import Stacks

def sort_stack (ori_stack):
	temp_stack = Stacks()

	while not ori_stack.is_empty():
		temp = ori_stack.pop_item()

		while (not temp_stack.is_empty()) and (temp_stack.peek() < temp):
			ori_stack.push_item(temp_stack.pop_item())

		temp_stack.push_item(temp)

	while (not temp_stack.is_empty()):
		ori_stack.push_item(temp_stack.pop_item())

	return ori_stack

if __name__ == '__main__':
	print ("This is the implementation of CTCI 3_5, Sort Stack")

	StacksObject = Stacks()

	StacksObject.push_item (10)
	StacksObject.push_item (30)
	StacksObject.push_item (70)
	StacksObject.push_item (40)
	StacksObject.push_item (80)
	StacksObject.push_item (20)
	StacksObject.push_item (90)
	StacksObject.push_item (60)
	StacksObject.push_item (50)

	sorted_stack = sort_stack(StacksObject)

	print (sorted_stack.stack)