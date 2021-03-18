import datetime

class AssignmentException(Exception):
    def __init__(self,msg):
        self._msg = msg

class AssignmentValidatorException(AssignmentException):
    def __init__(self, errors):
        self._errors = errors
    @property
    def errors(self):
        return self._errors

    def __str__(self):
        result =''
        for e in self.errors:
            result += e
            result +='\n'
        return result


class Assignment_Validator:
    """
    We initialize the assignment validator
    """
    @staticmethod
    def find_assignment(list_of_assignments, id):
        done = False  # if ok == false we didnt find the given id / true otherwise
        index = 0
        length = len(list_of_assignments)
        while index < length and not done:
            if list_of_assignments[index].assignment_ID == id:
                return index
                done = True
            index += 1

        if not done:
            raise AssignmentException("There is no assignment with this ID!...\n")

    @staticmethod
    def validate_datetime(date_text):
        try:
            if date_text != datetime.datetime.strptime(date_text, "%Y-%m-%d").strftime('%Y-%m-%d'):
                raise ValueError("Invalid date for deadline!...\n")
            current_date = date_text.split('-')

            if datetime.date(int(current_date[0]), int(current_date[1]), int(current_date[2])) < datetime.date.today():
                raise AssignmentException("Invalid date for deadline!...\n")

            return True
        except AssignmentException:
            return False
        except ValueError:
            return False

    @staticmethod
    def check_if_deadline_passed(date_text):
        try:
            if date_text != datetime.datetime.strptime(date_text, "%Y-%m-%d").strftime('%Y-%m-%d'):
                raise ValueError("Invalid date for deadline!...\n")
            current_date = date_text.split('-')

            if datetime.date(int(current_date[0]), int(current_date[1]), int(current_date[2])) < datetime.date.today():
                return True

            return False
        except ValueError:
            return False

    @staticmethod
    def validate(list, assignment):
        errors = []
        for element in list:
            if element.assignment_ID == assignment.assignment_ID:
                errors.append("Duplicate ID!...")
        if len(assignment.description) < 5:
            errors.append("Invalid description!...")
        try:
            if assignment.Deadline != datetime.datetime.strptime(assignment.Deadline, "%Y-%m-%d").strftime('%Y-%m-%d'):
                errors.append("Invalid date for deadline!...")
            current_date = assignment.Deadline.split('-')
            #if datetime.date(int(current_date[0]), int(current_date[1]), int(current_date[2])) < datetime.date.today():
            #    errors.append("Invalid date for deadline!...")
        except ValueError as ve:
            errors.append(str(ve))

        if len(errors) > 0:
            raise AssignmentValidatorException(errors)





class Assignment:
    def __init__(self,assignment_id, description, deadline):
        self._assignment_id = assignment_id
        self._description = description
        self._deadline = deadline

    def __str__(self):
        return ("-> ID: " + str(self.assignment_ID).ljust(8) + " Description: " + str(self.description).ljust(30) + " Deadline: " + str(self.Deadline))

    @property
    def assignment_ID(self):
        return self._assignment_id

    @property
    def description(self):
        return self._description

    @property
    def Deadline(self):
        return self._deadline


    @Deadline.setter
    def Deadline(self, value):
        self._deadline = value






