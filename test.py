def palindrome(str):
    if str == "":
        return True
    elif str[0] == str[-1:]:
        return palindrome(str[1:-1])
    else:
        return False

print(palindrome("level"))

def mul(a,b):
    if b == 0:
        return 0
    else:
        return a + mul(a,b - 1)

def multiply(a,b):
    if a > b:
        if b < 0:
            return -mul(a,abs(b))
        else: return mul(a,b)
    else:
        if a < 0:
            return -mul(b,abs(a))
        else: return mul(b,a)


print(multiply(-7,-9))


def flatten(l,i = 0):
    if len(l) > i:
        if type(l[i]) == list:
            l.extend(l[i])
            l.remove(l[i])
            flatten(l,i)
        else:
            flatten(l,i + 1)

l = [[1],[2,3,[4]]]
flatten(l)
print(l)


