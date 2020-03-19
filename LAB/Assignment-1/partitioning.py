# The following program partitions the given list with respect to the given element.

i = 0

n = int(input("Enter number of elements you want to keep in the list : "))

print("Now, enter the elements of the list : ")

List =[]
for i in range(n):
        List.append(int(input()))

x = int(input("Next, enter the element to partition the given list : "))


i = 0                   # Starting position of the array (or subarray)
j = n-1                 # Ending position of the array (or subarray)

# Loop Invariant : All the elements in List[0,...,i-1] and List[j+1,...,n-1] are partitioned

while(i <= j):
        if List[i] <= x:        # To make progress towards the desired result
                i = i+1         # To maintain the definition of i in List

        if List[j] > x:         # To make progress towards the desired result
                j = j-1         # To maintain the definition of j in Limit

        else :
                List[i], List[j] = List[j], List[i]
                i = i+1         # To maintain the definition of i in Limit
                j = j-1         # To maintain the definition of j in Limit

        print(List)


print("Partitioned list : ", List)
print("And the partitioning happens at position : ", i+1)
