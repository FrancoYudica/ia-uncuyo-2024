import math
import random

_STATE_EMPTY = 0
_STATE_DIRT = 1
_STATE_WALKED = 2

class Environment:
    def __init__(
            self, 
            nrows, 
            ncols,
            dirt_ratio: float) -> None:
        self.nrows = nrows
        self.ncols = ncols
        self.dirt_ratio = dirt_ratio

        self.cells = []
        self.clean_all_cells()

    @property
    def dirty_cell_count(self):
        return sum([column.count(_STATE_DIRT) for column in self.cells])

    @property
    def current_dirt_ratio(self):
        return self.dirty_cell_count / (self.nrows * self.ncols)

    def clean_all_cells(self):
        self.cells.clear()

        # Initializes cells as empty. Row major matrix
        self.cells = [[_STATE_EMPTY for _ in range(self.ncols)] for _ in range(self.nrows)]

    def get_performance(self):
        # Calculates the amount of dirt cells to satisfy the ratio
        total_cell_count = self.nrows * self.ncols
        total_dirt_cell_count = math.ceil(total_cell_count * self.dirt_ratio)

        # Returns the remaining dirty cell count
        return total_dirt_cell_count - self.dirty_cell_count

    def randomize(self, seed: int = None):
        
        self.clean_all_cells()

        # Calculates the amount of dirt cells to satisfy the ratio
        total_cell_count = self.nrows * self.ncols
        dirt_cell_count = math.ceil(total_cell_count * self.dirt_ratio)
        random.seed(seed)
        
        # Randomizes dirt in exactly 'dirt_cell_count' cells
        applied_dirt_count = 0
        while applied_dirt_count < dirt_cell_count:
            row = random.randrange(0, self.nrows)
            column = random.randrange(0, self.ncols)

            # Only sets dirt if cell doesn't have dirt. This is important,
            # otherwise the dirt ratio wont be satisfied
            if not self.is_cell_dirty(row, column):
                self.cells[row][column] = _STATE_DIRT
                applied_dirt_count += 1


    def is_valid_position(self, row, column) -> bool:
        return 0 <= row < self.nrows and 0 <= column < self.ncols
    
    def is_cell_dirty(self, row, column) -> bool:

        if not self.is_valid_position(row, column):
            raise Exception(f"Cell dirty check out of bounds position ({row}, {column})")

        return self.cells[row][column] == _STATE_DIRT
    
    def is_cell_walked(self, row, column):
        return self.cells[row][column] == _STATE_WALKED 

    def walk_cell(self, row, column):
        self.cells[row][column] = _STATE_WALKED


    def clean_cell(self, row, column):

        if not self.is_valid_position(row, column):
            raise Exception(f"Cell clean out of bounds position ({row}, {column})")
        
        self.walk_cell(row, column)

