"""
This module defines the NQueens class.
"""
from sys import argv
from state import *

class NQueens(object):
    """ Class to define the NQueens problem.
    Attributes:
        size (int): size of the board
        state (State): defines the state of the board
    Methods:
        dfs(self, row)
        print_sol(self)
        transition_model(self, row, col)
        goal_test(self, state)
        run(self)
    """
    def __init__(self, N):
        if N < 4:
            raise ValueError("N must be greater or equal to 4")
        self.size = N
        self.state = State(N)

    def count_sol(self, N):
        ones = 2**N - 1
        count = 0
        def helper(ld, col, rd):
            nonlocal count # scope includes outer function, but is not global
            if col == ones:
                count += 1
                return
            slots = ~(ld | col | rd) & ones
            while slots:
                bit = slots & -slots
                slots -= bit
                helper((ld | bit ) >> 1, col | bit, (rd | bit ) << 1)
        helper(0,0,0)
        return count

    
    def dfs(self, row):
        if self.goal_test(self.state):
            self.state.solution_set.add(self.state.frontier.top())
            return
        # interate through each column per row
        for col in range(self.size):
            #print(self.state.frontier)
            # if current square is safe
            if self.state.is_safe(row, col):
                # add square to solution
                self.state.add(row,col)
                # go to next row
                self.dfs(row + 1)
                # remove square from solution
                self.state.remove(row,col)
            
    def print_sol(self):
        for s in self.state.solution_set:
            print(*s)

    # returns the board with a queen added to the specified square
    def transition_model(self, row, col):
        self.add_queen(row, col)
        return board
    
    # returns N queens are on the board, none attacked (verified with dfs() function)
    def goal_test(self, state):
        return not -1 in state.frontier.top()

    def run(self):
        self.dfs(0)
        return self.state.solution_set


def main():
    N = int(argv[1])
    a1 = NQueens(N)
    out = a1.run()
    a1.print_sol()
    print(a1.count_sol(N) == len(a1.state.solution_set))

if __name__ == '__main__':
    main()

