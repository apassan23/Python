def copy(mList):
    if len(mList) == 0:
        return []
    else:
        return [mList[0]] + copy(mList[1:])


def deepCopy(mList):
    if len(mList) == 0:
        return []
    elif type(mList[0]) == list:
        return [deepCopy(mList[0])] + deepCopy(mList[1:])
    else:
        return [mList[0]] + deepCopy(mList[1:])


thisList = [1, 2, [3, 4, [5, [8, 9]]]]
shallow_copy = copy(thisList)
deep_copy = deepCopy(thisList)
print(f"Before Altering: {thisList}")
thisList[2][0] = -65
thisList[2][2][0] = 7
thisList[2][2][1][0] = 2

print(f"After Altering: {thisList}")
print(f"Shallow Copy: {shallow_copy}")
print(f"Deep Copy: {deep_copy}")
