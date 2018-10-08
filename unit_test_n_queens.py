from n_queens import *
import unittest

class TestProblem(unittest.TestCase):
    def n_queens(self):
        agent1, agent2 = NQueens(5), NQueens(8)
        self.assertEqual(agent1.run(), ())
        self.assertEqual(agent2.run(), (7, 3 ,0, 2, 5, 1, 6, 4))

if __name__ == '__main__':
    unittest.main()
