"""
    UI class.

    Calls between program modules
    ui -> service -> entity
    ui -> entity
"""
from src.domain.entity import complexException,complex
from src.services.service import complex_list
import random


class ui:
    @staticmethod
    def print_menu():
        print("1. Add a complex number")
        print("2. Display the list of complex numbers")
        print("3. Filter the list between 2 indexes")
        print("4. Undo the last operation")
        print("0. Exit")
        print("\n")
    @staticmethod
    def init_list(self):
        """
        we will generate randomly 10 complex numbers
        and we will add them
        :param complex_list:
        :return:
        """
        for i in range(10):
            real_part = round(random.uniform(-20.0, 20.0), 2)
            imag_part = round(random.uniform(-20.0, 20.0), 2)
            # we create now the complex number
            number = complex(real_part, imag_part)
            self.add_complex(number)

    def __init__(self):
        self.list_complex = complex_list()
        ui.init_list(self.list_complex)

    @property
    def list_complex(self):
        return self._list_complex

    @list_complex.setter
    def list_complex(self,value):
        self._list_complex = value

    def add_complex_ui(self):
        """
        we read a real part and an imaginary part
        and then we put the complex number in the complex list
        """
        Real_part = input("Enter real part: ")
        Imag_part = input("Enter imag part: ")
        Real_part = Real_part.strip()
        Imag_part = Imag_part.strip()
        # we can do this because we catch the TypeError in the start function of the class
        Real_part = round(float(Real_part),2)
        Imag_part = round(float(Imag_part),2)

        number = complex(Real_part, Imag_part)
        self.list_complex.update_history()
        self.list_complex.add_complex(number)
        print("Adding...\n")

    def filter_complex_ui(self):
        """

        """
        start_index = input("Enter the starting point: ")
        end_index = input("Enter the ending point: ")
        start_index = start_index.strip()
        end_index = end_index.strip()
        self.list_complex.update_history()
        self.list_complex.filter(start_index,end_index)
        print("Filtering...\n")



    def undo_complex_ui(self):
        self.list_complex.undo()
        print("Undoing...\n")

    def display_ui(self):
        print("Displaying...")
        for i in range(len(self.list_complex)):
            print(str(self.list_complex.print_element(i)))
        print("\n")




    def start(self):
        #init_list(self.list_complex)
        done = False
        command_dict = {'1': self.add_complex_ui, '3': self.filter_complex_ui, '4': self.undo_complex_ui, '2': self.display_ui}
        while not done:
            ui.print_menu()
            command = input("Enter the command> ")
            command = command.strip()
            try:
                if command in command_dict:
                    command_dict[command]()
                elif command == '0':
                    print("Exiting...")
                    done = True
                else:
                    print("Bad command entered\n")
            except complexException as ve:
                print(str(ve) + "\n")
            #except TypeError as ve:
            #    print(str(ve) + "\n")
            except ValueError as ve:
                print(str(ve) + "\n")



