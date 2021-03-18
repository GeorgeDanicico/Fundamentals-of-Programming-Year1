from tkinter import *
from tkinter import messagebox


#TODO AFTERR THE GUI IS FINISHED, FIX THE MOMENT WHEN A BUTTON IS CLICKED, MAKING THE STATE OF THE OTHER FALSE
class GUI:
    def __init__(self,student_service, assignment_service, grade_service, undo_service):
        self._student_service = student_service
        self._assignment_service = assignment_service
        self._grade_service = grade_service
        self._undo_service = undo_service

        self.tk = Tk()
        self.frame = None
        self.panelbuttons = None
        self.panelinputdata = None

    def start(self):
        self.tk.title("Student Lab Assignments")

        frame = Frame(self.tk, bd = 4)
        frame.pack()
        self.frame = frame
        self.tk.iconbitmap('C:/Users/georg/OneDrive/Desktop/Informatica/Facultate/a678-912-Danicico-George/icon.ico')
        #self.tk.geometry("600x100")
        #TODO SIZES FOR IMPLEMENTATION

        self.buttonstudents = Button(frame, text="Student Operations", command=self._show_students_functionalities, activebackground= "grey", padx=5,pady=10)
        self.buttonstudents.grid(row= 1, column = 0)

        self.buttonAssignment = Button(frame, text="Assignment Operations", command = self._show_assignments_functionalities, activebackground= "grey",padx=5,pady=10)
        self.buttonAssignment.grid(row= 1, column = 1)

        self.buttonGrades = Button(frame, text="Grade Operations",command= self._show_grades_functionalities, activebackground= "grey",padx=5,pady=10)
        self.buttonGrades.grid(row= 1, column = 2)

        self.buttonStatistic = Button(frame, text="Statisics Operations",command= self._show_Statistic_functionalities, activebackground= "grey",padx=5,pady=10)
        self.buttonStatistic.grid(row= 1, column = 3)

        self.buttonUndo = Button(frame, text="Undo ", command= self._undo_operation,activebackground= "grey",padx=5,pady=10)
        self.buttonUndo.grid(row= 1, column = 4)

        self.buttonRedo = Button(frame, text="Redo ", command= self._redo_operation,activebackground= "grey",padx=5,pady=10)
        self.buttonRedo.grid(row= 1, column = 5)
        self.tk.mainloop()

    def _deleteall(self):
        """
        this is the function for deletinng the panel
        """
        #TODO DO A TRY EXCEPT
        try:
            for widget in self.panelinputdata.winfo_children():
                widget.destroy()
            self.panelinputdata.pack_forget()
            self.panelinputdata = None
            self.buttonaction1["state"] = NORMAL
            self.buttonaction2["state"] = NORMAL
            self.buttonaction3["state"] = NORMAL
            try:
                self.buttonaction4["state"] = NORMAL
            except Exception:
                pass




        except Exception:
            for widget in self.panelbuttons.winfo_children():
                widget.destroy()
            self.panelbuttons.pack_forget()
            self.panelbuttons = None

            self.buttonstudents["state"] = NORMAL
            self.buttonAssignment["state"] = NORMAL
            self.buttonGrades["state"] = NORMAL
            self.buttonStatistic["state"] = NORMAL
            self.buttonUndo["state"] = NORMAL
            self.buttonRedo["state"] = NORMAL

    """
    FUNCTIONS THAT WORK WITH STUDENTS!!!!
    """

    def _show_students_functionalities(self):
        self.buttonstudents["state"] = DISABLED
        self.buttonAssignment["state"] = DISABLED
        self.buttonGrades["state"] = DISABLED
        self.buttonStatistic["state"] = DISABLED
        self.buttonUndo["state"] = DISABLED
        self.buttonRedo["state"] = DISABLED

        frame = self.frame
        panel1 = PanedWindow(bd= 4,bg= "white", height= 300, width= 300)
        panel1.pack()
        self.panelbuttons = panel1
        self.buttonaction1 = Button(panel1, text= "Add student", command= self._addstudent_interface)
        self.buttonaction1.grid(row= 4, column = 0)
        self.buttonaction2 = Button(panel1, text= "Remove student", command= self._removestudent_interface)
        self.buttonaction2.grid(row= 4, column = 1)
        self.buttonaction3 = Button(panel1, text="Update student", command=self._updatestudent_interface)
        self.buttonaction3.grid(row=4, column=2)
        self.buttonaction4 = Button(panel1, text="List all students", command=self._listStudData)
        self.buttonaction4.grid(row=4, column=3)
        buttonBack = Button(panel1, text= "Back",command=self._deleteall)
        buttonBack.grid(row= 4, column = 4)

    def _addstudent_interface(self):
        self.buttonaction1["state"] = DISABLED
        self.buttonaction2["state"] = DISABLED
        self.buttonaction3["state"] = DISABLED
        self.buttonaction4["state"] = DISABLED

        """
        this function creates the interface for student add
        """
        panel = PanedWindow(bd= 4, height= 300, width= 300)
        panel.pack()
        self.panelinputdata = panel
        label_studid= Label(panel,text= "Student ID")
        label_studid.grid(row=5,column= 0)
        label_studname= Label(panel,text= "Student Name")
        label_studname.grid(row=5,column= 2)
        label_studgroup= Label(panel,text= "Student Group")
        label_studgroup.grid(row=5,column= 4)

        self.studid = Entry(panel)
        self.studid.grid(row=6, column= 0)
        self.studname= Entry(panel)
        self.studname.grid(row=6, column = 2)
        self.studgroup = Entry(panel)
        self.studgroup.grid(row=6,column = 4)

        add_student_data = Button(panel,text="Add",command=self._addStudData)
        add_student_data.grid(row=7,column = 0)
    def _addStudData(self):
        try:
            student_id = self.studid.get()
            student_name = self.studname.get()
            student_group = self.studgroup.get()
            self._student_service.add_student(student_id, student_name, student_group)
            messagebox.showinfo("Succesful", "Student added succesfully")
        except Exception as ve:
            messagebox.showinfo("Error", "Something wrong occured!")


    def _removestudent_interface(self):
        """Function create the interface for delete"""
        self.buttonaction1["state"] = DISABLED
        self.buttonaction2["state"] = DISABLED
        self.buttonaction3["state"] = DISABLED
        self.buttonaction4["state"] = DISABLED

        panel = PanedWindow(bd=4, height=300, width=300)
        panel.pack()
        self.panelinputdata = panel
        label_studid = Label(panel, text="Student ID")
        label_studid.grid(row=5, column=0)
        self.studid = Entry(panel)
        self.studid.grid(row=6, column=0)

        remove_student_data = Button(panel, text="Remove", command=self._removeStudData)
        remove_student_data.grid(row=7, column=0)

    def _removeStudData(self):
        try:
            student_id = self.studid.get()
            self._student_service.remove_student(student_id)
            messagebox.showinfo("Succesful", "Student removed succesfully")
        except Exception as ve:
            messagebox.showinfo("Error", "Something wrong occured!")

    def _updatestudent_interface(self):
        self.buttonaction1["state"] = DISABLED
        self.buttonaction2["state"] = DISABLED
        self.buttonaction3["state"] = DISABLED
        self.buttonaction4["state"] = DISABLED

        panel = PanedWindow(bd=4, height=300, width=300)
        panel.pack()
        self.panelinputdata = panel
        label_studid = Label(panel, text="Student ID")
        label_studid.grid(row=5, column=0)

        label_group = Label(panel,text= "New Group")
        label_group.grid(row=5, column=2)

        self.studid = Entry(panel)
        self.studid.grid(row=6, column=0)
        self.newgroup = Entry(panel)
        self.newgroup.grid(row=6,column=2)

        update_student_data = Button(panel, text="Update", command=self._updateStudData)
        update_student_data.grid(row=7, column=0)

    def _updateStudData(self):
        try:
            student_id = self.studid.get()
            group = self.newgroup.get()
            self._student_service.update_student(student_id, group)
            messagebox.showinfo("Succesful", "Student updated succesfully")
        except Exception as ve:
            messagebox.showinfo("Error", "Something wrong occured!")
    #TODO THINK OF A WAY TO REPRESENT THE LIST OF STUDENTS
    def _listStudData(self):
        try:
            self.buttonaction1["state"] = DISABLED
            self.buttonaction2["state"] = DISABLED
            self.buttonaction3["state"] = DISABLED
            self.buttonaction4["state"] = DISABLED

            panel = PanedWindow(bd=4)
            panel.pack()
            self.panelinputdata = panel
            label_studid = Label(panel, text="Student ID")
            label_studid.grid(row=5, column=0)
            label_studname = Label(panel, text="Student Name")
            label_studname.grid(row=5, column=1)
            label_studgroup = Label(panel, text="Student Group")
            label_studgroup.grid(row=5, column=2)

            students_number = 0
            row_index = 6
            for student in self._student_service:
                new_studid = Label(panel, text=student.student_id)
                new_studname = Label(panel, text=student.student_name)
                new_studgroup = Label(panel, text=student.student_group)

                new_studid.grid(row = row_index, column=0)
                new_studname.grid(row = row_index, column = 1)
                new_studgroup.grid(row= row_index, column = 2)

                students_number += 1
                row_index += 1

            if students_number == 0:
                raise Exception("There are no students!")

        except Exception as ve:
            messagebox.showinfo("Error", str(ve))



    """ 
    FUNCTIONSS THAT WORK WITH THE ASSIGNMENTS!!!!
    """
    def _show_assignments_functionalities(self):
        self.buttonstudents["state"] = DISABLED
        self.buttonAssignment["state"] = DISABLED
        self.buttonGrades["state"] = DISABLED
        self.buttonStatistic["state"] = DISABLED
        self.buttonUndo["state"] = DISABLED
        self.buttonRedo["state"] = DISABLED

        frame = self.frame
        panel1 = PanedWindow(bd= 4,bg= "white", height= 300, width= 300)
        panel1.pack()
        self.panelbuttons = panel1
        self.buttonaction1 = Button(panel1, text= "Add assignment", command= self._addassignment_interface)
        self.buttonaction1.grid(row= 4, column = 0)
        self.buttonaction2 = Button(panel1, text= "Remove assignment", command= self._removeassignment_interface)
        self.buttonaction2.grid(row= 4, column = 2)
        self.buttonaction3 = Button(panel1, text="Update assignment", command=self._updateassignment_interface)
        self.buttonaction3.grid(row=4, column=4)
        self.buttonaction4 = Button(panel1, text="List all assignments", command=self._listAssignData)
        self.buttonaction4.grid(row=4, column=6)
        buttonBack = Button(panel1, text= "Back",command=self._deleteall)
        buttonBack.grid(row= 4, column = 8)

    def _addassignment_interface(self):
        """
        this function creates the interface for student add
        """
        self.buttonaction1["state"] = DISABLED
        self.buttonaction2["state"] = DISABLED
        self.buttonaction3["state"] = DISABLED
        self.buttonaction4["state"] = DISABLED

        panel = PanedWindow(bd= 4, height= 300, width= 300)
        panel.pack()
        self.panelinputdata = panel
        label_assignmentid= Label(panel,text= "Assignment ID")
        label_assignmentid.grid(row=5,column= 0)
        label_assignmentdesc= Label(panel,text= "Description")
        label_assignmentdesc.grid(row=5,column= 2)
        label_assignmentdead= Label(panel,text= "Deadline")
        label_assignmentdead.grid(row=5,column= 4)

        self.assignmentid = Entry(panel)
        self.assignmentid.grid(row=6, column= 0)
        self.assignmentdesc= Entry(panel)
        self.assignmentdesc.grid(row=6, column = 2)
        self.assignmentdead = Entry(panel)
        self.assignmentdead.grid(row=6,column = 4)

        add_assign_data = Button(panel,text="Add",command=self._addAssignData)
        add_assign_data.grid(row=7,column = 0)
    def _addAssignData(self):
        try:
            assign_id = self.assignmentid.get()
            assign_desc = self.assignmentdesc.get()
            assign_dead = self.assignmentdead.get()
            self._assignment_service.add_assignment(assign_id, assign_desc, assign_dead)
            messagebox.showinfo("Succesful", "Assignment added succesfully")
        except Exception as ve:
            messagebox.showinfo("Error", "Something wrong occured!")

    def _removeassignment_interface(self):
        """Function create the interface for delete"""
        self.buttonaction1["state"] = DISABLED
        self.buttonaction2["state"] = DISABLED
        self.buttonaction3["state"] = DISABLED
        self.buttonaction4["state"] = DISABLED

        panel = PanedWindow(bd=4, height=300, width=300)
        panel.pack()
        self.panelinputdata = panel
        label_assignmentid = Label(panel, text="Assignment ID")
        label_assignmentid.grid(row=5, column=0)
        self.assignmentid = Entry(panel)
        self.assignmentid.grid(row=6, column=0)

        remove_assignment_data = Button(panel, text="Remove", command=self._removeAssignData)
        remove_assignment_data.grid(row=7, column=0)

    def _removeAssignData(self):
        try:
            assign_id = self.assignmentid.get()
            self._assignment_service.remove_assignment(assign_id)
            messagebox.showinfo("Succesful", "Assignment removed succesfully")
        except Exception as ve:
            messagebox.showinfo("Error", "Something wrong occured!")

    def _updateassignment_interface(self):
        self.buttonaction1["state"] = DISABLED
        self.buttonaction2["state"] = DISABLED
        self.buttonaction3["state"] = DISABLED
        self.buttonaction4["state"] = DISABLED

        panel = PanedWindow(bd=4, height=300, width=300)
        panel.pack()
        self.panelinputdata = panel
        label_assignmentid = Label(panel, text="Assignment ID")
        label_assignmentid.grid(row=5, column=0)

        label_deadline = Label(panel,text= "New Deadline")
        label_deadline.grid(row=5, column=2)

        self.assignmentid = Entry(panel)
        self.assignmentid.grid(row=6, column=0)
        self.new_deadline = Entry(panel)
        self.new_deadline.grid(row=6,column=2)

        update_assignment_data = Button(panel, text="Update", command=self._updateAssignData)
        update_assignment_data.grid(row=7, column=0)

    def _updateAssignData(self):
        try:
            assign_id = self.assignmentid.get()
            new_dead = self.new_deadline.get()
            self._assignment_service.update_assignment(assign_id, new_dead)
            messagebox.showinfo("Succesful", "Assignment updated succesfully")
        except Exception as ve:
            messagebox.showinfo("Error", "Something wrong occured!")
    #TODO THINK OF A WAY TO REPRESENT THE LIST OF ASSIGMNETS
    def _listAssignData(self):
        try:
            self.buttonaction1["state"] = DISABLED
            self.buttonaction2["state"] = DISABLED
            self.buttonaction3["state"] = DISABLED
            self.buttonaction4["state"] = DISABLED

            panel = PanedWindow(bd=4, height=300, width=300)
            panel.pack()
            self.panelinputdata = panel
            label_assignid = Label(panel, text="Assignment ID")
            label_assignid.grid(row=5, column=0)
            label_assigndesc = Label(panel, text="Description")
            label_assigndesc.grid(row=5, column=1)
            label_assigndead = Label(panel, text="Deadline")
            label_assigndead.grid(row=5, column=2)

            assignment_number = 0
            row_index = 6
            for assignment in self._assignment_service:
                new_assignid = Label(panel, text=assignment.assignment_ID)
                new_desc = Label(panel, text=assignment.description)
                new_assigngroup = Label(panel, text=assignment.Deadline)

                new_assignid.grid(row=row_index, column=0)
                new_desc.grid(row=row_index, column=1)
                new_assigngroup.grid(row=row_index, column=2)

                assignment_number += 1
                row_index += 1

            if assignment_number == 0:
                raise Exception("There are no assignments!")

        except Exception as ve:
            messagebox.showinfo("Error", str(ve))

    """ 
        FUNCTIONSS THAT WORK WITH THE ASSIGNMENTS!!!!
        """

    def _show_grades_functionalities(self):
        self.buttonstudents["state"] = DISABLED
        self.buttonAssignment["state"] = DISABLED
        self.buttonGrades["state"] = DISABLED
        self.buttonStatistic["state"] = DISABLED
        self.buttonUndo["state"] = DISABLED
        self.buttonRedo["state"] = DISABLED

        panel1 = PanedWindow(bd=4, bg="white", height=300, width=300)
        panel1.pack()
        self.panelbuttons = panel1
        self.buttonaction1 = Button(panel1, text="Give assignment", command=self._giveGrade_interface)
        self.buttonaction1.grid(row=4, column=0)
        self.buttonaction2 = Button(panel1, text="Grade assignment", command=self._gradeAssignment_interface)
        self.buttonaction2.grid(row=4, column=2)
        self.buttonaction3 = Button(panel1, text="List all grades", command=self._listGradeData)
        self.buttonaction3.grid(row=4, column=6)
        buttonBack = Button(panel1, text="Back", command=self._deleteall)
        buttonBack.grid(row=4, column=8)

    def _giveGrade_interface(self):
        """
        this function creates the interface for student add
        """
        self.buttonaction1["state"] = DISABLED
        self.buttonaction2["state"] = DISABLED
        self.buttonaction3["state"] = DISABLED

        panel = PanedWindow(bd=4, height=300, width=300)
        panel.pack()
        self.panelinputdata = panel
        label_condition = Label(panel, text="Give to:")
        label_condition.grid(row=5, column=0)
        label_studentorGroup = Label(panel, text="Student ID/Group")
        label_studentorGroup.grid(row=5, column=2)
        label_assignmentid = Label(panel, text="Assignment_ID")
        label_assignmentid.grid(row=5, column=4)

        self.condition = Entry(panel)
        self.condition.grid(row=6, column=0)
        self.studentorGroup = Entry(panel)
        self.studentorGroup.grid(row=6, column=2)
        self.assignmentid = Entry(panel)
        self.assignmentid.grid(row=6, column=4)

        give_assign_data = Button(panel, text="Give", command=self._giveAssignData)
        give_assign_data.grid(row=7, column=0)

    def _giveAssignData(self):
        try:
            if self.condition.get() == "student":
                self._grade_service.give_assignment(self.studentorGroup.get(), self.assignmentid.get())
            elif self.condition.get() == "group":
                self._grade_service.give_assignment_to_group(self.studentorGroup.get(), self.assignmentid.get())
            else:
                raise Exception("Invalid giving...")

            messagebox.showinfo("Succesful", "Assigned succesfully")
        except Exception as ve:
            messagebox.showinfo("Error",str(ve))

    def _gradeAssignment_interface(self):
        """Function create the interface for delete"""
        self.buttonaction1["state"] = DISABLED
        self.buttonaction2["state"] = DISABLED
        self.buttonaction3["state"] = DISABLED

        panel = PanedWindow(bd=4, height=300, width=300)
        panel.pack()
        self.panelinputdata = panel
        label_Studentid = Label(panel, text="Student ID")
        label_Studentid.grid(row=5, column=0)
        label_assignmentid = Label(panel, text="Assignment ID")
        label_assignmentid.grid(row=5, column=1)
        label_grade = Label(panel, text="Grade")
        label_grade.grid(row=5, column=2)
        self.Studentid = Entry(panel)
        self.Studentid.grid(row=6, column=0)
        self.assignmentid = Entry(panel)
        self.assignmentid.grid(row=6, column=1)
        self.grade = Entry(panel)
        self.grade.grid(row=6, column=2)


        grade_assignment_data = Button(panel, text="Grade", command=self._gradeAssignData)
        grade_assignment_data.grid(row=7, column=0)

    def _gradeAssignData(self):
        try:
            self._grade_service.add_object(self.Studentid.get(), self.assignmentid.get(), self.grade.get())
            messagebox.showinfo("Succesful", "Graded succesfully")
        except Exception as ve:
            messagebox.showinfo("Error", str(ve))

    # TODO THINK OF A WAY TO REPRESENT THE LIST OF Grades
    def _listGradeData(self):
        try:
            self.buttonaction1["state"] = DISABLED
            self.buttonaction2["state"] = DISABLED
            self.buttonaction3["state"] = DISABLED

            panel = PanedWindow(bd=4, height=200, width=200)
            panel.pack()
            self.panelinputdata = panel

            canvas = Canvas(panel)
            scrollbar = Scrollbar(panel, orient="vertical", command=canvas.yview)
            scrollable_frame = Frame(canvas)

            scrollable_frame.bind(
                "<Configure>",
                lambda e: canvas.configure(
                    scrollregion=canvas.bbox("all")
                )
            )

            canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

            canvas.configure(yscrollcommand=scrollbar.set)
            text = "Student ID".ljust(3) + "   Assignment ID".ljust(3) + "   Grade"
            label_studid = Label(panel, text=text)
            label_studid.pack()


            grade_number = 0
            for grade in self._grade_service:
                text = "                                   " +str(grade.student_id) +"               "+  str(grade.assignment_ID) + "                    "+ str(grade.grade_value)
                Label(scrollable_frame, text=text).pack()
                grade_number += 1

            canvas.pack(side="left", fill="both", expand=True)
            scrollbar.pack(side="right", fill="y")

            if grade_number == 0:
                raise Exception("There are no grades!")

        except Exception as ve:
            messagebox.showinfo("Error", str(ve))

    """
    Functions that work with the statistic Functionalities
    """
    def _show_Statistic_functionalities(self):
        self.buttonstudents["state"] = DISABLED
        self.buttonAssignment["state"] = DISABLED
        self.buttonGrades["state"] = DISABLED
        self.buttonStatistic["state"] = DISABLED
        self.buttonUndo["state"] = DISABLED
        self.buttonRedo["state"] = DISABLED

        panel1 = PanedWindow(bd=4, bg="white", height=300, width=300)
        panel1.pack()
        self.panelbuttons = panel1
        self.buttonaction1 = Button(panel1, text="Stats for an assignment", command=self._statistics_for_a_given_assignment_interface)
        self.buttonaction1.grid(row=4, column=0)
        self.buttonaction2 = Button(panel1, text="Stats for late students", command=self._statistics_for_late_handlings_interface)
        self.buttonaction2.grid(row=4, column=2)
        self.buttonaction3 = Button(panel1, text="Stats for best students", command=self._statistics_for_best_students_interface)
        self.buttonaction3.grid(row=4, column=6)
        buttonBack = Button(panel1, text="Back", command=self._deleteall)
        buttonBack.grid(row=4, column=8)

    def _statistics_for_a_given_assignment_interface(self):
        """
        this function creates the interface for student add
        """
        self.buttonaction1["state"] = DISABLED
        self.buttonaction2["state"] = DISABLED
        self.buttonaction3["state"] = DISABLED

        panel = PanedWindow(bd= 4, height= 300, width= 300)
        panel.pack()
        self.panelinputdata = panel
        label_assignmentid= Label(panel,text= "Assignment ID")
        label_assignmentid.grid(row=5,column= 0)

        self.assignmentid = Entry(panel)
        self.assignmentid.grid(row=6, column= 0)

        show_assign_data = Button(panel,text="Show",command=self._addStatsForAssignmentData)
        show_assign_data.grid(row=7,column = 0)
    def _addStatsForAssignmentData(self):
        try:
            normal_students = self._grade_service.create_statistics_for_a_assignment(self.assignmentid.get())
            panel1 = self.panelinputdata
            panel = PanedWindow(panel1,bd=4, height=300, width=300)
            panel.grid()
            label_studid = Label(panel, text="Student ID")
            label_studid.grid(row=5, column=0)
            label_studname = Label(panel, text="Student Name")
            label_studname.grid(row=5, column=1)
            label_studgroup = Label(panel, text="Student Group")
            label_studgroup.grid(row=5, column=2)
            label_grade = Label(panel, text= "Grade")
            label_grade.grid(row=5, column = 3)


            students_number = 0
            row_index = 6
            for student in normal_students:
                new_studid = Label(panel, text=student.student.student_id)
                new_studname = Label(panel, text=student.student.student_name)
                new_studgroup = Label(panel, text=student.student.student_group)
                new_grade = Label(panel, text=student.grade)

                new_studid.grid(row=row_index, column=0)
                new_studname.grid(row=row_index, column=1)
                new_studgroup.grid(row=row_index, column=2)
                new_grade.grid(row= row_index, column= 3)

                students_number += 1
                row_index += 1

            if students_number == 0:
                raise Exception("There are no students with that assignment!")

        except Exception as ve:
            messagebox.showinfo("Error", str(ve))

    def _statistics_for_late_handlings_interface(self):
        """Function create the interface for delete"""
        try:
            self.buttonaction1["state"] = DISABLED
            self.buttonaction2["state"] = DISABLED
            self.buttonaction3["state"] = DISABLED

            late_students = self._grade_service.create_statistics_for_latet()
            panel = PanedWindow(bd=4, height=300, width=300)
            panel.pack()
            self.panelinputdata = panel
            label_studid = Label(panel, text="Student ID")
            label_studid.grid(row=5, column=0)
            label_studname = Label(panel, text="Student Name")
            label_studname.grid(row=5, column=1)
            label_studgroup = Label(panel, text="Student Group")
            label_studgroup.grid(row=5, column=2)
            label_grade = Label(panel, text="Grade")
            label_grade.grid(row=5, column=3)



            students_number = 0
            row_index = 6
            for student in late_students:
                new_studid = Label(panel, text=student.student.student_id)
                new_studname = Label(panel, text=student.student.student_name)
                new_studgroup = Label(panel, text=student.student.student_group)
                new_grade = Label(panel, text=student.grade)

                new_studid.grid(row=row_index, column=0)
                new_studname.grid(row=row_index, column=1)
                new_studgroup.grid(row=row_index, column=2)
                new_grade.grid(row=row_index, column=3)

                students_number += 1
                row_index += 1

            if students_number == 0:
                raise Exception("There are no late students!")

        except Exception as ve:
            messagebox.showinfo("Error", str(ve))
        #TODO ONLY LISTING
    def _statistics_for_best_students_interface(self):
        try:
            self.buttonaction1["state"] = DISABLED
            self.buttonaction2["state"] = DISABLED
            self.buttonaction3["state"] = DISABLED

            best_students = self._grade_service.create_statistics_for_best()
            panel = PanedWindow(bd=4, height=300, width=300)
            panel.pack()
            self.panelinputdata = panel
            label_studid = Label(panel, text="Student ID")
            label_studid.grid(row=5, column=0)
            label_studname = Label(panel, text="Student Name")
            label_studname.grid(row=5, column=1)
            label_studgroup = Label(panel, text="Student Group")
            label_studgroup.grid(row=5, column=2)
            label_grade = Label(panel, text="Grade")
            label_grade.grid(row=5, column=3)

            students_number = 0
            row_index = 6
            for student in best_students:
                new_studid = Label(panel, text=student.student.student_id)
                new_studname = Label(panel, text=student.student.student_name)
                new_studgroup = Label(panel, text=student.student.student_group)
                new_grade = Label(panel, text=student.grade)

                new_studid.grid(row=row_index, column=0)
                new_studname.grid(row=row_index, column=1)
                new_studgroup.grid(row=row_index, column=2)
                new_grade.grid(row= row_index, column= 3)

                students_number += 1
                row_index += 1

            if students_number == 0:
                raise Exception("There are no late students!")

        except Exception as ve:
            messagebox.showinfo("Error", str(ve))

    def _undo_operation(self):
        try:
            self._undo_service.undo()
        except Exception as ve:
            messagebox.showinfo("Error", str(ve))

    def _redo_operation(self):
        try:
            self._undo_service.redo()
        except Exception as ve:
            messagebox.showinfo("Error", str(ve))

