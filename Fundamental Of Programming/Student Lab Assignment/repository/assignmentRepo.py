import datetime
from domain.assignment import Assignment
class assignmentRepoException(Exception):
    def __init__(self,msg):
        self._msg = msg

class assignmentRepo:
    """
    class for the assigment list/repository
    """
    def __init__(self):
        self._assignment_list = []

    def __len__(self):
        return len(self.assignments)

    def __getitem__(self, item):
        return self.assignments[item]

    @property
    def assignments(self):
        return self._assignment_list

    def add_assingment_to_list(self, assignment):
        """
        we add an assignment to the list
        :param assignment: the given assignment
        :return:
        """
        self.assignments.append(assignment)

    def remove_assignment_from_list(self, assignment):
        """
        we delete a given assignment
        :param assigment: the given assignment we want to delete
        """
        self.assignments.remove(assignment)


    def update_assignment_in_list(self, index, deadline):
        """
        we update a given assignment with a new deadline
        :param index: the index of the given assingment
        :param deadline: the new deadline
        """
        self.assignments[index].Deadline = deadline
