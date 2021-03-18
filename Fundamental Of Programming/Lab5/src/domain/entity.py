"""
    Entity class should be coded here
"""


class complexException(Exception):
    """
    custom exception class
    """
    def __init__(self,msg):
        self._msg = msg

class complex:
    """
    the complex number
    """
    def __init__(self,real, imag):
        self.real_part = float(real)
        self.imag_part= float(imag)

    @property
    def real_part(self):
        return self._real

    @property
    def imag_part(self):
        return self._imag

    @real_part.setter
    def real_part(self,value):
        self._real = value

    @imag_part.setter
    def imag_part(self, value):
        self._imag = value

    def __str__(self):
        """
        we return the complex number in a nice format to be printed out
        :return: -
        """
        return "-> " + str(self.real_part) + " + (" + str(self.imag_part) + ")i"




def test_create_complex():
    c = complex('0.54','5')
    #print(str(c))


test_create_complex()