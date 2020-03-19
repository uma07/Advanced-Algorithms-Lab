# This program prints all primes smaller than or equal to n using Sieve of Eratosthenes

def SieveOfEratosthenes(n):

    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):

        if (prime[p] == True):

            for i in range(p * 2, n+1, p):
                prime[i] = False
        p += 1

    for p in range(2, n):
        if prime[p]:
            print (p)

# driver program
n = int(input("Enter the limit number for primes lesser : "))
print ("Following are the prime numbers smaller than or equal to", n)
SieveOfEratosthenes(n)

