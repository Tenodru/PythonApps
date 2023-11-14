
#  File: BST_Cipher.py

#  Description: Encrypts and decrypts strings.

#  Developers: Alex Kong, Victor Do

#  Date Created: 11/14/2020

#  Date Last Modified: 11/15/2020

import sys

class Node (object):
  def __init__ (self, data):
    self.data = data
    self.lchild = None
    self.rchild = None
    self.parent = None

class Tree (object):
  # the init() function creates the binary search tree with the
  # encryption string. If the encryption string contains any
  # character other than the characters 'a' through 'z' or the
  # space character drop that character.
  def __init__ (self, encrypt_str):
    self.root = None
    for char in encrypt_str:
      if (97 <= ord(char) <= 122) or (char == " "):
        # print ("Inserting:", char, end = ' ')
        self.insert(char)

  # the insert() function adds a node containing a character in
  # the binary search tree. If the character already exists, it
  # does not add that character. There are no duplicate characters
  # in the binary search tree.
  def insert (self, ch):
    new_node = Node (ch)

    if (self.root == None):
      self.root = new_node
      return
    else:
      self.search(ch)
      current = self.root
      parent = self.root
      while (current != None):
        parent = current
        if (ch == current.data):
          return
        if (ch < current.data):
          current = current.lchild
        else:
          current = current.rchild

      # found location now insert node
      if (ch < parent.data):
        parent.lchild = new_node
      else:
        parent.rchild = new_node

  # the search() function will search for a character in the binary
  # search tree and return a string containing a series of lefts
  # (<) and rights (>) needed to reach that character. It will
  # return a blank string if the character does not exist in the tree.
  # It will return * if the character is the root of the tree.
  def search (self, ch):
    current = self.root
    str = ''
    if (current.data == ch):
      str = '*'
      # print ("Search Result:", str)
      return str
    while (current != None):
      if (current.data == ch):
        # print ("Search Result:", str)
        return str
      if (ch < current.data):
        current = current.lchild
        str += '<'
      else:
        current = current.rchild
        str += '>'
    # print ("Search Result:", str)
    return str

  # the traverse() function will take string composed of a series of
  # lefts (<) and rights (>) and return the corresponding 
  # character in the binary search tree. It will return an empty string
  # if the input parameter does not lead to a valid character in the tree.
  def traverse (self, st):
    str = ''
    adj_st = st + '!'
    current = self.root
    
    # Parse through st
    for char in adj_st:
      if char == '*':
        str += current.data
      if char == '<':
      	if current.lchild == None:
      	  return 'Char not found'
      	current = current.lchild
      elif char == '>':
      	if current.rchild == None:
      	  return 'Char not found'
      	current = current.rchild
      elif char == '!':
        str += current.data
        current = self.root

    return str


  # the encrypt() function will take a string as input parameter, convert
  # it to lower case, and return the encrypted string. It will ignore
  # all digits, punctuation marks, and special characters.
  def encrypt (self, st):
    str = ''
    for char in st:
      if (97 <= ord(char) <= 122) or (char == " "):
      	str += self.search(char)
      	str += '!'
    return str[:len(str)-1]

  # the decrypt() function will take a string as input parameter, and
  # return the decrypted string.
  def decrypt (self, st):
    return self.traverse(st)


def main():
  # read encrypt string
  line = sys.stdin.readline()
  encrypt_str = line.strip()

  # create a Tree object
  the_tree = Tree (encrypt_str)

  # read string to be encrypted
  line = sys.stdin.readline()
  str_to_encode = line.strip()

  # print the encryption
  print (the_tree.encrypt(str_to_encode))

  # read the string to be decrypted
  line = sys.stdin.readline()
  str_to_decode = line.strip()
  
  # print the decryption
  print (the_tree.decrypt(str_to_decode))
 
if __name__ == "__main__":
  main()