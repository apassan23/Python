def length(str):
    if str == "":
        return 0
    else:
        return (1 + length(str[1:]))


print("The Length of the String is {}".format(
    length(input("Enter a String: "))))
