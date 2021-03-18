

def print_solution(solution, array, length):
    paranthesis_string = ''
    for i in range(length):
        if array[i] == 1:
            paranthesis_string = paranthesis_string + '('
        else:
            paranthesis_string = paranthesis_string + ')'
    solution.append(paranthesis_string)


def is_solution(length, k):
    return length == k


def is_valid(array, length, k):
    if array[0] == 2:
        return False

    count_1 = 0
    count_2 = 0
    for i in range(k + 1):
        if array[i] == 1:
            count_1 += 1
        else:
            count_2 += 1

    if count_1 > length//2:
        return False
    if count_2 > length//2:
        return False
    if count_2 > count_1:
        return False

    return True


def bkt(array, length, k, paranthesis):
    for i in [1, 2]:
        array[k] = i
        if is_valid(array, length, k):
            if is_solution(length - 1, k):
                print_solution(paranthesis, array, length)
            else:
                bkt(array[:], length, k+1, paranthesis)
        array[k] = 0


def create_array():
    done = False
    length = 0
    while not done:

        length = input("Please insert the length of the sequence: ")
        try:
            length = int(length)
            done = True
        except Exception:
            print("Invalid length!")

    array = [0] * length
    return array, length


paranthesis = []
array, length = create_array()
bkt(array, length, 0, paranthesis)

if len(paranthesis) == 0:
    print("Unfortunately, there are no correctly combinations... :(")
else:
    print(f"There are {len(paranthesis)} combinations: ")
    index = 1
    for solution in paranthesis:
        print("\t"+ str(index) + ". " + solution)
        index += 1