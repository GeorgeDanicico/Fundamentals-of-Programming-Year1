"""
Functions that implement program features. They should call each other, or other functions from the domain
"""
from src.domain.entity import get_average_grade,get_contestant,create_contestant,to_str,set_new_grade
import copy

def sort_decreasing(my_list):
    """
    we sort in the decreasing order by the average points of the
    :param my_list: the contestants list
    :return: the sorted list
    """
    return sorted(my_list, key= lambda k :get_average_grade(k), reverse= True)

def sort_decreasing_by_problem(my_list,problem):
    return sorted(my_list, key=lambda k: k[problem], reverse=True)

def update_history(my_list):
    """
    we update the history
    :param my_list: the contestant dictionary
    :return: none
    """
    new_list = copy.deepcopy(my_list['list'])
    #new_list = []
    #for index in range(len(my_list['list'])):
        #new_list.append(my_list['list'][index])

    my_list['history'].append(new_list)

# FUNCTION FOR CHECKING THE INPUT FOR COMMANDS OVER HERE
def check_insert_input(my_list, tokens):
    """
    we check if the input is corect
    :param my_list:
    :param tokens:
    :return: - / raise error if the input is not correct
    """
    for i in range(len(tokens)):
        tokens[i] = tokens[i].strip()

    if len(tokens) != 5:
        raise ValueError("Invalid number of arguments for the insert command")

    # check if the parameter input is correct ( not valid )
    if not tokens[0].isdigit() or not tokens[1].isdigit() or not tokens[2].isdigit() or not tokens[3] == 'at' or not tokens[4].isdigit():
        raise ValueError("Invalid arguments for the insert command")

    if int(tokens[0]) not in list(range(0,11)) or int(tokens[1]) not in list(range(0,11)) or int(tokens[2]) not in list(range(0,11)):
        raise ValueError("Invalid grades for insert command!")

    if int(tokens[4]) not in list(range(len(my_list) + 1)):
        raise ValueError("Invalid position for insert command")


def check_x1tox2_input(my_list, params):
    """
    we check if the input is valid for avg, simple remove and min
    :param my_list:
    :param params:
    :return: params
    """
    if len(params) != 3:
        raise ValueError("Invalid parameters for avg command!")

    for i in range(len(params)):
        params[i] = params[i].strip()

    if not params[0].isdigit() or not params[2].isdigit() or params[1] != 'to':
        raise ValueError("Invalid input data for avg command!")

    if int(params[0]) not in range(len(my_list)) or int(params[2]) not in range(len(my_list)):
        raise ValueError("Invalid input data for avg command!")

    return int(params[0]), int(params[2])

def calculate_average(my_list,index1, index2):

    avg_sum = 0.0
    for i in range(index1,index2+1):
        avg_sum += get_average_grade(my_list[i])

    return (round(avg_sum / (index2 - index1 + 1), 2))

def calculate_minimum(my_list,index1,index2):
    minimum = get_average_grade(my_list[index1])
    for i in range(index1+1, index2 + 1):
        current_avg = get_average_grade(my_list[i])
        if current_avg < minimum:
            minimum =  current_avg

    return minimum

def find_top_list(my_list, command_params):
    '''
    we make the top of a certain number given
    :param my_list: contestant list
    :param command_params:
    :return: the top list
    '''
    tokens = command_params.split(' ')
    tokens[0] = tokens[0].strip()
    if len(tokens) != 1 or not tokens[0].isdigit() or int(tokens[0]) < 0 or int(tokens[0]) > len(my_list):
        raise ValueError("Invalid parameters for the top command!")

    sorted_list = sort_decreasing(my_list)
    new_list = []
    i = 0
    j = int(tokens[0])
    while i < j:
        new_list.append(sorted_list[i])
        i += 1

    return new_list

def find_top_problem(my_list, command_params):
    """
    we make the top for a certain problem
    :param my_list:
    :param command_params:
    :return:
    """
    tokens = command_params.split(' ')
    tokens[0] = tokens[0].strip()
    tokens[1] = tokens[1].strip()

    if not tokens[0].isdigit() or tokens[1].upper() not in ['P1', 'P2', 'P3'] or int(tokens[0]) > len(my_list):
        raise ValueError("Invalid parameters for the top command! ")

    sorted_list = sort_decreasing_by_problem(my_list, tokens[1].upper())
    new_list =[]
    i = 0
    j = int(tokens[0]) - 1
    while i <= j:
        new_list.append(sorted_list[i])
        i += 1

    return new_list

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


