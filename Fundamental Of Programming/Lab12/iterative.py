"""
Iterative version of the problem 6.
"""
from copy import deepcopy


def read_length():
    """
    The user read from the console the length of the string
    :return: the length
    """
    done, length = False, None
    while not done:
        try:
            length = input("Enter the length: ").strip()
            length = int(length)
            if length % 2 == 1:
                raise Exception("The length must be an even number!...")
            done = True
        except Exception as ve:
            print(str(ve))

    return length


def add(array, string):
    """
    we add in 'array' the string in a nicer format
    :param array: the array of solutions
    :param string: the list of characters '(', ')'
    """
    copy_string = ''
    for character in string:
        copy_string += character

    array.append(copy_string)


def generate_iterative_paranthesis(length, solution):
    """
    We generate iteratively all the solutions.
    We start from the first case where we have (((... length / 2 times and )))... length / 2 times.
    :param length: the length of the string
    :param solution: the list that will contain the solutions
    :return: Nothing
    """
    string = ['('] * (length // 2) + [')'] * (length // 2)
    # basically we start from the basic case, where there are on the first half positions '(' and on the other ')'
    #   In order to make sure that the paranthesis will be closed correctly at the end, the number of close paranthesis
    #   ')' will always be >= than the number of the opened paranthesis '('

    # What is important is that always the first paranthesis will be always an open one
    # That is why the program will stop when the frist position of the string is reached in the loop, because it will mean
    # that all the possibilities were computed
    add(solution, string)
    while True:
        string = string[:]

        opened, closed = 0, 0
        for i in range(length - 1, -1, -1):
            if i == 0:
                return
            if string[i] == '(':
                opened += 1
                if closed > opened:
                    # if we find an open paranthesis and the number of the closed ones >= nr of opened ones, it means that
                    # there is a new solution
                    string[i:] = [')'] + ['('] * opened + [')'] * (closed - 1)
                    break
            else:
                closed += 1

        if string not in solution:
            add(solution, string)


paranthesis = []
length = read_length()
generate_iterative_paranthesis(length, paranthesis)

if len(paranthesis) == 0:
    print("Unfortunately, there are no correctly combinations... :(")
else:
    print(f"There are {len(paranthesis)} combinations: ")
    index = 1
    for solution in paranthesis:
        print("\t" + str(index) + ". " + str(solution))
        index += 1

