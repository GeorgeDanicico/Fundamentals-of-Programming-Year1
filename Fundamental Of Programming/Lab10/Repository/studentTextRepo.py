from Repository.Repository import Repository, RepositoryException
from Domain.student import Student

class StudentTextRepo(Repository):
    def __init__(self, filename):
        super().__init__()
        self._filename = filename
        self._load()

    def add_object(self,object):
        super().add_object(object)
        self._save()

    def remove_object(self,object):
        super().remove_object(object)
        self._save()

    def update_object(self, index, value):
        super().update_object(index, value)
        self._save()

    def _save(self):
        try:
            file = open(self._filename, "wt")
            for object in self.objects:
                text = object.student_id + ";" + object.student_name + ";" + object.student_group + "\n"
                file.write(text)
            file.close()
        except FileNotFoundError:
            raise RepositoryException(f"File {self._filename} does not exist!...\n")
        except EOFError:
            pass
        except IOError as ve:
            raise RepositoryException("An error occured - " + str(ve))

    def _load(self):
        """
        We load the data from file
        """
        try:
            file = open(self._filename, 'rt')
            lines = file.readlines()
            file.close()
            for line in lines:
                line = line.split(";")
                super().add_object(Student(line[0], line[1], str(int(line[2]))))
        except FileNotFoundError:
            raise RepositoryException(f"File {self._filename} does not exist!...\n")