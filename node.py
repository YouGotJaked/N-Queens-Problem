"""
This module defines the Node class.
"""

class Node(object):
    def __init__(self, locs, next=None):
        self.locs = locs
        self.next = next

class UnorderedList(list):
    def __init__(self):
        self.head = None
    
    def __str__(self):
        lst = []
        current = self.head
        while current is not None:
            lst.append(current.locs)
            current = current.next
        return str(lst)
            
    def empty(self):
        return self.head == None

    def append(self, locs):
        current = self.head
        if current:
            while current.next is not None:
                current = current.next
            current.next = Node(locs)
        else:
            self.head = Node(locs)

    def pop(self):
        prev = None
        current = self.head
        while current.next is not None:
            prev = current
            current = current.next
        prev.next = None
        return current.locs



N=8
n1 = Node(tuple([-1 for row in range (N)]))
l1 = n1.locs
n2 = Node(n1.locs[:3] + (7,) + n1.locs[3+1:])
l2 = n2.locs

ul = UnorderedList()
ul.append(l1)
ul.append(l2)
ul.append(l1)
ul.append(l2)
ul.append(l1)
ul.append(l2)
ul.append(l1)
ul.append(l2)
ul.append(l1)
ul.append(l2)
current = ul.head
print(ul)

print("Popped: {}".format(ul.pop()))
print(ul)
