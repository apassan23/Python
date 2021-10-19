class Laptop:
    # class constructor to initialise data members
    # @param self: object -> reference to the object
    # @param brand: str -> brand of the laptop
    # @param ram: int -> Amount of memory installed in GB
    # @param color: str -> color of the laptop
    # OUTPUT: None
    def __init__(self, brand, processor, ram, color):
        self.brand = brand
        self.processor = processor
        self.ram = ram
        self.color = color

    # setter to set the brand of the laptop
    # @param self: object -> reference to the object
    # @param brand: str -> brand of the laptop
    # OUTPUT: None
    def setBrand(self, brand):
        self.brand = brand

    # getter to get brand of the laptop
    # @param self: object -> reference to the object
    # OUTPUT: str -> brand of the laptop
    def getBrand(self):
        return self.brand

    # setter to set the processor
    # @param self: object -> reference to the object
    # @param processor: str -> processor of the laptop
    # OUTPUT: None
    def setProcessor(self, processor):
        self.processor = processor

    # getter to get the processor of the laptop
    # @param self: object -> reference to the object
    # OUTPUT: str -> processor of the laptop
    def getProcessor(self):
        return self.processor

    # setter to set the RAM of laptop
    # @param self: object -> reference to the object
    # @ram: int -> RAM installed in GBs
    # OUTPUT: None
    def setRAM(self, ram):
        self.ram = ram

    # getter to get the RAM of the laptop
    # @param self: object -> reference to the object
    # OUTPUT: int -> RAM installed in GBs
    def getRAM(self):
        return self.ram

    # setter to set the color of the laptop
    # @param self: object -> reference to the object
    # @param color: str -> color of the laptop
    # OUTPUT: None
    def setColor(self, color):
        self.color = color

    # getter to get the color of laptop
    # @param self: object -> reference to the object
    # OUTPUT: str -> color of the laptop
    def getColor(self):
        return self.color

    # method to print all the details
    # @param self: object -> reference to the object
    # OUTPUT: None
    def show(self):
        print(
            f"Brand: {self.brand}\nProcessor: {self.processor}\nRAM: {self.ram}\ncolor: {self.color}")

    # method to get the object in a string form
    # @param self: object -> reference to the object
    # OUTPUT: str -> object in string form
    def __str__(self):
        return f"Brand: {self.brand}, Processor: {self.processor}, RAM: {self.ram}, color: {self.color}"


# taking input
brand = input("Enter brand: ")
cpu = input("Enter Processor: ")
ram = int(input("Enter Amount of RAM installed: "))
color = input("Enter Color of the laptop: ")

laptop = Laptop(brand, cpu, ram, color)
print(laptop)
