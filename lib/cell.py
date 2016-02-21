class Cell:
    def __init__(self, cell):
        self.cell = cell
        self.col = cell[0]
        self.row = int(cell[1:])

    def __lt__(self, other):
        if self.col < other.col:
            return True
        if self.col > other.col:
            return False

        return self.row < other.row

    def __gt__(self, other):
        if self.col > other.col:
            return True
        if self.col < other.col:
            return False

        return self.row > other.row

    def __str__(self):
        return self.cell

    def __repr__(self):
        return self.cell

    def __eq__(self, other):
        return self.col == other.col and self.row == other.row

    def __ne__(self, other):
        return self.col != other.col or self.row != other.row

    @staticmethod
    def from_cell(row, col):
        return Cell('{}{}'.format(col, row))

    @staticmethod
    def col_range(end_cell, start_cell='A1'):
        cells = []

        cur_cell = start_cell
        while cur_cell < end_cell:
            cells.append(cur_cell)
            cur_cell = Cell.from_cell(row=cur_cell.row, col=chr(ord(cur_cell.col) + 1))

        return cells

    @staticmethod
    def row_range(end_cell, start_cell='A1'):
        cells = []

        cur_cell = start_cell
        while cur_cell < end_cell:
            cells.append(cur_cell)
            cur_cell = Cell.from_cell(row=cur_cell.row + 1, col=cur_cell.col)

        return cells
