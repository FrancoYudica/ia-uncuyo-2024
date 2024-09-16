from chess_board_state import ChessBoardState
from local_search_algo.local_search_result import LocalSearchResult

from local_search_algo.hill_climb.random_restart_hill_climb import hill_climb
from local_search_algo.hill_climb.random_restart_hill_climb import random_restart_hill_climb


def hill_climb_test(board):
    print("RUNNING: HILL CLIMB")
    result: LocalSearchResult = hill_climb(board)

    print(f"Hill climb traversed {result.traversed_states} states in {result.time_taken} seconds")

    if result.board.cached_threats == 0:
        print("Success")
        print(result.board)

    else:
        print(f"Failure. Stuck at {result.board.cached_threats} threats")


def hill_climb_success_rate_test(
        random_board_count,
        board_size, 
        iterations_per_board):

    success_count = 0

    for _ in range(random_board_count):
        board = ChessBoardState(board_size)

        for _ in range(iterations_per_board):
            result: LocalSearchResult = hill_climb(board)

            if result.board.cached_threats == 0:
                success_count += 1

    total_samples = random_board_count * iterations_per_board
    print(f"Success count {success_count}/{total_samples}. Success rate: {success_count/total_samples}")    



def random_restart_hill_climb_test(board):
    print("RUNNING: RANDOM RESTART HILL CLIMB")

    result: LocalSearchResult = random_restart_hill_climb(board)

    print(f"Random restart hill climb traversed {result.traversed_states} states in {result.time_taken} seconds")
    print(result.board)


if __name__ == "__main__":
    board = ChessBoardState(8)
    hill_climb_success_rate_test(20, 8, 30)
