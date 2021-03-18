import pickle

from Repository.Repository import Repository


class BinaryFileRepo(Repository):
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
        file = open(self._filename, 'wb')
        pickle.dump(self.objects, file)
        file.close()

    def _load(self):
        try:
            file = open(self._filename, 'rb')
            self.objects = pickle.load(file)
            # file.close()
        except EOFError:
            pass
