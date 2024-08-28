from map import Map
from common import apply_action_to_position
from copy import deepcopy

def bfs(map: Map) -> list:

    # Creates a copy of the map
    walked_map = [[False for _ in range(map.n)] for _ in range(map.n)]
    
    # Stores the position to explore alongside the parent actions index
    queued = [(map.start_pos, 0)]
    
    # Stores all the actions taken to reach each node from the start position
    actions = [[]]
    reached = False
    while len(queued):
        position, actions_index = queued.pop(0)

        reached = position == map.end_pos 
        if reached:
            break

        for action in range(0, 4):
            
            pos = apply_action_to_position(position, action)

            # When not in range
            if not map.is_pos_valid(pos):
                continue
            
            # Already walked
            if walked_map[pos[0]][pos[1]]:
                continue
            
            walked_map[position[0]][position[1]] = True

            # Copies the parent path and adds it's position
            path = deepcopy(actions[actions_index])
            path.append(action)

            queued.append((pos, len(actions)))

            actions.append(path)

    if not reached:
        return None
    
    return actions[-1]