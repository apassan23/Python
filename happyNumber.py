def square_digits(sqdNumber):
    sqdNumber_result = 0
    while sqdNumber != 0:
        digit = sqdNumber % 10
        sqdNumber_result += digit * digit
        sqdNumber = int(sqdNumber / 10)

    return sqdNumber_result


def isHappyNumber(num):
    iterations = 0
    while iterations <= 10:
        num = square_digits(num)
        if num == 1:
            return True
        iterations += 1
    return False


print("Is a Happy Number: {}".format(
    isHappyNumber(int(input("Enter a Number: ")))))
