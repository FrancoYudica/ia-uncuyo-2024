from map import Map
from common import apply_action_to_position, insert_sorted, find_index
from .walk_results import WalkResults


def ucs(map: Map) -> WalkResults:

    # Stores the last action used to reach the node, 
    # parent position and cost to reach that node
    reached_nodes = [[None for _ in range(map.n)] for _ in range(map.n)]
    reached_nodes[map.start_pos[0]][map.start_pos[1]] = (None, None)

    # Stores the positions to explore and it's cost
    sorted_frontier = [(map.start_pos, 0)]

    def insert_to_frontier(position, cost):

        insert_sorted(
            sorted_frontier,
            (position, cost),

            # Compares by cost, stored in second index
            lambda a, b: a[1] < b[1]
        )

    reached = False

    results = WalkResults()
    results.start_timing()

    # Sets the lowest cost to infinite since it's not reached yet
    goal_lowest_cost = float("inf")

    while len(sorted_frontier):
        position, cost = sorted_frontier.pop(0)
        
        # When a the goal is reached and the current costs are getting
        # higher, it means that there aren't any other paths with lower
        # cost to reach the goal
        if cost >= goal_lowest_cost:
            break
        
        # Goal reached with lower cost
        if position == map.end_pos:
            reached = True
            goal_lowest_cost = cost
            continue

        for action in range(0, 4):
            
            child_pos = apply_action_to_position(position, action)

            # When not in range or not walkable or already walked
            if not map.is_pos_valid(child_pos) or \
                not map.is_pos_walkable(child_pos):
                continue
            
            child_cost = cost + action

            cell = reached_nodes[child_pos[0]][child_pos[1]]

            cell_in_frontier_index = find_index(sorted_frontier, lambda cell: cell[0] == child_pos)

            cell_explored = cell is not None

            # Inserts to frontier for the first time
            if not cell_explored:
                
                insert_to_frontier(child_pos, child_cost)

                # Stores the action taken to reach the node
                reached_nodes[child_pos[0]][child_pos[1]] = (action, position)
            
            # Already in frontier
            elif cell_in_frontier_index:

                # Tests if current path has a lower cost
                _, frontier_cost = sorted_frontier[cell_in_frontier_index]
                if frontier_cost > child_cost:

                    # Removes the cell from frontier
                    sorted_frontier.pop(cell_in_frontier_index)

                    # Adds the cell again, ensuring it's sorted
                    insert_to_frontier(child_pos, child_cost)

                    # Updates the taken action as well
                    reached_nodes[child_pos[0]][child_pos[1]] = (action, position)


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