#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'is_rectangle' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts ARRAY of INTEGER TUPLES points as parameter.
#

def is_rectangle(points):
    # empty lists will hold tuples of point tuples.
    lineListH = []
    lineListV = []
    
    
    for point in points:
        for newPoint in points:
            # found a straight vertical line
            if (newPoint[0] == point[0]) and (newPoint[1] != point[1]):
                # if both configurations of newPoint and point are not in lineList V,
                # append (newPoint, point) as a new vertical line to lineListV.
                if ((newPoint, point) not in lineListV) and ((point, newPoint) not in lineListV):
                    lineListV.append ( (newPoint, point) )
            # found a straight horizontal line
            elif (newPoint[1] == point[1]) and (newPoint[0] != point[0]):
                # if both configurations of newPoint and point are not in lineList H,
                # append (newPoint, point) as a new horizontal line to lineListH.
                if ((newPoint, point) not in lineListH) and ((point, newPoint) not in lineListH):
                    lineListH.append ( (newPoint, point) )
    
    # debug statements.
    print ('lineListH:')
    for pointPair in lineListH:
        print (pointPair)
    print ('lineListV:')
    for pointPair in lineListV:
        print (pointPair)
    
    # empty lists will hold tuples of exactly parallel lines.
    # exactly parallel lines are lines that are parallel,
    # and have the same "start" and "end."
    # each line is a tuple of points.
    parallelLineListH = []
    parallelLineListV = []
    
    # line is a tuple of points.
    # lineListH is a list of horizontal lines.
    for line in lineListH:
        for newLine in lineListH:
            # if line and newLine are not the same...
            if line != newLine:
                # ...and the y-coordinates of point A of each line are the same,
                # and the y-coordinates of point B of each line are the same...
                if (newLine[1][1] == line[1][1]) and (newLine[0][1] == line[0][1]):
                    # ...and both configurations of line and newLine are not found
                    # in parallelLineListH, append the (line, newLine) tuple to parallelLineListH.
                    if ((line, newLine) not in parallelLineListH) and ((newLine, line) not in parallelLineListH):
                        parallelLineListH.append((line, newLine))
                
    # line is a tuple of points.
    # lineListV is a list of vertical lines.
    for line in lineListV:
        for newLine in lineListV:
            # if line and newLine are not the same...
            if line != newLine:
                # ...and the x-coordinates of point A of each line are the same,
                # and the x-coordinates of point B of each line are the same...
                if (newLine[1][0] == line[1][0]) and (newLine[0][0] == line[0][0]):
                    # ...and both configurations of line and newLine are not found
                    # in parallelLineListV, append the (line, newLine) tuple to parallelLineListV.
                    if ((line, newLine) not in parallelLineListV) and ((newLine, line) not in parallelLineListV):
                        parallelLineListV.append((line, newLine))
    
    # debug statements.
    print ('parallelLineListH:')
    for linePair in parallelLineListH:
        print (linePair)
    print ('parallelLineListV:')
    for linePair in parallelLineListV:
        print (linePair)
    
    # if a pair of exactly parallel lines exists,
    # and there are horizontal and vertical lines,
    # then a rectangle can be found.
    if len(parallelLineListH) > 0 or len(parallelLineListV) > 0:
        if len(lineListH) > 0 and len(lineListV) > 0:
            return True
        else:
            return False
    else:
        return False
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    points_count = int(input().strip())

    points = []

    for _ in range(points_count):
        points_item = input().split()
        a = int(points_item[0])
        b = int(points_item[1])
        points.append((a, b))

    result = is_rectangle(points)

    fptr.write(str(int(result)) + '\n')

    fptr.close()
