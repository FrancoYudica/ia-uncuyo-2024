class NQueensSearchResult:
    def __init__(self) -> None:
        self.traversed_states = 0
        self.time_taken = 0
        self.solution_found = False
        self.board = []


def create_empty_board(size):
    return [-1 for _ in range(size)]


def print_board(board) -> str:
    string = ""
    n = len(board)
    for row in range(n):
        for column in range(n):
            if board[column] == row:
                string += " Q"
            else:
                string += " *"

        string += "\n"
        
    print(string)


def has_any_threats(board) -> bool:
    """
    Returns True if any pair of queens is threatening each other.
    board = [1, 2, 5, 6, 1, 4, 7, 0]
    """

    n = len(board)
    for column in range(n):
        row = board[column]

        if row == -1:
            continue

        # Tests with the remaining rows
        for child_column in range(column + 1, n):

            child_row = board[child_column]

            if child_row == -1:
                continue

            # Same row
            if row == child_row:
                return True

            else:
                direction = column - child_column, row - child_row
                slope = direction[0] / direction[1]

                # In diagonal
                if abs(slope) == 1.0:
                    return True

    return False