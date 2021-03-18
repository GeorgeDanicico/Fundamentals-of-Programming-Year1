#
# Write the implementation for A3 in this file
#
'''
We have to implement functions for:
    - add_contestant_ui
    - insert_contestant_ui
    - remove_contestant_ui ( keep in mind that we have 2 different removes
        * remove <position>
        * remove <start> to <end>
    - replace_contestant_ui
    - list_contestants_ui

'''
#
# domain section is here (domain = numbers, transactions, expenses, etc.)
# getters / setters
# No print or input statements in this section
# Specification for all non-trivial functions (trivial usually means a one-liner)
def get_average_grade(contestant):
    return round((float(contestant['P1']) + float(contestant['P2']) + float(contestant['P3']))/3, 2)

def get_contestant(my_list, position):
    return my_list[position ]

def set_new_grade(contestant, problem, value):
    contestant[problem.upper()] = value

# Functionalities section (functions that implement required features)
# No print or input statements in this section
# Specification for all non-trivial functions (trivial usually means a one-liner)
# Each function does one thing only
# Functions communicate using input parameters and their return values


def create_list_space(my_list, tokens):
    """
    printing the list according to the sign in the tokens string
    :param my_list: the contestants list
    :param tokens: the list of the sign and the number ( if correct )
    :return: -
    """
    if tokens[0] not in ['>','<','='] or not tokens[1].isdigit():
        raise ValueError("Invalid arguments for the list command")

    new_list = []
    # we create a new list with the values that needs to satisfy the condition that
    # is stored in tokens[0]

    if float(tokens[1]) > 10 or float(tokens[1]) < 0:
        raise ValueError("Invalid grade for the list command")
    #we raise a value error if the tokens[1] is not in [0,10]
    if tokens[0] == '=':
        for index in range(len(my_list)):
            if get_average_grade(my_list[index]) == round(float(tokens[1]), 2):
                new_list.append(my_list[index])

    # we do 2 more value checks because for the strictly greater o less the grade cant be 0 or 10
    if tokens[0] == '>':
        if float(tokens[1]) > 10:
            raise ValueError("Invalid grade for the list > command")

        for index in range(len(my_list)):
            if get_average_grade(my_list[index]) > round(float(tokens[1]), 2):
                new_list.append(my_list[index])

    if tokens[0] == '<':
        if float(tokens[1]) < 0:
            raise ValueError("Invalid grade for the list < command")

        for index in range(len(my_list)):
            if get_average_grade(my_list[index]) < round(float(tokens[1]), 2):
                new_list.append(my_list[index])


    if len(new_list) == 0:
        raise ValueError("There are no elements that satisfy the condition")

    return new_list




def remove_interval(my_list, tokens):
    """
    Remove from the list a given interval
    :param my_list: the list of contestants
    :param tokens: parameters as a string
    :return: -
    """
    # checking if the input is correct and after if it is valid
    if not tokens[0].isdigit() or not tokens[2].isdigit() or tokens[1] != 'to':
        raise ValueError("Invalid arguments for the remove command!")

    if int(tokens[0]) not in list(range(len(my_list))) or int(tokens[0]) not in list(range(len(my_list))):
        raise ValueError("Invalid positions for the remove command")

    index1 = int(tokens[0])
    index2 = int(tokens[2])
    while index2 >= index1:
        remove_position(my_list, index1)
        index2 -= 1





def remove_position(my_list, position):
    """
    delete the element at the given position
    :param my_list: the contestants list
    :param position: the position we want to delete
    :return: -
    """
    if not str(position).isdigit():
        raise ValueError("Invalid parameter for remove command!")

    if int(position) not in list(range(len(my_list))):
        raise ValueError("Invalid position to remove in the current list!")


    my_list.pop(position)

def replace_score(my_list, tokens):
    """
    replace the score for the given position in tokens list
    :param my_list:
    :param tokens:
    :return:
    """

    if int(tokens[0]) > len(my_list):
        raise ValueError("Invalid contestant position!")

    if int(tokens[3]) not in list(range(11)):
        raise ValueError("Invalid grade for the problem!")

    # we get the contestant and change his grade on the given problem
    # and then we remove it from the list and then insert at the same position
    contestant = get_contestant(my_list, int(tokens[0]))
    set_new_grade(contestant, tokens[1], int(tokens[3]))

    remove_position(my_list, int(tokens[0]))
    add_contestant(my_list, contestant, int(tokens[0]))


