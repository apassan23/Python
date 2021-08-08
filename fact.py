# Factorial with recursion (1 to N)

result = 1


def fact(num):
    global result
    if num == 0 or num == 1:
        print("Factorial of " + str(num) + " is 1")
        return 1
    else:
        result = num * fact(num - 1)
        print("Factorial of " + str(num) + " is " + str(result))
        return result


fact(5)


# Factorial with recursion (N to 1)

result = 1
factorials = []


def fact_reverse(num):
    if num == 0 or num == 1:
        factorials.append(1)
        return 1
    else:
        result = num * fact_reverse(num - 1)
        factorials.append(result)
        return result


fact_reverse(5)

for index in range(len(factorials))[::-1]:
    print("Factorial of " + str(index + 1) + " is " + str(factorials[index]))


# Factorial without recursion

def fact_iter(num):
    result = 1
    for number in range(2, num + 1):
        result *= number
    return result


print(fact_iter(7))
