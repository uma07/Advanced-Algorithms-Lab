# This program is the implementation of the PERMUTE-BY-SORTING randomized algorihm.

import random


# Function that sorts the given array 'A' by applying the bubble sort

def bubble_sort(A, P) :

    for i in P:
        j = P.index(i)		# P.index() finds the given element in P and returns its position

        while j > 0 :

            if P[j-1] > P[j] :
                P[j-1],P[j] = P[j],P[j-1]
                A[j-1],A[j] = A[j],A[j-1]

            else :
                break

            j = j-1

    return A



# Function that randomizes the input by permuting the given input array
def permute_by_sorting(A) :

    n = len(A)
    P = []

    for i in range(n) :
        r = random.randint(1, n*n*n)
        if r not in P :
            P.append(r)

    print "P : ", P
    A = bubble_sort(A, P)

    print "After permuting, A = ", A




# Main Program

A = []

n = int(input("Enter no. of elements u want to permute : "))

print("Now, enter the elements : ")

for i in range(n) :
    A.append(int(input()))

print "A : ", A

permute_by_sorting(A)
