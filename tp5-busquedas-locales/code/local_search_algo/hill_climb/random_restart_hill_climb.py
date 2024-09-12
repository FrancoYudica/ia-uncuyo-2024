from chess_board_state import ChessBoardState
from .hill_climb import hill_climb
from local_search_algo.local_search_result import LocalSearchResult
import time

def random_restart_hill_climb(
        board: ChessBoardState,
        maximum_states: int = 30,
        maximum_shoulder_iterations: int = 10) -> LocalSearchResult:
    """Complete local search algorithm that runs hill climb until a solution is found"""

    # Random restart result
    rr_result: LocalSearchResult = LocalSearchResult()
    t0 = time.time()
    
    hill_success_result: LocalSearchResult = None

    while True:

        hill_climb_result = hill_climb(
            initial_board=board, 
            maximum_states=maximum_states,
            maximum_shoulder_iterations=maximum_shoulder_iterations)
        
        rr_result.traversed_states += hill_climb_result.traversed_states

        if hill_climb_result.board.cached_threats == 0:
            hill_success_result = hill_climb_result
            break

    rr_result.time_taken = time.time() - t0
    rr_result.board = hill_success_result.board
    
    return rr_result