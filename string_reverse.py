def rev(str):
    if str == "":
        return ""
    else:
        return (str[-1] + rev(str[:-1]))


str = input("Enter a String: ")
print("The Reverse of \"{}\" is \"{}\"".format(str, rev(str)))
