from cell import Cell

class Row:

    def __init__(self, number: int, row: list = None):
        self.number = number
        self.row = row or []
        for i in range(3):
            cell = Cell(self.number, i, "")
            self.row.append(cell)