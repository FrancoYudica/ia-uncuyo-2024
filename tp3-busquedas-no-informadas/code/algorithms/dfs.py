from map import Map
from common import apply_action_to_position
from .walk_results import WalkResults


def dfs(
        map: Map,
        max_recursion_depth: int = None) -> WalkResults:

    # Recursive function used to traverse the grid
    def _dfs_recursive(
            map: Map, 
            current_position, 
            reached_nodes,
            current_recursion_depth,
            max_recursion_depth,
            results: WalkResults):
        
        if max_recursion_depth is not None and current_recursion_depth > max_recursion_depth:
            return False

        results.explored_cells += 1
        # Reached target node
        if current_position == map.end_pos:
            return True
        
        # Iterates through all possible children
        for action in range(0, 4):
            
            child_pos = apply_action_to_position(current_position, action)

            # When not in range or not walkable or already walked
            if not map.is_pos_valid(child_pos) or \
                not map.is_pos_walkable(child_pos) or \
                reached_nodes[child_pos[0]][child_pos[1]] is not None:
                continue
            
            # Stores the action taken to reach the node
            reached_nodes[child_pos[0]][child_pos[1]] = (action, current_position)

            # If the dfs reaches the node, exits the recursion
            if _dfs_recursive(
                map=map, 
                current_position=child_pos, 
                reached_nodes=reached_nodes,
                current_recursion_depth=current_recursion_depth + 1,
                max_recursion_depth=max_recursion_depth,
                results=results):

                return True
        
        # Any of the branches reached the target position
        return False

    # Stores the last action used to reach the node and the parent position
    reached_nodes = [[None for _ in range(map.n)] for _ in range(map.n)]
    reached_nodes[map.start_pos[0]][map.start_pos[1]] = (None, None)

    results = WalkResults()
    results.start_timing()

    reached = _dfs_recursive(
        map=map,
        current_position=map.start_pos,
        reached_nodes=reached_nodes,
        current_recursion_depth=0,
        max_recursion_depth=max_recursion_depth,
        results=results)


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