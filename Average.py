#Write a function to calculate the average of the numbers in a list of items using the built-in sum function

def average(n):
    total = sum(n)
    avg = total/len(n)
    return avg

n = (1,2,3,4,5)
print("Average:", average(n))