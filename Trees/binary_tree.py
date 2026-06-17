class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


root = Node(50)
root.left = Node(30)
root.left.left = Node(10)
root.left.right = Node(20)

root.right = Node(70)
root.right.left = Node(60)
root.right.right = Node(90)



def search(node, target):

    if node is None:
        return False
    
    if node.data == target:
        return True
    
    if target < node.data:
        return search(node.left, target)
    return search(node.right, target)

def insert(node, val):

    if node is None:
        return Node(val) 
    
    if val < node.data:
        node.left = insert(node.left, val)
    else:
        node.right = insert(node.right, val)
    return node

def inorder(node):
    if node is None:
        return 
    
    inorder(node.left)
    print(node.data)
    inorder(node.right)

s = search(root, 60)
print(s)

i = insert(root, 25)
# print(i.data)

inorder(root)
