"""
This module defines the Board class.
"""

class Board(object):
    """ Class to define a Chess gameboard.
    Attributes:
        N (int): size of the board
    Methods:
        no_conflict(self, row, col)
    """
    # O(1)
    def __init__(self, N):
        self.size = N
        self.board = [['-1' for row in range(N)] for col in range(N)]
        self.locs = ()

    # O(N), N = row
    def no_conflict(self, row, col):
        """ Checks rows before 'row' as no queen can be on rows > 'row'.
            Args:
            Returns:
        """
        l_diag = r_diag = col
        for i in range(row, -1, -1):
        #   print("row: {}\tcol: {}".format(i,col))
            if self.board[i][col] == 'Q':
                return False
            if l_diag >= 0 and self.board[i][l_diag] == 'Q':
                return False
            if r_diag < self.size and self.board[i][r_diag] == 'Q':
                return False
            l_diag -= 1
            r_diag += 1
        return True

    def add(self, row, col):
        self.board[row][col] = 'Q'
        self.locs += (col,)

    def remove(self, row, col):
        self.board[row][col] = '-1'
        self.locs = self.locs[:len(self.locs)-1]

    def outputFormat(self):
            return [''.join(x) for x in self.board]
