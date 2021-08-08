def square_digits(sqdNumber):
    sqdNumber_result = 0
    while sqdNumber != 0:
        digit = sqdNumber % 10
        sqdNumber_result += digit * digit
        sqdNumber = int(sqdNumber / 10)

    return sqdNumber_result


sqdNumber = int(input("Enter a Number: "))
print(f"Sum of Squared Digits : {square_digits(abs(sqdNumber))}")
