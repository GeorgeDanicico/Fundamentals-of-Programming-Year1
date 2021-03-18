from jproperties import Properties


class Settings:
    def __init__(self, filename):
        self._file_data = Properties()
        self._filename = filename
        self._load_settings_data()

    @property
    def get_mode(self):
        return self._file_data.get("repository").data

    @property
    def get_studentfile(self):
        student_file = self._file_data.get("students").data
        student_file = student_file[1:len(student_file)-1]
        return student_file

    @property
    def get_assignmentfile(self):
        assignment_file = self._file_data.get("assignments").data
        assignment_file = assignment_file[1:len(assignment_file) - 1]
        return assignment_file

    @property
    def get_gradesfile(self):
        grade_file = self._file_data.get("grades").data
        grade_file = grade_file[1:len(grade_file) - 1]
        return grade_file

    @property
    def get_uimode(self):
        ui_mode = self._file_data.get("ui").data
        ui_mode = ui_mode[1:len(ui_mode) - 1]
        return ui_mode

    def _load_settings_data(self):
        with open(self._filename, 'rb') as files:
            self._file_data.load(files)




