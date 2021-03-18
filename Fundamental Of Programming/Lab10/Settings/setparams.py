class SetParameters:
    def __init__(self, filename):
        self._filename = filename

    def setup_parameters(self):

        entity, atr1, atr2, atr3 = None, None, None, None
        if self._filename == 'TextFiles/students.json' or self._filename == "student":
            entity = 'Student'
            atr1 = 'student_id'
            atr2 = 'student_name'
            atr3 = 'student_group'

        if self._filename == 'TextFiles/assignments.json' or self._filename == "assignment":
            entity = 'Assignment'
            atr1 = 'assignment_ID'
            atr2 = 'description'
            atr3 = 'Deadline'

        if self._filename == 'TextFiles/grades.json' or self._filename == "grade":
            entity = 'Grade'
            atr1 = 'student_id'
            atr2 = 'assignment_ID'
            atr3 = 'grade_value'

        return entity, atr1, atr2, atr3
