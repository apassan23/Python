def sumTwoNum(x, y):
    z = x + y
    return z


def sumList(list1, list2):
    result = []
    if len(list1) != len(list2):
        return []
    for i in range(len(list1)):
        result.append(sumTwoNum(list1[i], list2[i]))
    return result


list1 = [int(x) for x in input("Enter List 1 : ").split()]
list2 = [int(x) for x in input("Enter List 2 : ").split()]

print(sumList(list1, list2))
