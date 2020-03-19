# This programs gives the number of ways the coin-exchanges can be done for 2 and 5 rupees coins to the given input


i = 0
sum_2 = 0
sum_5 = 0
extra = 0

n = int(input("Enter the amount for the change : \n"))
val = n

# sum_5 & sum_2 are number of Rs.5 & Rs.2 coins in 'val-n'

# Loop Invariant : In 'while' loop, n+(sum_5*5)+(sum_2*2) = val

while n>0 :
    if (n%5) == 0 :             # To progress towards the result
        sum_5 = sum_5 + 1       # To maintain the def. of sum_5
        n = n-5

    else :			# To progress towards the result
        sum_2 = sum_2 + 1	# To maintain the def. of sum_5
        n = n-2


print("The coin-exchange for '", val, "' are : \n2's -> ", sum_2, "\n5's -> ", sum_5)
