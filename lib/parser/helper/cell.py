import re

ROW_COL_SPLIT_RE = '([A-Z]+)(\d+)'


class Cell:
    def __init__(self, cell):
        self.cell = cell

        self.col, self.row = Cell.split_col_row(cell)

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

    def left(self, count=1):
        return Cell.from_cell(row=self.row, col=chr(ord(self.col) - count))

    def right(self, count=1):
        return Cell.from_cell(row=self.row, col=chr(ord(self.col) + count))

    def up(self, count=1):
        return Cell.from_cell(row=self.row - count, col=self.col)

    def down(self, count=1):
        return Cell.from_cell(row=self.row + count, col=self.col)

    @staticmethod
    def from_cell(row, col):
        return Cell('{}{}'.format(col, row))

    @staticmethod
    def col_range(start_cell, end_cell):
        cells = []

        cur_cell = start_cell
        while cur_cell < end_cell:
            cells.append(cur_cell)
            cur_cell = Cell.from_cell(row=cur_cell.row, col=chr(ord(cur_cell.col) + 1))

        return cells

    @staticmethod
    def row_range(start_cell, end_cell):
        cells = []

        cur_cell = start_cell
        while cur_cell < end_cell:
            cells.append(cur_cell)
            cur_cell = Cell.from_cell(row=cur_cell.row + 1, col=cur_cell.col)

        return cells

    @staticmethod
    def split_col_row(cell):
        if isinstance(cell, Cell):
            cell = str(cell)

        split = _clear_blanks(re.split(ROW_COL_SPLIT_RE, cell))

        return split[0], int(split[1])


def _clear_blanks(lst):
    return [el for el in lst if el != '']
