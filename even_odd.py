def printEven_Odd(n):
    even = []
    odd = []
    for i in range(1, n + 1, 2):
        odd.append(i)
        even.append(i + 1)

    print(f"Even : {even}")
    print(f"Odd : {odd}")


n = int(input("Enter n: "))
printEven_Odd(n)
