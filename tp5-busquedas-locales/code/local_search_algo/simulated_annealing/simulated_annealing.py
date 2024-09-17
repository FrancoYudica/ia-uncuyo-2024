from chess_board_state import ChessBoardState
from local_search_algo.utils import random_successor_chess_board
from local_search_algo.local_search_result import LocalSearchResult
import random
import time
import math

def schedule(t) -> float:
    # Slower cooling schedule
    return max(1.0 / math.log(t + 1), 1e-10)

def simulated_annealing(
        initial_board: ChessBoardState,
        maximum_states: int = 30,
        maximum_shoulder_iterations: int = 10) -> LocalSearchResult:

    search_result = LocalSearchResult()
    t0 = time.time()
    current_board = initial_board
    traversed_states = 1
    iterations = 0
    shoulder_counter = 0

    while traversed_states < maximum_states and iterations < maximum_states * 5:
        iterations += 1

        T = schedule(iterations)

        if T == 0:
            break
        
        if current_board.cached_threats == 0:
            break
        
        # Computes all the possible successors for the current state
        successor_board = random_successor_chess_board(current_board)

        # If the shoulder maximum count is reached, ensures that the successor
        # has a different value
        while shoulder_counter == maximum_shoulder_iterations:
            if successor_board.cached_threats == current_board.cached_threats:
                successor_board = random_successor_chess_board(current_board)
            else:
                break

        delta_e = successor_board.cached_threats - current_board.cached_threats

        next_board = None

        # When successor gets closer to local minimum or same (shoulders)
        if delta_e <= 0.0:
            next_board = successor_board
            # print(f"Picking better {current_board.cached_threats}")
        else:
            probability = math.exp(-delta_e / T)
            # print(f"T: {T}, delta_e: {delta_e}, probability: {probability}")

            if random.random() < probability:
                next_board = successor_board
                # print(f"Picking worse {current_board.cached_threats}")
            else:
                next_board = current_board

        if next_board.cached_threats == current_board.cached_threats:
            shoulder_counter += 1
        else:
            shoulder_counter = 0

        # Only updates when state is changed
        if current_board != next_board:
            traversed_states += 1
            search_result.h_values.append(current_board.cached_threats)

        current_board = next_board

    search_result.board = current_board
    search_result.time_taken = time.time() - t0
    search_result.traversed_states = traversed_states
    return search_result