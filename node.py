"""
This module defines the Node and Stack class.
"""

class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Stack(object):
    def __init__(self, top=None):
        self.top = top
    
    def __str__(self):
        lst = []
        current = self.top
        while current is not None:
            lst.append(current.data)
            current = current.next
        return str(lst)

    # add a new element to the top of the stack
    def push(self, data):
        if self.top is None:
           self.top = Node(data)
        else:
           temp = Node(data)
           temp.next = self.top
           self.top = temp

    # remove and return the last element added to the stack
    def pop(self):
        if self.top is None:
            return None
        temp = self.top
        self.top = self.top.next
        return temp.data
