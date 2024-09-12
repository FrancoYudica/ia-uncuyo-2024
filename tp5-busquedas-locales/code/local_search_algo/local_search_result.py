from chess_board_state import ChessBoardState


class LocalSearchResult:
    """Common result data structure to all algorithms"""
    def __init__(self) -> None:
        self.board: ChessBoardState = None
        self.time_taken: float = 0.0
        self.traversed_states: int = 0