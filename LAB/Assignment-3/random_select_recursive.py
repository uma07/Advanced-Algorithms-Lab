# This program is the implementation of RANDOMIZED-SELECT Algorithm in recursive version.

import random
import time



# Function to partition the given array
def partitioning(A, l, u) :

    x = A[u]
    i = l-1

    for j in range(l, u-1) :
        if A[j] <= x :
            i = i+1
            A[i], A[j] = A[j], A[i]

    A[i+1], A[u] = A[u], A[i+1]
    return i+1



# This function swaps before actually partition the array 'A'
def randomized_partition(A, l, u) :
    r = random.randint(l, u)
    A[r], A[u] = A[u], A[r]
    return partitioning(A, l, u)



# This function returns the 'k'th smallest element of the array A[l, ---, u]
def randomized_select(A, l, u, k) :

    if l == u :
        return A[u]

    pivot = randomized_partition(A, l, u)
    pos = pivot-l+1

    if pos == k :
        return A[pivot]

    elif k < pos :
        return randomized_select(A, l, pivot-1, k)

    else :
        return randomized_select(A, pivot+1, u, k-pos)




# Main program

i = 0

n = int(input("Enter number of elements you want to sort : "))

List =[]

for i in range(n):
    List.append(random.randint(1, n))

infile = open("input_list.txt", "w")
outfile = open("sorted.txt", "w")
infile.write("\tList : \n")
infile.write("\t=====\n")
infile.writelines([str(x) + ",\n" for x in List])

k = int(input("Enter the value of 'k' to find kth smallest element in 'A' : "))
start = time.time()

rand = randomized_select(List, 0, n-1, k)

end = time.time()

List.sort()
outfile.write("\tSorted List : \n")
outfile.write("\t============\n")
outfile.writelines([str(x) + ",\n" for x in List])

infile.close()
outfile.close()

print k, "th smallest element : ", rand
print "Time taken : ", end-start
