class vector:
    # constructor to initialise the vector object
    # @param self: object -> reference to the class
    # object
    # @param x: int|float|double -> x component of
    # the vector
    # @param y: int|float|double -> y component of
    # the vector
    # OUTPUT: None
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # function to add two vectors
    # @param self: object -> reference to the class
    # object
    # @param vec: vector -> operand vector to add
    # OUTPUT: vector -> resultant vector

    def add(self, vec):
        return vector(self.x + vec.x, self.y + vec.y)

    # function to multiply two vectors
    # @param self: object -> reference to the class
    # object
    # @param vec: vector -> operand vector to multiply
    # OUTPUT: vector -> resultant vector
    def multiply(self, vec):
        return vector(self.x * vec.x, self.y * vec.y)

    # function to subtract two vectors
    # @param self: object -> reference to the class
    # object
    # @param vec: vector -> operand vector to subtract
    # OUTPUT: vector -> resultant vector
    def subtract(self, vec):
        return vector(self.x - vec.x, self.y - vec.y)

    # function to convert object into a string formar
    # @param self: object -> reference to the class
    # object
    # OUTPUT: str -> string form of object
    def __str__(self):
        return f"x: {self.x}, y: {self.y}"


# Taking input
x = float(input("Enter x component of vector1: "))
y = float(input("Enter y component of vector1: "))
vector1 = vector(x, y)
x = float(input("Enter x component of vector2: "))
y = float(input("Enter y component of vector2: "))
vector2 = vector(x, y)

# Printing results
print(f"Addition: {vector1.add(vector2)}")
print(f"Subtraction: {vector1.subtract(vector2)}")
print(f"Multiplication: {vector1.multiply(vector2)}")
