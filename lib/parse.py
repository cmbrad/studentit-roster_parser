import os
import openpyxl

from lib.parser import XLSParser, XLSXParser


# Which parser is used for which file type
ext_to_parser = {
	'.xls':  XLSParser,
	'.xlsx': XLSXParser
}


def parse_document(file_name):
	parser = select_parser(file_name)
	roster = parser.parse()

	print(roster)


def select_parser(file_name):
	# Get the file extension of the file passed in. Different excel
	# file versions need different python packages to parse
	_, ext = os.path.splitext(file_name)

	# Select the appropriate type of parser to use for this file type
	# and then initialize it
	parser = ext_to_parser.get(ext)(file_name)

	if parser is None:
		supported_types = ','.join(ext_to_parser.keys())
		raise Exception("Unsupported file type. Supported types are [{file_types}]".format(file_types=supported_types))

	return parser

