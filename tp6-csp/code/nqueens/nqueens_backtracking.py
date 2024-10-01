from nqueens_utils import *


def backtracking_search(board) -> dict:
    """
    Implementation of backtracking algorithm for CSP. It's the most basic backtracking
    """
    
    if _backtrack(board):
        return board

    return []

def _backtrack(board: list) -> bool:

    ## Helper functions ----------------------------------------------------
    def select_unassigned_var() -> int:
        for column_index, row_index in enumerate(board):
            if row_index == -1:
                return column_index
            
        return -1

    def order_domain_values() -> iter:
        # Iterator that removes the values from the domain once it's yield
        for i in range(len(board)):
            yield i

    def is_consistent_assignment() -> bool:
        # Is consistent if the amount of threats doesn't increase
        return count_board_threats(board) == 0
    
    ## Actual code -----------------------------------------------------------
    var = select_unassigned_var()

    # When all variables got assigned
    if var == -1:
        return True

    # Iterates through all the possible values
    for value in order_domain_values():

        board[var] = value

        # Skips assignments that break the restrictions
        if not is_consistent_assignment():
            continue
        
        # Tries to find a solution with the assignment
        if _backtrack(board):
            return True

    # All assignments failed, sets variable to default state for backtracking        
    board[var] = -1
    return False
    

if __name__ == "__main__":
    board = create_empty_board(16)
    print_board(board)

    backtracking_search(board)
    print_board(board)
    print(board)
