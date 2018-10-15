"""
This module defines the NQueens class.
"""
from board import *

class GoalTestError(Exception):
    pass

class NQueens(object):
    def __init__(self, N):
        self.size = N
        self.num_queens = 0
        self.state = [] #self.init_state(N)
        self.board = Board(N)
        self.solution_set = set()#[[] for sol in range(self.count_sol(N))]
    
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

    def add_queen(self, row, col):
        self.board.add(row,col)
        self.num_queens += 1
    
    def remove_queen(self, row, col):
        self.board.remove(row,col)
        self.num_queens -= 1
    
    def dfs(self, row):
        #     if self.goal_test(row):
        if len(self.board.locs) == self.size:
            if self.board.locs not in self.solution_set:

                self.solution_set.add(self.board.locs)
                print("WE JUST APPENDED: {}".format(self.board.locs))
                print("ITS LENGTH IS NOW: {}".format(len(self.solution_set)))
            print("WTF?")
            self.print_sol()
            print("_________________________")
            return "I have returned into run()"
        for col in range(self.size):
            if self.board.no_conflict(row, col):
                self.board.add(row,col)
                self.dfs(row + 1)
                self.board.remove(row,col)
            print(self.board.locs)
        return "I have ran more than I should"
            
    def print_sol(self):
        i = 0
        for s in self.solution_set:
            print("[{}]".format(i))
            i += 1
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
        alg = self.dfs(0)
        print("alg={}".format(alg))
        print("THE SOLUTION SET IS:")
        self.print_sol()
        self.state = self.final_state(self.board.locs)
        return self.state

def main():
    a1 = NQueens(8)
    print(a1.count_sol(8))
    print(a1.run())

if __name__ == '__main__':
    main()
