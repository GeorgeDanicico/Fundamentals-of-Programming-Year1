"""
    Service class includes functionalities for implementing program features
"""
from src.domain.entity import complex
from src.domain.entity import complexException
import copy


#def isFloat(number):
#    try:
#        float(number)
#        return True
#    except ValueError:
#        print("Invalid values for real part and imaginary part\n")
#        return False
class ValidatePosition:
    """
    we used this class in order to check the start and end indexes if they are correct
    """
    def __init__(self, start, end, value):
        self._start = start
        self._end = end
        self._value = value

    @property
    def value(self):
        return self._value

    @property
    def start(self):
        return self._start

    @property
    def end(self):
        return self._end

    def check_positions(self):
        """
        we check if the start/end indexes are integers
        """
        if not self.start.isdigit() or not self.end.isdigit():
            raise complexException("Invalid indexes for start/end positions\n")

        if int(self.start) < 0 or int(self.end) < 0:
            raise complexException("Invalid indexes for start/end positions\n")

        if int(self.start) > int(self.end):
            raise complexException("The first index can't be bigger than the second\n")

        if int(self.start) >= self.value or int(self.end) >= self.value:
            raise complexException("The indexes can't be bigger than the length of the list\n")


class complex_list:
    """
    create a list of complex numbers
    """
    def __init__(self):
        self._complexlist = {'list': [], 'history': []}

    def __len__(self):
        return len(self._complexlist['list'])


    @property
    def list(self):
        return self._complexlist['list']

    @property
    def history(self):
        return self._complexlist['history']


    def update_history(self):
        """
        we make a deep copy in order to update the history with the current list before making changes in data
        :return:
        """
        new_list = copy.deepcopy(self.list)
        self.history.append(new_list)


    def add_complex(self, complex):
        """
        we add the complex number in the list
        :param complex: the complex number who has the time of class complex
        :return: -
        """
        self.list.append(complex)



    def undo(self):
        """
        we undo the last step of the function
        :return:-
        """

        if  len(self.history) == 0:
            raise ValueError("No more steps to undo!\n")
        new_list = self.history[-1]
        self.list.clear()
        for element in new_list:
            self.list.append(element)

        # we now pop the last element in the history
        self.history.pop()

    def print_element(self,index):
        return self.list[index]



    def filter(self,start,end):
        """
        we filter the list of complex numbers
        :param start: the starting position of the list we will keep
        :param end: the ending position of the list we will keep
        :return:
        """

        list_length = len(self.list)
        c = ValidatePosition(start, end, list_length)
        c.check_positions()

        start = int(start)
        end = int(end) - start + 1 # and now end will be the length of the interval we will have after filtration
        i1 = 0
        # if the first index of the interval its not 0, then we eliminate everything up to that position
        while i1 < start:
            self.list.pop(i1)
            start -= 1
            list_length -= 1

        # we then eliminates all the elements that are out of the interval
        while end < list_length:
            self.list.pop()
            list_length -= 1

