from lib.models.roster import Roster
from lib.parser import BaseParser
from lib.parser.helper.cell import Cell
from openpyxl import load_workbook


class XLSXParser(BaseParser):
    def parse(self):
        workbook = load_workbook(filename=self.file_name)
        ws = workbook.active

        people = self.extract_people(ws)

        for i in range(1, 100):
            cell_name = 'C' + str(i)
            fill = ws[cell_name].fill
            if fill.fgColor.type == 'indexed':
                print('({},{},{})'.format(cell_name, fill.fgColor.index, self.colour_to_location(fill.fgColor.index)))

        return Roster(people=people)

    def extract_people(self, ws):
        people_start_cell = Cell('C6')
        people_end_cell = Cell('Z6')

        people = []
        cells = Cell.col_range(start_cell=people_start_cell, end_cell=people_end_cell)
        for cell in cells:
            name = ws[str(cell)].value
            if name:
                people.append(name)
            else:
                break

        return people

    def extract_shifts(self, ws, start_cell, end_cell):
        pass
