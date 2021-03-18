"""
This is the user interface module. These functions call functions from the domain and functions module.
"""
#
# Write the implementation for A3 in this file
#
from src.functions.functions import *
from src.domain.test import *

def add_command_ui(my_list, command_params):
    # we will add to the my list the grades in command_params
    # if the grades are valid

    add_contestant(my_list, add_check_params(command_params), -1, 1)
    print("Adding...")

def average_list_ui(my_list,command_params):
    tokens = command_params.split()

    index1, index2 = check_x1tox2_input(my_list['list'],tokens)

    average_sum = calculate_average(my_list['list'], index1, index2)

    print(f"The average from {index1} to {index2} is: {average_sum}")

def minimum_list_ui(my_list,command_params):
    tokens = command_params.split()

    index1, index2 = check_x1tox2_input(my_list['list'],tokens)

    minimum = calculate_minimum(my_list['list'],index1, index2)

    print(f"The minimum from {index1} to {index2} is: {minimum}")

def insert_command_ui(my_list, command_params):
    #insert <P1> <P2> <P3> at <position>
    tokens = command_params.split(' ')

    # we eliminate the additional spaces(if there are any)
    check_insert_input(my_list['list'], tokens)

    contestant = create_contestant(int(tokens[0]), int(tokens[1]), int(tokens[2]))
    add_contestant(my_list, contestant, int(tokens[4]), 1)
    print("Inserting...")

def remove_command_ui(my_list, command_params):
    # remove <position> / remove <start> to <end>
    tokens = command_params.split(' ')

    # we eliminate the additional spaces(if there are any)
    for i in range(len(tokens)):
        tokens[i] = tokens[i].strip()

    if len(tokens) == 1:
        # check if the parameter is a digit and if it is in the length of the list
        remove_position(my_list, int(tokens[0]), 1)

    elif len(tokens) == 3:
        remove_interval(my_list, tokens)

    elif len(tokens) == 2:
        remove_set_0(my_list, tokens)
        # we check now if the input data is valid
    else:
        raise ValueError("Invalid arguments for delete function")

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
    if not tokens[0].isdigit() or not tokens[3].isdigit() or tokens[2] != 'with' or tokens[1].upper() not in ['P1','P2','P3'] or int(tokens[0]) > len(my_list) or int(tokens[3]) not in list(range(11)):
        raise ValueError("Invalid arguments for this command!")

    replace_score(my_list, int(tokens[0]), tokens[1], int(tokens[3]), 1)
    print("Replacing...")



def list_command_ui(my_list, command_params):

    if command_params == '':
        for index in range(len(my_list['list'])):
            print(to_str(my_list['list'][index], index))
    elif command_params == 'sorted':
        sorted_list = sort_decreasing(my_list['list'])
        for index in range(len(sorted_list)):
            print(to_str(sorted_list[index], index))
    else:
        tokens = command_params.split(' ')

        for i in range(len(tokens)):
            tokens[i] = tokens[i].strip()

        sorted_list = create_list_space(my_list['list'], tokens)
        for index in range(len(sorted_list)):
            print(to_str(sorted_list[index], index))

def top_list_ui(my_list, command_params):
    # if the command_params have only 1 word is can only be the top <digit>
    # else we print that with bigger
    if len(command_params.split(' ')) == 1:
        max_list = find_top_list(my_list['list'], command_params)

        for i in range(len(max_list)):
            print(to_str(max_list[i],i))

    elif len(command_params.split(' ')) == 2:
        max_list = find_top_problem(my_list['list'],command_params)

        for i in range(len(max_list)):
            print(to_str(max_list[i],i))

    else:
        raise ValueError("Invalid arguments for the top command! ")


def undo_func_ui(my_list, params):
    if params != '':
        raise ValueError("Invalid arguments for undo command! ")
    if len(my_list['history']) == 0:
        raise ValueError("No more steps to undo! ")
    undo_function(my_list)
    print("Undoing...")



def start_command_ui():
    # contestants_list will be names my_list in the functions
    # in order to be easier and faster to write
    contestants_list = {'list': [] , 'history': []}
    test_init(contestants_list['list'])
    done = False
    command_dict = {'add': add_command_ui, 'insert': insert_command_ui,
                    'remove':remove_command_ui, 'replace':replace_command_ui,
                    'list':list_command_ui, 'avg': average_list_ui,
                    'min': minimum_list_ui, 'top': top_list_ui, 'undo':undo_func_ui}

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


#start_command_ui()