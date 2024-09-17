from chess_board_state import ChessBoardState
from local_search_algo.utils import random_successor_chess_board, all_successors
from local_search_algo.local_search_result import LocalSearchResult
import random
import time
import math


def schedule(t) -> float:

    return max(0.0, 1.0 / t)
    # return 1.0 / t

def simulated_annealing(
        initial_board: ChessBoardState,
        maximum_states: int = 30) -> LocalSearchResult:

    search_result = LocalSearchResult()
    t0 = time.time()
    current_board = initial_board

    for t in range(1, maximum_states + 1):
        search_result.h_values.append(current_board.cached_threats)

        search_result.traversed_states += 1
        T = schedule(t)

        if T == 0:
            break
        
        if current_board.cached_threats == 0:
            break
        
        # Computes all the possible successors for the current state
        successor_board = random_successor_chess_board(current_board)

        delta_e = successor_board.cached_threats - current_board.cached_threats

        # When successor gets closer to local minimum.
        # By adding equals, it moves in shoulders
        if delta_e <= 0.0:
            current_board = successor_board
            print(f"Picking better {current_board.cached_threats}")

        else:
            # Picks successor with some probability in [0, 1.0]
            probability = math.exp(-delta_e * 0.01 / T)

            print(probability)
            if random.random() < probability:
                current_board = successor_board
                print(f"Picking worse {current_board.cached_threats}")


    search_result.board = current_board
    search_result.time_taken = time.time() - t0
    return search_result