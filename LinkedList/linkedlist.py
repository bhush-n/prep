"""
Node1
data = 10
next = address of node2

Node2
data = 20
next = address of node3

Node3
data = 30
next = address of node4

Node4
data = 40
next = None


+------+------+
| 10   |  •----->

+------+------+
| 20   |  •----->

+------+------+
| 30   |  •----->

+------+------+
| 40   | None |
+------+------+

"""


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
    
    def insert_at_begin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_middle(self,pos,data):
        new_node = Node(data)

        if pos == 1:
            self.insert_at_begin(data)
            return
        
        temp = self.head

        for i in range(pos-2):
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node


    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        
        temp = self.head

        while temp.next:
            temp = temp.next
        temp.next = new_node
    
    def delete_at_begin(self):
        if self.head is None:
            print("Linked List is empty")
            return
        
        self.head = self.head.next
    
    def delete_at_end(self):
        temp = self.head

        while temp.next.next:
            temp = temp.next
        temp.next = None
        
    def display(self):
        temp = self.head

        while temp:
            print(temp.data)
            temp = temp.next

ll = LinkedList()
ll.insert_at_begin(20)
ll.insert_at_begin(10)
ll.insert_at_middle(1, 60)
ll.insert_at_end(30)

ll.display()

print("-----------------")
ll.delete_at_begin()
ll.delete_at_end()
ll.display()
