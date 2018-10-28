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
        """Constructor for the NQueens class.

        Raises:
            ValueError if `n` is less than 4
        """
        if n < 4:
            raise ValueError("N must be greater or equal to 4")
        self.size = n
        self.state = State(n)

    def dfs(self, col):
        """Perform depth-first search over valid queen placements on the board.
            
        Iterate through each row, per column.
        Check if the current square is safe.
        If it is safe, add the square to the frontier stack.
        Then, recursively call `dfs()` on the next column.
        Remove the current square from the board and state from the frontier
        stack after returning from previous recursive call.
        
        Args:
            col (int): current column index
        """
        if self.goal_test():
            self.state.solution_set.add(self.state.frontier.top.data)
            return
        for row in range(self.size):
            if self.state.is_safe(row, col):
                self.state.add(row, col)
                self.dfs(col + 1)
                self.state.remove(row, col)

    def goal_test(self):
        """Return `self.size` queens are on the board, none attacked.
            
        Guaranteed to be safe if `self.size` queens in current search state.
        This is verified with the `dfs()` method.
    
        Returns:
            bool: True if successful, False otherwise
        """
        return -1 not in self.state.frontier.top.data

    def run(self):
        """Run the depth-first search algorithm.
            
        Returns:
            The complete set of goal states
        """
        self.dfs(0)
        return self.state.solution_set
