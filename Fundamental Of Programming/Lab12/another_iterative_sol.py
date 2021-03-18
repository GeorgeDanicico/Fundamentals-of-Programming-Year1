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


def add_sol(solution, paranthesis):
    paranthesis_string = ''
    for i in range(len(solution)):
        if solution[i] == 1:
            paranthesis_string = paranthesis_string + '('
        else:
            paranthesis_string = paranthesis_string + ')'

    paranthesis.append(paranthesis_string)


def is_solution(length, n):
    return length == n


def is_valid(solution, length, n):
    """
    The same valid function for recursive solution
    :param solution:
    :param length:
    :param n:
    :return:
    """

    if solution[0] == 2:
        return False

    count_1 = 0
    count_2 = 0
    for i in range(length):
        if solution[i] == 1:
            count_1 += 1
        else:
            count_2 += 1

    if count_1 > n // 2:
        return False
    if count_2 > n // 2:
        return False
    if count_2 > count_1:
        return False

    return True


def bkt_iterative(paranthesis, length):

    solution = [[]]

    while len(solution) != 0:
        last_elem = solution.pop() # we make a copy of the solution without the last element
        for i in [1, 2]:
            last_elem.append(i) # add a number/ 1 represents an open bracket, 2 represents a closed brackets

            # we check if the current list of elements it is valid
            if is_valid(last_elem, len(last_elem), length):
                # if there are 'length' elements in the last_elem list, it means that we have a solution
                if is_solution(len(last_elem), length):
                    add_sol(last_elem, paranthesis)
                else:
                    solution.append(last_elem[:])

            last_elem.pop()


paranthesis = []
length = read_length()

bkt_iterative(paranthesis, length)

if len(paranthesis) == 0:
    print("Unfortunately, there are no correctly combinations... :(")
else:
    print(f"There are {len(paranthesis)} combinations: ")
    index = 1
    for solution in paranthesis:
        print("\t" + str(index) + ". " + str(solution))
        index += 1