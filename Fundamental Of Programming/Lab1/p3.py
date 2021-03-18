#
# Implement the program to solve the problem statement from the third set here
#
# Implement problem 15 from the Set 3

def Read_given_number(): # we read the given number
    number = int(input("Please insert your number: "))
    return number

def Is_perfect(number): # we check if the current number is perfect
    div_sum = 1

    divisor = 2
    while divisor * divisor <= number:
        if number % divisor == 0:
            # if varriable divisor is a divisor of the number, then number// divisor is also a divisor
            # but we have to check if its not a perfect square to avoid the case when it adds the same divisor
            # twice
            div_sum += divisor
            if divisor != (number // divisor):
                div_sum += (number // divisor)

        divisor += 1

    if div_sum == number:
        return True
    else:
        return False

def find_smaller_perfect(number): # we find the greatest perfect number smaller than a natural given number
    # or we stop when the number = 5 because the first perfect number is 6
    number -= 1
    while number > 5 and Is_perfect(number) == False:
        number -= 1

    return number

if __name__ == "__main__":
    number = Read_given_number()

    perfect_number = find_smaller_perfect(number)

    if perfect_number < 6:
        print(f"There is no smaller perfect number than {number}")
    else:
        print(f"The greatest perfect number  smaller than {number} is {perfect_number} !")

