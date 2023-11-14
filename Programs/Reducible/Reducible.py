
#  File: Reducible.py

#  Description: A program that determines how many words of length 10 are reducible.

#  Developer: Alex Kong,  Victor Do

#  Date Created: 10/26/2020

#  Date Last Modified: 10/30/2020

# Input: takes as input a positive integer n
# Output: returns True if n is prime and False otherwise
def is_prime ( n ):
  if (n == 1):
    return False

  limit = int (n ** 0.5) + 1
  div = 2
  while (div < limit):
    if (n % div == 0):
      return False
    div += 1
  return True

# Input: takes as input a string in lower case and the size
#        of the hash table 
# Output: returns the index the string will hash into
def hash_word (s, size):
  hash_idx = 0
  for j in range (len(s)):
    letter = ord (s[j]) - 96
    hash_idx = (hash_idx * 26 + letter) % size
  return hash_idx

# Input: takes as input a string in lower case and the constant
#        for double hashing 
# Output: returns the step size for that string 
def step_size (s, const):
  key = hash_word(s, 113809)
  size_step = const - ( key % const )
  return size_step

# Input: takes as input a string and a hash table 
# Output: no output; the function enters the string in the hash table, 
#         it resolves collisions by double hashing
def insert_word (s, hash_table):
  temp_idx = hash_word(s, len(hash_table))
  while (hash_table[temp_idx] != None):
    temp_idx += step_size(s, 3)
    if (temp_idx >= len(hash_table)):
      temp_idx = len(hash_table) - temp_idx
  hash_table[temp_idx] = s

# Input: takes as input a string and a hash table 
# Output: returns True if the string is in the hash table 
#         and False otherwise
def find_word (s, hash_table):
  idx = hash_word (s, len(hash_table))
  while (hash_table[idx] != None):
    if (hash_table[idx] == s):
    	return True
    else:
    	idx += step_size(s, 3)
    	if (idx >= len(hash_table)):
          idx = len(hash_table) - idx
  return False

# Input: string s, a hash table, and a hash_memo 
#        recursively finds if the string is reducible
# Output: if the string is reducible it enters it into the hash memo 
#         and returns True and False otherwise
def is_reducible (s, hash_table, hash_memo):
  for charIdx in range(len(s)):
    reduced_word = s[:charIdx] + s[charIdx+1:]
    if (find_word(reduced_word, hash_memo)):
      return True
    if (reduced_word == 'a' or reduced_word == 'i' or reduced_word == 'o'):
      return True
    if (find_word(reduced_word, hash_table)):
      if (is_reducible (reduced_word, hash_table, hash_memo)):
        insert_word(s, hash_memo)
        return True
    
  return False
  

# Input: string_list a list of words
# Output: returns a list of words that have the maximum length
def get_longest_words (string_list):
  long_list = []
  for word in string_list:
    if (len(word) == 10):
      long_list.append(word)
  return long_list

def main():
  # create an empty word_list
  word_list = []

  # open the file words.txt
  in_file = open ('words.txt', 'r')

  # read words from words.txt and append to word_list

  line = in_file.readline()
  while (line != ""):
    word_list.append(line)
    line = in_file.readline()

  for i in range(len(word_list)):
    word_list[i] = str(word_list[i])
    word_list[i] = word_list[i].rstrip('\n')

  # close file words.txt
  in_file.close()

  # find length of word_list

  # determine prime number N that is greater than twice
  # the length of the word_list
  test_num = 2 * len(word_list)
  while (is_prime(test_num) != True):
    test_num += 1
  hash_list_length = test_num

  # create an empty hash_list

  # populate the hash_list with N blank strings
  hash_list = [None for r in range(hash_list_length)]

  # hash each word in word_list into hash_list
  # for collisions use double hashing
  collisions = 0
  for i in range(len(word_list)):
    insert_word(word_list[i], hash_list)

  # create an empty hash_memo of size M
  # we do not know a priori how many words will be reducible
  # let us assume it is 10 percent (fairly safe) of the words
  # then M is a prime number that is slightly greater than 
  # 0.2 * size of word_list

  # populate the hash_memo with M blank strings
  test_num = len(word_list) // 5
  while (is_prime(test_num) != True):
    test_num += 1
  hash_memo_length = test_num
  hash_memo = [None for r in range(hash_memo_length)]

  # create an empty list reducible_words
  reducible_words = []

  # for each word in the word_list recursively determine
  # if it is reducible, if it is, add it to reducible_words
  for word in word_list:
    if (is_reducible(word, hash_list, hash_memo)):
      reducible_words.append(word)

  # find words of length 10 in reducible_words
  list_of_words = get_longest_words(reducible_words)
  # print the words of length 10 in alphabetical order
  # one word per line
  list_of_words.sort()
  for word in list_of_words:
  	print (word)


if __name__ == "__main__":
  main()