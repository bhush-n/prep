"""
Circular Queue implementation in Python. 
A circular queue is a linear data structure that follows the First In First Out (FIFO) principle, 
but it connects the end of the queue back to the front, forming a circle. 
This allows for efficient use of space and prevents the need for shifting elements when enqueuing or dequeuing.
"""
class CircularQueue:

    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    def enqueue(self, value):

        # Queue Full
        if (self.rear + 1) % self.size == self.front:
            print("Queue Full")
            return

        # First element
        if self.front == -1:
            self.front = self.rear = 0

        else:
            self.rear = (self.rear + 1) % self.size

        self.queue[self.rear] = value
        print(f"{value} inserted")

    def dequeue(self):

        # Queue Empty
        if self.front == -1:
            print("Queue Empty")
            return

        item = self.queue[self.front]

        # Only one element present
        if self.front == self.rear:
            self.front = self.rear = -1

        else:
            self.front = (self.front + 1) % self.size

        print(f"Removed: {item}")

    def get_front(self):

        if self.front == -1:
            print("Queue Empty")
        else:
            print("Front:", self.queue[self.front])

    def get_rear(self):

        if self.rear == -1:
            print("Queue Empty")
        else:
            print("Rear:", self.queue[self.rear])

    def is_empty(self):

        if self.front == -1:
            print("Queue Empty")
        else:
            print("Queue Not Empty")

    def display(self):

        if self.front == -1:
            print("Queue Empty")
            return

        print("Queue Elements:")

        i = self.front

        while True:
            print(self.queue[i], end=" ")

            if i == self.rear:
                break

            i = (i + 1) % self.size

        print()


# Driver Code

size = int(input("Enter Queue Size: "))
cq = CircularQueue(size)

while True:

    print("\n1. Enqueue")
    print("2. Dequeue")
    print("3. Front")
    print("4. Rear")
    print("5. Display")
    print("6. Is Empty")
    print("7. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        value = int(input("Enter value: "))
        cq.enqueue(value)

    elif choice == "2":
        cq.dequeue()

    elif choice == "3":
        cq.get_front()

    elif choice == "4":
        cq.get_rear()

    elif choice == "5":
        cq.display()

    elif choice == "6":
        cq.is_empty()

    elif choice == "7":
        print("Program Ended")
        break

    else:
        print("Invalid Choice")