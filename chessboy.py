
            
import chess

from rand_move import RandMove
from alphabetic import Alphabetic
from upward import Upward
from stockfish_bots import Stockfish
from stockfish_bots import NegativeStockfish



        

import time
def play_game(white, black, watch=False):
    board = chess.Board()
    for turn in range(200):
           
        assert(board.turn == chess.WHITE)
        move = white.play(board)
        board.push(move)
            
        if watch:
            print(board,'\r')
            print('\n')
            
        if board.outcome(): 
            break
            
        assert(board.turn == chess.BLACK)
        move = black.play(board)
        board.push(move)
        
        if watch:
            print(board,'\r')
            print('\n')
            
        if board.outcome(): 
            break

    if board.outcome():
        'Either chess.BLACK, chess.WHITE, or None'
        winner = board.outcome().winner
        if winner == None:
            return None
        if winner == chess.WHITE:
            return white
        if winner == chess.BLACK:
            return black
    else:
        ' Special case of timeout.'
        return None


NoneClass = type(None)
def play_games(ClassA, ClassB, n_games=1, watch=False):
    'A plays white, B plays black.'
    wins = {NoneClass: 0, ClassA: 0, ClassB:0}
    for i in range(50):
        winner = play_game(ClassA(), ClassB(), watch=watch)
        print('*'*20,'\n WINNER:',type(winner),'\n','*'*20,'\n')
        wins[type(winner)] += 1
    print(wins)

import chess.engine


print(play_games(NegativeStockfish, NegativeStockfish, n_games=10, watch=True))