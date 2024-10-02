from nqueens_utils import *
import time


def nqueens_backtracking(initial_board) -> NQueensSearchResult:
    """
    Implementation of backtracking algorithm for CSP. It's the most basic backtracking
    """
    
    result = NQueensSearchResult()
    result.board = initial_board.copy()
    result.time_taken = time.time()

    _backtrack(result.board, result)

    result.time_taken = time.time() - result.time_taken
    return result

def _backtrack(board: list, result: NQueensSearchResult) -> bool:

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
        return not has_any_threats(board)
    
    ## Actual code -----------------------------------------------------------
    var = select_unassigned_var()

    # When all variables got assigned
    if var == -1:
        return True

    # Iterates through all the possible values
    for value in order_domain_values():

        result.traversed_states += 1

        board[var] = value

        # Skips assignments that break the restrictions
        if not is_consistent_assignment():
            continue
        
        # Tries to find a solution with the assignment
        if _backtrack(board, result):
            return True

    # All assignments failed, sets variable to default state for backtracking        
    board[var] = -1
    return False
    

if __name__ == "__main__":
    board = create_empty_board(16)

    # Available domains for all the variables
    print_board(board)

    result = nqueens_backtracking(board)
    print_board(result.board)
    print(result.traversed_states)
    print(result.time_taken)
