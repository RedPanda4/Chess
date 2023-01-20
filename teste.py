import chess
import chess.pgn as pgn
import chess.engine as engine
from pprint import pprint
from CONFIG import GAME_PGN_PATH, STOCKFISH_PATH

with open(GAME_PGN_PATH) as file:
    game_1: pgn.Game = pgn.read_game(file)

stockfish = engine.SimpleEngine.popen_uci(STOCKFISH_PATH)

board = game_1.board()
print(board)

info = stockfish.analyse(board, chess.engine.Limit(time=2), multipv=5, info=engine.INFO_ALL)


pprint(info, indent=4)

stockfish.quit()