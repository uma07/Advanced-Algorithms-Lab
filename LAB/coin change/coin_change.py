# This programs gives coin-exchange for the given input using 1, 2 and 5 rupees coins


i = 0
sum_1 = 0
sum_2 = 0
sum_5 = 0
extra = 0

n = int(input("Enter the amount for the change : \n"))
val = n

# sum_1, sum_5 & sum_2 are number of Rs.5, Rs.2 & Rs.1 coins in 'val-n'

# Loop Invariant : In 'while' loop, n+(sum_5*5)+(sum_2*2)+(sum_1*1) = val

while n>0 :
    if (n%5) == 0 :             # To progress towards the result
        sum_5 = sum_5 + 1       # To maintain the def. of sum_5
        n = n-5

    elif (n%2) == 0 :		# To progress towards the result
        sum_2 = sum_2 + 1	# To maintain the def. of sum_2
        n = n-2
        
    else :
        sum_1 = sum_1 +1	# To progress towards the result
        n = n-1			# To maintain the def. of sum_1


print "The coin-exchange for '", val, "' are : \n1's -> ", sum_1, "\n2's -> ", sum_2, "\n5's -> ", sum_5
