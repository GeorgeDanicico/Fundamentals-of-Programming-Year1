from Repository.Repository import Repository
from Domain.assignment import Assignment
import datetime

class AssignmentTextRepo(Repository):
    def __init__(self, filename):
        super().__init__()
        self._filename = filename
        self._load()

    def add_object(self, object):
        super().add_object(object)
        self._save()

    def remove_object(self, object):
        super().remove_object(object)
        self._save()

    def update_object(self, index, value):
        super().update_object(index, value)
        self._save()


    def _save(self):
        file = open(self._filename, "wt")
        for object in self.objects:
            text = object.assignment_ID + ";" + object.description + ";" + object.Deadline + "\n"
            file.write(text)
        file.close()

    def _load(self):
        """
        We load the data from file
        """

        file = open(self._filename, "rt")
        lines = file.readlines()
        file.close()

        for line in lines:
            line = line.split(";")
            current_date = line[2].split("-")
            line[2] = datetime.date(int(current_date[0]), int(current_date[1]), int(current_date[2]))
            super().add_object(Assignment(line[0], line[1], line[2]))