# This program takes input two numbers and outputs their quotient and reamainder using euclid's algorithm (a = bq+r)

# Boundary :
# Exception : b = 0
# Alternative : b = 1
# normal :


a = int(input("Enter the value of first number (a)  : "))
b = int(input("Enter the value of second number (b) : "))


q = 0           # To satisfy a = bq+r (initially)
r = a           # To satisfy a = bq+r (initially)


while r >= b :
        r = r-b         # To make progress towards the desired result
        q = q+1         # To maintain the definition of r and q


print("Quotient  : ", q, "\nRemainder : ", r, "\n")

