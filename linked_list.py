#!/usr/bin/python

class node:
  def __init__(self, n):
    self.color = n
    self.next = None

  def setNext(self, nextNode):
    self.next = nextNode

  def next():
    return self.next


N1 = node(5)
N2 = node(270)
print N1.color
print N2.color

N1.setNext(N2)
print N1.next.color

# create new node and add to list
N2.setNext(node(99))
print N2.next.color

n = N1
while (n):
  print ("Color: {0}").format(n.color)
  n = n.next

# move last node to the middle position of the 3 node linked list
print "Moving..."
N2.next.next = N2
N1.next = N2.next
N2.next = None

n = N1
while (n):
  print ("Color: {0}").format(n.color)
  n = n.next
