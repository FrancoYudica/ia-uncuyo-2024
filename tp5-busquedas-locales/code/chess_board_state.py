import random

class ChessBoardState:
    def __init__(
            self, 
            size,
            seed=None,
            columns=None,
            calculate_threats=True) -> None:
        
        if columns is None:
            random.seed(seed)
            self.columns = [random.randrange(0, size) for _ in range(size)]
            random.seed(None)
        else:
            self.columns = columns

        # Stores the threats in this variable since calculating the threats
        # is an expensive operation
        self.cached_threats = 0
        
        if calculate_threats:
            self.recalculate_threats()
            
    @property
    def size(self):
        return len(self.columns)

    def __str__(self) -> str:
        string = ""
        for row in range(self.size):
            for column in range(self.size):
                if self.columns[column] == row:
                    string += " Q"
                else:
                    string += " *"

            string += "\n"

        return string
    
    def recalculate_threats(self):

        threats_count = 0

        for column in range(self.size):
            row = self.columns[column]

            # Tests with the remaining rows
            for child_column in range(column + 1, self.size):

                child_row = self.columns[child_column]

                # Same row
                if row == child_row:
                    threats_count += 1

                else:
                    direction = column - child_column, row - child_row
                    slope = direction[0] / direction[1]

                    # In diagonal
                    if abs(slope) == 1.0:
                        threats_count += 1

        self.cached_threats = threats_count