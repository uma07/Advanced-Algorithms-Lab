#This program is the implementation of the RANDOMIZE-IN-PLACE algorithm

import random



# Function that takes array 'A' as input and prints its randomized version

def randomize_in_place(A) :

    n = len(A)		# Length of array 'A'

    print "Random values : "

    i = 0		# Position at which the value to be randomized

    # Loop Invariant : At 'i'th iteration, A[0, ---, i-1] has randomized values.

    while i < n :
        r = random.randint(i, n-1)	# Return a random integer k such that i <= k <= n-1
        print r, " "
        A[i], A[r] = A[r], A[i]		# To make progress towards the desired result
        i = i+1				# To maintain the def. of 'i'

    print "After randomizing in place, A = ", A



# Main Program

A = []

n = int(input("Enter no. of elements u want to permute : "))

print "Now, enter the elements : "

for i in range(n) :
    A.append(int(input()))

print "A : ", A

randomize_in_place(A)
