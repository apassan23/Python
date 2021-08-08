def getMultiples(n):
    result = []
    for i in range(1, n + 1):
        intermediate = []
        for j in range(1, 6):
            intermediate.append(i * j)
        result.append(intermediate)
    return result


n = int(input("Enter Number of Iterations: "))
print(f"Resultant List: {getMultiples(n)}")
