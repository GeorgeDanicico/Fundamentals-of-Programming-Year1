from domain.student import Student


class studentRepoException(ValueError):
    def __init__(self, msg):
        self._msg = msg


class studentRepo:
    def __init__(self):
        self.student_list = []

    def __getitem__(self, item):
        return self.student_list[item]

    def __len__(self):
        return len(self.student_list)

    @property
    def student_list(self):
        return self._student_list

    @student_list.setter
    def student_list(self, value):
        self._student_list = value

    def add_student_to_list(self, student):
        """
        we add a student to the list
        :param student: the given student
        :return:
        """
        self.student_list.append(student)
    def remove_student_from_list(self, student):
        """
        we delete a student
        :param student: the student we want to delete
        """
        self.student_list.remove(student)

    def update_student_in_list(self, index, group):
        """
        we update the student we read from console with the new group
        :param index: the index of the student with the given id
        :param group: the new group
        :return:
        """
        self.student_list[index].student_group = group

