"""
Queue is a linear data structure that follows the First In First Out (FIFO) principle.
It allows adding elements at the rear end and removing elements from the front end.
The main operations of a queue are enqueue (to add an element), dequeue (to remove the front element),
and peek (to view the front element without removing it). Queues are commonly used in various applications such as
task scheduling, breadth-first search algorithms, and managing resources in computer systems.
"""

from collections import deque

class Queue:
    def __init__(self, que):
        self.que = que

    def enque(self):
        element = input("Enter the element: ")
        self.que.append(element)
        print(self.que)
    
    def dequeue(self):
        if len(self.que) == 0:
            print("The queue is empty cannot perform the operation")
        else:
            t = self.que.popleft()
            print(t)

    def rear_element(self):
        if len(self.que) == 0:
            print("The queue is empty cannot perform the operation")
        else:
            r = self.que[-1]
            print(r)
            
    def front(self):
        if len(self.que) == 0:
            print("The queue is empty cannot perform the operation")
        else:
            f = self.que[0]
            print(f)

    def isEmpty(self):
        if len(self.que) == 0:
            print("The queue is empty")
        else:
            print("The queue is not empty.")
    
que = deque()
q = Queue(que)

while True:
    choices = input("Enter the choice: \n 1]Enque \n 2]Dequeue \n 3]Rear Element \n 4]Front Element \n 5]isEmpty \n 6]Exit \n : ")
    if choices == '1':
        q.enque()
    elif choices == '2':
        q.dequeue()
    elif choices == '3':
        q.rear_element()
    elif choices == '4':
        q.front()
    elif choices == '5':
        q.isEmpty()
    elif choices == '6':
        break
    else:
        print("Invalid choice")
