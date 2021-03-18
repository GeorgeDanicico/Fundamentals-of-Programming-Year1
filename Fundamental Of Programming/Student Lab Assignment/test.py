from domain.assignment import Assignment, Assignment_Validator, AssignmentException,AssignmentValidatorException
from domain.student import Student, Student_Validator, studentException, studentValidatorException
from repository.studentRepo import studentRepo, studentRepoException
from service.UndoService import UndoService, UndoServiceError
from service.studentService import studentService, studentServiceException
from service.assignmentService import assignmentService, assignmentServiceException
from repository.assignmentRepo import assignmentRepo
from domain.grade import Grade,Grade_Validator, GradeExceptions
from repository.gradeRepo import gradeRepo
from service.gradeService import gradeService, gradeServiceException
import unittest


class TestStudent(unittest.TestCase):
    def setUp(self):
        student_repo = studentRepo()
        grade_repo = gradeRepo()
        student_validator = Student_Validator()
        undo_service = UndoService()
        student_service = studentService(student_repo, grade_repo, student_validator,undo_service)
        self._student_list = student_service
        self._student_list_repo = student_repo
    @property
    def list_s(self):
        return self._student_list
    @property
    def list_s_repo(self):
        return self._student_list_repo

    def test_addstudentrepo(self):
        stud = str(Student('123', 'Mark Park', '912'))

        self.list_s_repo.add_student_to_list(stud)
        self.assertEqual(len(self.list_s_repo.student_list), 1)

        stud = Student('124', 'Mark Park', '912')
        self.list_s_repo.add_student_to_list(stud)
        stud = Student('125', 'Mark Park', '912')
        self.list_s_repo.add_student_to_list(stud)
        stud = Student('126', 'Mark Park', '912')
        self.list_s_repo.add_student_to_list(stud)
        stud = Student('127', 'Mark Park', '912')
        self.list_s_repo.add_student_to_list(stud)

        self.assertEqual(len(self.list_s_repo.student_list), 5)

    def test_addstudentservice(self):
        stud = Student('123','Mark Park','912')
        self.list_s.add_student('123','Mark Park','912')
        try:
            val = Student_Validator()
            val.validate(self.list_s,Student('123','MarkP','112'))
            self.assertFalse('not ok')
        except studentValidatorException as ve:
            s = str(ve)
            self.assertTrue('ok')
        self.assertEqual(len(self.list_s), 1)
        self.assertEqual(len(self.list_s.student_list_service), 1)
        try:
            self.list_s.add_student('123', 'Mark Park', '912')
            self.assertFalse('Not good')
        except studentException:
            self.assertTrue('OK')
        self.list_s.add_student('124', 'Mark Park', '912')
        self.list_s.add_student('125', 'Mark Park', '912')
        self.list_s.add_student('126', 'Mark Park', '912')

        self.assertEqual(len(self.list_s.student_list_service), 4)

        try:
            self.list_s.add_student('12a', 'Mark Park','123')
            self.assertFalse('Not good')
        except studentException:
            self.assertTrue('OK')

        try:
            self.list_s.add_student('392', 'Mark Park','123')
            self.assertFalse('Not good')
        except studentException:
            self.assertTrue('OK')

        try:
            self.list_s.add_student('392', 'Mark P@rk','912')
            self.assertFalse('Not good')
        except studentException:
            self.assertTrue('OK')



    def test_removestudentservice(self):
        stud = Student('123', 'Mark Park', '912')
        student_repo = studentRepo()
        assignment_repo = assignmentRepo()
        grade_repo = gradeRepo()

        student_validator = Student_Validator()
        assignment_validator = Assignment_Validator()
        grade_validator = Grade_Validator()
        undo_service = UndoService()
        g_list = gradeService(student_repo, assignment_repo, grade_repo, student_validator, assignment_validator, grade_validator, undo_service)
        self.list_s.add_student('234', 'Mark Park', '912')
        self.list_s.add_student('235', 'Mark Park', '912')
        self.list_s.add_student('236', 'Mark Park', '912')
        self.list_s.remove_student('234')

        self.assertEqual(len(self.list_s.student_list_service), 2)

        try:
            self.list_s.remove_student('234')
            self.assertFalse('Not good')
        except studentException:
            self.assertTrue('OK')

        try:
            self.list_s.remove_student('za2')
            self.assertFalse('Not good')
        except studentException:
            self.assertTrue('OK')

        try:
            self.list_s.remove_student('392')
            self.assertFalse('Not good')
        except studentException:
            self.assertTrue('OK')
        self.assertEqual(len(self.list_s.student_list_service), 2)

    def test_removestudentrepo(self):

        self.assertEqual(len(self.list_s_repo.student_list), 0)

        stud = Student('124', 'Mark Park', '912')
        self.list_s_repo.add_student_to_list(stud)
        self.list_s_repo.remove_student_from_list(stud)
        stud = Student('125', 'Mark Park', '912')
        self.list_s_repo.add_student_to_list(stud)
        self.list_s_repo.remove_student_from_list(stud)
        stud = Student('126', 'Mark Park', '912')
        self.list_s_repo.add_student_to_list(stud)
        self.list_s_repo.remove_student_from_list(stud)
        stud = Student('127', 'Mark Park', '912')
        self.list_s_repo.add_student_to_list(stud)
        self.list_s_repo.remove_student_from_list(stud)

        self.assertEqual(len(self.list_s_repo.student_list), 0)


    def test_updatestudentservice(self):
        # we will already elements in the list when we will test this function
        # so we can use the data we defined previously
        self.list_s.add_student('234', 'Mark Park', '912')
        self.list_s.add_student('235', 'Mark Park', '912')
        self.list_s.add_student('236', 'Mark Park', '912')
        self.list_s.update_student('235', '913')
        self.assertEqual(self.list_s.student_list_service[1].student_group, '913')

        try:
            self.list_s.update_student('236', '913')
            self.assertTrue('OK')
        except studentRepoException:
            self.assertFalse('Not good')

        try:
            self.list_s.update_student('23a', '913')
            self.assertFalse('Not good')
        except studentException:
            self.assertTrue('OK')

    def test_updatestudentrepo(self):
        stud = Student('124', 'Mark Park', '912')
        self.list_s_repo.add_student_to_list(stud)
        stud = Student('125', 'Mark Park', '912')
        self.list_s_repo.add_student_to_list(stud)
        stud = Student('126', 'Mark Park', '912')
        self.list_s_repo.add_student_to_list(stud)
        stud = Student('127', 'Mark Park', '912')
        self.list_s_repo.add_student_to_list(stud)


        self.list_s_repo.update_student_in_list(0, '913')
        self.assertEqual(self.list_s_repo[0].student_group, '913')
        try:
            self.list_s_repo.update_student_in_list(0,'912')
            self.assertTrue('OK')
        except studentRepoException:
            self.assertFalse('Not good')



