from chess_board_state import ChessBoardState
from typing import List
import random

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


def hill_climb(
        initial_board: ChessBoardState,
        maximum_states: int = 30,
        maximum_shoulder_iterations: int = 10):

    current_board = initial_board

    # Used to avoid large loop over shoulder
    consecutive_shoulder_count = 0

    for _ in range(maximum_states):

        current_threats = current_board.cached_threats
        
        if current_threats == 0:
            break

        successors = all_successors(current_board)
        successors.sort(key=lambda b: b.cached_threats)

        better_equal_successors = [successor for successor in successors if successor.cached_threats <= current_threats]

        if len(better_equal_successors) == 0:
            print("Local maximum reached!")
            break
        
        # Swaps for successor
        current_board = better_equal_successors[0]

        # When in shoulder
        if current_board.cached_threats == current_threats:
            print("Shoulder reached!")
            consecutive_shoulder_count += 1

            # Shoulder iteration limit reached
            if consecutive_shoulder_count == maximum_shoulder_iterations:
                print("Maximum shoulder iteration limit reached...")
                break

        else:
            print("Better successor found!")
            consecutive_shoulder_count = 0


    return current_board


if __name__ == "__main__":

    success_count = 0
    iterations = 1000
    for i in range(iterations):

        board = ChessBoardState(8)
        
        final_board = hill_climb(
            initial_board=board, 
            maximum_states=100,
            maximum_shoulder_iterations=30)
        
        if final_board.cached_threats == 0:
            success_count += 1

    print(f"Success ratio: {success_count / iterations}")
    # final_board = hill_climb(
    #     initial_board=board, 
    #     maximum_states=5,
    #     maximum_shoulder_iterations=1)

    # if final_board.cached_threats == 0:
    #     print("Success")
    # else:
    #     print("Failure")

    # print(final_board)

    # Random successor test
    # for i in range(3):

    #     print(f"Successor: {i}")
    #     successor_board = random_successor_chess_board(board)
    #     print(successor_board)

    # All successors test
    # for successor in all_successors(board):
    #     print("Successor")
    #     print(successor)


    


