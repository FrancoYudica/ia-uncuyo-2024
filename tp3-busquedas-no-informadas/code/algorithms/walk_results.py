from time import time


class WalkResults:
    def __init__(
            self, 
            cost_by_action=False) -> None:
        self.actions = []

        # When the cost of each action is the
        # action number itself
        self.cost_by_action = cost_by_action
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
    def total_cost(self):
        
        # When each action costs 1
        if not self.cost_by_action:
            return len(self.actions)
        
        # When each action costs 1 + action index
        return sum([1 + action for action in self.actions])