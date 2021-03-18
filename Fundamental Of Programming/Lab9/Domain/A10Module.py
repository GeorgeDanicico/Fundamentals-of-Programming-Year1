from Domain.assignment import Assignment_Validator

class IterableDataStructure:
    def __init__(self):
        self._object_list = []

    def append(self, obj):
        self._object_list.append(obj)

    def __len__(self):
        return len(self._object_list)

    def __getitem__(self, item):
        """
        we will get the item with the specified key
        :param key: the key we want to delete
        """
        return self._object_list[item]

    def __setitem__(self, item, value):
        """
        we set for a certain key a new value
        :param
        """
        self._object_list[item] = value

    def __delitem__(self, item):
        """
        we delete a certain term in the dict using the unique key
        """
        self._object_list.remove(item)

    def __next__(self):

        if len(self._object_list) - 1 == self._position:
            raise StopIteration()

        self._position += 1
        return self._object_list[self._position]

    def __iter__(self):
        """
        we will keep in mind that the iterator starts at 0
        """
        self._position = -1
        return self


class FilterAcceptance:
    def __init__(self, grade_repo, assignment_repo, assignment_id=None):
        self._grade_repo = grade_repo
        self._assignment_repo = assignment_repo
        # we will use this in order to save the id for the filter the students by a given assignment
        self._assignment = assignment_id

    def filter_assignment(self, student):
        """
        for the moment, this function will be the filtering type with respect to a certain assignment
        :param student: the student we check
        """
        for grade in self._grade_repo.dictionary_data():
            if grade.student_id == student.student_id and grade.assignment_ID == self._assignment and grade.grade_value is not None:
                return True
        return False

    def filter_late(self, student):
        """
        we filter the late students in this case where the object is a student
        :param student: the student we want to check if he passes all the steps
        """
        date_check = Assignment_Validator()
        for grade in self._grade_repo.dictionary_data():
            if grade.student_id == student.student_id and grade.grade_value is None:
                if date_check.check_if_deadline_passed(self._assignment_repo[grade.assignment_ID].Deadline):
                    return True

        return False

    def filter_best(self, student):
        """

        """
        assignments_counter = 0
        for grade in self._grade_repo.dictionary_data():
            if grade.student_id == student.student_id and grade.grade_value is not None:
                assignments_counter += 1
                if len(self._assignment_repo.dictionary_data()) == assignments_counter:
                    return True
        return False



def FilterMethod(objects_list, filter_type):
    """
    we will filter the given object list accord to the filter_type function which is at the beginning considered an object
    :param objects_list: the list we want to filter
    :param filter_type: the filter function connection we will use to filter the list
    """
    filtered_list = []
    for object in objects_list:
        if filter_type(object):
            filtered_list.append(object)

    return filtered_list

def SortingMethod():
    pass


# d = IterableDataStructure()
# d['123'] = 'adadada'
# d['124'] = 'adadada'
# d['125'] = 'adadada'
#
# del d['123']
# for el in d:
#     print(el)
