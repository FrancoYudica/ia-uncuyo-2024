from nqueens_utils import *
import time

def nqueens_forward_chaining(initial_board, domains) -> NQueensSearchResult:
    """
    Implementation of backtracking algorithm for CSP. It uses forward chaining
    to reduce the exploration domain. In order to implement forward chaining, the
    memory usage is increased, in comparison with a simple backtracking implementation,
    since multiple copies if the `sub domains` are kept in the stack frames

    returns the amount of explored states
    """
    result = NQueensSearchResult()
    result.board = initial_board.copy()
    result.time_taken = time.time()

    _fc_backtrack(result.board, domains, result)

    result.time_taken = time.time() - result.time_taken
    return result

def _fc_backtrack(
        board: list, 
        domains: list, 
        result: NQueensSearchResult) -> bool:

    ## Helper functions ----------------------------------------------------
    def select_unassigned_var() -> int:
        for column_index, row_index in enumerate(board):
            if row_index == -1:
                return column_index
            
        return -1

    def order_domain_values(var) -> iter:
        return domains[var]

    def inference(var, value) -> list:
        """
        With the current variable assignment, var = value, reduces the domain
        of the remaining variables.
        In NQueens, it means that the current queen attack lines will be 
        removed from the other queen possible positions, aka domains.
        """
        # Copies all the domains, since these will be modified and we
        # want to keep the current domain intact in case we backtrack
        sub_domains = [domain.copy() for domain in domains]
        sub_domains[var] = [value]
        n = len(board)

        # Iterates for all the remaining columns (Note that iterating
        # through the previous columns doesn't make sense, since the 
        # variables are already set)
        for column_index in range(var + 1, n):

            domain = sub_domains[column_index]

            # Queen attacking the row
            if value in domain:
                domain.remove(value)

            # Queen attacking diagonals. Note that it's iterating over
            # a copy of domain. This is necessary to avoid skipping
            # indices while removing and iterating
            for domain_value in domain.copy():
                
                column_delta = column_index - var # Always positive!
                row_delta = value - domain_value

                # In any diagonal
                if column_delta == abs(row_delta):
                    sub_domains[column_index].remove(domain_value)

        return sub_domains
  
    ## Actual code -----------------------------------------------------------

    var = select_unassigned_var()

    # When all variables got assigned
    if var == -1:
        return True

    # Iterates through all the possible values
    for value in order_domain_values(var):
        
        result.traversed_states += 1
        
        # No need to check if the assignment if consistent, 
        # since it's done by previous inferences
        board[var] = value

        sub_domains = inference(var, value)

        # Tries to find a solution with the assignment
        if _fc_backtrack(board, sub_domains, result):
            return True

    # All assignments failed, sets variable to default state for backtracking        
    board[var] = -1
    return False
    

if __name__ == "__main__":
    board = create_empty_board(16)

    # Available domains for all the variables
    domains = [[i for i in range(len(board))] for _ in range(len(board))]
    print_board(board)

    result = nqueens_forward_chaining(board, domains)
    print_board(result.board)
    print(result.traversed_states)
    print(result.time_taken)
