from json.decoder import JSONDecodeError

from Domain.assignment import Assignment
from Domain.grade import Grade
from Domain.student import Student
from Repository.Repository import Repository
import json

from Settings.setparams import SetParameters


class JSONFileRepo(Repository):
    def __init__(self, filename):
        super().__init__()
        self._filename = filename
        self._data = {}

        setupParams = SetParameters(filename)
        self._entity, self._atr1, self._atr2, self._atr3 = setupParams.setup_parameters()

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
        self._data[self._entity]=[]
        for obj in self.objects:
            self._data[self._entity].append({
                self._atr1: getattr(obj, self._atr1),
                self._atr2: getattr(obj, self._atr2),
                self._atr3: getattr(obj, self._atr3)
            })


        with open(self._filename, 'w') as outputfile:
            json.dump(self._data, outputfile)
            outputfile.close()

    def _load(self):
        """
        we will load into the memory repos the data from the files
        """


        try:

            file = open(self._filename, "r")
            self._data = json.load(file)
            # we check which file was opened to enter data correctly // we could have done 3 repo's instead of this one
            for item in self._data[self._entity]:
                if self._entity == 'Student':
                    super().add_object(Student(item[self._atr1], item[self._atr2], item[self._atr3]))
                if self._entity == 'Assignment':
                    super().add_object(Assignment(item[self._atr1], item[self._atr2], item[self._atr3]))
                if self._entity == 'Grade':
                    super().add_object(Grade(item[self._atr1], item[self._atr2], item[self._atr3]))
            # file.close()
        except JSONDecodeError:
            self._data[self._entity] = []

            with open(self._filename, 'w') as outfile:
                json.dump(self._data, outfile)
                outfile.close()