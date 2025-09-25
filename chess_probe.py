import sys
import chess
import random

board = chess.Board()

def log(message):
    with open("log.txt", "a") as f:
        f.write(message + "\n")

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

    if line == "uci":
        print("id name RandomUCI")
        print("id author Daniel")
        print("uciok")
        sys.stdout.flush()

    elif line == "isready":
        print("readyok")
        sys.stdout.flush()

    elif line.startswith("ucinewgame"):
        board.reset()

    elif line.startswith("position"):
        if "startpos" in line:
            board.set_fen(chess.STARTING_FEN)
            moves_part = line.split("moves")
            if len(moves_part) > 1:
                moves = moves_part[1].strip().split()
                for move in moves:
                    board.push_uci(move)
        elif "fen" in line:
            fen = line.split("fen")[1].split("moves")[0].strip()
            board.set_fen(fen)
            if "moves" in line:
                moves = line.split("moves")[1].strip().split()
                for move in moves:
                    board.push_uci(move)
        log(f"FEN set: {board.fen()}")

    elif line.startswith("go"):
        if not board.is_game_over():
            move = random.choice(list(board.legal_moves))
            # Enviar primero una línea "info"
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
        break

