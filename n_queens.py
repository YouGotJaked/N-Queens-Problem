"""
This module defines the NQueens class.
"""
from sys import argv
from state import *

class NQueens(object):
    def __init__(self, N):
        if N < 4:
            raise ValueError("N must be greater or equal to 4")
        self.size = N
        self.state = State(N)
    
    # https://www.cl.cam.ac.uk/~mr10/backtrk.pdf #
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
        if self.goal_test(len(self.state.locs)):
            # don't add duplicates to solution set
            if self.state.locs not in self.state.solution_set:
                self.state.solution_set.add(self.state.locs)
            return
        for col in range(self.size):
            if self.state.is_safe(row, col):
                self.state.add(row,col)
                self.dfs(row + 1)
                self.state.remove(row,col)
            print(self.state.locs)
            
    def print_sol(self):
        for s in self.state.solution_set:
            print(*s)

    # returns the board with a queen added to the specified square
    def transition_model(self, row, col):
        self.add_queen(row, col)
        return board
    
    # returns N queens are on the board, none attacked (verified with dfs() function)
    def goal_test(self, state):
        return state == self.size

    def run(self):
        self.dfs(0)
        return self.state.solution_set

def main():
    N = int(argv[1])
    a1 = NQueens(N)
    out = a1.run()
    n_sols = a1.count_sol(N)
    a1.print_sol()
    print(len(out) == n_sols)
main()
