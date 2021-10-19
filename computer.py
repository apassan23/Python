from typing import Counter


class Computer:

    count = 0

    def __init__(self, cpu, ram, color, brand):
        self.cpu = cpu
        self.ram = ram
        self.color = color
        self.brand = brand
        Computer.count += 1

    def getCPU(self):
        return self.cpu

    def getBrand(self):
        return self.brand

    def getRAM(self):
        return self.ram

    def getColor(self):
        return self.color

    def setCPU(self, cpu):
        self.cpu = cpu

    def setBrand(self, brand):
        self.brand = brand

    def setRAM(self, ram):
        self.ram = ram

    def setColor(self, color):
        self.color = color

    @classmethod
    def getCount(cls):
        return cls.count

    def compare(self, obj):
        return ((self.cpu == obj.cpu) and (self.color == obj.color) and (self.brand == obj.brand) and (self.ram == obj.ram))

    def displayDetails(self):
        print(
            f"Processor: {self.cpu}\nRAM: {self.ram}GB\nColor: {self.color}\nBrand: {self.brand}")


pc = Computer('Ryzen 5 1600', 16, 'Black', 'AMD')
pc2 = Computer('i9 10900k', 16, 'white', 'Lenovo')
pc.displayDetails()
pc2.displayDetails()
print(f"Number of Objects: {pc.getCount()}")
print(pc.compare(pc2))
