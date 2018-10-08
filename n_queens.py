class NQueens(object):
    def __init__(self, N):
        self.size = N
        self.sol = self.init_solution(N)
    
    def init_solution(self, N):
        return tuple([-1 for i in range(N)])

    def solver():
    # place queen in upper left corner
        return 0
    # add a queen to any empty square
    def action():
        return 0

    # returns the board with a queen added to the specified square
    def transition_model(square):
        return 0
    
    # returns N queens are on the board, none attacked
    def goal_test(self, state):
        return state

a = NQueens(8)
print(a.sol)
