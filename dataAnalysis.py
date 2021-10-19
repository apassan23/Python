# importing matplotlib and numpy
import matplotlib.pyplot as plt
import numpy as np

# list for storing names and marks
marks = []

# function to plot scatterplots of the data
# @param mList: list
# OUTPUT: None
def plotScatter(mList):
    listKeys = list(mList[0].keys())
    col = 3
    # calculating rows for 3 columns
    rows = int(np.ceil((len(listKeys) - 1) / col))
    # extracting names of students to use as labels
    names = np.array(list(map(lambda x: x["name"], mList)))
    for i in range(1,len(listKeys)):
        # extracting marks from subjects
        y = np.array(list(map(lambda x: x[listKeys[i]], mList)))
        # subplot
        plt.subplot(rows, col, i)
        plt.scatter(names, y)
        # setting label
        plt.ylabel("Marks")
        plt.title(listKeys[i].capitalize())
    plt.show()

# function to plot histograms of the data
# @param mList: list
# OUTPUT: None
def plotHist(mList):
    listKeys = list(mList[0].keys())
    col = 3
    # calculating rows for 3 columns
    rows = int(np.ceil((len(listKeys) - 1) / col))
    for i in range(1, len(listKeys)):
        # extracting marks from subjects
        x = np.array(list(map(lambda x: x[listKeys[i]], mList)))
        # subplot
        plt.subplot(rows, col, i)
        plt.hist(x)
        # setting label
        plt.ylabel("Frequency")
        plt.title(listKeys[i].capitalize())
    plt.show()

# Taking input
n = int(input("Enter Number of Students: "))
subjects = input("Enter Subjects seperated by spaces: ").split()

for i in range(n):
    data = {}
    print("\n> Student {}".format(i + 1))
    name = input("Enter Student's Name: ")
    data["name"] = name
    for subject in subjects:
       data[subject] = eval(input("Enter marks in {}: ".format(subject)))
    marks.append(data)

print("1. Plot a ScatterPlot")
print("2. Plot a Histogram")
choice = int(input("Enter your choice: "))
if choice == 1:
    plotScatter(marks)
elif choice == 2:
    plotHist(marks)
else:
    print("Invalid Choice!")
