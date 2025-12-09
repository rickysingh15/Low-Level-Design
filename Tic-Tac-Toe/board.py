from row import Row
import threading
from player import Player
class Board:

    _instance = None
    _lock = threading.Lock()
    _is_valid = True

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance


    def __init__(self):
        if not hasattr(self, "_initialized"):
            self._initialized = True
            self.symbol_dict = {
                "x": None,
                "o": None
            }
            self.moves_count = 0
            self.board = list()
            for i in range(3):
                row = Row(i)
                self.board.append(row)

    def init_players(self, player_1_name: str, player_1_symbol: str, player_2_name: str, player_2_symbol: str):

        if player_1_symbol not in self.symbol_dict or player_2_symbol not in self.symbol_dict:
            print("Invalid symbol provided")
            return False
        player1 = Player(player_1_name, player_1_symbol)
        player2 = Player(player_2_name, player_2_symbol)
        self.symbol_dict[player_1_symbol] = player1
        self.symbol_dict[player_2_symbol] = player2

    def print_board(self):
        for row in self.board:
            for j in range(len(row)):
                print(" | ", row[j].get_symbol(), " | ")
            print("\n")

    def play_turn(self, row: int, col: int, player: Player):
        if not self.board[row][col].is_empty():
            print("Cell already has a value")
            return False
        
        self.board[row][col].set_symbol(player.symbol)
        self.is_winner(player.symbol, row, col)

    def is_winner(self, curr_symbol: str, row: int, col: int):
    
        for cell in self.board[row]:
            if cell.get_symbol() != curr_symbol:
                return False
        
        for r in self.board:
            if r[col].get_symbol() != curr_symbol:
                return False
        i,j = 2,0
        while i>0 and j<len(self.board[0]):
            if self.board[i][j].get_symbol() != curr_symbol:
                return False
            i -= 1
            j += 1
            
        i,j = 2,2
        while i>0 and j<len(self.board[0]):
            if self.board[i][j].get_symbol() != curr_symbol:
                return False
            i -= 1
            j -= 1

        if self.moves_count == len(self.board) * len(self.board[0]):
            return False
        
        return True
    
        