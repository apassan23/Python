def palindrome(str):
    if str == "":
        return True
    elif str[0] != str[-1]:
        return False
    else:
        return palindrome(str[1:-1])


print("Is Palindrome: {}".format(palindrome(input("Enter a String: "))))
