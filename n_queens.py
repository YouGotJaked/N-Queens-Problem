"""n_queens.py - module to define and implement the N Queens problem.
This module defines the NQueens class.
"""
from state import State


class NQueens():
    """Class to define the NQueens problem.
        
    Args:
        n (int): number of queens
    
    Attributes:
        size (int): size of the board
        state (State): state space of the board
    """
    def __init__(self, n):
        """Constructor
            Args:
                n (int): number of queens
            Raises:
                ValueError if `n` is less than 4
        """
        if n < 4:
            raise ValueError("N must be greater or equal to 4")
        self.size = n
        self.state = State(n)

    def dfs(self, col):
        """Perform depth-first search over valid queen placements on the board.
        Args:
            col (int): current column index
        """
        if self.goal_test(self.state.frontier.top.data):
            self.state.solution_set.add(self.state.frontier.top.data)
            return
        # interate through each row per column
        for row in range(self.size):
            # if current square is safe
            if self.state.is_safe(row, col):
                # add square to solution
                self.state.add(row, col)
                # go to next column
                self.dfs(col + 1)
                # remove square from solution
                self.state.remove(row, col)

    # returns N queens are on the board, none attacked
    def goal_test(self, state):
        """Return `self.size` queens are on the board, none attacked.
        Args:
            state (tuple):
        """
        return -1 not in state

    def run(self):
        """Run the depth-first search algorithm.
        Returns:
            The complete set of goal states
        """
        self.dfs(0)
        return self.state.solution_set
