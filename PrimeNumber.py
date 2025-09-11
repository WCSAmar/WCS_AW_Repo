#Prime Numbers
n1 = 2
n2 = int(input("User Input:"))

for prime in range(n1, n2+1):
     
    for i in range(2, prime):
         
        if (prime % i) == 0:
            break
    else:
        print(prime)