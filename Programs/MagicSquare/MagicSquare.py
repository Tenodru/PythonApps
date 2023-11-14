#  File: MagicSquare.py

#  Description: A program that generates and prints a magic square
#               of the given order.

#  Developers: Alex Kong, Victor Do

#  Date Created: 10/17/2020

#  Date Last Modified: 10/19/2020

# Permutes the given list a.
# For each permutation, uses check_if_magic_square to determine if
# the 1D list is a magic square if converted to a 2D list.
# If so, prints the 1D list.
def permute (a, lo, n):
  # Converts the 1D list to a 2D list.
  hi = len(a)
  if (lo == hi):
    list_2d = []
    offset = 0
    for i in range(0, n):
      row = []
      for j in range(0, n):
        row.append(a[j + offset])
      offset += n
      list_2d.append(row)
    
    # Checks if the 2D list is a magic square.
    if (check_if_magic_square(list_2d, n)):
      final_list = []
      for i in range(0, n):
        for j in range(0, n):
          final_list.append(list_2d[i][j])
      print(final_list)
  else:
    for i in range (lo, hi):
      a[lo], a[i] = a[i], a[lo]
      permute (a, lo + 1, n)
      a[lo], a[i] = a[i], a[lo]

# Checks if the given 2D list is a magic square of the
# given order n.
def check_if_magic_square(list_2d, n):
  constant = n * ((n ** 2) + 1) / 2
  
  # Horizontal check
  for i in range(0, n):
    if sum(list_2d[i]) != constant:
      return False
  
  # Vertical check
  for j in range(0, n):
    col = []
    for k in range(0, n):
      col.append(list_2d[k][j])
    if (sum(col) != constant):
      return False
  
  # Diagonal check from top left to bottom right
  diag = []
  for l in range(0,n):
    diag.append(list_2d[l][l])
  if (sum(diag) != constant):
    return False
  
  # Diagonal check from top rigght to bottom left
  diag = []
  for m in range(0,n):
    diag.append(list_2d[m][(n-1) - m])
  if (sum(diag) != constant):
    return False

  return True
  

def main():
  n = int(input("Enter an integer: "))
  list = []
  # Creates a list of integers from 1 to n**2.
  for i in range(0, n ** 2):
    list.append(i + 1)
  permute (list, 0, n)
  '''
  list = [[1, 2, 15, 16], [12, 14, 3, 5], [13, 7, 10, 4], [8, 11, 6, 9]]
  print(check_if_magic_square(list, 4))
  '''
  
main()