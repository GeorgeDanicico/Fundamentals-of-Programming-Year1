class GradeExceptions(Exception):
    def __init__(self, msg):
        self._msg = msg

class Grade_Validator:
    # WITH THIS METHOD WE CHECK IF IN THE GRADES LIST THERE IS A GRADE WITH A GIVEN STUDENT ID AND ASSIGNMENT ID
    @staticmethod
    def check_if_grade_exist(grade_list,s_id,a_id, grade):
        errors = []
        for index in range(len(grade_list)):
            if grade_list[index].student_id == s_id and grade_list[index].assignment_ID == a_id:
                if grade_list[index].grade_value != None:
                    raise GradeExceptions("The assignment has already been graded!...")
                else:
                    if not grade.isdigit() :
                        raise GradeExceptions("The grade is invalid!...")
                    if (float(grade) > 10 or float(grade) < 1):
                        raise GradeExceptions("The grade is invalid!...")
                    return index

        raise GradeExceptions("The student doesn't have that assignment given!...")

    @staticmethod
    def validate(grade):
        if not grade.assignment_ID.isdigit():
            raise GradeExceptions("The id must be an integer!...\n")
        if not grade.student_id.isdigit():
            raise GradeExceptions("The id must be aa integer!...\n")
        if not grade.grade_value.isdigit():
            raise GradeExceptions("The grade must be an number!...\n")
        if float(grade.grade_value) < 0 or float(grade.grade_value) > 10:
            raise GradeExceptions("The grade must be between 0 and 10!...\n")

class Grade:
    def __init__(self, student_id,assignment_id, grade_value):
        self._assignment = assignment_id
        self._student_id = student_id
        self._grade_value = grade_value
        # we do this in order to check to be sure when reading from the database because we put the value None as a string
        if grade_value == 'None':
            self._grade_value = None


    def __str__(self):
        return ("Student ID: " + str(self.student_id).ljust(7) + " Assignment ID: " + str(self.assignment_ID).ljust(7) + " Grade: " + str(self.grade_value))

    @property
    def assignment_ID(self):
        return self._assignment

    @property
    def student_id(self):
        return self._student_id

    @property
    def grade_value(self):
        return self._grade_value

    @grade_value.setter
    def grade_value(self, value):
        self._grade_value = value

def test_grade():
    gr = Grade('123','234','10')
    #print(gr)

test_grade()