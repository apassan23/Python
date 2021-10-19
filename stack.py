from student import Student

class Stack:
    # class variable for max elements
    MAX = 3

    # constructor for initialisation
    # @param self: object
    # OUTPUT: None
    def __init__(self):
        # top of the stack
        self.tos = -1
        # list for storing elements
        self.content = []

    # function to check if stack is empty
    # @param self: object
    # OUTPUT: bool
    def isEmpty(self):
        return self.tos == -1

    # function to check if stack is full
    # @param self: object
    # OUTPUT: bool
    def isFull(self):
        return self.tos == (Stack.MAX - 1)

    # function to push an element onto the stack
    # @param self: object
    # @param element: Any
    # OUTPUT: None
    def push(self, element):
        if self.isFull():
            print("Error: Stack Overflow")
            return
        self.content.append(element)
        self.tos += 1

    # function to pop an element off the stack
    # @oaram self: object
    # OUTPUT: Any
    def pop(self):
        if self.isEmpty():
            print("Error: Stack Underflow")
            return

        element = self.content[self.tos]
        del self.content[self.tos]
        self.tos -= 1
        return element

    # function to get the element at the top of
    # stack
    # @param self: object
    # OUTPUT: Any
    def peek(self):
        return self.content[self.tos]

    # function to get number of elements in the
    # stack
    # @param self: object
    def size(self):
        return self.tos + 1

    # overriding __str__
    # @param self: object
    # OUTPUT: str
    def __str__(self):
        if not(stack.isEmpty()) and type(self.content[0]) == Student:
            return "\n".join([x.__str__() for x in self.content]) 
        return self.content.__str__()


# creating the stack instance
stack = Stack()

choice = 1

while choice != 5:
    print("\n1. Push an Item")
    print("2. Pop an Item")
    print("3. Display the contents of Stack")
    print("4. Peek")
    print("5. Exit")
    choice = int(input("Choice: "))
    if choice == 1:
        name = input("Enter Name: ")
        rollNo = int(input("Enter Roll No.: "))
        marks = [int(x) for x in input("Enter Marks seperated by whitespaces: ").split()]
        stack.push(Student(rollNo, name, marks))
    elif choice == 2:
        stack.pop()
    elif choice == 3:
        print("Stack Contents: ", stack)
    elif choice == 4:
        print(stack.peek())
