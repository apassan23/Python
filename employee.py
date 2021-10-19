class Employee:
    # class variable to keep track of employee ID
    counter = 1

    # class constructor to initialise data members
    # @param self: object -> reference to the object
    # @param name: str -> name of the employee
    # @param designation: str -> designation of the employee
    # @param exp: int -> experience of the employee
    # OUTPUT: None
    def __init__(self, name, designation, exp):
        self.name = name
        self.empId = Employee.counter
        Employee.updateCounter()
        self.designation = designation.lower()
        self.exp = exp
        self.updateSalary()

    # class method to update class variable counter
    # @param cls: class -> reference to the class
    # OUTPUT: None
    @classmethod
    def updateCounter(cls):
        cls.counter += 1

    # utlity method to calculate/update salary
    # @param self: object -> reference to object
    # OUTPUT: None
    def updateSalary(self):
        base = 0
        if self.designation == 'worker':
            base = 10000
        elif self.designation == 'supervisor':
            base = 15000
        elif self.designation == 'manager':
            base = 20000

        # since salary = base+5%*base+exp%*base = (1 + 0.05 + exp/100) * base
        self.salary = (1.05 + (float(self.exp) / 100)) * base

    # setter to set name of the employee
    # @param self: object -> reference to the object
    # @param name: str -> name of the employee to update/set
    # OUTPUT: None
    def setName(self, name):
        self.name = name

    # getter to get name of the employee
    # @param self: object -> reference to the object
    # OUTPUT: str -> name of the employee
    def getName(self):
        return self.name

    # getter to get employee ID of the employee
    # @param self: object -> reference to the object
    # OUTPUT: int -> ID of the employee
    def getEmpID(self):
        return self.empId

    # setter to set the designation of the employee
    # @param self: object -> reference to the object
    # @param designation: str -> designation of the employee
    # OUTPUT: None
    def setDesignation(self, designation):
        self.designation = designation.lower()
        self.updateSalary()

    # getter to get the designation of the employee
    # @param self: object -> reference to the object
    # OUTPUT: str -> designation of the employee
    def getDesignation(self):
        return self.designation

    # setter to set experience of the employee
    # @param self: object -> reference to the object
    # @param exp: int -> experience to update/set
    # OUTPUT: None
    def setExperience(self, exp):
        self.exp = exp
        self.updateSalary()

    # getter to get the experience of the employee
    # @param self: object -> reference to the object
    # OUTPUT: int -> experience of the employee
    def getExperience(self):
        return self.exp

    # method to print all the details
    # @param self: object -> reference to the object
    # OUTPUT: None
    def show(self):
        print(f"Name: {self.name}\nEmployee ID: {self.empId}\nDesignation: {self.designation}\nSalary: {self.salary}\nExperience: {self.exp} years")

    # method to get the object in a string form
    # @param self: object -> reference to the object
    # OUTPUT: str -> object in string form
    def __str__(self):
        return f"Name: {self.name}, Employee ID: {self.empId}, Designation: {self.designation}, Salary: {self.salary}, Experience: {self.exp}"


# taking input
name = input("Enter Employee Name: ")
designation = input("Enter Employee Designation: ")
experience = int(input("Enter Experience: "))

emp = Employee(name, designation, experience)
print("\n=> Show Method")
emp.show()
print("\n__str__()")
print(emp)
