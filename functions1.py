def inputMarks(numMarks):
    marksList = []
    for i in range(numMarks):
        m1 = int(input(f"Enter Marks for Student {i+1}: "))
        marksList.append(m1)
    return marksList


def validateMarks(marks):
    for i in marks:
        if not(i >= 0 and i <= 100):
            return False
    return True


totalMarks = []
numStudent = int(input("Enter Number of Students: "))
print("Enter Marks in Subject 1")
marks1 = inputMarks(numStudent)
print("Enter Marks in Subject 2")
marks2 = inputMarks(numStudent)

if not(validateMarks(marks1)) or not(validateMarks(marks2)):
    print("Invalid Marks")

else:
    for i in range(numStudent):
        totalMarks.append(marks1[i] + marks2[i])

print(totalMarks)
