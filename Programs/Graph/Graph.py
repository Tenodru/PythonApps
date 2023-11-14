#  File: Graph.py

#  Description: A program that contains and tests various methods with graphs.

#  Developers: Alex Kong, Victor Do

#  Date Created: 11/21/2020

#  Date Last Modified: 11/22/2020

import sys

class Stack (object):
  def __init__ (self):
    self.stack = []

  # add an item to the top of the stack
  def push (self, item):
    self.stack.append (item)

  # remove an item from the top of the stack
  def pop (self):
    return self.stack.pop()

  # check the item on the top of the stack
  def peek (self):
    return self.stack[-1]

  # check if the stack if empty
  def is_empty (self):
    return (len (self.stack) == 0)

  # return the number of elements in the stack
  def size (self):
    return (len (self.stack))


class Queue (object):
  def __init__ (self):
    self.queue = []

  # add an item to the end of the queue
  def enqueue (self, item):
    self.queue.append (item)

  # remove an item from the beginning of the queue
  def dequeue (self):
    return (self.queue.pop(0))

  # check if the queue is empty
  def is_empty (self):
    return (len (self.queue) == 0)

  # return the size of the queue
  def size (self):
    return (len (self.queue))


class Vertex (object):
  def __init__ (self, label):
    self.label = label
    self.visited = False

  # determine if a vertex was visited
  def was_visited (self):
    return self.visited

  # determine the label of the vertex
  def get_label (self):
    return self.label

  # string representation of the vertex
  def __str__ (self):
    return str (self.label)


class Graph (object):
  def __init__ (self):
    self.Vertices = []
    self.adjMat = []

  # check if a vertex is already in the graph
  def has_vertex (self, label):
    nVert = len (self.Vertices)
    for i in range (nVert):
      if (label == (self.Vertices[i]).get_label()):
        return True
    return False

  # given the label get the index of a vertex
  def get_index (self, label):
    nVert = len (self.Vertices)
    for i in range (nVert):
      if (label == (self.Vertices[i]).get_label()):
        return i
    return -1

  # add a Vertex with a given label to the graph
  def add_vertex (self, label):
    if (self.has_vertex (label)):
      return

    # add vertex to the list of vertices
    self.Vertices.append (Vertex (label))

    # add a new column in the adjacency matrix
    nVert = len (self.Vertices)
    for i in range (nVert - 1):
      (self.adjMat[i]).append (0)

    # add a new row for the new vertex
    new_row = []
    for i in range (nVert):
      new_row.append (0)
    self.adjMat.append (new_row)

  # add weighted directed edge to graph
  def add_directed_edge (self, start, finish, weight = 1):
    self.adjMat[start][finish] = weight

  # add weighted undirected edge to graph
  def add_undirected_edge (self, start, finish, weight = 1):
    self.adjMat[start][finish] = weight
    self.adjMat[finish][start] = weight

  # get edge weight between two vertices
  # return -1 if edge does not exist
  def get_edge_weight (self, fromVertexLabel, toVertexLabel):
    fromIdx = self.get_index(fromVertexLabel)
    toIdx = self.get_index(toVertexLabel)

    if (self.adjMat[fromIdx][toIdx] <= 0):
      return -1
    else:
      return self.adjMat[fromIdx][toIdx]

  # get a list of immediate neighbors that you can go to from a vertex
  # return a list of indices or an empty list if there are none
  def get_neighbors (self, vertexLabel):
    neighbors = []
    nVert = len (self.Vertices)
    for i in range (nVert):
      weight = self.get_edge_weight(vertexLabel, self.Vertices[i].label)
      if (weight > 0):
        neighbors.append(self.Vertices[i].label)
    return neighbors

  # return an unvisited vertex adjacent to vertex v (index)
  def get_adj_unvisited_vertex (self, v):
    nVert = len (self.Vertices)
    for i in range (nVert):
      if (self.adjMat[v][i] > 0) and (not (self.Vertices[i]).was_visited()):
        return i
    return -1

  # get a copy of the list of Vertex objects
  def get_vertices (self):
    return self.Vertices

  # do a depth first search in a graph
  def dfs (self, v):
    # create the Stack
    theStack = Stack ()

    # mark the vertex v as visited and push it on the Stack
    (self.Vertices[v]).visited = True
    print (self.Vertices[v])
    theStack.push (v)

    # visit all the other vertices according to depth
    while (not theStack.is_empty()):
      # get an adjacent unvisited vertex
      u = self.get_adj_unvisited_vertex (theStack.peek())
      if (u == -1):
        u = theStack.pop()
      else:
        (self.Vertices[u]).visited = True
        print (self.Vertices[u])
        theStack.push (u)

    # the stack is empty, let us rest the flags
    nVert = len (self.Vertices)
    for i in range (nVert):
      (self.Vertices[i]).visited = False

  # do the breadth first search in a graph
  def bfs (self, v):
    # create the Queue
    theQueue = Queue ()
    nVert = len (self.Vertices)

    # mark the vertex v as visited and enqueue it on the Queue
    (self.Vertices[v]).visited = True
    print (self.Vertices[v])
    theQueue.enqueue (v)

    # visit all the other vertices according to breadth
    while (not theQueue.is_empty()):
      # get an adjacent unvisited vertex
      u = self.get_adj_unvisited_vertex (theQueue.queue[0])
      if (u == -1):
        u = theQueue.dequeue()
      else:
        (self.Vertices[u]).visited = True
        print (self.Vertices[u])
        theQueue.enqueue (u)

    # the queue is empty, let us rest the flags
    for j in range (nVert):
      (self.Vertices[j]).visited = False
  
  # delete an edge from the adjacency matrix
  # delete a single edge if the graph is directed
  # delete two edges if the graph is undirected
  def delete_edge (self, fromVertexLabel, toVertexLabel):
    fromIdx = self.get_index(fromVertexLabel)
    toIdx = self.get_index(toVertexLabel)
    fromWeight = self.get_edge_weight(fromVertexLabel, toVertexLabel)
    toWeight = self.get_edge_weight(toVertexLabel, fromVertexLabel)
    
    if (fromWeight == toWeight):
      self.adjMat[fromIdx][toIdx] = 0
      self.adjMat[toIdx][fromIdx] = 0
    else:
      self.adjMat[fromIdx][toIdx] = 0

  # delete a vertex from the vertex list and all edges from and
  # to it in the adjacency matrix
  def delete_vertex (self, vertexLabel):
    nVert = len (self.Vertices)
    idx = self.get_index(vertexLabel)
    self.Vertices.pop(idx)
    for j in range (nVert):
      self.adjMat[j].pop(idx)
    self.adjMat.pop(idx)

