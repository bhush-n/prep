"""
Stack is a linear data structure that follows the Last In First Out (LIFO) principle. 
It allows adding and removing elements from only one end, called the top of the stack. 
The main operations of a stack are push (to add an element), pop (to remove the top element), 
and peek (to view the top element without removing it). Stacks are commonly used in various applications such as 
expression evaluation, backtracking algorithms, and function call management in programming languages.
"""

class Stack:
    def __init__(self, stk):
        self.stk = stk

    def push(self):
        element = input("Enter the element: ")
        self.stk.append(element)
        print(self.stk)
    
    def pop(self):
        if len(self.stk) == 0:
            print("The stack is empty. You cannot pop the element")
        else:
            s = self.stk.pop()
            print(s)
    
    def peek(self):
        if len(self.stk) == 0:
            print("The stack is empty")
        else:
            print(self.stk[-1])
    
    def isEmpty(self):
        if len(self.stk) == 0:
            print("The stack is empty.")
        else:
            print("The stack is not empty")
        
    def search(self):
        element = input("Enter the element to search: ")
        for i in self.stk:
            if element == i:
                return element

stk = []
s = Stack(stk)

while True:
    choices = int(input("Enter the choice index. \n 1]Push \n 2]Pop \n 3]Peek \n 4]isEmpty \n 5]Search \n 6]Exit \n : "))
    if choices == 1:
        s.push()
    elif choices == 2:
        s.pop()
    elif choices == 3:
        s.peek()
    elif choices == 4:
        s.isEmpty()
    elif choices == 5:
        if s.search():
            print("The element is found")
    elif choices == 6:
        break
    else:
        print("Please enter the correct index")