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

    if root == None :
        print("Tree is empty !\n")
        
    else :
        print(root[DATA])

        if root[LEFT] != None :
            preorder_traversal(root[LEFT])

        if root[RIGHT] != None :
            preorder_traversal(root[RIGHT])




# Function for printing the elements in the tree in inorder traversal fashion
def inorder_traversal(root) :

    if root == None :
        print("Tree is empty !\n")
        
    else :
        if root[LEFT] != None :
            inorder_traversal(root[LEFT])

        print(root[DATA])

        if root[RIGHT] != None :
            inorder_traversal(root[RIGHT])




# Function for printing the elements in the tree in postorder traversal fashion
def postorder_traversal(root) :

    if root == None :
        print("Tree is empty !\n")
        
    else :
        if root[LEFT] != None :
            postorder_traversal(root[LEFT])

        if root[RIGHT] != None :
            postorder_traversal(root[RIGHT])

        print(root[DATA])



# Function for deleting an element in the tree
def delete(x, root) :

    if root == None :
        print("Tree is empty !\n")

    else :
        





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
