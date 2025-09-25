import chess
import random

class ChessLogic:
    def __init__(self):
        self.board = chess.Board()

    def reset(self):
        self.board.reset()

    def set_position(self, line: str):
        if "startpos" in line:
            self.board.set_fen(chess.STARTING_FEN)
            moves_part = line.split("moves")
            if len(moves_part) > 1:
                moves = moves_part[1].strip().split()
                for move in moves:
                    self.board.push_uci(move)
        elif "fen" in line:
            fen = line.split("fen")[1].split("moves")[0].strip()
            self.board.set_fen(fen)
            if "moves" in line:
                moves = line.split("moves")[1].strip().split()
                for move in moves:
                    self.board.push_uci(move)

    def best_move(self):
        if not self.board.is_game_over():
            move = random.choice(list(self.board.legal_moves))
            return move
        return None
