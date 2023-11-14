
#  File: RPN.py

#  Description: Takes in a mathematical expression in Reverse Polish Notation form and
#				outputs the result.

#  Developer: Alex Kong

#  Date Created: 10/26/2020

#  Date Last Modified: 10/26/2020

class Stack (object):
	def __init__ (self):
		self.stack = []

	# add an item on the top of the stack
	def push (self, item):
		self.stack.append (item)

	# remove an item from the top of the stack
	def pop (self):
		return self.stack.pop()

	# check the item on the top of the stack
	def peek (self):
		return self.stack[-1]

	# check if the stack is empty
	def is_empty (self):
		return (len(self.stack) == 0)

	# return the number of elements in the stack
	def size (self):
		return (len(self.stack))

class Queue (object):
	def __init__ (self):
		self.queue = []

	# add an item to the end of the queue
	def enqueue (self, item):
		self.queue.append (item)

	# remove an item from the beginning of the queue
	def dequeue (self):
		return (self.queue.pop(0))

	# check if the queue if empty
	def is_empty (self):
		return (len(self.queue) == 0)

	# return the size of the queue
	def size (self):
		return (len(self.queue))

def operate (oper1, oper2, token):
	expr = str(oper1) + token + str(oper2)
	return eval (expr)

def rpn (s):
	rpnStack = Stack()

	operators = ['+', '-', '*', '/', '//', '%', '**']

	tokens = s.split()

	for item in tokens:
		if (item in operators):
			oper2 = rpnStack.pop()
			oper1 = rpnStack.pop()
			rpnStack.push (operate (oper1, oper2, item))
		else:
			rpnStack.push (item)

	return rpnStack.push (item)


def main():
	in_file = open ("rpn.txt", "r")
	for line in in_file:
		line = line.strip()
		value = rpn (line)
		print (line, ' = ', value)
	in_file.close()

main()