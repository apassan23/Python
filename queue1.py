class Queue:
    # constructor
    # @param self: object reference
    # OUTPUT: None
    def __init__(self, max):
        self.front = -1
        self.rear = -1
        self.size = 0
        self.content = []
        self.MAX = max  

    # function to check if the queue is full
    # @param self: object reference
    # OUTPUT: bool
    def isFull(self):
        return (self.rear + 1) % self.MAX == self.front

    # function to check if the queue is empty
    # @param self: object reference
    # OUTPUT: bool
    def isEmpty(self):
        return self.front == -1

    # function to enqueue an element into the
    # queue
    # @param self: object reference
    # @param element: Any
    # OUTPUT: None
    def enqueue(self, element):
        if self.isFull():
            print("Error: Queue is full, can't enqueue '{}'".format(element))
            return

        # since initially front = -1
        if self.isEmpty():
            self.front += 1
            
        self.rear = (self.rear + 1) % self.MAX
        self.size += 1

        try:
            # if there was an element at the rear
            # previously
            self.content[self.rear] = element
        except IndexError:
            self.content.append(element)


    # function to dequeue an element from the rear
    # @param self: object reference
    # OUTPUT: Any
    def dequeue(self):

        if self.isEmpty():
            print("Error: Queue is Empty, can't dequeue")
            return

        # if there is only one element in the queue
        elif self.front == self.rear:
            element = self.content[self.front]
            self.rear = self.front = -1

        else:
            element = self.content[self.front]
            self.front = (self.front + 1) % self.MAX
            
    
        return element

    # __str__ function
    # @param self: object reference
    # OUTPUT: str    
    def __str__(self):
        display = ''
        if self.front <= self.rear:
            display = self.content[self.front:self.rear + 1].__str__()
        else:
           display = (self.content[self.front:self.MAX] + self.content[0:self.rear + 1]).__str__()
        return display

    # function to display the list
    # @param self: object reference
    # OUTPUT: None
    def display(self):
       print(self.__str__())

# taking input
size = int(input("Enter Max Size of the Queue: "))
q = Queue(size)
choice = 1
while choice != 3:
    print("1. Enqueue an Element")
    print("2. Dequeue an Element")
    print("3. Exit")
    choice = int(input("Select what you wanna do: "))
    if choice == 1:
        q.enqueue(eval(input("Enter an Element: ")))
    if choice == 2:
       element = q.dequeue()
       if not(q.isEmpty()):
           print("'{}' dequeued...".format(element))
    print("Queue: ", end='')
    q.display()
    print()