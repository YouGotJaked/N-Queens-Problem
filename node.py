"""node.py - module to
This module defines the Node and Stack classes.
"""


class Node():   # pylint: disable=too-few-public-methods
    """Class to define a node in the frontier.
        
    Args:
        data (tuple): n-element tuple representing a state in the search
        next (Node): node pointed to by this node (default is `None`)
    """
    def __init__(self, data, next=None):    # pylint: disable=redefined-builtin
        """Constructor for the Node class.
        """
        self.data = data
        self.next = next

class Stack():
    """Class to define the stack abstract data type.
        
    Attributes:
        top (Node): last element inserted into the stack
    """
    def __init__(self, top=None):
        """Constructor for the Stack class.
            
        Args:
            top (Node, optional): top element of the stack (default is `None`)
        """
        self.top = top

    def push(self, data):
        """Add a new element to the top of the stack.
            
        Args:
            data (tuple): n-element tuple representing a state in the search
        """
        if self.top is None:
            self.top = Node(data)
        else:
            temp = Node(data)
            temp.next = self.top
            self.top = temp

    def pop(self):
        """Remove and return the last element added to the stack.
            
        Returns:
            None if stack is empty, otherwise the last element of the stack
        """
        if self.top is None:
            return None
        temp = self.top
        self.top = self.top.next
        return temp.data
