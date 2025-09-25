import sys
from logger import log

class UCIHandler:
    def __init__(self, chess_logic):
        self.chess_logic = chess_logic

    def run(self):
        print("id name RandomUCI")
        print("id author Daniel")
        print("uciok")
        sys.stdout.flush()
        log("Engine started")

        while True:
            line = sys.stdin.readline().strip()
            if not line:
                continue

            log(f"IN: {line}")
            self.handle_command(line)

    def handle_command(self, line: str):
        if line == "uci":
            print("id name RandomUCI")
            print("id author Daniel")
            print("uciok")
            sys.stdout.flush()

        elif line == "isready":
            print("readyok")
            sys.stdout.flush()

        elif line.startswith("ucinewgame"):
            self.chess_logic.reset()

        elif line.startswith("position"):
            self.chess_logic.set_position(line)
            log(f"FEN set: {self.chess_logic.board.fen()}")

        elif line.startswith("go"):
            move = self.chess_logic.best_move()
            if move:
                print(f"info depth 1 score cp 0 pv {move}")
                print(f"bestmove {move}")
                sys.stdout.flush()
                log(f"OUT: info depth 1 score cp 0 pv {move}")
                log(f"OUT: bestmove {move}")
            else:
                print("bestmove 0000")
                sys.stdout.flush()
                log("OUT: bestmove 0000")

        elif line == "quit":
            sys.exit(0)