def sort_decreasing(my_list):
    """
    we sort in the decreasing order by the average points of the
    :param my_list: the contestants list
    :return: the sorted list
    """
    return sorted(my_list, key= lambda k :get_average_grade(k), reverse= True)

def to_str(contestant, index):
    return (str(index) + ". " + "P1= " + str(contestant['P1'])+"; " + "P2= " + str(contestant['P2']) +"; " + "P3= " + str(contestant['P3']))


def create_contestant(P1, P2, P3):
    """
    Create the contestant with the grades on the 3 problems
    :param P1: first problem
    :param P2: second problem
    :param P3: third problem
    :return: the contestant as a dict with the grades
    """
    return {'P1': P1, 'P2': P2, 'P3': P3}


def add_check_params(command_params):
    """
    we check if the command_params for the add command are correct
    :param command_params: command_params as string
    :return: the values if no ValueError is raised
    """
    tokens = command_params.split(' ')
    # if there are more or less than 3 elements in tokens list we raise an error
    if len(tokens) != 3:
        raise ValueError("Invalid arguments for the command...")

    # if the elements of the tokens list are no numbers we raise an error
    if not tokens[0].isdigit() or not tokens[1].isdigit() or not tokens[2].isdigit():
        raise ValueError("Invalid arguments for the command...")

    if int(tokens[0]) not in list(range(0, 11)) or int(tokens[1]) not in list(range(0, 11)) or int(tokens[2]) not in list(range(0, 11)):
        raise ValueError("Invalid arguments for the command...")

    return create_contestant(int(tokens[0]), int(tokens[1]), int(tokens[2]))



def add_contestant(my_list, contestant, position = -1):
    """
    add the contestant to the list
    :param my_list: the list of contestants
    :param contestant: contestant as a dictionary
    :return: -
    """
    # we modified the function in order to be used by the replace function
    # or by the insert function
    if position == -1:
        my_list.append(contestant)
    else:
        if position not in list(range(len(my_list))):
            raise ValueError("Invalid position in the contestant list")
        my_list.insert(position, contestant)


def split_function(command):
    """
    we split the command string in comm word and comm params
    :param command: the string the programmer entered
    :return: command_word, command_params // the command word and the params
    """
    command = command.strip()
    tokens = command.split(' ', 1)
    command_word = tokens[0].strip()
    command_params = tokens[1].strip() if len(tokens) == 2 else ''
    return command_word, command_params


# UI section
# (all functions that have input or print statements, or that CALL functions with print / input are  here).
# Ideally, this section should not contain any calculations relevant to program functionalities

def add_command_ui(my_list, command_params):
    # we will add to the my list the grades in command_params
    # if the grades are valid

    add_contestant(my_list, add_check_params(command_params), -1)
    print("Adding...")




def insert_command_ui(my_list, command_params):
    #insert <P1> <P2> <P3> at <position>
    tokens = command_params.split(' ')

    if len(tokens) != 5:
        raise ValueError("Invalid number of arguments for the insert command")

    # we eliminate the additional spaces(if there are any)
    for i in range(len(tokens)):
        tokens[i] = tokens[i].strip()

    # check if the parameter input is correct ( not valid )
    if not tokens[0].isdigit() or not tokens[1].isdigit() or not tokens[2].isdigit() or not tokens[3] == 'at' or not tokens[4].isdigit():
        raise ValueError("Invalid arguments for the insert command")

    if int(tokens[0]) not in list(range(0,11)) or int(tokens[1]) not in list(range(0,11)) or int(tokens[2]) not in list(range(0,11)):
        raise ValueError("Invalid grades for insert command!")

    if int(tokens[4]) not in list(range(len(my_list) + 1)):
        raise ValueError("Invalid position for insert command")
    contestant = create_contestant(int(tokens[0]), int(tokens[1]), int(tokens[2]))
    add_contestant(my_list, contestant, int(tokens[4]))
    print("Inserting...")

def remove_command_ui(my_list, command_params):
    # remove <position> / remove <start> to <end>
    tokens = command_params.split(' ')

    # we eliminate the additional spaces(if there are any)
    for i in range(len(tokens)):
        tokens[i] = tokens[i].strip()

    if len(tokens) == 1:
        # check if the parameter is a digit and if it is in the length of the list


        remove_position(my_list, int(tokens[0]))

    else:
        if len(tokens) != 3:
            raise ValueError("Invalid arguemters for the remove command")

        remove_interval(my_list, tokens)

        # we check now if the input data is valid

    print("Removing...")


