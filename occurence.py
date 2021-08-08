def freq_pos(list1):
    freq = {}
    pos = {}
    for i in range(len(list1)):
        freq[list1[i]] = freq.get(list1[i], 0) + 1
        posList = pos.get(list1[i], [])
        posList.append(i)
        pos[list1[i]] = posList

    return [freq, pos]


inputList = [int(x) for x in input("Enter a List: ").split()]
print(freq_pos(inputList))
