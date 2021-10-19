def printPattern(n, patternType):
    if patternType == 1:
        for i in range(1, n + 1):
            for j in range(i + 1, 2*i + 1):
                print(j * j, end=' ')
            print()
    else:
        for i in range(1,n+1):
            for j in range(1, i+1):
                print(i, end="")
            print()


printPattern(3, 1)