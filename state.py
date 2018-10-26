"""state.py - module to store the state of the N Queens problem.
This module defines the State class.
"""
from node import Node, Stack


class State():
    """Class to define the state space for the N Queens problem.
        
    Args:
        n (int): number of queens
    Attributes:
        size (int): size of the board
        board (str[][]): matrix to define the board
        frontier (Stack):
        solution_set (set): unordered set of total valid solutions
    """
    def __init__(self, n):
        """Constructor for the State class.
        Args:
            n (int): number of queens
        """
        self.size = n
        self.board = [['-1' for row in range(n)] for col in range(n)]
        self.frontier = Stack(Node(self.init_state()))
        self.solution_set = set()

    def init_state(self):
        """Return a tuple of length `self.size`, each element set to -1."""
        return tuple([-1 for row in range(self.size)])

    def is_safe(self, row, col):
        """Check if the current square is safe to place a queen.
            
        Only check columns before `col` as no queen can be on columns greater
        than the current column.
        The current square is not safe if the current square or one of its
        diagonals contains a queen.
        
        Args:
            row (int): current row index
            col (int): current column index
        Returns:
            bool: True if successful, False otherwise
        """
        l_diag = r_diag = row
        for i in range(col, -1, -1):
            # current square has a queen
            if self.board[row][i] == 'Q':
                return False
            # l_diag is valid square and has a queen
            if l_diag >= 0 and self.board[l_diag][i] == 'Q':
                return False
            # r_diag is valid square and has a queen
            if r_diag < self.size and self.board[r_diag][i] == 'Q':
                return False
            l_diag -= 1
            r_diag += 1
        return True

    def add(self, row, col):
        """Add a queen to the board at the specified square.
            
        Assign square at row `row` and column `col` to 'Q', or a queen.
        Push a new to the frontier stack.
        
        Args:
            row (int):
            col (int):
        """
        self.board[row][col] = 'Q'
        temp = self.frontier.top.data
        self.frontier.push(temp[:col] + (row,) + temp[col + 1:])

    def remove(self, row, col):
        """Remove a queen from the board at the specified square.
            
        Assign square at row `row` and column `col` to '-1', or not a queen.
        Pop the top element from the frontier stack.
        
        Args:
            row (int): current row index
            col (int): current column index
        """
        self.board[row][col] = '-1'
        self.frontier.pop()
