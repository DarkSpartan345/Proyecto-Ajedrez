from chess_logic import ChessLogic
from uci import UCIHandler

def main():
    chess_logic = ChessLogic()
    uci = UCIHandler(chess_logic)
    uci.run()

if __name__ == "__main__":
    main()
