
#  File: Boxes.py

#  Description: A program that determines the number of a number of boxes
#               of given dimensions that can nest inside each other.

#  Developers: Alex Kong, Victor Do

#  Date Created: 10/14/2020

#  Date Last Modified: 10/15/2020

import sys

# generates all subsets of boxes and stores them in all_box_subsets
# box_list is a list of boxes that have already been sorted
# sub_set is a list that is the current subset of boxes
# idx is an index in the list box_list
# all_box_subsets is a 3-D list that has all the subset of boxes
def sub_sets_boxes (box_list, sub_set, idx, all_box_subsets):
  high = len(box_list)
  if (idx + 1 >= high):
    all_box_subsets.append (sub_set)
    return
  else:
    # make a copy of b, an array
    copy = sub_set[:]
    if (len(sub_set) == 0):
      sub_set.append (box_list[idx])
      sub_sets_boxes (box_list, sub_set, idx + 1, all_box_subsets)
      sub_sets_boxes (box_list, copy, idx + 1, all_box_subsets)
    elif (does_fit(sub_set[len(sub_set)-1], box_list[idx])):
      sub_set.append (box_list[idx])
      sub_sets_boxes (box_list, sub_set, idx + 1, all_box_subsets)
      sub_sets_boxes (box_list, copy, idx + 1, all_box_subsets)
    else:
      sub_sets_boxes (box_list, copy, idx + 1, all_box_subsets)

# goes through all the subset of boxes and only stores the
# largest subsets that nest in the 3-D list all_nesting_boxes
# largest_size keeps track what the largest subset is
def largest_nesting_subsets (all_box_subsets, largest_size, all_nesting_boxes):
  largest_size = 1
  for i in range(len(all_box_subsets)):
    if len(all_box_subsets[i]) > largest_size:
      largest_size = len(all_box_subsets[i])
  for i in range(len(all_box_subsets)):
    if len(all_box_subsets[i]) == largest_size:
      all_nesting_boxes.append(all_box_subsets[i])
  return largest_size

# returns True if box1 fits inside box2
def does_fit (box1, box2):
  return (box1[0] < box2[0] and box1[1] < box2[1] and box1[2] < box2[2])

def main():
  # read the number of boxes 
  in_file = open ('boxes.in', 'r')
  line = in_file.readline()
  line = line.strip()
  num_boxes = int (line)

  # create an empty list for the boxes
  box_list = []

  # read the boxes from the file
  for i in range (num_boxes):
    line = in_file.readline()
    line = line.strip()
    box = line.split()
    for j in range (len(box)):
      box[j] = int (box[j])
    box.sort()
    box_list.append (box)

  # close the file
  in_file.close()

  '''
  # print to make sure that the input was read in correctly
  print (box_list)
  print()
  '''

  # sort the box list
  box_list.sort()
  
  '''
  # print the box_list to see if it has been sorted.
  print (box_list)
  print()
  '''

  # create an empty list to hold all subset of boxes
  all_box_subsets = []

  # create a list to hold a single subset of boxes
  sub_set = []

  # generate all subsets of boxes and store them in all_box_subsets
  sub_sets_boxes (box_list, sub_set, 0, all_box_subsets)

  # initialize the size of the largest sub-set of nesting boxes
  largest_size = 0

  # create a list to hold the largest subsets of nesting boxes
  all_nesting_boxes = []

  # go through all the subset of boxes and only store the
  # largest subsets that nest in all_nesting_boxes
  largest_size = largest_nesting_subsets (all_box_subsets, largest_size, all_nesting_boxes)

  # print the largest number of boxes that fit
  print (largest_size)

  # print the number of sets of such boxes
  print (len(all_nesting_boxes))

if __name__ == "__main__":
  main()

