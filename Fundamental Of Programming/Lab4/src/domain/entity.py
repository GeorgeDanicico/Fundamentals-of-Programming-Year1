"""
Domain file includes code for entity management
entity = number, transaction, expense etc.
"""


""" 
getter and setters over here
"""
def get_average_grade(contestant):
    return round((float(contestant['P1']) + float(contestant['P2']) + float(contestant['P3']))/3, 2)

def get_contestant(my_list, position):
    return my_list[position ]

def set_new_grade(contestant, problem, value):
    contestant[problem.upper()] = value

def to_str(contestant, index):
    return (str(index) + ". " + "P1= " + str(contestant['P1'])+"; " + "P2= " + str(contestant['P2']) +"; " + "P3= " + str(contestant['P3']) + ' Average: ' + str(get_average_grade(contestant)))


def create_contestant(P1, P2, P3):
    """
    Create the contestant with the grades on the 3 problems
    :param P1: first problem
    :param P2: second problem
    :param P3: third problem
    :return: the contestant as a dict with the grades
    """
    return {'P1': P1, 'P2': P2, 'P3': P3}

