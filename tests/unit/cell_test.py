from lib.parser.helper import Cell


def test_cells_with_same_row_and_col_should_be_equal():
    cell_ref = 'A1'

    cell1 = Cell(cell_ref)
    cell2 = Cell(cell_ref)

    assert cell1 == cell2


def test_cells_with_same_row_and_col_should_not_be_not_equal():
    assert not Cell('A1') != Cell('A1')


def test_cells_with_different_col_should_not_be_equal():
    assert Cell('A1') != Cell('B1')


def test_cells_with_different_row_should_not_be_equal():
    assert Cell('A1') != Cell('A2')


def test_cells_with_different_row_and_col_should_not_be_equal():
    assert Cell('A1') != Cell('B2')


def test_cells_with_same_row_and_smaller_col_should_be_lt():
    assert Cell('A1') < Cell('B1')


def test_cells_with_same_row_and_bigger_col_should_be_gt():
    assert Cell('B1') > Cell('A1')


def test_cells_with_same_col_and_smaller_row_should_be_lt():
    assert Cell('A1') < Cell('A2')


def test_cells_with_same_col_and_bigger_row_should_be_gt():
    assert Cell('A2') > Cell('A1')
