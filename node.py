"""
This module defines the Node class.
"""

class Node(object):
    def __init__(self, locs, parent=None):
        self.locs = locs
        self.parent = parent
