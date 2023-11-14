
# File: Fibonacci.py

# Description: A program that calculates the number of occurrences of a bit string p
#              in f(n).

# Student's Name: Alex Kong

# Student's UT EID: ak39768

# Partner's Name: Victor Do

# Partner's UT EID: vd4877

# Course Name: CS 313E

# Unique Number: 50845

# Date Created: 10/6/2020

# Date Last Modified: 10/9/2020

import sys

# Input: n a positive integer
# Output: a bit string
def f ( n, memo ):
	if n == 0 or n == 1:
		return memo[n]
	else:
		if (n >= len(memo)):
			fib = str(f (n - 1, memo)) + str(f (n - 2, memo))
			memo.append (fib)
			return fib
		else:
			return memo[n]

# Input: s and p are bit strings
# Output: an integer that is the number of times p occurs in s
def count_overlap (s, p):
	count = 0
	pos = 0

	# checks the substring of the current position to the current position
	# plus the length of p.
	# if equal, then increase count by 1.
	while pos < len(s):
		if (s[pos:pos+len(p)] == p):
			count += 1
		pos += 1
	return count

def main():
  # read n and p from standard input
  n = sys.stdin.readline()
  n = int (n.strip())
  p = sys.stdin.readline()
  p = p.strip()

  # compute the bit string f(n)
  memo = [0, 1]
  fn = f(n, memo)

  # determine the number of occurrences of p in f(n)
  countN = count_overlap(fn, p)

  # print the number of occurrences of p in f(n)
  print (countN)


if __name__ == "__main__":
  main()