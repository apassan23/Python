def printPrime(n):
    count = 0
    for i in range(2, n + 1):
        factors = 0
        for j in range(1, i):
            if i % j == 0:
                factors += 1
        if factors == 1:
            print(i)
            count += 1
    print(f"Total Prime Numbers: {count}")


printPrime(int(input("Enter n: ")))
