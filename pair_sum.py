def printPairsSum(mList, m):
    result = []
    for i in range(len(mList)):
        for j in range(i + 1, len(mList)):
            if mList[i] + mList[j] == m:
                result.append([mList[i], mList[j]])

    print(f"Pairs: {result}")


n = int(input("Enter Number of Elements: "))
list = []
print("Enter Elements")
for i in range(n):
    list.append(int(input()))

m = int(input("Enter Sum: "))
printPairsSum(list, m)
