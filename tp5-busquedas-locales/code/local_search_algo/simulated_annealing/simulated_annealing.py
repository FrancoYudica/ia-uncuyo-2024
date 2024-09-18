from chess_board_state import ChessBoardState
from local_search_algo.utils import random_successor_chess_board
from local_search_algo.local_search_result import LocalSearchResult
import random
import time
import math

def schedule(t, cooling_rate) -> float:
    # Slower cooling schedule
    # return max(1.0 / (math.log(t + 1) * cooling_rate), 1e-10)
    return 1.0 / (t * cooling_rate)

def simulated_annealing(
        initial_board: ChessBoardState,
        maximum_states: int = 30,
        maximum_shoulder_iterations: int = 10) -> LocalSearchResult:

    search_result = LocalSearchResult()
    t0 = time.time()
    current_board = initial_board

    for t in range(1, maximum_states + 1):

        if current_board.cached_threats == 0:
            break

        # Computes all the possible successors for the current state
        successor_board = random_successor_chess_board(current_board)

        delta_e = successor_board.cached_threats - current_board.cached_threats

        next_board = None
        T = schedule(t, 0.5)

        # When successor gets closer to local minimum or same (shoulders)
        if delta_e <= 0.0:
            next_board = successor_board
        else:
            probability = math.exp(-delta_e / T)
            # print(T, probability)
            if random.random() < probability:
                next_board = successor_board
            else:
                next_board = current_board

        # Only updates when state is changed
        if current_board != next_board:
            search_result.traversed_states += 1
            search_result.h_values.append(current_board.cached_threats)

        current_board = next_board

    search_result.h_values.append(current_board.cached_threats)
    search_result.board = current_board
    search_result.time_taken = time.time() - t0
    return search_result