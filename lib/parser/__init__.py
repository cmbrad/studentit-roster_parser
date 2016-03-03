import os

from .base_parser import BaseParser
from .xls_parser import XLSParser
from .xlsx_parser import XLSXParser

from lib.exceptions import UnsupportedFileTypeException

# Which parser is used for which file type
EXT_TO_PARSER = {
    '.xls': XLSParser,
    '.xlsx': XLSXParser
}


def parse_roster(file_name):
    parser = select_parser(file_name)

    roster = parser.parse()

    return roster


def select_parser(file_name):
    # Get the file extension of the file passed in. Different excel
    # file versions need different python packages to parse
    _, ext = os.path.splitext(file_name)

    # Select the appropriate type of parser to use for this file type
    # and then initialize it
    try:
        parser = EXT_TO_PARSER.get(ext)(file_name)
    except TypeError:
        supported_types = ','.join(EXT_TO_PARSER.keys())
        raise UnsupportedFileTypeException(
            "Unsupported file type. Supported types are [{file_types}]".format(file_types=supported_types))

    return parser
