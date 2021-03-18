class studentException(Exception):
    def __init__(self,msg):
        self._msg = msg

class studentValidatorException(studentException):
    def __init__(self, errors):
        self._errors = errors
    @property
    def errors(self):
        return self._errors
    def __str__(self):
        result = ''
        for e in self.errors:
            result += e
            result += '\n'
        return result

class Student_Validator:
    @staticmethod
    def check_group(group):
        if group not in ['911', '912', '913', '914', '915', '916', '917']:
            raise studentException("Invalid group given!...\n")


    @staticmethod
    def find_student_by_id(student_list, id):
        """
        we check if the id is in the list and if it is a digit
        :param id: the id we read from the cnsole
        :return: we return the index of the given id if it exist/otherwise we raise an exception
        """
        if not id.isdigit():
            raise studentException("Invadid id!...\n")
        index = 0
        ''' we find the student with the given id and give him the assignment'''
        length = len(student_list.objects)
        done = False
        while not done and index < length:
            if id == student_list.objects[index].student_id:
                done = True
                return index
            index += 1

        if done == False:
            raise studentException("There is no student with the given id!...\n")



    @staticmethod
    def validate(list, student):
        errors = []
        for element in list:
            if element.student_id == student.student_id:
                errors.append("Duplicate ID!...")

        if student.student_group not in ['911','912','913','914','915','916','917']:
            errors.append("Invalid student group!...")

        if len(student.student_name) < 8:
            errors.append("Incorrect name!...")

        if len(errors) > 0:
            raise studentValidatorException(errors)


class Student:

    def __init__(self,student_id, name, group):
        if not student_id.isdigit() or not group.isdigit():
            raise studentException("Invalid student_id or group!...\n")

        if not name.replace(' ','').isalpha():
            raise studentException("Invalid name!...\n")

        self._student_id = student_id
        self._name = name
        self._group = group
        self._given_assignment_id = None

    def __str__(self):
        return ("->" + "ID: "+ str(self.student_id).ljust(10) + "Name: " + str(self.student_name).ljust(20) + "Group: " + str(self.student_group).ljust(10))

    @property
    def student_id(self):
        return self._student_id

    @property
    def student_name(self):
        return self._name

    @property
    def student_group(self):
        return self._group

    @student_group.setter
    def student_group(self, value):
        self._group = value





