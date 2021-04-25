import chess
import random

class RandMove():
    def play(self, board):
        moves = list(board.legal_moves)
        return random.choice(moves)
        
