

            
import chess
import chess.engine

import numpy
import re

path_to_stockfish = 'stockfish_13_win_x64_bmi2/stockfish_13_win_x64_bmi2.exe'

class Stockfish():
    def __init__(self):
        engine = chess.engine.SimpleEngine.popen_uci(path_to_stockfish)
        self.engine = engine
        
    def play(self, board):
        result = self.engine.play(board, chess.engine.Limit(time=0.1))
        return(result.move)
        
      
class NegativeStockfish():
    def __init__(self):
        engine = chess.engine.SimpleEngine.popen_uci(path_to_stockfish)
        self.engine = engine
        
    def play(self, board):
    
        scores = []
        for move in board.legal_moves:
            board.push(move)
            res = self.engine.analyse(board, chess.engine.Limit(time=.1))
            scores.append(res.get('score'))
            board.pop()
            
        scores = re.findall("\+?\-?\d+", str(scores))
        
        # get worst possible move (best move from black's pov)
        index = numpy.argmax([int(s) for s in scores])
        move = list(board.legal_moves)[index]
        return(move)