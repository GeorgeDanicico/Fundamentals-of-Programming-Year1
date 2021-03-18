from domain.grade import Grade



class gradeRepo:
    def __init__(self):
        self._grades = []
    def __len__(self):
        return len(self.grades)
    def __getitem__(self, item):
        return self.grades[item]
    @property
    def grades(self):
        return self._grades
    def add_grade(self, grade):
        """
        we add a grade to the grades list
        :param grade: the given grade
        """
        self.grades.append(grade)
    def delete_grade(self, grade):
        """
        we delete a grade from the list of grades
        :param grade: the given we want to delete
        """
        # if the student id is none it means that we delete all the grades with a given assignment
        self.grades.remove(grade)



    def update_grade(self, index, new_grade):
        """
        update a grade, grades value with a new grade.
        """
        self.grades[index].grade_value = new_grade

