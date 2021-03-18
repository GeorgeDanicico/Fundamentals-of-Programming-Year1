"""
here we will init function for the complex list in order to have 10 randomly generated numbers

"""
from src.services.service import complex_list,ValidatePosition
from src.domain.entity import complex,complexException
import random
import copy

#complx_list = complex_list()
class tests:


    def __init__(self):
        self._complx_list = complex_list()

    def __len__(self):
        return self._list

    @property
    def _list(self):
        return self._complx_list

    def init_list(self):
        """
        we will generate randomly 10 complex numbers
        and we will add them
        :param complex_list:
        :return:
        """
        for i in range(11):
            real_part = round(random.uniform(-20.0, 20.0), 2)
            imag_part = round(random.uniform(-20.0, 20.0), 2)
            # we create now the complex number
            number = complex(real_part, imag_part)
            self._complx_list.add_complex(number)

    def test_add(self):

        c = complex('2','3')
        try:
            self._list.add_complex(c)
            assert True
        except ValueError:
            assert False

        assert len(self._list) == 1

        c = complex('2.54', '3.23')
        self._list.add_complex(c)
        assert len(self._list) != 1

    def test_filter(self):
        tests.init_list(self)
        list_length = len(self._list)
        try:
            c = ValidatePosition('0','2',list_length)
            c.check_positions()
            self._list.filter('0','2')
            assert len(self._list) == 3
            assert True
        except ValueError as ve:
            print(str(ve))
            assert False

        try:
            list_length = len(self._list)
            c = ValidatePosition('0', '6', list_length)
            c.check_positions()
            self._list.filter('0', '6')
            assert False
        except complexException:
            assert True


    def test_undo(self):
        #self._list.clear()
        tests.init_list(self)
        self._list.update_history()

        list_length = len(self._list)
        c = ValidatePosition('0', '2', list_length)
        c.check_positions()
        self._list.filter('0', '2')
        try:
            self._list.undo()
            #for i in range(len(list_complex)):
            #   print(str(list_complex.print_element(i)))
            assert True
        except ValueError as ve:
            print(str(ve))
            assert False


#init_list(complx_list)
#print(complx_list.print_element(0))


