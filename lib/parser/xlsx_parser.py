from datetime import datetime

from dateutil import parser as date_parser

from openpyxl import load_workbook

from lib.models.roster import Roster
from lib.models.shift import Shift
from lib.parser import BaseParser
from lib.parser.helper.cell import Cell
from lib.config import PEOPLE_START_CELL, PEOPLE_END_CELL, SHIFT_ROW_LIMIT, TIMES_START_CELL, TIMES_END_CELL


class XLSXParser(BaseParser):
    def parse(self):
        workbook = load_workbook(filename=self.file_name)
        ws = workbook.active

        times = self.extract_times(ws)
        people = self.extract_people(ws)
        shifts = self.extract_shifts(ws, times, people)

        return Roster(shifts=shifts, people=people)

    @staticmethod
    def extract_times(ws):
        times = {}
        cells = Cell.row_range(start_cell=TIMES_START_CELL, end_cell=TIMES_END_CELL)

        current_date = None
        for cell in cells:
            _, row = Cell.split_col_row(cell)
            date_value = ws[str(cell)].value

            new_date = validate_date(date_value)
            current_date = new_date if new_date is not None else current_date

            time_value = ws[str(cell.right())].value

            if time_value:
                start_time, end_time = validate_times(time_value)

                start_datetime = combine_date_and_time(current_date, start_time)
                end_datetime = combine_date_and_time(current_date, end_time)

                times[row] = Shift(start_time=start_datetime, end_time=end_datetime)

        return times

    @staticmethod
    def extract_people(ws):
        people = []
        cells = Cell.col_range(start_cell=PEOPLE_START_CELL, end_cell=PEOPLE_END_CELL)
        for cell in cells:
            _, row = Cell.split_col_row(cell)

            name = ws[str(cell)].value
            if name:
                people.append(name)
            else:
                break

        return people

    @staticmethod
    def extract_shifts(ws, times, people):
        shifts = []

        for p in range(len(people)):
            start_cell = Cell.from_cell(row=PEOPLE_START_CELL.down().row, col=PEOPLE_START_CELL.right(p).col)
            end_cell = Cell.from_cell(row=SHIFT_ROW_LIMIT, col=start_cell.col)

            cells = Cell.row_range(start_cell=start_cell, end_cell=end_cell)
            for cell in cells:
                value = ws[str(cell)].value
                fill = ws[str(cell)].fill

                if fill.fgColor.type == 'indexed':
                    shift = Shift(
                        start_time=times[cell.row].start_time,
                        end_time=times[cell.row].end_time,
                        person=people[p],
                        location=BaseParser.colour_to_location(fill.fgColor.index)
                    )

                    shifts.append(shift)

        return shifts


def validate_date(date_str):
    try:
        return date_parser.parse(date_str)
    except Exception as e:
        return None


def validate_times(time_str):
    try:
        time_split = time_str.split('-', maxsplit=2)
        times = list(map(date_parser.parse, time_split))

        return times[0], times[1]
    except Exception as e:
        return None, None


def combine_date_and_time(date, time):
    return datetime(year=date.year, month=date.month, day=date.day,
                    hour=time.hour, minute=time.minute)
