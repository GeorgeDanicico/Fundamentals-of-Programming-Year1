# Test functions go here
#
# Test functions:
#   - no print / input
#   - great friends with assert

from src.functions.functions import *



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
    my_list = {'list':[], 'history' :[]}
    test_init(my_list['list'])
    contestant = create_contestant(9, 8, 7)

    try:
        add_contestant(my_list, contestant, -1) # when it is -1 , it appends to the end of the list
        #if it is different then -1 it is used for the insert function
        #print(my_list['history'])
        assert True # no exception was raised
    except ValueError:
        assert False

def test_insert_contestant():
    my_list = {'list':[], 'history' :[]}
    test_init(my_list['list'])
    contestant = create_contestant(0, 0, 0)

    try:
        add_contestant(my_list, contestant, 0)  # when it is -1 , it appends to the end of the list
        #print(my_list['history'])
        # if it is different then -1 it is used for the insert function
        assert True  # no exception was raised
    except ValueError:
        assert False

def test_replace_score():
    my_list = {'list':[], 'history' :[]}
    test_init(my_list['list'])

    tokens = "0 P1 with 0"
    tokens = tokens.split(' ')

    try:
        replace_score(my_list, int(tokens[0]), tokens[1], int(tokens[3]), 1)
        #print(my_list['history'])
        assert True
    except ValueError:
        assert False

def test_remove_set0():
    my_list = {'list': [], 'history': []}
    test_init(my_list['list'])
    tokens = "< 70"
    tokens = tokens.split(' ')

    try:
        remove_set_0(my_list, tokens)
        assert True
    except ValueError:
        assert False


def test_remove_position():
    my_list = {'list':[], 'history' :[]}
    test_init(my_list['list'])

    try:
        remove_position(my_list, 4, 1)
        assert True
    except ValueError:
        assert False

def test_remove_interval():
    my_list = {'list':[], 'history' :[]}
    test_init(my_list['list'])

    tokens = "1 to 3"
    tokens = tokens.split()

    try:
        remove_interval(my_list, tokens)
        assert True
    except ValueError:
        assert False

def test_create_list_space():
    my_list = {'list':[], 'history' :[]}
    test_init(my_list['list'])

    tokens = "< 6"
    tokens = tokens.split()

    try:
        create_list_space(my_list['list'], tokens)
        assert True
    except ValueError:
        assert False

def test_undo():
    my_list = {'list': [], 'history': []}
    test_init(my_list['list'])
    contestant = create_contestant(9, 8, 7)
    add_contestant(my_list, contestant, -1)
    try:
        undo_function(my_list)
          # when it is -1 , it appends to the end of the list
        # if it is different then -1 it is used for the insert function
        #print(my_list['list'])
        assert True  # no exception was raised
    except ValueError:
        assert False

def test_top():
    my_list = {'list': [], 'history': []}
    test_init(my_list['list'])
    tokens = "3 p1"
    new_list = find_top_problem(my_list['list'], tokens)

    assert len(new_list) != 0, len(new_list)

    tokens = "5"
    new_list = find_top_list(my_list['list'],tokens)

    assert len(new_list) != 0

def test_average():
    my_list = {'list': [], 'history': []}
    test_init(my_list['list'])
    assert calculate_average(my_list['list'],0,5) == 7.67

def test_minim():
    my_list = {'list': [], 'history': []}
    test_init(my_list['list'])
    assert calculate_minimum(my_list['list'], 0, 5) == 5.33

test_add_contestant()
test_undo()
test_insert_contestant()
test_replace_score()
test_remove_interval()
test_remove_position()
test_create_list_space()
test_average()
test_minim()
test_remove_set0()
test_top()