def main():
  # create the Graph object
  cities = Graph()

  # read the number of vertices
  line = sys.stdin.readline()
  line = line.strip()
  num_vertices = int (line)

  # read the vertices to the list of Vertices
  for i in range (num_vertices):
    line = sys.stdin.readline()
    city = line.strip()
    #print (city)
    cities.add_vertex (city)

  # read the number of edges
  line = sys.stdin.readline()
  line = line.strip()
  num_edges = int (line)
  #print (num_edges)

  # read each edge and place it in the adjacency matrix
  for i in range (num_edges):
    line = sys.stdin.readline()
    edge = line.strip()
    #print (edge)
    edge = edge.split()
    start = int (edge[0])
    finish = int (edge[1])
    weight = int (edge[2])

    cities.add_directed_edge (start, finish, weight)

  # read the starting vertex for dfs and bfs
  line = sys.stdin.readline()
  start_vertex = line.strip()
  #print (start_vertex)

  # get the index of the starting vertex
  start_index = cities.get_index (start_vertex)
  #print (start_index)

  # do the depth first search
  print ("\nDepth First Search")
  cities.dfs (start_index)
  print ()

  # do the breadth first search
  print ("\nBreadth First Search")
  cities.bfs (start_index)
  print ()

  line = sys.stdin.readline()
  vertexes = line.strip()
  vertexes = vertexes.split()

  print("Deletion of an edge")
  cities.delete_edge(vertexes[0], vertexes[1])

  # print the adjacency matrix
  print ("\nAdjacency Matrix")
  for i in range (num_vertices):
    for j in range (num_vertices):
      print (cities.adjMat[i][j], end = " ")
    print ()
  print ()

  line = sys.stdin.readline()
  delVertex = line.strip()

  print("Deletion of a vertex")
  cities.delete_vertex(delVertex)
  print(" ")

  print("List of Vertices")
  num_vertices = len(cities.Vertices)
  for k in range (num_vertices):
    print(cities.Vertices[k])

  # print the adjacency matrix
  print ("\nAdjacency Matrix")
  for i in range (num_vertices):
    for j in range (num_vertices):
      print (cities.adjMat[i][j], end = " ")
    print ()
  print ()

  #testing get_neighbors
  #print(cities.get_neighbors("Chicago"))
    
if __name__ == "__main__":
  main()
