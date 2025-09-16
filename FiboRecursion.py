#Write the Fibonacci function you wrote in the last submodule, but this time with recursion

def fibo_recursive(n):
    if n <= 0: #Base case
        return 0
    elif n == 1: #Base case
        return 1
    else:
        return fibo_recursive(n-1) + fibo_recursive(n-2) #recursive
terms = 10
print("Fibo_Recursion", fibo_recursive(terms))

        



