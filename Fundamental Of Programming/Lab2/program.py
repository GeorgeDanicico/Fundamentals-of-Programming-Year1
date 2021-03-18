#
# Write the implementation for A2 in this file
#

# UI section
# (write all functions that have input or print statements here). 
# Ideally, this section should not contain any calculations relevant to program functionalities


def print_longest_sequence(my_list, index1, index2):
    """
    we print the longest sequence of a given property between 2 indexes
    :param my_list: the list of the complex numbers
    :param index1: the first index of the interval
    :param index2: the second index of the interval
    :return:
    """
    for i in range(index1, index2 ):
        print(to_str(my_list[i]))

def ls_distinct_numbers_ui(my_list):
    """
    we find the longest sequence of distinct numbers
    :param my_list: the list of complex numbers
    :return:
    """
    max = 0
    max_index = 0
    for index in range(0,len(my_list)):
        length = find_ls_dist(my_list, index) - index + 1
        if length > max:
            max = length
            max_index = index

    print(f"The longest sequence of distinct numbers is between positions {max_index} and {max_index + max - 1}: ")
    print_longest_sequence(my_list, max_index , max_index + max - 1)



def ls_incr_real_ui(my_list):
    """
    we find the longest sequence of strictly increasing real part
    :param my_list: the list of complex numbers
    :return:
    """
    max = 0
    max_index = 0
    for index in range(0, len(my_list) - 1):
        length = find_ls_incre_real(my_list, index) - index + 1
        #print(f"{index} + {length} + {max}")
        # we will print here the first longest sequence with the given propertyif there are more
        if length > max:
            max = length
            max_index = index

    print(f"The longest sequence of stricly increasing real part is between positions {max_index } and {max_index + max - 1}: ")
    print_longest_sequence(my_list, max_index, max_index + max - 1)

def read_complex(my_list):
    """
    read a number of complex numbers
    and then read in a loop all the complex numbers

    :return:
    """
    # TODO Ask the teacher if the new list should append to the old list or not
    #my_list.clear()
    done = False
    while not done:
        counter = input("Enter a number: ")

        if not isNumber(counter):
            print("Bad input... try again...")
        else:
            done = True
            counter = int(counter)
            while counter :
                real_part = input("Real part: ")
                imaginary_part = input("Imaginary part: ")
                if not isNumber(real_part) or not isNumber(imaginary_part):
                    print("Bad input... try again...")
                else:
                    print("Adding...")
                    my_list.append(create_complex(int(real_part), int(imaginary_part)))
                    counter -= 1



def print_menu():
    print('\n')
    print("1 add a complex number")
    print("2 display the complex numbers list")
    print("3 display the l.s. of numbers with increasingly real part")
    print("4 display the l.s of the numbers with distinct numbers")
    print("5 exit the application")

def display_list(my_list):
    """
    Display the current list of complex numbers
    :param my_list: the complex numbers list
    :return:
    """
    for complex_number in my_list:
        print(to_str(complex_number))

def start():
    """
    Handle the main menu
    :return: returns once the program is finished
    """
    my_list = []
    init_list(my_list)
    done = False
    command_dict = {'1': read_complex, '2': display_list, '3': ls_incr_real_ui, '4':ls_distinct_numbers_ui}
    while not done:
        #we print the current menu before knowing the ass the teacher will give
        print_menu()
        operation = input("Enter operation: ")
        #handling the operation input
        if operation in command_dict:
            command_dict[operation](my_list)
        elif operation == '5':
            print("Exit...")
            done = True
        else:
            print("Bad command entered!")


# Function section
# (write all non-UI functions in this section)
# There should be no print or input statements below this comment
# Each function should do one thing only
# Functions communicate using input parameters and their return values

def find_ls_dist(my_list, index1):
    """
    we find the longest sequence of distinct numbers starting from position index1 in the list
    :param my_list:
    :param index1:
    :return:
    """
    done = False
    index2 = index1 + 1
    while not done and (index2 < len(my_list)):
        if my_list[index2] in my_list[index1:index2]:
            done = True
        else:
            index2 += 1

    # if number on position index1 is the same as the number on position 2 then the longest sequence
    # would be 1, so in order to do that we substract 1 from index2
    if index1 == index2 - 1:
        index2 -= 1

    return index2


def find_ls_incre_real(my_list, index):
    """
    find the longest sequence of strictly increasingly real part
    :param my_list: the list
    :param index: starting index/position
    :return: the ending position of the longest sequence
    """
    done = False
    while not done and (index < len(my_list) - 1):

        if get_real(my_list[index]) >= get_real(my_list[index + 1]):
            done = True

        if not done:
            index += 1

    return index


def get_real(complex_number):
    return complex_number['real']


def get_imag(complex_number):
    return complex_number['imag']

def to_str(complex_number):
    return (str(get_real(complex_number)) + ' + (' + str(get_imag(complex_number)) + 'i)')

def create_complex(real_part, imaginary_part = 0):
    """
    Create a real number with a given real and imaginary part and append it to the list
    :param real_part:
    :param imaginary_part:
    :return:
    """
    return {'real': real_part, 'imag': imaginary_part}


def init_list(my_list):
    """
    We initialize the list with 10 random complex numbers
    :param my_list: The list where we will store all the complex numbers
    :return:
    """
    my_list.append({'real': -7, 'imag': 3})
    my_list.append({'real': 3, 'imag': 4})
    my_list.append({'real': 22, 'imag': 19})
    my_list.append({'real': -12, 'imag': 9})
    my_list.append({'real': 6, 'imag': -3})
    my_list.append({'real': 6, 'imag': -3})
    my_list.append({'real': 9, 'imag': -4})
    my_list.append({'real': 11, 'imag': 9})
    my_list.append({'real': 13, 'imag': 7})
    my_list.append({'real': 7, 'imag': -3})


def isNumber(number):
    try:
        check = int(number)
        return True
    except ValueError:
        return False




start()


# print('Hello A2'!) -> prints aren't allowed here!
