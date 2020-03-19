# randomized selection ---> 'i'th smallest element. comparison spreads the infection.

import random
import time



# Function to partition the given array
def partitioning(A, d, l, u) :

    x = A[u]
    i = l-1

    for j in range(l, u-1) :
        if A[j] <= x :
            i = i+1
            A[i], A[j] = A[j], A[i]

            if d[i] == 0 or d[j] == 0 :
                d[i] = d[j] = 0

    A[i+1], A[u] = A[u], A[i+1]
    return i+1



# This function swaps before actually partition the array 'A'
def randomized_partition(A, d, l, u) :

    r = random.randint(l, u)
    A[r], A[u] = A[u], A[r]

    if d[l] == 0 or d[u] == 0 :
        d[l] = d[u] = 0

    return partitioning(A, d, l, u)



# This function returns the 'k'th smallest element of the array A[l, ---, u]
def randomized_select(A, d, l, u, k) :

    if l == u :
        return A[u]

    pivot = randomized_partition(A, d, l, u)
    pos = pivot-l+1

    if pos == k :
        return A[pivot]

    elif k < pos :
        return randomized_select(A, d, l, pivot-1, k)

    else :
        return randomized_select(A, d, pivot+1, u, k-pos)




# Main program

i = 0
count1 = 0

n = int(input("Enter number of elements you want to sort : "))

List =[]
dis = []

for i in range(n) :
    List.append(random.randint(1, n))
    dis.append(1)

dis[0] = 0
infile = open("input_list.txt", "w")
outfile = open("sorted.txt", "w")

infile.write("\tList : \n")
infile.write("\t=====\n")
infile.writelines([str(x) + ",\n" for x in List])

infile.write("\tInfection Array : \n")
infile.write("\t================\n")
infile.writelines([str(y) + ",\n" for y in dis])

k = int(input("Enter the value of 'k' to find kth smallest element in 'A' : "))
start = time.time()

rand = randomized_select(List, dis, 0, n-1, k)

i = 0
for i in range(n) :
    if dis[i] == 0 :
        count1 = count1+1

end = time.time()

List.sort()
outfile.write("\tSorted List : \n")
outfile.write("\t============\n")
outfile.writelines([str(x) + ",\n" for x in List])

outfile.write("\tSorted Infection Array : \n")
outfile.write("\t=======================\n")
outfile.writelines([str(y) + ",\n" for y in dis])

infile.close()
outfile.close()

print k, "th smallest element : ", rand
print "Number of infected species : count1 = ", count1
print "Time taken : ", end-start
