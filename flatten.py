# Implementation 1
# problem with this: original ordering
# of the elements may not be conserved
def flatten(mList, i=0):
    if i < len(mList):
        if type(mList[i]) == list:
            mList.extend(mList[i])
            mList.remove(mList[i])
            flatten(mList, i)
        else:
            flatten(mList, i + 1)


# implementation 2
def flatten1(mList):
    if len(mList) == 0:
        return mList
    elif type(mList[0]) == list:
        return flatten1(mList[0]) + flatten1(mList[1:])
    else:
        return [mList[0]] + flatten1(mList[1:])


def input_list():
    mList = []
    print("Elements to be entered in format: X X [X,X] [X,X] X ")
    raw_input = input("Enter Elements: ")
    mList = raw_input.split()
    i = 0
    while i < len(mList):
        if mList[i][0] == '[':
            mList[i] = [int(x) for x in mList[i][1:-1].split(",")]
        else:
            mList[i] = int(mList[i])
        i += 1

    return mList


myList = input_list()
print(f"List Entered: {myList}")
myList = flatten1(myList)
print(f"Flattened List: {myList}")

# without taking input
thisList = [1, [2, 3, [5, 6], [7, [68, -97, -42], [71, 43]], [12]], 4, [5, 67]]
print(f"\nSample List: {thisList}")
thisList = flatten1(thisList)
print(f"Flattened List: {thisList}")
