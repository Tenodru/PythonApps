
#  File: ExpressionTree.py

#  Description: Makes an expression tree.

#  Developers: Alex Kong, Victor Do

#  Date Created: 11/11/2020

#  Date Last Modified: 11/12/2020

import sys

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

class Node (object):
  def __init__ (self, data):
    self.data = data
    self.lchild = None
    self.rchild = None
    self.parent = None
  # self.visited = False

class Tree (object):
  def __init__ (self):
    self.root = None
    self.list = []

  def create_tree (self, expr):
    operators = ['+', '-', '*', '/', '//', '%', '**']
    expressionStack = Stack()
    self.root = Node(None)
    currentNode = self.root
    # rootNode = Node()
    for char in expr:
      # insert(char)
      if char == '(':
        # Add new node as left child of current node
        # Push current node on stack, make equal to left child 
        currentNode.lchild = Node(None)
        expressionStack.push(currentNode)
        # print ("Current Node Data (lparen):", currentNode.data)
        currentNode = currentNode.lchild
        
      elif char == ')':
        # If stack not empty, pop the stack and make current node equal to parent node
        if not expressionStack.is_empty():
          # expressionStack.pop()
          currentNode = expressionStack.pop()

      elif char in operators:
        # Set current node data to operator
        # Push current node on stack
        # Add new node as right child of current node, make current node equal to right child
        currentNode.data = char
        expressionStack.push(currentNode)
        # print ("Current Node Data (operator):", currentNode.data)
        newNode = Node(None)
        currentNode.rchild = newNode
        currentNode = currentNode.rchild

      #elif (isinstance(char, int) or isinstance(char, float)):
      elif (char != ' '):
        # Set current node data to the operand
        # Make current node equal to parent by popping stack
        currentNode.data = char
        # print ("Current Node Data (operand):", currentNode.data)
        currentNode = expressionStack.pop()

  def printExpr(self):
    for char in self.list:
      print (char, end = ' ')

  def evaluate (self, aNode):
    operators = ['+', '-', '*', '/', '//', '%', '**']
    result = 0
    startIndex = 0
    if (aNode != None):
      self.evaluateHelper(aNode, result)
      currentNums = []
      # Run through expression sequence and evaluate
      for char in self.list:
        if char in operators:
          if char == '+':
            # print (currentNums[len(currentNums)-2], '+', currentNums[len(currentNums)-1])
            subResult = currentNums[len(currentNums)-2] + currentNums[len(currentNums)-1]
            result += subResult
          elif char == '-':
            # print (currentNums[len(currentNums)-2], '-', currentNums[len(currentNums)-1])
            subResult = currentNums[len(currentNums)-2] - currentNums[len(currentNums)-1]
            result += subResult
          elif char == '*':
            # print (currentNums[len(currentNums)-2], '*', currentNums[len(currentNums)-1])
            subResult = currentNums[len(currentNums)-2] * currentNums[len(currentNums)-1]
            result += subResult
          elif char == '/':
            # print (currentNums[len(currentNums)-2], '/', currentNums[len(currentNums)-1])
            subResult = currentNums[len(currentNums)-2] / currentNums[len(currentNums)-1]
            result += subResult
          elif char == '//':
            # print (currentNums[len(currentNums)-2], '//', currentNums[len(currentNums)-1])
            subResult = currentNums[len(currentNums)-2] // currentNums[len(currentNums)-1]
            result += subResult
          elif char == '%':
            # print (currentNums[len(currentNums)-2], '%', currentNums[len(currentNums)-1])
            subResult = currentNums[len(currentNums)-2] % currentNums[len(currentNums)-1]
            result += subResult
          elif char == '**':
            # print (currentNums[len(currentNums)-2], '**', currentNums[len(currentNums)-1])
            subResult = currentNums[len(currentNums)-2] ** currentNums[len(currentNums)-1]
            result += subResult
          currentNums.pop(len(currentNums)-2)
          currentNums.pop(len(currentNums)-1)
          currentNums.append(subResult)
          # print (currentNums)
        else:
          currentNums.append(float(char))

    return currentNums[-1]
  
  # Create expression sequence
  def evaluateHelper (self, aNode, curResult):
    operators = ['+', '-', '*', '/', '//', '%', '**']
    result = curResult
    if (aNode != None):
      self.evaluateHelper (aNode.lchild, result)
      self.evaluateHelper (aNode.rchild, result)
      self.list.append(aNode.data)

  def test (self):
    self.post_order (self.root)

  # in order traversal - left, center, right
  def in_order (self, aNode):
    if (aNode != None):
      self.in_order (aNode.lchild)
      print (aNode.data)
      self.in_order (aNode.rchild)

  def pre_order (self, aNode):
    if (aNode != None):
      print (aNode.data, end = ' ')
      self.pre_order (aNode.lchild)
      self.pre_order (aNode.rchild)

  def post_order (self, aNode):
    if (aNode != None):
      self.post_order (aNode.lchild)
      self.post_order (aNode.rchild)
      print (aNode.data, end = ' ')

def main():
  # read infix expression
  line = sys.stdin.readline()
  expr = line.strip()
  
  # evaluate the expression and print the result
  exprTree = Tree()
  exprTree.create_tree(expr)
  result = exprTree.evaluate(exprTree.root)
  print (expr, "=", result)

  # get the prefix version of the expression and print
  print ("Prefix Expression:", end = ' ')
  exprTree.pre_order(exprTree.root)
  print ('')

  # get the postfix version of the expression and print
  print ("Postfix Expression:", end = ' ')
  exprTree.post_order(exprTree.root)

if __name__ == "__main__":
  main()