def remove_set_0(my_list, tokens):
    if tokens[0] not in ['>', '<'] or not tokens[1].isdigit():
        raise ValueError("Invalid parameters for remove function")

    number = int(tokens[1])
    if tokens[0] == '>' and number == 100:
        raise ValueError("The maximum score is 10!")
    if tokens[0] == '<' and number == 0:
        raise ValueError("The minimum score is 0!")
    number = number / 10
    update_history(my_list)
    check_set_0 = 0 # if it is 1 there was one element set to 0/ otherwise none elements were modified
    if tokens[0] == '>':
        for index in range(len(my_list['list'])):
            if get_average_grade(my_list['list'][index]) > number:
                replace_score(my_list, index, 'P1', 0 , 0) # 4th parameter will be the score
                replace_score(my_list, index, 'P2', 0, 0)
                replace_score(my_list, index, 'P3', 0, 0)
                check_set_0 = 1
    else:
        for index in range(len(my_list['list'])):
            if get_average_grade(my_list['list'][index]) < number:
                replace_score(my_list, index, 'P1', 0, 0) # 4th parameter will be the score
                replace_score(my_list, index, 'P2', 0, 0)
                replace_score(my_list, index, 'P3', 0, 0)
                check_set_0 = 1

    if check_set_0 == 0:
        my_list['history'].pop()
        raise ValueError("No elements were modified!!")



def remove_interval(my_list, tokens):
    """
    Remove from the list a given interval
    :param my_list: the list of contestants
    :param tokens: parameters as a string
    :return: -
    """
    index1, index2 = check_x1tox2_input(my_list['list'], tokens)

    update_history(my_list)
    while index2 >= index1:
        remove_position(my_list, index1, 0)
        index2 -= 1





def remove_position(my_list, position, ok):
    """
    delete the element at the given position
    :param my_list: the contestants list
    :param position: the position we want to delete
    :return: -
    """
    if not str(position).isdigit():
        raise ValueError("Invalid parameter for remove command!")

    #TODO solve this issue with remove < avg
    if position not in range(len(my_list['list'])):
        raise ValueError("Invalid position to remove in the current list!")
    if ok == 1:
        update_history(my_list)
    my_list['list'].pop(position)

def replace_score(my_list, position, problem, score, ok):
    """
    we replace the given position value of the problem
    :param my_list: the list of contestants
    :param position: the position
    :param problem: the problem
    :param score: the score
    :param ok: its 0 if we dont have to update the history/ otherwise it is 1
    :return:
    """

    # we get the contestant and change his grade on the given problem
    # and then we remove it from the list and then insert at the same position
    if ok == 1:
        update_history(my_list)

    contestant = get_contestant(my_list['list'], position)
    set_new_grade(contestant, problem, score)

    remove_position(my_list, position,0)
    add_contestant(my_list, contestant, position, 0)





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



def add_contestant(my_list, contestant, position = -1, ok = 1):
    """
    we add a contestant to the list
    :param my_list: the list of contestants
    :param contestant: contestant
    :param position: given position
    :param ok:
     :return:
    """
    # we modified the function in order to be used by the replace function
    # or by the insert functiom

    if position == -1:
        if ok == 1:
            update_history(my_list)
        my_list['list'].append(contestant)
    else:
        if position not in range(len(my_list['list']) + 1):
            raise ValueError("Invalid position in the contestant list")
        if ok == 1:
            update_history(my_list)
        my_list['list'].insert(position, contestant)


def undo_function(my_list):
    """
    we undo the last step of the that change the data
    :param my_list:
    :return:
    """
    #new_list = my_list['history'][len(my_list['history']) - 1]
    new_list = copy.deepcopy(my_list['history'][len(my_list['history']) - 1])
    my_list['list'].clear()
    for element in new_list:
        my_list['list'].append(element)

    my_list['history'].pop()

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