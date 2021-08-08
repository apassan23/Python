def unique(list1):
    i = 0
    while i < len(list1):
        if list1.index(list1[i]) != i:
            del list1[i]
        else:
            i += 1


list1 = [int(x) for x in input("Enter a List: ").split()]
unique(list1)
print(f"After Removing Duplicates: {list1}")
