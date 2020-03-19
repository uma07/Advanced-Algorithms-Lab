# This program shows the implementation of the insertion sort using an array


i = 0

n = int(input("Enter number of elements you want to sort : \n"))

print("Now, enter the elements to sort : \n")

List =[]
for i in range(n):
        List.append(int(input()))


print(List)
i = 1           # Number of elements sorted till now (initially only 1 element is trivially sorted)

# Loop Invariant : At the start of each iteration of 1st 'while' loop, the subarray List[1,...,i] consists of elements originally in List[1,...,i], but in sorted order

while i < len(List) :
        key = List[i]
        j = i-1         # Present element that has to be sorted in the array

        while j >= 0 and key < List[j] :
                List[j+1] = List[j]             # To make progress towards the desired result
                j = j-1                         # To maintain the definition of j and List

        List[j+1] = key                         # To maintain the definition of i and List
        i = i+1


print("SORTED ARRAY : \n", List)
