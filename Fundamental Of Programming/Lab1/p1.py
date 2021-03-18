#
# Implement the program to solve the problem statement from the first set here
#
#Implement Problem 3 from Set 1

def Read_given_number():# we read the given natural number
    number = int(input("Please insert the number: "))
    return number


def digits_list(digits, number): #we will store the number's digits into a list , we sort it and will return it
    number1 = number
    while number1 != 0:
        digits.append(int(number1 % 10))
        number1 = number1 // 10

    digits.sort()
    return digits

def minimal_number(digits):
    # we check if there is atleast one 0 in the list so that the minimal number begins with  the first digit > 0

    min_number = 0
    if 0 not in digits:
        for digit in digits:
            min_number = min_number* 10 + digit
    else:
        index = 0
        # we find the first position with a digits > 0 , add it to the number as the first digit, and then make it -1
        while digits[index] == 0:
            index += 1

        min_number = digits[index]
        digits[index] = -1
        for digit in digits:
            if digit != -1:
                min_number = min_number* 10 + digit

    return min_number

#we use the functions
if __name__ == "__main__":
    digits = []
    number = Read_given_number()
    digits = digits_list(digits, number)
    print(f"The minimal number is: {minimal_number(digits)}")






