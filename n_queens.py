"""
This module defines the NQueens class.
"""
from board import *

class GoalTestError(Exception):
    pass

class NQueens(object):
    def __init__(self, N):
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
    #   if len(self.state.locs) == self.size:
            if self.state.locs not in self.state.solution_set:
                self.state.solution_set.add(self.state.locs)
            return
        for col in range(self.size):
            if self.state.no_conflict(row, col):
                self.state.add(row,col)
                self.dfs(row + 1)
                self.state.remove(row,col)
            print(self.state.locs)
            
    def print_sol(self):
        for s in self.state.solution_set:
            print(*s)

    def init_state(self, N):
        return [-1 for i in range(N)]
    
    def final_state(self, state):
        return tuple(state)

    # returns the board with a queen added to the specified square
    def transition_model(self, row, col):
        self.add_queen(row, col)
        return board
    
    # returns N queens are on the board, none attacked (verified with dfs() function)
    def goal_test(self, state):
        return state == self.size

    def run(self):
        self.dfs(0)
        print("THE SOLUTION SET IS:")
        self.print_sol()
        return self.state.solution_set

def main():
    a1 = NQueens(8)
    print(a1.count_sol(8))
    sset = a1.run()
    print((2,7,3,6,0,5,1,4) in sset)

if __name__ == '__main__':
    main()
