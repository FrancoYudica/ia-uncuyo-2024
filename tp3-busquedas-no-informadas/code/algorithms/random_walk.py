from map import Map
from common import apply_action_to_position
from .walk_results import WalkResults
from random import randrange

def random_walk(
        map: Map,
        max_iterations: int = 10000) -> WalkResults:
    
    results = WalkResults()
    results.start_timing()
    
    position = map.start_pos

    # When the end isn't reached, and there isn't a limit in iterations
    # or the iteration limit isn't reached
    while position != map.end_pos and \
          (max_iterations is None or len(results.actions) < max_iterations):
        
        action = randrange(0, 4)
        next_pos = apply_action_to_position(position, action)

        if not map.is_pos_valid(next_pos) or not map.is_pos_walkable(next_pos):
            continue

        # Updates position and stores action
        position = next_pos
        results.actions.append(action)
        
    results.stop_timing()

    return results