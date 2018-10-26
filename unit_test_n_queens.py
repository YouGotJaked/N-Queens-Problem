import unittest
from n_queens import NQueens


class TestProblem(unittest.TestCase):
    """Class to define a test
    """
    def test_n_queens(self):
        """
        """
        agent1, agent2 = NQueens(5), NQueens(8)
        self.assertIn((3, 1, 4, 2, 0), agent1.run())
        self.assertIn((7, 3, 0, 2, 5, 1, 6, 4), agent2.run())


if __name__ == '__main__':
    unittest.main()
