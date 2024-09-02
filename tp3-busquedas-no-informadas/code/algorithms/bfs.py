from map import Map
from common import apply_action_to_position
from .walk_results import WalkResults


def bfs(map: Map) -> WalkResults:

    # Stores the last action used to reach the node and the parent position
    reached_nodes = [[None for _ in range(map.n)] for _ in range(map.n)]
    reached_nodes[map.start_pos[0]][map.start_pos[1]] = (None, None)

    # Stores the positions to explore
    queued = [map.start_pos]

    reached = False

    results = WalkResults()
    results.start_timing()
    
    while len(queued):
        position = queued.pop(0)
        results.explored_cells += 1

        reached = position == map.end_pos 
        if reached:
            break

        for action in range(0, 4):
            
            child_pos = apply_action_to_position(position, action)

            # When not in range or not walkable or already walked
            if not map.is_pos_valid(child_pos) or \
                not map.is_pos_walkable(child_pos) or \
                reached_nodes[child_pos[0]][child_pos[1]] is not None:
                continue
            
            # Stores the action taken to reach the node
            reached_nodes[child_pos[0]][child_pos[1]] = (action, position)

            queued.append(child_pos)
        
    results.stop_timing()

    if not reached:
        return None
    
    # Traverses backwards the reached nodes matrix to gather all the actions
    current_pos = map.end_pos

    while True:

        # Gets the action taken to reach the current position, and parent position
        action_taken, current_pos = reached_nodes[current_pos[0]][current_pos[1]]

        # Only is None when it's the start
        if action_taken is None:
            break

        results.actions.insert(0, action_taken)

    return results