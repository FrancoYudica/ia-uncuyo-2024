from time import time


class WalkResults:
    def __init__(self) -> None:
        self.actions = []
        self.explored_cells = 0
        # When the cost of each action is the
        # action number itself
        self._t0 = 0
        self._t1 = 0

    def start_timing(self):
        self._t0 = time()

    def stop_timing(self):
        self._t1 = time()

    @property
    def time_taken(self):
        return self._t1 - self._t0
    
    @property
    def reached(self):
        return len(self.actions) > 0
    
    def calculate_cost(self, cost_by_action=False):
        
        # When each action costs 1
        if not cost_by_action:
            return len(self.actions)
        
        # When each action costs 1 + action index
        return len(self.actions) + sum(self.actions)