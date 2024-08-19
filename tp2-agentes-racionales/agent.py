from environment import Environment
from random import randrange

class Agent:

    def __init__(
            self,
            row,
            col,
            env: Environment) -> None:
        
        self.env: Environment = env

        if not self.env.is_valid_position(row, col):
            raise Exception("Trying to set initial position, but it's out of environment bounds")

        self.row = row
        self.col = col

    def up(self):
        self.row -= 1
        if not self.env.is_valid_position(self.row, self.col):
            raise Exception("Trying to move out of environment")
        
    def down(self):
        self.row += 1
        if not self.env.is_valid_position(self.row, self.col):
            raise Exception("Trying to move out of environment")
    
    def right(self):
        self.col += 1
        if not self.env.is_valid_position(self.row, self.col):
            raise Exception("Trying to move out of environment")
        
    def left(self):
        self.col -= 1
        if not self.env.is_valid_position(self.row, self.col):
            raise Exception("Trying to move out of environment")
        
    def clean(self):
        self.env.clean_cell(self.row, self.col)

    def perspective(self):
        # TODO: ??
        pass

    def think(self):

        # Randomized thinking
        action_methods = []

        # Ensures that the available actions are valid and doesn't
        # move the agent out of environment bounds
        if self.row < self.env.nrows - 1:
            action_methods.append(self.down)

        if self.row > 0:
            action_methods.append(self.up)

        if self.col < self.env.ncols - 1:
            action_methods.append(self.right)

        if self.col > 0:
            action_methods.append(self.left)

        # Executes the action
        action_methods[randrange(0, 3)]()

