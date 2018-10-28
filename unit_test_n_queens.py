"""unit_test_n_queens.py - module to create a unit test for the N Queens problem.
    
This module defines the TestProblem class.
"""
import unittest
from n_queens import NQueens


class TestProblem(unittest.TestCase):
    """Class to define a unit test for the N Queens problem.
    
    Create two agents for the 5 and 8 queens problems.
    Verify that the given solutions are in the solution set.
    """
    
    def test_n_queens(self):
        """Create two test cases instances for the N Queens Problem."""
        agent1, agent2 = NQueens(5), NQueens(8)
        self.assertIn((3, 1, 4, 2, 0), agent1.run())
        self.assertIn((7, 3, 0, 2, 5, 1, 6, 4), agent2.run())


if __name__ == '__main__':
    unittest.main()
