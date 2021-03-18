from domain.assignment import Assignment,Assignment_Validator
from domain.student import Student,Student_Validator
from repository.studentRepo import  studentRepo
from service.UndoService import FunctionCall, OperationCall, CascadedOperation
from service.studentService import studentService
from repository.assignmentRepo import assignmentRepo
from domain.grade import Grade,Grade_Validator
from repository.gradeRepo import gradeRepo
from service.gradeService import gradeService

import datetime

class assignmentServiceException(Exception):
    def __init__(self, msg):
        self._msg = msg


class assignmentService:
    def __init__(self,assignment_repo,grades_repo, validator, undo_service):
        self._assignments = assignment_repo
        self._grades_list = grades_repo
        self._validator = validator
        self._undo_service = undo_service

    def __len__(self):
        return len(self.list_of_assignments)

    def __getitem__(self, item):
        return self.list_of_assignments[item]
    @property
    def validator(self):
        return self._validator

    @property
    def service_assign_grades(self):
        return self._grades_list
    @property
    def list_of_assignments(self):
        return self._assignments

    def add_assignment(self, id, description, deadline):
        """
        we add a given assignment if it is valid
        :param id: the given ID
        :param description: the given description
        :param deadline: the given Deadline

        """
        # if there is no exception raised, it means that the id is unique
        self._validator.validate(self.list_of_assignments,Assignment(id, description, deadline))
        ass = Assignment(id, description, deadline)
        # if the code gets to this point it means that the assignment is valid so we can do the undo/redo

        undo_function = FunctionCall(self.list_of_assignments.remove_assignment_from_list, ass)
        redo_function = FunctionCall(self.list_of_assignments.add_assingment_to_list, ass)
        operation = OperationCall(undo_function, redo_function)
        self._undo_service.record(operation)


        self.list_of_assignments.add_assingment_to_list(ass)

    def remove_assignment(self, id):
        """
        we delete the assignment with the given id
        :param id: the given id
        # :grades_list: the grades_list because we will delete every given assignment with that ID
        """

        index = self.validator.find_assignment(self.list_of_assignments,id)
        assignment = self.list_of_assignments[index]
        # UNDO STARTS HERE ----------------------------------------
        undo_function = FunctionCall(self.list_of_assignments.add_assingment_to_list, assignment)
        redo_function = FunctionCall(self.list_of_assignments.remove_assignment_from_list, assignment)
        operation = OperationCall(undo_function, redo_function)

        Cascading_Operations = []
        Cascading_Operations.append(operation)

        index = 0
        while index < (len(self.service_assign_grades)):
            if self.service_assign_grades[index].assignment_ID == assignment.assignment_ID:
                # now we will add and undo operation for every grade we delete

                undo_function = FunctionCall(self.service_assign_grades.add_grade, self.service_assign_grades[index])
                redo_function = FunctionCall(self.service_assign_grades.delete_grade, self.service_assign_grades[index])
                operation = OperationCall(undo_function, redo_function)

                # And now we will store it for the cascading operation -------

                Cascading_Operations.append(operation)

                self.service_assign_grades.delete_grade(self.service_assign_grades[index])
                index -= 1
            index += 1

        # we record the entire cascading operations
        Cascading_Operations = tuple(Cascading_Operations)
        Cascading_Operations = CascadedOperation(*Cascading_Operations)
        self._undo_service.record(Cascading_Operations)
        # STORING THE CASCADED OPERATIONS ENDS HERE --------------------------------


        self.list_of_assignments.remove_assignment_from_list(assignment)

    def update_assignment(self, id, deadline):
        """
        we check if there is an assignment with the given id and update it in the list if the deadline is valid
        :param id: the given ID
        :param deadline: the given deadline
        """

        index = self.validator.find_assignment(self.list_of_assignments, id)
        if not self.validator.validate_datetime(deadline):
            raise assignmentServiceException("Invalid deadline!...\n")

        previous_deadline = self.list_of_assignments[index].Deadline
        # if we get to this point it means that the
        undo_function = FunctionCall(self.list_of_assignments.update_assignment_in_list, index, previous_deadline)
        redo_function = FunctionCall(self.list_of_assignments.update_assignment_in_list, index, deadline)
        operation = OperationCall(undo_function, redo_function)
        self._undo_service.record(operation)

        self.list_of_assignments.update_assignment_in_list(index, deadline)



