from jproperties import Properties

class Settings:
    def __init__(self, filename):
        self._file_data = Properties()
        self._filename = filename
        self._load_data()

    @property
    def get_apples(self):
        return self._file_data.get("apple_numbers").data[1:-1]

    @property
    def get_dimension(self):
        return self._file_data.get("board_dimension").data[1:-1]

    def _load_data(self):
        with open(self._filename, 'rb') as files:
            self._file_data.load(files)