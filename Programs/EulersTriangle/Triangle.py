#  File: Triangle.py

#  Description: This program uses brute force, greedy, recursive, and dynamic programming
#               methods to find the greatest path sum of a Euler's Triangle.

#  Developers: Alex Kong, Victor Do

#  Date Created: 10/24/2020

#  Date Last Modified: 10/24/2020

import sys

from timeit import timeit

brute_force_path_list = []

# returns the greatest path sum using exhaustive search
def brute_force (grid):
  if (len(grid) == 1):
      return grid[0]
  else:
      brute_force_helper(grid, 0, 0, 0)
      return max(brute_force_path_list)

def brute_force_helper (grid, row, idx, total):
  if (row >= len(grid)):
    brute_force_path_list.append(total)
  else:
    total += grid[row][idx]
    brute_force_helper(grid, row + 1, idx, total) or brute_force_helper(grid, row + 1, idx + 1, total)

# returns the greatest path sum using greedy approach
def greedy (grid):
  if (len(grid) == 1):
      return grid[0]
  else:
      return greedy_helper(grid, 0, 0, 0)

def greedy_helper (grid, row, idx, total):
  total += grid[row][idx]
  if (row >= len(grid) - 1):
    return total
  else:
    # if the leftmost index between the two branch numbers is greater,
    # add the leftmost number to the total.
    if (grid[row + 1][idx] > grid[row + 1][idx + 1]):
      return greedy_helper(grid, row + 1, idx, total)
    # if the rightmost index between the two branch numbers is greater,
    # add the rightmost number to the total.
    elif (grid[row + 1][idx] <= grid[row + 1][idx + 1]):
      return greedy_helper(grid, row + 1, idx + 1, total)

# returns the greatest path sum using divide and conquer (recursive) approach
def divide_conquer (grid):
  if (len(grid) == 1):
      return grid[0]
  else:
      return max(divide_conquer_helper(grid, 0, 0, 0))

def divide_conquer_helper (grid, row, idx, total):
  total += grid[row][idx]
  if (row >= len(grid) - 1):
    return [total]
  else:
    # if this is the last row, run one last recursive call and end the function
    if row == len(grid) - 1:
      return divide_conquer_helper(grid, row + 1, idx, total)
    # if not the last row, return the largest sum from either branch working downwards recursively.
    else:
      return divide_conquer_helper(grid, row + 1, idx, total) + divide_conquer_helper(grid, row + 1, idx + 1, total)

# returns the greatest path sum and the new grid using dynamic programming
def dynamic_prog (grid):
  # start from second-to-last row and work backwards
  for row in range(len(grid)-2, -1, -1):
    nextRowIndex = 0
    for col in range(len(grid[row])-1):
      if (grid[row][col] != 0):
        currentNum = grid[row][col]
        branchNum1 = grid[row+1][nextRowIndex]
        branchNum2 = grid[row+1][nextRowIndex + 1]
        # print ("Current Num:", currentNum, "Option 1:", branchNum1, "Option 2:", branchNum2)
        
        # replace current row nums with the greatest possible sum for each
        # by looking at the numbers below each current row number
        if (branchNum1 >= branchNum2):
          grid[row][col] = currentNum + branchNum1
        else:
          grid[row][col] = currentNum + branchNum2
        nextRowIndex += 1
    # print ("")
  return grid[0][0]

# reads the file and returns a 2-D list that represents the triangle
def read_file ():
  # read number of lines
  line = sys.stdin.readline()
  line = line.strip()
  n = int (line)

  # create an empty grid with 0's
  grid = [[0 for i in range (n)] for j in range (n)]

  # read each line in the input file and add to the grid
  for i in range (n):
    line = sys.stdin.readline()
    line = line.strip()
    row = line.split()
    row = list (map (int, row))
    for j in range (len(row)):
      grid[i][j] = grid[i][j] + row[j]

  return grid 

def main ():
  # read triangular grid from file
  grid = read_file()

  
  # check that the grid was read in properly
  for row in range(len(grid)):
    for col in range (len(grid[row])):
      if not (grid[row][col] == 0):
        print (" ", grid[row][col], end= " ")
    print ('')
  
  
  # output greatest path from exhaustive search
  times = timeit ('brute_force({})'.format(grid), 'from __main__ import brute_force', number = 10)
  times = times / 10
  print(brute_force(grid))
  # print time taken using exhaustive search
  print (times)

  # output greatest path from greedy approach
  times = timeit ('greedy({})'.format(grid), 'from __main__ import greedy', number = 10)
  times = times / 10
  print(greedy(grid))
  # print time taken using greedy approach
  print (times)

  # output greatest path from divide-and-conquer approach
  times = timeit ('divide_conquer({})'.format(grid), 'from __main__ import divide_conquer', number = 10)
  times = times / 10
  print (divide_conquer(grid))
  # print time taken using divide-and-conquer approach
  print (times)

  # output greatest path from dynamic programming 
  times = timeit ('dynamic_prog({})'.format(grid), 'from __main__ import dynamic_prog', number = 10)
  times = times / 10
  print(dynamic_prog(grid))
  # print time taken using dynamic programming
  print (times)

if __name__ == "__main__":
  main()