def replace_command_ui(my_list, command_params):
    # replace <position> <P1/P2/P3> with <new score>
    tokens = command_params.split(' ')
    if len(tokens) != 4:
        raise ValueError("Invalid arguments for this command!")

    # we eliminate the additional spaces(if there are any)
    for i in range(len(tokens)):
        tokens[i] = tokens[i].strip()

    # check if the params are correct input ( not necessarily valid )
    if not tokens[0].isdigit() or not tokens[3].isdigit() or tokens[2] != 'with' or tokens[1].upper() not in ['P1','P2','P3']:
        raise ValueError("Invalid arguments for this command!")

    replace_score(my_list, tokens)
    print("Replacing...")



def list_command_ui(my_list, command_params):

    if command_params == '':
        for index in range(len(my_list)):
            print(to_str(my_list[index], index))
    elif command_params == 'sorted':
        sorted_list = sort_decreasing(my_list)
        for index in range(len(sorted_list)):
            print(to_str(sorted_list[index], index))
    else:
        tokens = command_params.split(' ')

        for i in range(len(tokens)):
            tokens[i] = tokens[i].strip()

        sorted_list = create_list_space(my_list, tokens)
        for index in range(len(sorted_list)):
            print(to_str(sorted_list[index], index))



def start_command_ui():
    # contestants_list will be names my_list in the functions
    # in order to be easier and faster to write
    contestants_list = []
    test_init(contestants_list)
    done = False
    command_dict = {'add': add_command_ui, 'insert': insert_command_ui,
                    'remove':remove_command_ui, 'replace':replace_command_ui,
                    'list':list_command_ui}

    while not done:
        command = input("Enter the command> ").lower()
        try:
            command_word, command_params = split_function(command)

            if command_word in command_dict:
                command_dict[command_word](contestants_list, command_params)
            elif command_word == 'exit' and command_params == '':
                print("Exiting...")
                done = True
            else:
                print("Bad command entered")
        except ValueError as ve:
            print(str(ve))


# Test functions go here
#
# Test functions:
#   - no print / input
#   - great friends with assert
def test_init(my_list):
    my_list.append({'P1': 10, 'P2': 10, 'P3': 8})
    my_list.append({'P1': 5, 'P2': 10, 'P3': 8})
    my_list.append({'P1': 6, 'P2': 9, 'P3': 9})
    my_list.append({'P1': 7, 'P2': 10, 'P3': 7})
    my_list.append({'P1': 8, 'P2': 0, 'P3': 8})
    my_list.append({'P1': 8, 'P2': 9, 'P3': 6})
    my_list.append({'P1': 1, 'P2': 10, 'P3': 8})
    my_list.append({'P1': 2, 'P2': 3, 'P3': 8})
    my_list.append({'P1': 8, 'P2': 9, 'P3': 8})
    my_list.append({'P1': 7, 'P2': 5, 'P3': 8})


def test_add_contestant():
    my_list = []
    contestant = create_contestant(9, 8, 7)

    try:
        add_contestant(my_list, contestant, -1) # when it is -1 , it appends to the end of the list
        #if it is different then -1 it is used for the insert function
        assert True # no exception was raised
    except ValueError:
        assert False

def test_insert_contestant():
    my_list = []
    test_init(my_list)
    contestant = create_contestant(9, 8, 7)

    try:
        add_contestant(my_list, contestant, 4)  # when it is -1 , it appends to the end of the list
        # if it is different then -1 it is used for the insert function
        assert True  # no exception was raised
    except ValueError:
        assert False

def test_replace_score():
    my_list = []
    test_init(my_list)

    tokens = "4 P1 with 0"
    tokens = tokens.split(' ')

    try:
        replace_score(my_list, tokens)
        assert True
    except ValueError:
        assert False

def test_remove_position():
    my_list = []
    test_init(my_list)

    try:
        remove_position(my_list, 4)
        assert True
    except ValueError:
        assert False

def test_remove_interval():
    my_list = []
    test_init(my_list)

    tokens = "1 to 3"
    tokens = tokens.split()

    try:
        remove_interval(my_list, tokens)
        assert True
    except ValueError:
        assert False

def test_create_list_space():
    my_list = []
    test_init(my_list)

    tokens = "< 6"
    tokens = tokens.split()

    try:
        create_list_space(my_list, tokens)
        assert True
    except ValueError:
        assert False

test_add_contestant()
test_insert_contestant()
test_replace_score()
test_remove_interval()
test_remove_position()
test_create_list_space()

start_command_ui()