# This program shows the implementation of the quick sort using an array input given by user

# Boundary : n = 0, 1
# Exception : n is a -ve number
# Alternative :
# Normal :


# Function to partition the given array

def partitioning(arr, l, u) :
    i = l+1             # Stating position in array(subarray)
    pivot = arr[l]      # Starting element in arr is pivot
    j = u               # Last position in array(subarray)

    while(i <= j):

        if arr[i] <= pivot:     # To make progress towards the desired result
            i = i+1             # To maintain the def of i in arr

        elif arr[j] > pivot:    # To make progress towards the desired result
            j = j-1             # To maintain the def of j in arr

        else :
            arr[i], arr[j] = arr[j], arr[i]     # To make progress towards the desired result
            i = i+1             # To maintain the def of i in arr
            j = j-1             # To maintain the def of j in arr

    arr[l], arr[j] = arr[j], arr[l]
    return j


# Function to do quick sort for the given array

def quick_sort(arr, l, u) :

    if l < u:
        p = partitioning(arr, l, u)

        if(l!=p):
            quick_sort(arr, l, p-1)

        if(p!=u):
            quick_sort(arr, p+1, u)



# Main function

k = 0

n = int(input("Enter number of elements you want to sort : "))

print("Now, enter the elements to sort : ")
List =[]
for k in range(n):
    List.append(int(input()))


print(List)


quick_sort(List, 0, n-1)


print(List)

