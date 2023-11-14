
#  File: Hull.py

#  Description: A program that returns the points of a convex hull.

#  Developers: Alex Kong, Victor Do

#  Date Created: 10/28/2020

#  Date Last Modified: 10/28/2020

import os
import re
import sys
import math

import math

class Point (object):
  # constructor
  def __init__(self, x = 0, y = 0):
    self.x = x
    self.y = y

  # get the distance to another Point object
  def dist (self, other):
    return math.hypot (self.x - other.x, self.y - other.y)

  # string representation of a Point
  def __str__ (self):
    return '(' + str(self.x) + ', ' + str(self.y) + ')'

  # equality tests of two Points
  def __eq__ (self, other):
    tol = 1.0e-8
    return ((abs(self.x - other.x) < tol) and (abs(self.y - other.y) < tol))

  def __ne__ (self, other):
    tol = 1.0e-8
    return ((abs(self.x - other.x) >= tol) or (abs(self.y - other.y) >= tol))

  def __lt__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return False
      else:
        return (self.y < other.y)
    return (self.x < other.x)

  def __le__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return True
      else:
        return (self.y <= other.y)
    return (self.x <= other.x)

  def __gt__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return False
      else:
        return (self.y > other.y)
    return (self.x > other.x)

  def __ge__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return True
      else:
        return (self.y >= other.y)
    return (self.x >= other.x)

# compute and return the determinant of the coordinates of three points
# p, q, and r are Point objects
def det (p, q, r):
    grid = [[None for r in range(3)] for c in range(3)]
    grid[0][0] = 1
    grid[0][1] = p.x
    grid[0][2] = p.y
    grid[1][0] = 1
    grid[1][1] = q.x
    grid[1][2] = q.y
    grid[2][0] = 1
    grid[2][1] = r.x
    grid[2][2] = r.y
    det_part1 = grid[0][0] * ((grid[1][1] * grid[2][2]) - (grid[1][2] * grid[2][1]))
    det_part2 = grid[0][1] * ((grid[1][0] * grid[2][2]) - (grid[1][2] * grid[2][0]))
    det_part3 = grid[0][2] * ((grid[1][0] * grid[2][1]) - (grid[1][1] * grid[2][0]))
    determinant = det_part1 - det_part2 + det_part3
    # Point R is to the left if determinant > 0.
    return determinant   
    
# computes and returns the convex hull of a sorted list of Points
# convex hull is a list of Point objects starting at the extreme
# left point and going clockwise in order
def convex_hull (sorted_points):
    n = len(sorted_points) - 1
    upper_hull = []
    upper_hull.append (sorted_points[0])
    upper_hull.append (sorted_points[1])

    newI = 2
    for i in range (2, len(sorted_points)):
        upper_hull.append (sorted_points[i])
        while len(upper_hull) >= 3 and det(upper_hull[newI-2], upper_hull[newI-1], upper_hull[newI]) >= 0:
            upper_hull.pop(newI-1)
            newI -= 1
        newI += 1
    
    lower_hull = []
    lower_hull.append (sorted_points[n])
    lower_hull.append (sorted_points[n-1])

    newI = 2
    for i in range (n-2, -1, -1):
        lower_hull.append (sorted_points[i])
        while len(lower_hull) >= 3 and det(lower_hull[newI-2], lower_hull[newI-1], lower_hull[newI]) >= 0:
            lower_hull.pop(newI-1)
            newI -= 1
        newI += 1
    
    lower_hull.pop (0)
    lower_hull.pop (len(lower_hull)-1)
    
    convex_hull = upper_hull + lower_hull
    return convex_hull

# compute and return the area of a convex polygon
# convex_poly is a list of Point objects that define the vertices
# of a convex polygon in order
def area_poly (convex_poly):
    #grid = createDetGrid(pointList)
    grid = convex_poly
    sideLength = len(grid)

    # calculates the area of the polygon according to the
    # Shoelace formula.
    total = 0
    prev = sideLength-1
    for row in range (sideLength):
        total += ((grid[prev].x + grid[row].x) * (grid[prev].y - grid[row].y))
        prev = row
    total = abs(total/2)
    
    # formats the calculated area.
    formatTotal = '{:.1f}'.format(total)
    return formatTotal

# sorts a given list of Point objects in ascending order
# by each Point object's x-coordinate.
def sort (pointList):
    newList = pointList
    for i in range (len(newList) - 1):
        # find the minimum
        minValue = newList[i]
        minIndex = i

        for j in range (i + 1, len(newList)):
            # if the x-coordinate of the next Point is less than the x-coordinate
            # of the current Point, we have found a new minValue and minIndex.
            # store these new values.
            if (newList[j].x < minValue.x):
                minValue = newList[j]
                minIndex = j

        # Swap the minimum element with the element at the ith place
        newList[minIndex] = newList[i]
        newList[i] = minValue
    return newList

# Input: no input
# Output: a string denoting all test cases have passed
def test_cases():
    # write your own test cases

    return "all test cases passed"

def main(coords):
    # convert the tuples in coords to Point objects.
    pointList = []
    i = 0
    for tupleCoord in coords:
        pointList.append (Point(tupleCoord[0], tupleCoord[1]))
        i += 1
    
    sortedList = sort(pointList)

    hull = convex_hull(sortedList)

    return area_poly(hull)
    
if __name__ == "__main__":
  fptr = open(os.environ['OUTPUT_PATH'], 'w')
  inpt = sys.stdin.read().split()
  coords = []
  for i in range(1, (int(inpt[0])*2), 2):
    coords.append((int(inpt[i]), int(inpt[i+1])))
  fptr.write(str(main(coords)))
  fptr.close() 