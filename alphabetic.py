import chess
import random

class Alphabetic():
    def play(self, board):
        return sorted(board.legal_moves, key=lambda x: str(x).lower())[0]
        