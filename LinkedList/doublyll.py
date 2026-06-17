class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLL:
    def __init__(self):
        self.head = None

    def add_at_begin(self, data):
        new_node = Node(data)
        if self.head is not None:
            self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node

    def add_at_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        temp = self.head

        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp

    def delete_at_begin(self):
        if self.head is None:
            print("DLL Empty")
            return

        if self.head.next is None:
            self.head = None
            return
        self.head = self.head.next
        self.head.prev = None

    def delete_at_end(self):
        if self.head is None:
            print("Dl is empty")

        temp = self.head

        while temp.next:
            temp = temp.next
        temp.prev.next = None

    def forward_traverse(self):
        temp = self.head

        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next

    def backward_traverse(self):
        temp = self.head
        while temp.next:
            temp = temp.next

        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.prev


dll = DoublyLL()
dll.add_at_begin(10)
dll.add_at_begin(20)
dll.add_at_begin(30)
dll.add_at_end(60)
dll.forward_traverse()
print("\n")
dll.backward_traverse()
print("\n")
dll.delete_at_begin()
print("\n")
dll.forward_traverse()
print("\n")
dll.delete_at_end()
print("\n")
dll.forward_traverse()
