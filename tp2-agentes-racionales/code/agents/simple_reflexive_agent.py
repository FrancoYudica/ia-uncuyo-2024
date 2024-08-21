from agent import Agent
from random import choice

class SimpleReflexiveAgent(Agent):

   def think(self):

        # Cleans the cell if dirty     
        if self.env.is_cell_dirty(self.row, self.col):
            self.env.clean_cell(self.row, self.col)

        # Randomized thinking
        actions = []

        # Only adds acceptable actions
        if self.can_move_down():
            actions.append(self.down)

        if self.can_move_up():
            actions.append(self.up)

        if self.can_move_right():
            actions.append(self.right)

        if self.can_move_left():
            actions.append(self.left)

        # Executes the action
        choice(actions)()