# This program implements the min-max problem for the given input which is stored in an array.

# Boundary Condition : n = 1
# Exception : n is a -ve number
# Alternative : 
# Normal :


import math


# Function to find min and max of the given array

def min_max(arr, l, u) :
    print(u,l)
    if u == l+1 or u == 1:
        l = int(l)
        u = int(u)
        if arr[l] < arr[u] :
            Min = arr[l]
            Max = arr[u]

        else :
            Min = arr[u]
            Max = arr[l]

    else :
        (Min1, Max1) = min_max(arr, l, int((l+u)/2))
        (Min2, Max2) = min_max(arr, int((l+u)/2), u)

        if Min1 < Min2 :
            Min = Min1

        else :
            Min = Min2

        if Max1 < Max2 :
            Max = Max2

        else :
            Max = Max1

    return (Min,Max)




# Main function

k = 0

n = int(input("Enter the size of the array to find MIN-MAX : "))

print("Now, enter the elements of the array : ")

arr = []

for k in range(n) :
    arr.append(int(input()))


print("Given array : ", arr)


(Min,Max) = min_max(arr, 0, n-1)


print("Minimum and Maximum elements in the given array are : ", Min, "  &  ", Max, " respectively")

