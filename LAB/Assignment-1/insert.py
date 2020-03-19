# This program inserts the given element in it's correct position in an ascendingly ordered array


i = 0

n = int(input("Enter number of elements you want to keep in the list : \n"))

print("Now, enter the elements of the list in the ascending order : \n")


List =[]
for i in range(n):
        List.append(int(input()))

print(List)

x = int(input("Next, enter the element to insert in the given list : \n"))


List.append(x)
limit = n;              # Length of the array

# Loop Invariant : At the end of 'while loop', all the elements in List[limit, ... ,n] are sorted in ascending order and limit is the position of x 

while limit > 0 :
        if List[limit-1] > x:
                List[limit], List[limit-1] = List[limit-1], List[limit]         # To make progress

        limit = limit-1                 # To maintain the definition of limit in the array
        print(List)


print("After inserting '", x , "' in the array and sorting it : \n", List)

