from Domain.grade import Grade
from Service.UndoService import FunctionCall, OperationCall, CascadedOperation


class gradeServiceException(Exception):
    def __init__(self, msg):
        self._msg = msg

class GradeDTO:
    """
    This is a class for Grade Data Transfer Object
    """
    def __init__(self,student, grade):
        self._student = student
        self._grade = grade
    @property
    def student(self):
        return self._student
    @property
    def grade(self):
        return self._grade
    def __str__(self):
        return ("Student: " + str(self._student).ljust(7) + " Grade: " + str(self.grade) )



class gradeService:
    def __init__(self, student_repo,assignment_repo,grade_repo,validators, validatora,validatorg, undo_service):
        self._grades_list = grade_repo
        self._students_list = student_repo
        self._assignments_list = assignment_repo
        self._validators = validators
        self._validatorg = validatorg
        self._validatora = validatora
        self._undo_service = undo_service


    def __len__(self):
        return len(self.grade_list)
    def __getitem__(self, item):
        return self.grade_list[item]
    @property
    def validatorg(self):
        return self._validatorg
    @property
    def validators(self):
        return self._validators
    @property
    def validatora(self):
        return self._validatora

    @property
    def student_list(self):
        return self._students_list

    @property
    def assignment_list(self):
        return self._assignments_list
    @property
    def grade_list(self):
        return self._grades_list

    def return_list_assignments(self,student_id):
        """
        :param student_id: the student id
        :return : we will return a list that will contain the Assignments id of the assignments given to that student if the grade value is NOne
        """
        assignment_id_list = []
        # the next line of code will show if the student exist and if not, it will raise an error

        self.validators.find_student_by_id(self.student_list, student_id)
        for grade in self.grade_list:
            if grade.student_id == student_id and grade.grade_value == None:
                assignment_id_list.append(grade.assignment_ID)
        if len(assignment_id_list) == 0:
            raise gradeServiceException("There is no assignment given/graded with None for that student!...\n")
        return assignment_id_list

    def add_grade(self, student_id, assignment_id, student_grade):
        """
        We grade an assignment !
        """
        index = self.validatorg.check_if_grade_exist(self.grade_list,student_id, assignment_id, student_grade)

        # if we get here it means that we found the correct grade so now we can do the undo for "updating" the grade from value none to a number

        undo_function = FunctionCall(self.grade_list.update_object, index, None)
        redo_function = FunctionCall(self.grade_list.update_object, index, student_grade)
        operation = OperationCall(undo_function, redo_function)
        self._undo_service.record(operation)


        self.grade_list.update_object(index, student_grade)



    def give_assignment(self, student_id, assignment_id, student_grade= None):
        """
        We give an assingment to a student and we set the grade to None
        :param student_id: the student id
        :param assignment_id: the assignment id
        """
        self.validators.find_student_by_id(self.student_list,student_id)
        self.validatora.find_assignment(self.assignment_list, assignment_id)
        for grade in self.grade_list:
            if grade.student_id == student_id and grade.assignment_ID == assignment_id:
                raise gradeServiceException("Invalid student and assignment id. The student already has this assignment!...\n")
        # the grade when we assign an assignment is None

        new_grade = Grade(student_id,assignment_id, None)
        # we can now make the undo/redo for giving an assignment to a student
        #--------------------------

        undo_function = FunctionCall(self.grade_list.remove_object, new_grade)
        redo_function = FunctionCall(self.grade_list.add_object, new_grade)
        operation = OperationCall(undo_function, redo_function)
        self._undo_service.record(operation)

        #----------------------------------------------------------
        self.grade_list.add_object(new_grade)

    def give_assignment_to_group(self, group, assignment_id, student_grade = None):
        """
             We give an assingment to a student and we set the grade to None
             :param group: the group of students where we will assign that assignment
             :param assignment_id: the assignment id
        """
        # in order to do the undo we need to use a cascade operation because we need to delete all the grades
        # given to a group when we undo/ add when we do redo
        self.validatora.find_assignment(self.assignment_list, assignment_id)

        Cascaded_Operation = []
        for index in range(len(self.student_list)):
            if self.student_list[index].student_group == group:
                done = False
                for grade in self.grade_list:
                    if grade.student_id == self.student_list[index].student_id and grade.assignment_ID == assignment_id:
                        done = True
                if done == False:
                    new_grade = Grade(self.student_list[index].student_id, assignment_id, None)
                    # here the undo of the assignments began-----------------

                    undo_function = FunctionCall(self.grade_list.remove_object, new_grade)
                    redo_function = FunctionCall(self.grade_list.add_object, new_grade)
                    operation = OperationCall(undo_function, redo_function)

                    Cascaded_Operation.append(operation)
                    # undo/redo ends here ------------------------------------
                    self.grade_list.add_object(new_grade)

        # If the length of the cascaded operation is not 0 we can append the undo/redo
        # OTHER wise we can print an error message that all the students in that group already have that assignment
        if len(Cascaded_Operation) != 0:
            Cascaded_Operation = tuple(Cascaded_Operation)
            Cascaded_Operation = CascadedOperation(*Cascaded_Operation)
            self._undo_service.record(Cascaded_Operation)
        else:
            raise gradeServiceException(f"All the students in group {group} have the assignment {assignment_id} ")

    def create_statistics_for_a_assignment(self, assignment_id):
        """
        we will create statistics for a given assignment, where we will have the grades sorted by the average grade at
        this assignment
        :param assignment_id: the assignment id
        :return : we will return a list which will contain the index of that student and the grade
        """
        # we check if the assignment exists.
        self.validatora.find_assignment(self.assignment_list, assignment_id)
        # if we reach this, it means that the assignment exists

        ordered_list =[]
        average_grade = 0.0
        average_count = 0
        for grade in self.grade_list:

            if grade.assignment_ID == assignment_id and grade.grade_value != None:
                average_grade += round(float(grade.grade_value),2)
                average_count += 1
                student_index = self.validators.find_student_by_id(self.student_list,grade.student_id)
                ordered_list.append(GradeDTO(self.student_list[student_index], float(grade.grade_value)))


        if len(ordered_list) == 0:
            raise gradeServiceException("There is no student graded with that assignment!...\n")


        ordered_list = sorted(ordered_list ,key=lambda x:x.grade, reverse = True)
        return ordered_list

    def create_statistics_for_latet(self):
        """
        we create a list of students who are late in handling an assignment
        :return: We return a list containing all the students who have at least an assignment whose deadline passed
        """
        late_student = []
        for grade in self.grade_list:
            if grade.grade_value == None:
                done = False
                for student in late_student:
                    if student.student.student_id == grade.student_id:
                        done = True

                if not done:
                    assignment_index =  self.validatora.find_assignment(self.assignment_list, grade.assignment_ID)
                    if self.validatora.check_if_deadline_passed(self.assignment_list[assignment_index].Deadline) == True:
                        student_index = self.validators.find_student_by_id(self.student_list,grade.student_id)
                        late_student.append(GradeDTO(self.student_list[student_index], None))

        if len(late_student) == 0:
            raise gradeServiceException("There is no student with late submission!...\n")

        return late_student

    def create_statistics_for_best(self):
        """
        we store the best students who have all the assignments graded
        :return : we will return a list that will contain all the best students/ if the list is empty we will raise an error
        """
        best_students = []
        for student in self.student_list:
            student_grade = 0.0
            grade_counter = 0
            for grade in self.grade_list:
                if grade.student_id == student.student_id:
                    if grade.grade_value != None:
                        student_grade += round(float(grade.grade_value))
                        grade_counter += 1

            if grade_counter == len(self.assignment_list):
                student_grade = round(float(student_grade/grade_counter), 2)
                best_students.append(GradeDTO(student,student_grade))


        if len(best_students) == 0:
            raise gradeServiceException("There is no student graded at all assignments!...")

        best_students = sorted(best_students ,key=lambda x:x.grade, reverse = True)
        return best_students



