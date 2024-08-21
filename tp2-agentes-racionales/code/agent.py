from environment import Environment

class Agent:

    def __init__(
            self,
            row = 0,
            col = 0,
            env: Environment = None) -> None:
        
        self.env: Environment = env
        self.row = row
        self.col = col

    def up(self):
        if not self.can_move_up():
            raise Exception("Trying to move out of environment")
        self.row -= 1
        
    def down(self):
        if not self.can_move_down():
            raise Exception("Trying to move out of environment")
        self.row += 1
    
    def right(self):
        if not self.can_move_right():
            raise Exception("Trying to move out of environment")
        self.col += 1
        
    def left(self):
        if not self.can_move_left():
            raise Exception("Trying to move out of environment")
        self.col -= 1
    
    def can_move_up(self):
        return self.env.is_valid_position(self.row - 1, self.col)
    
    def can_move_down(self):
        return self.env.is_valid_position(self.row + 1, self.col)

    def can_move_left(self):
        return self.env.is_valid_position(self.row, self.col - 1)
    
    def can_move_right(self):
        return self.env.is_valid_position(self.row, self.col + 1)

    def clean(self):
        self.env.clean_cell(self.row, self.col)

    def perspective(self) -> bool:
        return self.env.is_cell_dirty(self.row, self.col)

    def think(self):
        raise NotImplementedError("Subclasses must implement this method")