class TestAssignment(unittest.TestCase):
    def setUp(self):
        assignment_repo = assignmentRepo()
        grade_repo = gradeRepo()
        assignment_validator = Assignment_Validator()
        self._undo_service = UndoService()
        self._assignment_list = assignmentService(assignment_repo, grade_repo, assignment_validator,self._undo_service)
        self._assignment_repo = assignmentRepo()
    @property
    def assing_repo(self):
        return self._assignment_repo
    @property
    def assing_list(self):
        return self._assignment_list

    def test_addassignmentservice(self):
        assing = str(Assignment('123','Homework due Tomorrow', '2021-12-22'))
        val = Assignment_Validator()
        #assing = Assignment('123', 'Homework due Tomorrow', '2021-12-22')
        self.assertEqual(val.check_if_deadline_passed('2020-12-12'), False)
        self.assertEqual(val.check_if_deadline_passed('20202-12-12'), False)
        self.assertEqual(val.check_if_deadline_passed('2020-12-32'), False)
        self.assertEqual(val.check_if_deadline_passed('2020-10-10-10'), False)
        self.assertEqual(val.validate_datetime('2020-12-32'), False)
        self.assertEqual(val.validate_datetime('2020-10-10-10'), False)
        self.assertEqual(val.validate_datetime('2020-10-30'), False)
        try:
            val.validate(self.assing_list.list_of_assignments, Assignment('123', 'Ho', '2020-10-20'))
            self.assertFalse('not ok')
        except AssignmentValidatorException as ve:
            s = str(ve)
            self.assertTrue('ok')
        try:
            val.validate(self.assing_list.list_of_assignments,Assignment('123','Ho', '20212-12-22'))
            self.assertFalse('not ok')
        except AssignmentValidatorException as ve:
            s = str(ve)
            self.assertTrue('ok')
        self.assing_list.add_assignment('123', 'Homework due Tomorrow', '2021-12-22')
        try:
            self.assing_list.add_assignment('123', 'Homework due Tomorrow', '2021-12-22')
            self.assertFalse('Not good')
        except AssignmentException:
            self.assertTrue('OK')
        self.assertEqual(len(self.assing_list), 1)

        self.assing_list.add_assignment('124', 'Homework due Tomorrow', '2021-12-22')
        self.assing_list.add_assignment('125', 'Homework due Tomorrow', '2021-12-22')
        self.assing_list.add_assignment('126', 'Homework due Tomorrow', '2021-12-22')
        self.assing_list.add_assignment('127', 'Homework due Tomorrow', '2021-12-22')
        self.assertEqual(len(self.assing_list), 5)
        try:
            self.assing_list.add_assignment('128', 'Ho', '2021-12-22')
            self.assertFalse('Not good')
        except AssignmentException:
            self.assertTrue('OK')

        try:
            self.assing_list.add_assignment('128', 'Homework due Tomorrow', '2021-12-222')
            self.assertFalse('Not good')
        except AssignmentException:
            self.assertTrue('OK')

        try:
            self.assing_list.add_assignment('123', 'Homework due Tomorrow', '2021-12-22')
            self.assertFalse('Not good')
        except AssignmentException:
            self.assertTrue('OK')

    def test_addassignmentrepo(self):
        assing = Assignment('123', 'Homework due Tomorrow', '2021-12-22')
        self.assing_repo.add_assingment_to_list(assing)
        try:
            self.assing_repo.add_assingment_to_list(assing)
            self.assertTrue('OK')
        except AssignmentException:
            self.assertFalse('Not good')

        self.assertEqual(len(self.assing_repo), 2)
        assing = Assignment('123', 'Homework due Tomorrow', '2021-12-22')
        self.assing_repo.add_assingment_to_list(assing)
        assing = Assignment('124', 'Homework due Tomorrow', '2021-12-22')
        self.assing_repo.add_assingment_to_list(assing)
        assing = Assignment('125', 'Homework due Tomorrow', '2021-12-22')
        self.assing_repo.add_assingment_to_list(assing)
        assing = Assignment('126', 'Homework due Tomorrow', '2021-12-22')
        self.assing_repo.add_assingment_to_list(assing)
        self.assertEqual(len(self.assing_repo), 6)

    def test_removeassignmentservice(self):
        self.assing_list.add_assignment('124', 'Homework due Tomorrow', '2021-12-22')
        self.assing_list.add_assignment('125', 'Homework due Tomorrow', '2021-12-22')
        self.assing_list.add_assignment('126', 'Homework due Tomorrow', '2021-12-22')
        self.assing_list.add_assignment('127', 'Homework due Tomorrow', '2021-12-22')

        student_repo = studentRepo()
        assignment_repo = assignmentRepo()
        grade_repo = gradeRepo()

        student_validator = Student_Validator()
        assignment_validator = Assignment_Validator()
        grade_validator = Grade_Validator()
        g_list = gradeService(student_repo, assignment_repo, grade_repo, student_validator, assignment_validator,
                              grade_validator, self._undo_service)
        self.assing_list.remove_assignment('124')

        self.assertEqual(len(self.assing_list.list_of_assignments), 3)

        try:
            self.assing_list.remove_assignment('124')
            self.assertFalse('Not good')
        except AssignmentException:
            self.assertTrue('OK')

        try:
            self.assing_list.remove_assignment('124a')
            self.assertFalse('Not good')
        except AssignmentException:
            self.assertTrue('OK')

        try:
            self.assing_list.remove_assignment('125')
            self.assertTrue('OK')
        except AssignmentException:
            self.assertFalse('Not good')
        self.assertEqual(len(self.assing_list.list_of_assignments), 2)

    def test_removeassignmentrepo(self):
        assing = Assignment('123', 'Homework due Tomorrow', '2021-12-22')
        self.assing_repo.add_assingment_to_list(assing)
        self.assing_repo.remove_assignment_from_list(assing)
        assing = Assignment('124', 'Homework due Tomorrow', '2021-12-22')
        self.assing_repo.add_assingment_to_list(assing)
        self.assing_repo.remove_assignment_from_list(assing)
        assing = Assignment('125', 'Homework due Tomorrow', '2021-12-22')
        self.assing_repo.add_assingment_to_list(assing)
        self.assing_repo.remove_assignment_from_list(assing)
        assing = Assignment('126', 'Homework due Tomorrow', '2021-12-22')
        self.assing_repo.add_assingment_to_list(assing)
        self.assing_repo.remove_assignment_from_list(assing)

        self.assertEqual(len(self.assing_repo.assignments), 0)

    def test_updateassignmentservice(self):
        # because we added data before we dont have to add again
        self.assing_list.add_assignment('124', 'Homework due Tomorrow', '2021-12-22')
        self.assing_list.add_assignment('125', 'Homework due Tomorrow', '2021-12-22')
        self.assing_list.add_assignment('126', 'Homework due Tomorrow', '2021-12-22')
        self.assing_list.add_assignment('127', 'Homework due Tomorrow', '2021-12-22')

        self.assing_list.update_assignment('124', '2022-12-23')
        self.assing_list.update_assignment('125', '2022-12-23')
        self.assing_list.update_assignment('126', '2022-12-23')
        self.assing_list.update_assignment('127', '2022-12-23')
        self.assertEqual(self.assing_list.list_of_assignments[0].Deadline, '2022-12-23')
        try:
            self.assing_list.update_assignment('124', '2022-12-233')
        except assignmentServiceException:
            self.assertTrue('OK')

        try:
            self.assing_list.update_assignment('1245', '2022-12-233')
        except AssignmentException:
            self.assertTrue('OK')

        try:
            self.assing_list.update_assignment('125', '2022-12-233')
        except assignmentServiceException:
            self.assertTrue('OK')

    def test_updateassignmentrepo(self):
        assing = Assignment('123', 'Homework due Tomorrow', '2021-12-22')
        self.assing_repo.add_assingment_to_list(assing)
        assing = Assignment('124', 'Homework due Tomorrow', '2021-12-22')
        self.assing_repo.add_assingment_to_list(assing)
        assing = Assignment('125', 'Homework due Tomorrow', '2021-12-22')
        self.assing_repo.add_assingment_to_list(assing)
        assing = Assignment('126', 'Homework due Tomorrow', '2021-12-22')
        self.assing_repo.add_assingment_to_list(assing)

        self.assing_repo.update_assignment_in_list(1,'2022-11-22')
        self.assertEqual(self.assing_repo[1].Deadline, '2022-11-22')


