from agent import Agent
from random import choice

class RandomAgent(Agent):

   def think(self):
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

        # Clean cell function
        actions.append(lambda: self.env.clean_cell(self.row, self.col))

        # Do nothing function
        actions.append(lambda: False)

        # Executes the action
        choice(actions)()