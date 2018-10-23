"""
This module defines the State class.
"""
from node import *

class State(object):
    """ Class to define a Chess gameboard.
    Attributes:
        size (int): size of the board
    Methods:
        is_safe(self, row, col)
        add(self, row, col)
        remove(self, row, col)
    """
    # O(1)
    def __init__(self, N):
        self.size = N
        self.board = [['-1' for row in range(N)] for col in range(N)] # N x N game board
        self.frontier = Stack(Node(self.init_state())) # keeps track of current queens on board,
        self.solution_set = set() # unordered set of total valid solutions

    def init_state(self):
        return tuple([-1 for row in range(self.size)])
    
    # O(N), N = row
    def is_safe(self, row, col):
        """ Checks rows before 'row' as no queen can be on rows > 'row'.
            Args:
            Returns:
        """
        l_diag = r_diag = col
        for i in range(row, -1, -1):
            # current square has a queen
            if self.board[i][col] == 'Q':
                return False
            # l_diag is valid square and has a queen
            if l_diag >= 0 and self.board[i][l_diag] == 'Q':
                return False
            # r_diag is valid square and has a queen
            if r_diag < self.size and self.board[i][r_diag] == 'Q':
                return False
            l_diag -= 1
            r_diag += 1
        return True

    def add(self, row, col):
        self.board[row][col] = 'Q'
        temp = self.frontier.top.data
        self.frontier.push(temp[:col] + (row, ) + temp[col+1:])
    
    def remove(self, row, col):
        self.board[row][col] = '-1'
        self.frontier.pop() # create new tuple with 'row'th element removed
