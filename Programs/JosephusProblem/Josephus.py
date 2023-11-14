#  File: Josephus.py

#  Description: A program that solves the Josephus problem, given starting soldier and elimination number.

#  Developers: Alex Kong, Victor Do

#  Date Created: 11/09/2020

#  Date Last Modified: 11/09/2020

import sys

class Link(object):
  def __init__ (self, data, next = None):
    self.data = data
    self.next = next

class CircularList(object):
  # Constructor
  def __init__ ( self ):
    self.first = None

  # Insert an element (value) in the list
  def insert ( self, data):
    new_link = Link (data)

    current = self.first
    # if there are no links yet, set link as first and link it to itself
    if (current == None):
      self.first = new_link
      new_link.next = new_link
      return
    else:
      current = current.next
    
    while (current.next != self.first):
      current = current.next
    
    # link the added link to the first link
    current.next = new_link
    current.next.next = self.first

  # Find the link with the given data (value)
  def find ( self, data ):
    current = self.first
    
    while (current.data != data):
      # once current.next is self.first, we've made a full circle
      if (current.next == self.first):
        if (current.next.data == data):
          return current.next
        else:
          #print("Error: Couldn't find " + str(data))
          return None
      else:
        current = current.next

    return current

  # Delete a link with a given data (value)
  def delete ( self, data ):
    previous = self.first
    current = self.first

    previous = current
    current = current.next

    while (current.data != data):
      if (current.next == self.first):
        # if we are deleting self.first, we need to set a new link as self.first, otherwise some functions will loop forever
        if (current.next.data == data):
          previous.next.next = current.next.next
          self.first = current.next
          return
        else:
          return
      else:
        previous = current
        current = current.next

    previous.next = current.next
    
    # print the number of the soldier executed
    print(current.data)

  # Delete the nth link starting from the Link start 
  # Return the next link from the deleted Link
  def delete_after ( self, start, n ):
    previous = start
    current = start
    # move down the linked list until we reach the correct target
    while (n > 1):
      previous = current
      current = current.next
      n -= 1
    
    # remove number from the linked list
    self.delete(current.data)

    return current.next.data

  # Return a string representation of a Circular List
  def __str__ ( self ):
    new_string = ""
    current = self.first
    count = 0

    if (current == None):
      return new_string
    else:
      new_string = new_string + str(current.data) + "  "
      current = current.next

    while (current != self.first):
      new_string = new_string + str(current.data) + "  "
      count += 1
      if (count == 10):
        new_string = new_string + "\n"
        count = 0
      current = current.next
    
    return new_string

def main():
  # read number of soldiers
  line = sys.stdin.readline()
  line = line.strip()
  num_soldiers = int (line)
  
  # read the starting number
  line = sys.stdin.readline()
  line = line.strip()
  start_count = int (line)

  # read the elimination number
  line = sys.stdin.readline()
  line = line.strip()
  elim_num = int (line)

  new_list = CircularList()
  # insert all soldiers into the linked list
  for i in range(0, num_soldiers):
    new_list.insert(i + 1)

  next_num = start_count
  # run until the number of soldiers remaining is 0
  while (num_soldiers > 0):
    next_num = new_list.delete_after(new_list.find(next_num), elim_num)
    num_soldiers -= 1


if __name__ == "__main__":
  main()