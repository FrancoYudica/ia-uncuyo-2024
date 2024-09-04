from map import Map
from common import apply_action_to_position, insert_sorted, find_index
from .walk_results import WalkResults

class Cell:
    def __init__(
            self,
            last_action = None,
            parent_location = None,
            in_frontier = False,
            reached = False,
            cost = float("inf")) -> None:
        self.reached = reached
        self.last_action = last_action
        self.parent = parent_location
        self.in_frontier = in_frontier
        self.cost = cost


def ucs(map: Map) -> WalkResults:

    # Stores the positions to explore and it's cost
    sorted_frontier = [(map.start_pos, 0)]

    def insert_to_frontier(position, cost):

        insert_sorted(
            sorted_frontier,
            (position, cost),

            # Compares by cost, stored in second index
            lambda a, b: a[1] < b[1]
        )

    # Stores the last action used to reach the node and parent position
    reached_nodes = [[Cell() for _ in range(map.n)] for _ in range(map.n)]
    reached_nodes[map.start_pos[0]][map.start_pos[1]] = Cell(
        last_action=None, 
        parent_location=None, 
        in_frontier=True, 
        reached=True,
        cost=0)

    reached = False

    results = WalkResults()
    results.start_timing()

    # Sets the lowest cost to infinite since it's not reached yet
    goal_lowest_cost = float("inf")

    while len(sorted_frontier):
        position, cost = sorted_frontier.pop(0)
        
        cell = reached_nodes[position[0]][position[1]]
        cell.in_frontier = False
        results.explored_cells += 1

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
            
            child_cost = cost + action + 1
            child_cell: Cell = reached_nodes[child_pos[0]][child_pos[1]]

            # Cell reached for the first time
            if not child_cell.reached:
                
                insert_to_frontier(child_pos, child_cost)

                # Stores the action taken to reach the node
                child_cell.in_frontier = True
                child_cell.reached = True
                child_cell.last_action = action
                child_cell.parent = position
                child_cell.cost = child_cost
            
            # Already reached, and the current path cost is less than previous
            elif child_cell.cost > child_cost:
                    
                # If it's on the frontier it's removed
                if child_cell.in_frontier:
                    cell_in_frontier_index = find_index(sorted_frontier, lambda cell: cell[0] == child_pos)
                    sorted_frontier.pop(cell_in_frontier_index)

                # Adds the cell again, ensuring it's sorted
                insert_to_frontier(child_pos, child_cost)

                # Updates the taken action as well
                child_cell.in_frontier = True
                child_cell.last_action = action
                child_cell.parent = position
                child_cell.cost = child_cost

    results.stop_timing()

    if not reached:
        return results
    
    # Traverses backwards the reached nodes matrix to gather all the actions
    current_pos = map.end_pos
    while True:

        # Gets the action taken to reach the current position, and parent position
        cell = reached_nodes[current_pos[0]][current_pos[1]]
        # Only is None when it's the start
        if cell.parent is None:
            break

        current_pos = cell.parent

        results.actions.insert(0, cell.last_action)

    return results