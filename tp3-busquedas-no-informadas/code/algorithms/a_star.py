from map import Map
from common import apply_action_to_position, insert_sorted, find_index
from .walk_results import WalkResults
import math

class Cell:
    def __init__(
            self,
            last_action = None,
            parent_location = None,
            real_cost = None,
            in_frontier = False,
            reached = False) -> None:
        self.reached = reached
        self.last_action = last_action
        self.parent = parent_location
        self.real_cost = real_cost
        self.in_frontier = in_frontier


def a_star(map: Map) -> WalkResults:


    # Stores the positions to explore and it's `f(n) = g(n) + h(n)` cost
    sorted_frontier = [(map.start_pos, 0)]

    def insert_to_frontier(position, cost):

        insert_sorted(
            sorted_frontier,
            (position, cost),

            # Compares by cost, stored in second index
            lambda a, b: a[1] < b[1]
        )

    def get_estimated_cost(pos):
        # Uses Manhattan / rectangular distance as heuristic. This is 
        # way faster than euclidean distance
        return abs(pos[0] - map.end_pos[0]) + abs(pos[1] - map.end_pos[1])

    # Stores the last action used to reach the node, parent position and
    # real cost to reach that node
    reached_nodes = [[Cell() for _ in range(map.n)] for _ in range(map.n)]
    reached_nodes[map.start_pos[0]][map.start_pos[1]] = Cell(
        last_action=None, 
        parent_location=None, 
        real_cost=0, 
        in_frontier=True, 
        reached=True)

    reached = False

    results = WalkResults()
    results.start_timing()

    while len(sorted_frontier):
        position, f_cost = sorted_frontier.pop(0)
        cell = reached_nodes[position[0]][position[1]]

        # No longer in frontier
        cell.in_frontier = False

        reached = position == map.end_pos
        if reached:
            break
        
        for action in range(0, 4):
            
            child_pos = apply_action_to_position(position, action)

            # When not in range or not walkable or already walked
            if not map.is_pos_valid(child_pos) or not map.is_pos_walkable(child_pos):
                continue
            
            # Moving 1 cell, adds 1 of cost
            child_real_cost = cell.real_cost + 1
            child_estimated_cost = get_estimated_cost(child_pos)
            child_f_cost = child_real_cost + child_estimated_cost

            child_cell = reached_nodes[child_pos[0]][child_pos[1]]

            # Cell reached for the first time
            if not child_cell.reached:
                
                insert_to_frontier(child_pos, child_f_cost)

                # Stores the action taken to reach the node
                child_cell.in_frontier = True
                child_cell.reached = True
                child_cell.last_action = action
                child_cell.parent = position
                child_cell.real_cost = child_real_cost
            
            # Already reached, and the current path cost is less than previous
            elif child_cell.real_cost > child_real_cost:
                    
                # If it's on the frontier, it's removed and then updated
                if child_cell.in_frontier:

                    # Performance bottleneck... O(n) search...
                    cell_in_frontier_index = find_index(sorted_frontier, lambda cell: cell[0] == child_pos)
                    sorted_frontier.pop(cell_in_frontier_index)

                # Adds the cell again, ensuring it's sorted
                insert_to_frontier(child_pos, child_f_cost)

                # Updates the taken action as well
                child_cell.in_frontier = True
                child_cell.last_action = action
                child_cell.parent = position
                child_cell.real_cost = child_real_cost


    results.stop_timing()

    if not reached:
        return None
    
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