class TestGrade(unittest.TestCase):
    def setUp(self):

        student_repo = studentRepo()
        assignment_repo = assignmentRepo()
        grade_repo = gradeRepo()
        student_validator = Student_Validator()
        assignment_validator = Assignment_Validator()
        grade_validator = Grade_Validator()
        self._undo_service = UndoService()

        student_service = studentService(student_repo, grade_repo, student_validator, self._undo_service )
        assignment_service = assignmentService(assignment_repo, grade_repo, assignment_validator, self._undo_service)
        grade_service = gradeService(student_repo, assignment_repo, grade_repo, student_validator, assignment_validator,grade_validator, self._undo_service)

        student_validator = Student_Validator()
        assignment_validator = Assignment_Validator()
        grade_validator = Grade_Validator()

        self._student_list = student_service
        self._assignment_list = assignment_service
        self._grade_list = grade_service
        self.list_s.add_student('124', 'Mark Park', '912')
        self.list_s.add_student('125', 'Mark Park', '912')
        self.list_s.add_student('126', 'Mark Park', '912')
        self.list_s.add_student('127', 'Mark Park', '913')
        self.list_s.add_student('128', 'Mark Park', '914')
        self.assing_list.add_assignment('124', 'Homework due Tomorrow', '2021-12-22')
        self.assing_list.add_assignment('125', 'Homework due Tomorrow', '2021-12-22')
        self.assing_list.add_assignment('126', 'Homework due Tomorrow', '2021-12-22')
        self.assing_list.list_of_assignments.add_assingment_to_list(Assignment('127', 'Homework due Tomorrow', '2020-10-22'))
    @property
    def list_s(self):
        return self._student_list

    @property
    def assing_list(self):
        return self._assignment_list

    @property
    def grade_list(self):
        return self._grade_list

    def test_grade(self):
        grade_val = Grade_Validator()

        grade_val.validate(Grade('124', '124', '10'))
        grade = Grade('124', '124', '10')
        try:
            grade_val.check_if_grade_exist(self.grade_list,'124','124','10')
        except GradeExceptions:
            self.assertTrue('ok')
        st = str(grade)
        try:
            grade_val.validate(Grade('124', '124', '11'))
            self.assertFalse('not ok')
        except GradeExceptions:
            self.assertTrue('ok')

        try:
            grade_val.validate(Grade('124', '12a', '11'))
            self.assertFalse('not ok')
        except GradeExceptions:
            self.assertTrue('ok')
        try:
            grade_val.validate(Grade('12a', '124', '11'))
            self.assertFalse('not ok')
        except GradeExceptions:
            self.assertTrue('ok')
        try:
            grade_val.validate(Grade('124', '124', '1a'))
            self.assertFalse('not ok')
        except GradeExceptions:
            self.assertTrue('ok')
        try:
            val = self.grade_list.return_list_assignments('124')
            self.assertFalse('not ok')
        except gradeServiceException:
            self.assertTrue('ok')



    def test_deletegrade(self):
        self.grade_list.give_assignment( '124', '124')
        self.assertEqual(len(self.grade_list), 1)
        self.grade_list.give_assignment_to_group( '912', '124')
        self.assertEqual(len(self.grade_list), 3)
        self.grade_list.give_assignment_to_group( '913', '124')
        self.assertEqual(len(self.grade_list), 4)

        self.list_s.remove_student('124')

        self.assing_list.remove_assignment('124')
        self.assertEqual(len(self.grade_list),0)

    def test_giveassignment(self):
        self.grade_list.give_assignment('124','124')
        self.assertEqual(len(self.grade_list), 1)
        self.grade_list.give_assignment_to_group( '912', '124')
        self.assertEqual(len(self.grade_list), 3)
        self.grade_list.give_assignment_to_group( '913', '124')
        self.assertEqual(len(self.grade_list), 4)
        val = self.grade_list.return_list_assignments('124')
        self.assertEqual(len(val), 1)

    def test_addgrade(self):
        # we first add the data we need to

        self.grade_list.give_assignment('124', '124')
        self.assertEqual(len(self.grade_list), 1)
        self.grade_list.give_assignment_to_group('912', '124')
        self.assertEqual(len(self.grade_list), 3)
        self.grade_list.give_assignment_to_group('913', '124')
        self.assertEqual(len(self.grade_list), 4)
        # and after that we just check if everyting is ok
        
        self.grade_list.add_grade( '124','124','10')
        self.grade_list.add_grade( '125', '124', '5')
        self.grade_list.add_grade( '126', '124', '7')
        self.assertEqual(self.grade_list[0].grade_value,'10')

        try:
            self.grade_list.add_grade('124', '124', '10')
            self.assertFalse('Not ok')
        except GradeExceptions:
            self.assertTrue('ok')

        try:
            self.grade_list.add_grade('125', '124', 'a')
            self.assertFalse('Not ok')
        except GradeExceptions:
            self.assertTrue('ok')

    def test_create_stat_assign(self):
        self.grade_list.give_assignment_to_group( '912', '125')
        self.assertEqual(len(self.grade_list), 3)

        self.grade_list.add_grade('124', '125', '10')
        self.grade_list.add_grade('125', '125', '5')
        self.grade_list.add_grade('126', '125', '7')

        ordered_list = self.grade_list.create_statistics_for_a_assignment('125')
        self.assertEqual(len(ordered_list),3)

        try:
            ordered_list = self.grade_list.create_statistics_for_a_assignment( '127')
            self.assertFalse('not ok')
        except gradeServiceException:
            self.assertTrue('ok')

    def test_create_late(self):
        self.grade_list.give_assignment('128', '127')
        self.assertEqual(self.grade_list.grade_list[0].grade_value, None)
        late_list = self.grade_list.create_statistics_for_latet()
        self.assertEqual(len(late_list), 1)

        try:
            self.grade_list.add_grade('128', '127', '10')
            late_list = self.grade_list.create_statistics_for_latet()
        except gradeServiceException:
            self.assertTrue('ok')

    def test_create_best(self):
        self.grade_list.give_assignment_to_group('912', '124')
        self.grade_list.give_assignment_to_group('912', '125')
        self.grade_list.give_assignment_to_group('912', '126')
        self.grade_list.give_assignment_to_group('912', '127')

        try:
            best_students = self.grade_list.create_statistics_for_best()
        except gradeServiceException:
            self.assertTrue('ok')

        self.grade_list.add_grade('124', '124', '10')
        self.grade_list.add_grade('125', '124', '5')
        self.grade_list.add_grade('126', '124', '7')

        self.grade_list.add_grade( '124', '125', '10')
        self.grade_list.add_grade( '125', '125', '5')
        self.grade_list.add_grade( '126', '125', '7')

        self.grade_list.add_grade( '124', '126', '10')
        self.grade_list.add_grade( '125', '126', '5')
        self.grade_list.add_grade( '126', '126', '7')

        self.grade_list.add_grade('124', '127', '10')
        self.grade_list.add_grade('125', '127', '5')
        self.grade_list.add_grade('126', '127', '7')

        self.assertEqual(len(self.grade_list), 12)
        best_students = self.grade_list.create_statistics_for_best()


