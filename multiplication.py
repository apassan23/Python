def mult(num1, num2):
    if num1 == 0 or num2 == 0:
        return 0
    else:
        return num1 + mult(num1, num2 - 1)


def multiply(num1, num2):
    if num1 > num2:
        if num2 < 0:
            return -mult(num1, abs(num2))
        else:
            return mult(num1, num2)
    else:
        if num1 < 0:
            return -mult(num2, abs(num1))
        else:
            return mult(num2, num1)


print("The Product is {}".format(multiply(int(input("Enter a Number: ")),
                                          int(input("Enter another Number: ")))))
