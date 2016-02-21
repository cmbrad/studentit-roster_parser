class BaseParser:
    def __init__(self, file_name):
        self.file_name = file_name

    def parse(self):
        pass

    @staticmethod
    def colour_to_location(colour):
        col_to_loc = {
            14: 'Baillieu',
            48: 'Giblin Eunson',
            50: 'ERC'
        }

        return col_to_loc.get(colour)
