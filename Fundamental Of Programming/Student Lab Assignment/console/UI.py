from service.studentService import studentService,studentServiceException
from domain.student import Student,studentException,Student_Validator
from domain.assignment import Assignment,Assignment_Validator, AssignmentException
from domain.grade import Grade,Grade_Validator,GradeExceptions
from service.assignmentService import assignmentService,assignmentServiceException
from service.gradeService import gradeService,gradeServiceException
from repository.studentRepo import studentRepoException
from service.UndoService import UndoService, UndoServiceError
import random

class UIException(Exception):
    def __init__(self, msg):
        self._msg = msg

class generateRandom:
    def __init__(self, list_students, list_assignments, grades_list):
        self._list = list_students
        self._alist = list_assignments
        self._grades_list = grades_list
        self._id = 0

    @property
    def llist_s(self):
        return self._list

    @property
    def llist_a(self):
        return self._alist

    def generate_random_id(self):
        """
        we generate randomly the id's for each student
        """
        rand_id = 0
        ok = True
        while ok :
            rand_id = random.randint(100,999)
            ok = False
            for student in self.llist_s:
                if str(rand_id) == student.student_id:
                    ok = True
        # when the loop stopped we have a guaranteed valid id
        return str(rand_id)

    def generate_rand_ass_id(self):
        """
        we generate randomly the id's for each assignment
        """
        rand_id = 0
        ok = True
        while ok:
            rand_id = random.randint(100, 999)
            ok = False
            for assignment in self.llist_a:
                if str(rand_id) == assignment.assignment_ID:
                    ok = True
        # when the loop stopped we have a guaranteed valid id
        return str(rand_id)

    def generate_random_student(self):
        for i in range(0, 10):
            id = self.generate_random_id()
            surname = ['Dan', 'Pop', 'Marcus', 'George', 'Farcau', 'Molnar', 'Vancea', 'Pintea', 'Nistor']  # 9 terms
            names = ['Sergiu', 'George', 'Raul', 'Catalin', 'Marian', 'Raluca', 'Andrei', 'Mircea', 'Alex',                       'Victor']  # 10
            groups = ['911', '912', '913', '914', '915', '916', '917']  # 7 terms
            rand_names = surname[random.randint(0,8)] + " " + names[random.randint(0,9)]
            rand_groups = groups[random.randint(0,6)]
            student = Student(id, rand_names, rand_groups)
            self.llist_s.student_list_service.add_student_to_list(student)


    def generate_random_assignment(self):
        for i in range(0, 10):
            id = self.generate_rand_ass_id()
            description = ['Homework with classes', 'Preparation for the written exam',' Project for passing the class','Optional Homework','Individual Exercises', 'Mandatory Homework', 'Final grade project', 'Bonus points project','Erasmus interview project']
            deadline = ['2020-10-10','2020-11-16','2020-08-12','2021-12-25','2020-11-19','2021-02-01','2021-01-10','2021-07-23','2021-05-18','2021-03-29']
            rand_desc = description[random.randint(0,8)]
            rand_dead = deadline[random.randint(0,9)]
            assignment = Assignment(id, rand_desc, rand_dead)
            self.llist_a.list_of_assignments.add_assingment_to_list(assignment)


    def generate_random_grades(self):
        grades = [None,'1','2','3','4','5','6','7','8','9','10']
        i = 0
        while i < 100:
            done = False

            random_stud_id = random.randint(0, len(self.llist_s) - 1)
            random_assign_id = random.randint(0, len(self.llist_a) - 1)
            if len(self._grades_list) > 0:
                for grade in self._grades_list:
                    if grade.student_id == self.llist_s.student_list_service[random_stud_id].student_id and grade.assignment_ID == self.llist_a.list_of_assignments[random_assign_id].assignment_ID:
                        done = True
                        break
            if done == False:
                rand_grade_index = random.randint(0,10)
                grade = Grade(self.llist_s.student_list_service[random_stud_id].student_id, self.llist_a.list_of_assignments[random_assign_id].assignment_ID, grades[rand_grade_index])
                i += 1
                self._grades_list.grade_list.add_grade(grade)


