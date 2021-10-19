# file handling
# file open, read, close

# 'r': read
# 'w': write
# 'a': append
# 'x': creating a file (will throw an error if already in existence)
# 't': text
# 'b': binary
file = open("dummy.txt")
# read takes an optional argument: the number of characters to read
print(file.read(3))
# tell returns the position of the file pointer
print(file.tell())
# seek changes the position of the file pointer
file.seek(0)
print(file.readline())
file.close()
