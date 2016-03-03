import pytest


def test_select_parser_should_be_xlsxparser_for_xlsx_files():
    from lib.parser import select_parser
    from lib.parser import XLSXParser

    test_file_name = 'hello_world.xlsx'

    selected_parser = select_parser(test_file_name)

    assert isinstance(selected_parser, XLSXParser)


def test_select_parser_should_be_xlsparser_for_xls_files():
    from lib.parser import select_parser
    from lib.parser import XLSParser

    test_file_name = 'hello_world.xls'

    selected_parser = select_parser(test_file_name)

    assert isinstance(selected_parser, XLSParser)


def test_select_parser_should_raise_exception_for_invalid_file_format():
    from lib.parser import select_parser
    from lib.exceptions import UnsupportedFileTypeException

    test_file_name = 'not_real.py'

    with pytest.raises(UnsupportedFileTypeException):
        select_parser(test_file_name)
