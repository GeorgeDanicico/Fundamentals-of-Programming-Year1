from domain.student import Student
from repository.studentRepo import studentRepo
from service.UndoService import FunctionCall, OperationCall, CascadedOperation


class studentServiceException(Exception):
    """ custom exception handler for student service """
    def __init__(self,msg):
        self._msg = msg

class studentService:
    def __init__(self, student_repo,grades_repo,validator, undo_service):
        self._student_list = student_repo
        self._undo_service = undo_service
        self._grades_list = grades_repo
        self._validator = validator
    def __len__(self):
        return len(self.student_list_service)

    def __getitem__(self, item):
        return self.student_list_service[item]

    @property
    def validator(self):
        return self._validator

    @property
    def student_grade_service(self):# throuh
        return self._grades_list
    @property
    def student_list_service(self):# through this we will go into the student repo
        return self._student_list

    def add_student(self, id, name, group):
        """
        we add a student with the given id, name, group
        :param id: the given id
        :param name: the given name
        :param group: the given group
        """
        self.validator.validate(self,Student(id, name, group))
        student = Student(id, name, group)

        undo_function = FunctionCall(self.student_list_service.remove_student_from_list, student)
        redo_function = FunctionCall(self.student_list_service.add_student_to_list, student)
        operation = OperationCall(undo_function,redo_function)
        self._undo_service.record(operation)

        self.student_list_service.add_student_to_list( student)

    def remove_student(self, id):
        """
        we delete a student if the id is valid and it exists
        :param id: the id entered from the keyboard
        :param grades_list: the list of grades because we will delete all the assignment given for that student
        """
        assignment_id = None
        # we know if the student id exist so we dont have to check again
        student_index = self.validator.find_student_by_id(self.student_list_service, id)

        # TODO THINK OF A WAY TO REPRESENT THE CASCADE OPERATIONS FOR THE DELETION OF THE GRADES FOR THAT STUDENT
        # if we are here it means that the student exists
        student = self.student_list_service[student_index]
        # UNDO STARTS HERE ----------------------------------------
        undo_function = FunctionCall(self.student_list_service.add_student_to_list, student)
        redo_function = FunctionCall(self.student_list_service.remove_student_from_list, student)
        operation = OperationCall(undo_function, redo_function)


        Cascading_Operations = []
        Cascading_Operations.append(operation)


        index = 0
        while index < (len(self.student_grade_service)):
            if self.student_grade_service[index].student_id == student.student_id:
                # now we will add and undo operation for every grade we delete

                undo_function = FunctionCall(self.student_grade_service.add_grade, self.student_grade_service[index])
                redo_function = FunctionCall(self.student_grade_service.delete_grade, self.student_grade_service[index])
                operation = OperationCall(undo_function, redo_function)

                # And now we will store it for the cascading operation -------

                Cascading_Operations.append(operation)

                self.student_grade_service.delete_grade(self.student_grade_service[index])
                index -= 1
            index += 1

        # we record the entire cascading operations
        # Because we delete a student, it means that the list of cascaded operations clearly can't have the length = 0
        Cascading_Operations = tuple(Cascading_Operations)
        Cascading_Operations = CascadedOperation(*Cascading_Operations)
        self._undo_service.record(Cascading_Operations)
        # STORING THE CASCADED OPERATIONS ENDS HERE --------------------------------
        self.student_list_service.remove_student_from_list(self.student_list_service[student_index])

    def update_student(self, id, group):
        """
        we update a student with the given id and the new group if the id is correct and there is a student with that id
        and if the group is a valid one
        :param id: the given id
        :param group: the new group
        """
        student_index = self.validator.find_student_by_id(self.student_list_service, id)
        previous_group = self.student_list_service[student_index].student_group

        self.validator.check_group(group)
        if self.student_list_service[student_index].student_group == group:
            raise studentServiceException("The student is already in this group!...\n")

        # if the code gets here it means that the update is valid so we can do an undo/redo
        undo_function = FunctionCall(self.student_list_service.update_student_in_list, student_index, previous_group)
        redo_function = FunctionCall(self.student_list_service.update_student_in_list,student_index, group)
        operation = OperationCall(undo_function, redo_function)
        self._undo_service.record(operation)


        self.student_list_service.update_student_in_list(student_index, group)


