

class Cell:

    def __init__(self, row_num: int, col_num: int, symbol: str):
        self.row_number = row_num
        self.col_number = col_num
        self.symbol = symbol

    def get_symbol(self):
        return self.symbol
    
    def set_symbol(self, symbol: str):
        self.symbol = symbol
    
    def is_empty(self):
        return self.symbol == ""