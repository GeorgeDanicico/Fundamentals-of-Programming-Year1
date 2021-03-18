from Domain.assignment import Assignment_Validator


class FunctionsAcceptance:
    def __init__(self, grade_repo, assignment_repo, assignment_id=None):
        self._grade_repo = grade_repo
        self._assignment_repo = assignment_repo
        # we will use this in order to save the id for the filter the students by a given assignment
        self._assignment = assignment_id

    def filter_assignment(self, studentDTO):
        """
        for the moment, this function will be the filtering type with respect to a certain assignment
        :param studentDTO:  This will be in this case a DTO object, so we will still have to call the student field from the object
        """
        for grade in self._grade_repo:
            if grade.student_id == studentDTO.student.student_id and grade.assignment_ID == self._assignment and grade.grade_value is not None:
                studentDTO.grade = float(grade.grade_value)
                return True
        return False

    def filter_late(self, student):
        """
        we filter the late students in this case where the object is a student
        :param student: the student obj we want to check
        """
        date_check = Assignment_Validator()
        # for grade in self._grade_repo:
        #     if grade.student_id == student.student_id and grade.grade_value is None:
        #         for assignment in self._assignment_repo:
        #             if date_check.check_if_deadline_passed(assignment.Deadline):
        #                 return True

        for assignment in filter(lambda x: date_check.check_if_deadline_passed(x.Deadline), self._assignment_repo):
            for grade in self._grade_repo:
                if grade.student_id == student.student_id and assignment.assignment_ID == grade.assignment_ID and grade.grade_value is None:
                    return True

        return False

    def filter_best(self, studentDTO):
        """
        This function will check a student if he has all the assignments graded
        :param studentDTO: in this case, the student is a DTO, so we will have to also call the student field
        """
        assignments_counter = 0
        average_grade = 0.0
        for grade in self._grade_repo:
            if grade.student_id == studentDTO.student.student_id and grade.grade_value is not None:
                assignments_counter += 1
                average_grade += float(grade.grade_value)
                if len(self._assignment_repo) == assignments_counter:
                    studentDTO.grade = average_grade / assignments_counter
                    return True
        return False
