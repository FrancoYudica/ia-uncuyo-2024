from chess_board_state import ChessBoardState
from local_search_algo.utils import all_successors
from local_search_algo.local_search_result import LocalSearchResult
import random
import time


def hill_climb(
        initial_board: ChessBoardState,
        maximum_states: int = 30,
        maximum_shoulder_iterations: int = 10) -> LocalSearchResult:

    search_result = LocalSearchResult()
    t0 = time.time()
    current_board = initial_board

    # Used to avoid large loop over shoulder
    consecutive_shoulder_count = 0

    for _ in range(maximum_states):
        search_result.traversed_states += 1
        current_threats = current_board.cached_threats
        
        if current_threats == 0:
            break
        
        # Computes all the possible successors for the current state
        successors = all_successors(current_board)
        successors.sort(key=lambda b: b.cached_threats)

        # Filters the successors with greater threats
        better_equal_successors = [successor for successor in successors if successor.cached_threats <= current_threats]

        # Local maximum reached. Exists with failure
        if len(better_equal_successors) == 0:
            break
        
        # Threats of the next successor
        successor_threats = better_equal_successors[0].cached_threats

        # Randomly chooses the successor from the successors that have the best cost
        current_board = random.choice([successor for successor in better_equal_successors if successor.cached_threats == successor_threats])

        # When in shoulder
        if current_board.cached_threats == current_threats:
            consecutive_shoulder_count += 1

            # Shoulder iteration limit reached. Exits with failure
            if consecutive_shoulder_count == maximum_shoulder_iterations:
                break
        
        # Better successor is found
        else:
            consecutive_shoulder_count = 0

    search_result.board = current_board
    search_result.time_taken = time.time() - t0
    return search_result