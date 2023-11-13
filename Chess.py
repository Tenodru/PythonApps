
#  File: Chess.py

#  Description: Solves the Eight Queen puzzle and returns the total number
#               of solutions for given board sizes.

#  Student Name: Alex Kong

#  Student UT EID: ak39768

#  Partner Name: Victor Do

#  Partner UT EID: vd4877

#  Course Name: CS 313E

#  Unique Number: 50845

#  Date Created: 10/23/2020

#  Date Last Modified: 10/23/2020

import sys

class Queens (object):
  def __init__ (self, n = 8):
    self.solutions = 0
    self.board = []
    self.n = n
    for i in range (self.n):
      row = []
      for j in range (self.n):
        row.append ('*')
      self.board.append (row)

  # print the board row by row
  def print_board (self, queenPositions):
    for i in range (self.n):
      currentRow = ''
      for col in range (self.n):
      	# if the current position in this row corresponds to a queen position,
      	# add a 'Q' to the row string.
      	# otherwise add a '*' to the row string.
        if (queenPositions[i] == col):
          currentRow += 'Q '
        else:
          currentRow += '* '
      print (currentRow)
    print ('')

  # check if a position on the board is valid
  # queenPositions is a list of integers representing the location
  # of the queen in each row. Each row can have a maximum of 1 queen.
  # takenRows is the number of rows already occupied.
  # col is the current column we are checking.
  def is_valid (self, queenPositions, takenRows, col):
    for i in range (takenRows):
      # check if there is a vertical attack (existing queen in same board column)
      # then check diagonals by parsing through each previous queen
      if ((queenPositions[i] == col) or 
        (queenPositions[i] - i == col - takenRows) or 
        (queenPositions[i] + i == col + takenRows)):
        #print ("Bad | Queens:", queenPositions, "Queen[i]:", queenPositions[i], "i:", i, "TakenRows:", takenRows, "col:", col)
        return False
    #print ("Good | Queens:", queenPositions, "TakenRows:", takenRows, "col:", col)
    return True
    
  # do the recursive backtracking
  # queenPositions is a list of integers representing
  # the location of the queen in each row. Each row can have a maximum of 1 queen.
  # currentRow is the current row on the board we are checking. Initial 0.
  def recursive_solve (self, queenPositions, currentRow):
    # end the function if the current row is equal to n (out of bounds)
    # increment solutions by 1.
    if (currentRow == self.n):
      # self.print_board(queenPositions)
      # print (queenPositions)
      self.solutions += 1

    else:
      # parse through each "square" in this row.
      # place queens and check all possible solutions that can be made
      # from those placed queens
      for col in range (self.n):
      	# check if a queen can be placed in this square
      	# if so, add to queenPositions and run function again for
      	# the next row.
        if (self.is_valid(queenPositions, currentRow, col)):
          queenPositions[currentRow] = col
          self.recursive_solve(queenPositions, currentRow + 1)

  # find all solutions
  # start with an "empty" first row of the board
  def solve (self):
    queenPositions = [0] * self.n
    self.recursive_solve (queenPositions, 0)
    
  # print the number of possible solutions
  def print_solutions(self):
    print ("Total Solutions:", self.solutions)

def main():
  # read the size of the board
  line = sys.stdin.readline()
  line = line.strip()
  n = int (line)

  # create a chess board
  game = Queens (n)

  # place the queens on the board and count the solutions
  game.solve()

  # print the number of solutions
  game.print_solutions()
 
if __name__ == "__main__":
  main()