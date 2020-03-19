# Given a set of k coins, this program determines whether we can provide a change for the given amount

import array


arr = array.array('i', [1])
sum_coin = array.array('i', [0])

k = int(input("No. of coins : \n"))
print "Now, enter the coins (other than 1): "
for i in range(1, k) :
    arr.append(int(input()))
    
for i in range(1, k) :
    sum_coin.append(0)

n = int(input("Next, enter the amount for the change : \n"))
val = n
i = k-1

while n>0 and i>=0 :
    if (n-arr[i]) >= 0 :
        sum_coin[i] = sum_coin[i] + 1
        n = n-arr[i]
        i = i-1

if n != 0 :
    print "Given amount cannot be exchanged!\n"
    
    for i in range(0, k) :
        if arr[i] != 0 :
            print arr[i], " coins :   ", sum_coin[i]
        
    print "Remaining Amount : ", n

else :
    print "The coin-exchange for '", val, "' are : \n "

    for i in range(0, k) :
        if arr[i] != 0 :
            print arr[i], " coins :   ", sum_coin[i]
