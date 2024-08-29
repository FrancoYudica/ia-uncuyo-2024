from map import Map
from common import apply_action_to_position
from copy import deepcopy
from .walk_results import WalkResults


def bfs(map: Map) -> WalkResults:

    # Creates a copy of the map
    walked_map = [[False for _ in range(map.n)] for _ in range(map.n)]
    
    # Stores the position to explore alongside the parent actions index
    queued = [(map.start_pos, 0)]
    
    # Stores all the actions taken to reach each node from the start position
    actions = [[]]
    reached = False

    results = WalkResults()
    results.start_timing()
    while len(queued):
        position, actions_index = queued.pop(0)

        reached = position == map.end_pos 
        if reached:
            break

        for action in range(0, 4):
            
            child_pos = apply_action_to_position(position, action)

            # When not in range or not walkable or already walked
            if not map.is_pos_valid(child_pos) or \
                not map.is_pos_walkable(child_pos) or \
                walked_map[child_pos[0]][child_pos[1]]:
                continue
            
            walked_map[child_pos[0]][child_pos[1]] = True

            # Copies the parent path and adds it's position
            path = actions[actions_index][:]
            path.append(action)

            queued.append((child_pos, len(actions)))

            actions.append(path)
        
    results.stop_timing()

    if not reached:
        return None
    
    results.actions = actions[actions_index]
    return results