class UImenus:
    @staticmethod
    def print_menu():
        print("1. -> Students operations.")
        print("2. -> Assignment operations.")
        print("3. -> Grade operations.")
        print("4. -> Statistics operations.")
        print("5. -> Undo last operation.")
        print("6. -> Redo last operation.")
        print("0. -> exit the program.")
        print("\n")
    @staticmethod
    def print_students():
        print("1.1 -> add student.")
        print("1.2 -> remove student.")
        print("1.3 -> update student.")
        print("1.4 -> list all students.")
        print("0.  -> back\n")
    @staticmethod
    def print_assignments():
        print("2.1 -> add assignment.")
        print("2.2 -> remove assigment.")
        print("2.3 -> update assignment.")
        print("2.4 -> list all assignments.")
        print("0.  -> back\n")
    @staticmethod
    def print_grades():
        print("3.1 -> give an assignment to a student/group.")
        print("3.2 -> grade an assignment given to a student.")
        print("3.3 -> list all given assignments.")
        print("0.  -> back\n")
    @staticmethod
    def print_statistics():
        print("4.1 -> create statistics for a given assignment.")
        print("4.2 -> create statistics for late handling.")
        print("4.3 -> create statistics for best students.")
        print("0.  -> back\n")

class UI(UImenus):
    def __init__(self,student_service, assignment_service, grade_service, undo_service):
        self._student_list = student_service
        self._assignment_list = assignment_service
        self._graded_list = grade_service
        self._undo_service = undo_service



    @property
    def student_list(self):
        return self._student_list
    @property
    def grade_list(self):
        return self._graded_list
    @property
    def assignments_list(self):
        return self._assignment_list

    """
    these functions are organising the menu and it makes very readable
    """
    def Student_functionalities(self):
        done = False
        command_dict = {'1.1':self.add_student_ui,'1.2':self.remove_student_ui,'1.3':self.update_student_ui,'1.4':self.list_student_ui}
        while not done:
            UI.print_students()
            operation = input("Enter the operation: ").strip().lower()
            if operation in command_dict:
                command_dict[operation]()
            elif operation == '0':
                done = True
                print("Back...\n")
            else: print("Bad command entered.")
    def Assignment_functionalities(self):
        done = False
        command_dict = {'2.1':self.add_assignment_ui,'2.2':self.remove_assignment_ui,'2.3':self.update_assignment_ui,'2.4':self.list_assignments_ui}
        while not done:
            UI.print_assignments()
            operation = input("Enter the operation: ").strip().lower()
            if operation in command_dict:
                command_dict[operation]()
            elif operation == '0':
                done = True
                print("Back...\n")
            else: print("Bad command entered.")
    def Grade_functionalities(self):
        done = False
        command_dict = {'3.1':self.give_an_assignment_ui,'3.2':self.grade_an_assignment_ui,'3.3':self.list_grades_ui}
        while not done:
            UI.print_grades()
            operation = input("Enter the operation: ").strip().lower()
            if operation in command_dict:
                command_dict[operation]()
            elif operation == '0':
                done = True
                print("Back...\n")
            else: print("Bad command entered.")
    def Statistic_functionalities(self):
        done = False
        command_dict = {'4.1':self.create_statistics_for_a_given_assignment,'4.2':self.create_statistics_for_late_handlings,'4.3':self.create_statistics_for_best_students}
        while not done:
            UI.print_statistics()
            operation = input("Enter the operation: ").strip().lower()
            if operation in command_dict:
                command_dict[operation]()
            elif operation == '0':
                done = True
                print("Back...\n")
            else: print("Bad command entered.")

    def add_student_ui(self):
        id = input("Enter student id: ").strip()
        surname = input("Enter surname: ").strip()
        name = input("Enter name: ").strip()
        group = input("Enter group: ").strip()
        name = surname + " " + name
        self.student_list.add_student(id, name, group)
        print("Adding...\n")

    def add_assignment_ui(self):
        id = input("Enter the assigment id: ").strip()
        description = input("Enter the assignment description: ").strip()
        deadline = input("Enter the assignment deadline(YYYY-MM-DD): ").strip()
        self.assignments_list.add_assignment(id, description, deadline)
        print("Adding...\n")

    def remove_student_ui(self):
        id = input("Enter the student id: ")
        self.student_list.remove_student(id)
        print("Removing...\n")

    def remove_assignment_ui(self):
        id = input("Enter the id of the assignment you want to delete: ")
        self.assignments_list.remove_assignment(id)
        print("Removing...\n")

    def update_student_ui(self):
        id = input("Enter the student id: ")
        group = input("Enter the new group: ")
        self.student_list.update_student(id,group)
        print("Updating...\n")

    def update_assignment_ui(self):
        id = input("Enter the id of the assignment you want to update: ")
        dead = input("Enter the new deadline: ")
        self.assignments_list.update_assignment(id, dead)
        print("Updating...\n")

    def list_student_ui(self):
        if len(self.student_list) == 0:
            raise UIException("There are no students!...\n")
        for student in self.student_list:
            student_info = str(student) + " Assignments: "
            number_of_assingments = 0
            for grade in self.grade_list:
                if grade.student_id == student.student_id:
                    number_of_assingments += 1
                    student_info += (str(grade.assignment_ID) + "; ")

            if number_of_assingments == 0:
                student_info += "None"
            print(student_info)
        print("\n")

    def list_assignments_ui(self):
        if len(self.assignments_list) == 0:
            raise UIException("There are no assignment!...\n")
        for assignment in self.assignments_list:
            print(str(assignment))
        print("\n")

    def list_grades_ui(self):
        if len(self.grade_list) == 0:
            raise UIException("There are no grades!...\n")
        for grade in self.grade_list:
            print(str(grade))
        print("\n")

    def give_an_assignment_ui(self):
        condition = input("Enter student/group whom/where you want to assign: ").lower().strip()
        if condition == 'student':
            student_id = input("Enter the student id: ").strip()
            assignmentID = input("Enter the assignment id: ").strip()
            if not student_id.isdigit() or not assignmentID.isdigit():
                raise UIException("Invalid student/assignment id!...\n")

            self.grade_list.give_assignment( student_id, assignmentID)

            print("Assigning...\n")
        elif condition == 'group':
            group = input("Enter the group: ").strip()
            if group not in ['911', '912', '913', '914', '915', '916', '917']:
                raise UIException("Invalid group entered!...\n")
            assignmentID = input("Enter the assignment id: ").strip()
            if not assignmentID.isdigit():
                raise UIException("Invalid ID for assignment!...\n")

            self.grade_list.give_assignment_to_group(group, assignmentID)
            print("Assigning...\n")
        else:
            raise UIException("Invalid command for the assign command!...\n")

    def create_statistics_for_a_given_assignment(self):
        assignment_id = input("Enter the assignment id: ").lower().strip()
        ordered_list = self.grade_list.create_statistics_for_a_assignment(assignment_id)

        for student in ordered_list:
            print(str(student))
        print("\n")
    def create_statistics_for_late_handlings(self):
        late_students = self.grade_list.create_statistics_for_latet()
        print("The late students are: ")
        for student in late_students:
            print(str(student))
        print("\n")

    def create_statistics_for_best_students(self):
        best_students = self.grade_list.create_statistics_for_best()
        print("The best students are:")
        for student in best_students:
            print(str(student))
        print("\n")


    def grade_an_assignment_ui(self):
        student_id = input("Enter the id of the student whom you want to grade: ").strip().lower()
        # list all the assignments for this person
        # the valid assigmnets // valid assignments means that there exist a grade, and its value is None
        list_assignments_available = self.grade_list.return_list_assignments(student_id)
        print("The availaible assignments to grade for this student are:")
        for element in list_assignments_available:
            print("\tAssignment ID: " + str(element))

        assignment_id = input("Enter the id of the assignment you want to grade: ").strip().lower()
        student_grade = input("Enter the grade of the student's work: ").strip().lower()
        self.grade_list.add_grade(student_id, assignment_id, student_grade)
        print("Grading...\n")

    def undo_operation_ui(self):
        self._undo_service.undo()
        print("Undoing...\n")

    def redo_operation_ui(self):
        self._undo_service.redo()
        print("Redoing...\n")


    def start(self):
        done = False
        command_dict = {
            '1':self.Student_functionalities,
            '2':self.Assignment_functionalities,
            '3':self.Grade_functionalities,
            '4':self.Statistic_functionalities,
            '5':self.undo_operation_ui,
            '6':self.redo_operation_ui
        }
        while not done:
            UI.print_menu()
            command = input("Enter command> ")
            command = command.strip()
            try:
                if command in command_dict:
                    command_dict[command]()
                elif command == '0':
                    print("Exiting...")
                    done = True
                else :
                    print("Bad command entered.\n")
            except studentRepoException as ve:
                print(str(ve)+"\n")
            except studentException as ve:
                print(str(ve)+ "\n")
            except studentServiceException as ve:
                print(str(ve)+ "\n")
            except assignmentServiceException as ve:
                print(str(ve)+ "\n")
            except UIException as ve:
                print(str(ve) + "\n")
            except GradeExceptions as ve:
                print(str(ve)+'\n')
            except AssignmentException as ve:
                print(str(ve)+'\n')
            except gradeServiceException as ve:
                print(str(ve)+'\n')
            except UndoServiceError as ve:
                print(str(ve) + '\n')
            except AttributeError as ve:
                print(str(ve))