class TestUndo(unittest.TestCase):
    def setUp(self):
        student_repo = studentRepo()
        assignment_repo = assignmentRepo()
        grade_repo = gradeRepo()
        student_validator = Student_Validator()
        assignment_validator = Assignment_Validator()
        grade_validator = Grade_Validator()
        undo_service = UndoService()
        self._undo_service = undo_service
        student_service = studentService(student_repo, grade_repo, student_validator, self._undo_service )
        assignment_service = assignmentService(assignment_repo, grade_repo, assignment_validator, self._undo_service)
        grade_service = gradeService(student_repo, assignment_repo, grade_repo, student_validator, assignment_validator,grade_validator, self._undo_service)

        self._grades_list = grade_service
        self._assignments = assignment_service
        self._student_list = student_service

    @property
    def assignments(self):
        return self._assignments

    @property
    def list_s(self):
        return self._student_list

    def test_undo(self):
        self.list_s.add_student('124', 'Mark Park', '912')
        self.list_s.add_student('125', 'Mark Park', '912')
        self.list_s.add_student('126', 'Mark Park', '912')

        # we test if the normal undo works
        self.assertEqual(len(self.list_s), 3)
        self._undo_service.undo()
        self.assertEqual(len(self.list_s), 2)
        self._undo_service.redo()
        self.assertEqual(len(self.list_s), 3)

        try:
            self._undo_service.redo()
            self.assertFalse('not ok')
        except UndoServiceError:
            self.assertTrue('ok')

        self.list_s.add_student('127', 'Mark Park', '913')
        self.list_s.add_student('128', 'Mark Park', '914')
        self.list_s.add_student('129', 'Mark Park', '915')

        self.assignments.add_assignment('124', 'Homework due Tomorrow', '2021-12-22')
        self.assignments.add_assignment('125', 'Homework due Tomorrow', '2021-12-22')
        self.assignments.add_assignment('126', 'Homework due Tomorrow', '2021-12-22')

        self.assertEqual(len(self.assignments), 3)
        self._undo_service.undo()
        self.assertEqual(len(self.assignments), 2)
        self._undo_service.redo()
        self.assertEqual(len(self.assignments), 3)

        self._grades_list.give_assignment_to_group('912','124')
        self.assertEqual(len(self._grades_list), 3)
        self._undo_service.undo()
        self.assertEqual(len(self._grades_list), 0)
        self._undo_service.redo()

        self._grades_list.add_grade('124','124','10')
        self._undo_service.undo()
        self.assertEqual(self._grades_list[0].grade_value, None)
        self._undo_service.redo()
        self.assertEqual(self._grades_list[0].grade_value, '10')