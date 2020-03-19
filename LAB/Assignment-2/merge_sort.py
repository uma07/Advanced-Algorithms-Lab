# This program implements the merge sort in a recursive fashion for a given unsorted array


import math


# Loop invariant : At the start of each iteration of 'while' loop, subarray arr[1,...,k-1] will be sorted. Also, left[i] and right[j] are the smallest elements in their
#                  respective arrays.

# Boundary Condition : n = 0, 1
# Exception Condition : n is a -ve number
# Alternative :
# Normal :


# Function to merge 2 sub-arrays

def merge(left, right, arr) :
    i = 0       # Current position in 'left' array
    j = 0       # Current position in 'right' array
    k = 0       # Current position in 'arr' array

    while (i < len(left) and j < len(right)) :
        if(left[i] < right[j]):
            arr[k] = left[i]    # To make progress towards the desired result
            i = i+1             # To maintain the def of i in left

        else :
            arr[k] = right[j]   # To make progress towards the desired result
            j = j+1             # To maintain the def of j in right

        k = k+1         # To maintain the def of k in arr

    while(i < len(left)) :
        arr[k] = left[i]        # To make proress towards the desired result
        i = i+1                 # To maintain the def of i in left
        k = k+1                 # To maintain the def of k in arr

    while(j < len(right)) :
        arr[k] = right[j]       # To make proress towards the desired result
        j = j+1                 # To maintain the def of j in right
        k = k+1                 # To maintain the def of k in arr




# Function to divide and call the above merge function

def mergesort(arr) :
    n = len(arr)

    if(n < 2):
        return

    center = math.floor(n/2)
    left = []
    right = []

    for i in range(center) :
        number = arr[i]
        left.append(number)

    for i in range(center,n) :
        number = arr[i]
        right.append(number)

    mergesort(left)
    mergesort(right)

    merge(left,right,arr)






# Main function


k = 0


n = int(input("Enter number of elements you want to sort : "))

print("Now, enter the elements to sort : ")

arr =[]

for k in range(n) :
    arr.append(int(input()))


print("Given Array is  : ", arr)


mergesort(arr)


print("Sorted Array is : ", arr)

