
#  File: Radix.py

#  Description: A program that uses an adjusted radix sort algorithm to sort a combination of digits and letters.

#  Developers: Alex Kong, Victor Do

#  Date Created: 10/30/2020

#  Date Last Modified: 10/30/2020

import sys

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

  def show (self):
  	print(self.queue)

  def clear (self):
    self.queue.clear()

  def sort (self):
  	self.queue.sort()

# Input: a is a list of strings that have either lower case
#        letters or digits
# Output: returns a sorted list of strings
def radix_sort (a):
  longest_len = 0
  for word in a:
    if len(word) > longest_len:
      longest_len = len(word)

  # Q0-Q9 will be number queues
  # Q10-Q36 will be letter queues
  queueList = [Queue() for r in range(37)]
  sort_result = a

  currentIndex = -1
  while longest_len + currentIndex >= 0:
    for word in sort_result:
      if (len(word) + currentIndex >= 0):
        # word index is number
        if (word[currentIndex].isdigit()):
          queueList[int(word[currentIndex])].enqueue(word)  
        else:
          queueList[ord(word[currentIndex]) - 87].enqueue(word)
      else:
        if (word[0].isdigit()):
          queueList[int(word[0])].enqueue(word)  
        else:
          queueList[ord(word[0]) - 87].enqueue(word)
    
    sort_result.clear() 
    #print ("New Sort --------------------------------", abs(currentIndex))
    for q in queueList:
      q.sort()
      while not q.is_empty():
        #q.show()
        sort_result.append(q.dequeue())
    currentIndex -= 1

  return sort_result


def main():
  # read the number of words in file
  line = sys.stdin.readline()
  line = line.strip()
  num_words = int (line)

  # create a word list
  word_list = []
  for i in range (num_words):
    line = sys.stdin.readline()
    word = line.strip()
    word_list.append (word)

  '''
  # print word_list
  print (word_list)
  '''

  # use radix sort to sort the word_list
  sorted_list = radix_sort (word_list)

  # print the sorted_list
  print (sorted_list)

if __name__ == "__main__":
  main()

    
