class Complex:
    # counter to maintain object count
    counter = 0
    # constructor
    # @param self: object reference
    # @param real: int|float|double
    # @param imag: int|float|double
    # OUTPUT: None
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
        Complex.counter += 1
    
    # overloading operator _add__
    # @param self: object reference
    # @param c2: Complex
    # OUTPUT: Complex
    def __add__(self, c2):
        return Complex(self.real + c2.real, self.imag + c2.imag)

    # overloading operator __mul__
    # @param self: object reference
    # @param c2: Complex
    # OUTPUT: Complex
    def __mul__(self, c2):
        return Complex((self.real * c2.real) - (self.imag * c2.imag), (self.real * c2.imag) + (self.imag * c2.real))

    # overriding __str__
    # @param self: object reference
    # OUTPUT: str
    def __str__(self):
        return "{} + {}i".format(self.real, self.imag)

    # getter to get the real part of the complex number
    # @param self: object reference
    # OUTPUT: int|float|double
    def getReal(self):
        return self.real

    # getter to get the imaginary part of the complex number
    # @param self: object reference
    # OUTPUT: int|float|double
    def getImaginary(self):
        return self.imag

    # class method to get class variable counter
    # @param cls: class reference
    # OUTPUT: int
    @classmethod
    def getCount(cls):
        return cls.counter

# Taking input
print("Complex Number 1....")
real = eval(input("Enter Real Part: "))
imag = eval(input("Enter Imaginary Part: "))
c1 = Complex(real, imag)
print("\nComplex Number 2....")
real = eval(input("Enter Real Part: "))
imag = eval(input("Enter Imaginary Part: "))
c2 = Complex(real, imag)

print("1. Add the 2 Complex Numbers")
print("2. Multiply the 2 Complex Numbers")
print("3. Get Real and Imaginary Parts")
print("4. Get Number of object of Complex Created")
choice = int(input("Enter your choice: "))
if choice == 1:
    print("Result: {}".format(c1 + c2))
elif choice == 2:
    print("Result: {}".format(c1 * c2))
elif choice == 3:
    print("For Complex Number 1")
    print("Real part: {}".format(c1.getReal()))
    print("Imaginary Part: {}".format(c1.getImaginary()))
    print("\nFor Complex Number 2")
    print("Real part: {}".format(c2.getReal()))
    print("Imaginary Part: {}".format(c2.getImaginary()))
elif choice == 4:
    print("Count: {}".format(Complex.getCount()))