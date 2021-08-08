def getSum(mList):
    result = []
    for i in range(len(mList)):
        sum = 0
        for j in range(i + 1):
            sum += mList[j]
        result.append(sum)
    return result


list = [int(x) for x in input("Enter a List: ").split()]
print(f"Resultant Cumulative List: {getSum(list)}")
