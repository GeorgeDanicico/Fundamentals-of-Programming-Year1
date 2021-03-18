from console.UI import UI, generateRandom
from domain.assignment import Assignment,Assignment_Validator,AssignmentException,AssignmentValidatorException
from domain.student import Student,Student_Validator,studentException,studentValidatorException
from gui import GUI
from repository.studentRepo import  studentRepo,studentRepoException
from service.studentService import studentService,studentServiceException
from service.assignmentService import assignmentService,assignmentServiceException
from repository.assignmentRepo import assignmentRepo
from domain.grade import Grade,Grade_Validator,GradeExceptions
from repository.gradeRepo import gradeRepo
from service.gradeService import gradeService, gradeServiceException
from service.UndoService import UndoService

student_repo = studentRepo()
assignment_repo = assignmentRepo()
grade_repo = gradeRepo()

student_validator = Student_Validator()
assignment_validator = Assignment_Validator()
grade_validator = Grade_Validator()

undo_service = UndoService()

student_service = studentService(student_repo, grade_repo,student_validator, undo_service)
assignment_service = assignmentService(assignment_repo, grade_repo, assignment_validator, undo_service)
grade_service = gradeService(student_repo, assignment_repo, grade_repo, student_validator, assignment_validator, grade_validator, undo_service)

number = generateRandom(student_service, assignment_service, grade_service)
number.generate_random_student()
number.generate_random_assignment()
number.generate_random_grades()

done = False
while not done:
    mode = input("Enter the UI you want to acces: ").strip().lower()
    if mode not in ['menu','graphical','0']:
        print("Bad command!...")
    elif mode == 'menu':
        print('Loading...\n')
        ui = UI(student_service, assignment_service, grade_service, undo_service)
        ui.start()
        done = True
    elif mode == 'graphical':
        print('Loading...\n')
        gui = GUI(student_service, assignment_service, grade_service, undo_service)
        gui.start()
        done = True
    elif mode == '0':
        print("Exiting...\n")
        done = True

