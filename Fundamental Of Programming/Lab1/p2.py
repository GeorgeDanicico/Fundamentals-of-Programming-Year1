#
# Implement the program to solve the problem statement from the second set here
#
# Implement problem 10 from the Second Set

def Read_given_number(): #we read the given natural number
    number = int(input("Please insert your number: "))
    return number

def find_palindrome(number):
    pal = 0
    while number != 0:
        pal = pal * 10 + number % 10
        number = number // 10

    return pal

if __name__ == "__main__":
    number = Read_given_number()
    print(f"The palindrom of {number} is {find_palindrome(number)}")