import random
from chess_board_state import ChessBoardState
from typing import List


def random_successor_chess_board(board: ChessBoardState) -> ChessBoardState:
    columns = board.columns.copy()

    # Picks random column to move
    randomize_column_index = random.randrange(0, board.size)

    previous_row = columns[randomize_column_index]

    # Picks a random new row value different than previous
    new_row = random.choice([i for i in range(0, board.size) if i != previous_row])

    columns[randomize_column_index] = new_row

    successor = ChessBoardState(None, None, columns=columns)
    return successor


def all_successors(board: ChessBoardState) -> List[ChessBoardState]:
    """
    Will return a list of N*(N-1) successors.
    These are immediate successors, taking just one move to reach
    """
    successors: List[ChessBoardState] = []

    for column in range(board.size):
        for row in range(board.size):
            
            # Skips when it's the same as the parent
            if board.columns[column] == row:
                continue

            columns = board.columns.copy()

            # Moves just one to the current position
            columns[column] = row
            successor = ChessBoardState(None, None, columns=columns)
            successors.append(successor)

    return successors