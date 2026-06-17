class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)
root.right.left = Node(60)
root.right.right = Node(70)


def preorder(node): # Root -> Left -> Right

    if node is None:
        return

    print(node.data)
    preorder(node.left)
    preorder(node.right)

def inorder(node): # Left -> Root -> Right

    if node is None:
        return 
    
    inorder(node.left)
    print(node.data)
    inorder(node.right)

def postorder(node):
    
    if node is None:
        return

    postorder(node.left)
    postorder(node.right)
    print(node.data)

def height(node):

    if node is None:
        return -1
    
    left_height = height(node.left)
    right_height = height(node.right)

    tree_height = max(left_height, right_height) +1
    return tree_height

def count_nodes(node):

    if node is None:
        return 0
    
    left = count_nodes(node.left)
    right = count_nodes(node.right)

    count = left+right+1

    return count

def count_leaf(node):

    if node is None:
        return 0

    if node.left is None and node.right is None:
        return 1
    
    left = count_leaf(node.left)
    right = count_leaf(node.right)

    count = left+right
    return count



th = height(root)
print(th)
print("\n")
cn = count_nodes(root)
print(cn)
print("\n")
cl = count_leaf(root)
print(cl)
print("\n")
print("\n")
preorder(root)
print("\n")
inorder(root)
print("\n")
postorder(root)


