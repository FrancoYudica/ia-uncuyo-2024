import random

class Map:

    """Stores the randomly generated map, 
    alongside the start and end positions"""

    SOURCE_SYMBOL = "S"
    FROZEN_SYMBOL = "F"
    HOLE_SYMBOL = "H"
    GOAL_SYMBOL = "G"

    def __init__(self, 
                 n: int,
                 hole_ratio: float,
                 seed: int) -> None:
        self.n = n
        self.hole_ratio = hole_ratio
        self.seed = seed
        # Matrix that holds symbols [["S", "H"], ["F", "G"]]
        env_map = [[Map.FROZEN_SYMBOL] * n for _ in range(n)]

        random.seed(seed)

        def add_cell_random(cell_type):
            pos = (random.randrange(0, n), random.randrange(0, n))
            
            # The random position should override frozen cells
            if env_map[pos[0]][pos[1]] != Map.FROZEN_SYMBOL:
                return None
            
            # Sets the frozen cell
            env_map[pos[0]][pos[1]] = cell_type
            return pos

        # Adds source
        self.start_pos = add_cell_random(Map.SOURCE_SYMBOL)

        end_pos = None
        # Adds goal, ensuring it isn't placed over the SOURCE
        while not (end_pos := add_cell_random(Map.GOAL_SYMBOL)):
            pass
            
        self.end_pos = end_pos

        # Amount of hole cells
        hole_cell_count = int(hole_ratio * n * n)
        
        # Adds all the required hole cells
        current_hole_cell_count = 0
        while current_hole_cell_count < hole_cell_count:
            if add_cell_random(Map.HOLE_SYMBOL):
                current_hole_cell_count += 1

        random.seed(None)

        # Transforms [["S", "H"], ["F", "G"]] to => ["SH", "FG"]
        # This transformation is in the required environment format 
        self.map = ["".join(sublist) for sublist in env_map]

    def is_pos_valid(self, pos):
        return pos[0] >= 0 and pos[0] < self.n and pos[1] >= 0 and pos[1] < self.n
    
    def is_pos_walkable(self, pos):
        return self.map[pos[0]][pos[1]] != Map.HOLE_SYMBOL