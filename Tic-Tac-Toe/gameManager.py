
import threading
from board import Board
from player import Player

class GameManager:

    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, "_initialized"):
            self._initialized = True
            self.board = Board()
            self.player1 = None
            self.player2 = None
            self.turn_player = None

    def create_players(self, player_1_name: str, player_1_symbol: str, player_2_name: str, player_2_symbol: str):
        if player_1_symbol not in self.symbol_dict or player_2_symbol not in self.symbol_dict:
            print("Invalid symbol provided")
            return False
        self.player1 = Player(player_1_name, player_1_symbol, "player1")
        self.player2 = Player(player_2_name, player_2_symbol, "player2")
        self.turn_player = self.player1

    def play_turn(self):
        print(self.turn_player.handle, " chance to play")
        row = input()
        col = input()
        

    