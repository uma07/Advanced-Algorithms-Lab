# Construction of Binary Search Tree for elements of distinct values in a recursive fashion.

DATA = 0
LEFT = 1
RIGHT = 2
PARENT = 3


# node structure : [DATA, LEFT, RIGHT, PARENT]


# Function for inserting a given elemnt in the tree
def insert(x, root, parent) :

    if root == None :
        root = [x, None, None, None]

    else :
        if root[DATA] > x :
            root[LEFT] = insert(x, root[LEFT], root)

        else :
            root[RIGHT] = insert(x, root[RIGHT], root)

    return root


# Function for printing the elements in the tree in preorder traversal fashion
def preorder_traversal(root) :

    s = []

    s.append(root)
        
    while len(s) != 0 :

        node = s.pop()

        if node == None :
            continue

        else :
            print(node[DATA])
            s.append(node[RIGHT])
            s.append(node[LEFT])



# Function for printing the elements in the tree in postorder traversal fashion
# 0 ---> traversal   &   1 ---> printing states
def postorder_traversal(root) :

    s = []

    s.append([root, 0])
        
    while len(s) != 0 :

        [node, state] = s.pop()

        if node == None :
            continue

        elif node != None and state == 0 :
            s.append([node, 1])
            s.append([node[RIGHT], 0])
            s.append([node[LEFT], 0])

        elif node != None and state == 1 :
            print(node[DATA])



# Function for printing the elements in the tree in inorder traversal fashion
def inorder_traversal(root) :

    s = []

    s.append([root, 0])
        
    while len(s) != 0 :

        [node, state] = s.pop()

        if node == None :
            continue

        elif node != None and state == 0 :
            s.append([node[RIGHT], 0])
            s.append([node, 1])
            s.append([node[LEFT], 0])

        elif node != None and state == 1 :
            print(node[DATA])



# MAIN PROGRAM

root = None
i = 0

n = int(input("Enter number of elements u want to keep in the Binary Search Tree :  "))

print("Now, enter the elements : ")

List =[]
for i in range(n) :
    List.append(int(input()))
    root = insert(List[i], root, None)

print("The elements in the tree are : \n")

print("Pre-order : ")
preorder_traversal(root)

print("In-order : ")
inorder_traversal(root)

print("Post-order : ")
postorder_traversal(root)
