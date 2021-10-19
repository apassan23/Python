class Student:
    # counter for number of instances of 'Student'
    count = 0

    # constructor
    # @param self: object
    # @param rollNo: int
    # @param name: str
    # @param markList: list
    # OUTPUT: None
    def __init__(self, rollNo, name, markList):
        self.rollNo = rollNo
        self.name = name
        self.markList = markList
        Student.count += 1
        self.updatePercentage()
        self.updateGrade()

    # function to update percentage
    # @param self: object
    # OUTPUT: None
    def updatePercentage(self):
        self.percentage = float(sum(self.markList)) / len(self.markList)

    # function to update Grade
    # @param self: object
    # OUTPUT: None
    def updateGrade(self):
        if self.percentage > 90:
            self.grade = 'A+'
        elif self.percentage > 75:
            self.grade = 'A'
        elif self.percentage > 60:
            self.grade = 'B+'
        elif self.percentage > 50:
            self.grade = 'B'
        elif self.percentage > 40:
            self.grade = 'C'
        else:
            self.grade = 'FAIL'

    # roll no setter
    # @param self: object
    # @param rollNo: int
    # OUTPUT: None
    def setRollNo(self, rollNo):
        self.rollNo = rollNo

    # rollno getter
    # @param self: object
    # OUTPUT: int
    def getRollNo(self):
        return self.rollNo

    # name setter
    # @param self: object
    # @param name: str
    # OUTPUT: None
    def setName(self, name):
        self.name = name

    # name getter
    # @param self: object
    # OUTPUT: str
    def getName(self):
        return self.name

    # setter for marks
    # @param self: object
    # @param markList: list
    # OUTPUT: None
    def setMarks(self, markList):
        self.markList = markList
        self.updatePercentage()
        self.updateGrade()

    # getter for marks
    # @param self: object
    # OUTPUT: list
    def getMarks(self):
        return self.markList

    # getter for percentage
    # @param self: object
    # OUTPUT: float
    def getPercentage(self):
        return self.percentage

    # getter for grade
    # @param self: object
    # OUTPUT: str
    def getGrade(self):
        return self.grade

    # classmethod for getting count
    # @param cls: class reference
    # OUTPUT: int
    @classmethod
    def getCount(cls):
        return cls.count

    # Overriding __str__
    # @param self: object
    # OUTPUT: str
    def __str__(self):
        return '(Roll No: {}, Name: {}, Marks: {}, Percentage: {}, Grade: {})'.format(self.rollNo, self.name, self.markList, self.percentage, self.grade)

    # function to print details of the object
    # @param self: object
    # OUTPUT: None
    def printDetails(self):
        print(
            f"Roll No: {self.rollNo}\nName: {self.name}\nMarks: {self.markList}\nPercentage: {self.percentage}\nGrade: {self.grade}")
