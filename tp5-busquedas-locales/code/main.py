from chess_board_state import ChessBoardState
from typing import List
import random
import time
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



def random_restart_hill_climb_test(board):
    print("RUNNING: RANDOM RESTART HILL CLIMB")

    result: LocalSearchResult = random_restart_hill_climb(board)

    print(f"Random restart hill climb traversed {result.traversed_states} states in {result.time_taken} seconds")
    print(result.board)


if __name__ == "__main__":
    board = ChessBoardState(20)
    hill_climb_test(board)
    random_restart_hill_climb_test(board)

    # for i in range(iterations):

        
    #     final_board = hill_climb(
    #         initial_board=board, 
    #         maximum_states=30,
    #         maximum_shoulder_iterations=10)
        
    #     if final_board.cached_threats == 0:
    #         success_count += 1

    # print(f"Success ratio: {success_count / iterations}")
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


    


