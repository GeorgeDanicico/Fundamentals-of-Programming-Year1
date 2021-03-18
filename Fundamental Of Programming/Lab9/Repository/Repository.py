from Domain.A10Module import IterableDataStructure
from Domain.student import Student
from Domain.assignment import Assignment
from Domain.grade import Grade

class RepositoryException(Exception):
    def __init__(self, msg):
        self._msg = msg



class Repository:
    def __init__(self):
        self._objects = IterableDataStructure()

    def __getitem__(self, item):
        return self.objects[item]

    def __len__(self):
        return len(self.objects)

    @property
    def objects(self):
        return self._objects

    @objects.setter
    def objects(self, value):
        self._objects = value

    def add_object(self,object):
        """
        We will add an object in the file/memory/database
        :param object:
        """
        self.objects.append(object)

    def remove_object(self,object):
        """
        we will remove an object from the file/memory/database
        """
        self.objects.remove(object)

    def update_object(self, index, value):
        """
        third attribute will be different in each case, student = group, assignment = deadline, grade = grade
        """
        if isinstance(self.objects[index],Student):
            setattr(self.objects[index],"student_group", value)

        if isinstance(self.objects[index],Assignment):
            setattr(self.objects[index],"Deadline", value)

        if isinstance(self.objects[index],Grade):
            setattr(self.objects[index],"grade_value", value)
