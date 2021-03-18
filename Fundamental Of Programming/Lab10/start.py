from Repository.BinaryFileRepo import BinaryFileRepo
from Repository.DBRepository import DataBaseRepo
from Repository.JSONFileRepo import JSONFileRepo
from UI.UI import UI, generateRandom
from Domain.assignment import Assignment_Validator
from Domain.student import Student_Validator
from UI.gui import GUI
from Service.studentService import studentService
from Service.assignmentService import assignmentService
from Domain.grade import Grade_Validator
from Service.gradeService import gradeService
from Service.UndoService import UndoService
from Repository.Repository import Repository, RepositoryException
from Repository.studentTextRepo import StudentTextRepo
from Repository.assignmentTextRepo import AssignmentTextRepo
from Repository.gradeTextRepo import GradeTextRepo
from Settings.settings import Settings

if __name__ == '__main__':
    filename = "Settings/settings.properties"
    repoSetUp = Settings(filename)
    # we set up the settings class
    student_repo, assignment_repo, grade_repo = None, None, None

    # we prepare the repo by selecting the mode in the settings properties
    # in case there is an error with initializing the repo, than we print a message and exit the program
    # in order to prevent further crashes
    try:
        if repoSetUp.get_mode == "inmemory":
            student_repo = Repository()
            assignment_repo = Repository()
            grade_repo = Repository()
        elif repoSetUp.get_mode == "textfiles":
            student_repo = StudentTextRepo(repoSetUp.get_studentfile)
            assignment_repo = AssignmentTextRepo(repoSetUp.get_assignmentfile)
            grade_repo = GradeTextRepo(repoSetUp.get_gradesfile)
        elif repoSetUp.get_mode == "binaryfiles":
            student_repo = BinaryFileRepo(repoSetUp.get_studentfile)
            assignment_repo = BinaryFileRepo(repoSetUp.get_assignmentfile)
            grade_repo = BinaryFileRepo(repoSetUp.get_gradesfile)
        elif repoSetUp.get_mode == "jsonfiles":
            student_repo = JSONFileRepo(repoSetUp.get_studentfile)
            assignment_repo = JSONFileRepo(repoSetUp.get_assignmentfile)
            grade_repo = JSONFileRepo(repoSetUp.get_gradesfile)
        elif repoSetUp.get_mode == "database":
            student_repo = DataBaseRepo("student")
            assignment_repo = DataBaseRepo("assignment")
            grade_repo = DataBaseRepo("grade")
        else:
            raise RepositoryException("Fatal Warning!... No repository initialized!\n")
    except RepositoryException as ve:
        print(str(ve))
        exit(0)


    # we now initialize the validators and so on
    student_validator = Student_Validator()
    assignment_validator = Assignment_Validator()
    grade_validator = Grade_Validator()

    undo_service = UndoService()

    student_service = studentService(student_repo, grade_repo, student_validator, undo_service)
    assignment_service = assignmentService(assignment_repo, grade_repo, assignment_validator, undo_service)
    grade_service = gradeService(student_repo, assignment_repo, grade_repo, student_validator, assignment_validator, grade_validator, undo_service)

    # we add random data if we use the inmemory storing method
    if repoSetUp.get_mode == "inmemory":
        number = generateRandom(student_service, assignment_service, grade_service)
        number.generate_random_student()
        number.generate_random_assignment()
        number.generate_random_grades()


    if repoSetUp.get_uimode == "gui":
        gui = GUI(student_service, assignment_service, grade_service, undo_service)
        gui.start()
    elif repoSetUp.get_uimode == "menu":
        ui = UI(student_service, assignment_service, grade_service, undo_service)
        ui.start()

"""
repository = inmemory
students = ""
assignments = ""
grades = ""
ui = "gui"

repository = binaryfiles
students = "TextFiles/students.bin"
assignments = "TextFiles/assignments.bin"
grades = "TextFiles/grades.bin"
ui = "gui"

repository = jsonfiles
students = "TextFiles/students.json"
assignments = "TextFiles/assignments.json"
grades = "TextFiles/grades.json"
ui = "gui"

repository = database
students = ""
assignments = ""
grades = ""
ui = "gui"

"""