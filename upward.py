import chess
import random

class Upward():
    def play(self, board):
        return sorted(board.legal_moves, key=lambda x: x.to_square)[0]
        

