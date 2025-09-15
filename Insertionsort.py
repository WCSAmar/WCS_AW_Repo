#The Insertion-sort function involves finding the correct place for a given element in a sorted list. 
# This process begins with comparing and sorting the first two elements. 
# A third element is then compared to the two previously sorted elements and found its proper position among them. 
# This way, more elements gradually added to a continuously sorted list by inserting them into their proper positions. 
# Write a program that sorts an array using the insertion-sort algorithm.
#
ls = [23,45,5,2,7]
for index in range (1, len(ls)):
    element = ls[index] #element to be inserted
    m = index - 1

    while m>=0 and element < ls[m]:
        ls[m + 1] = ls[m]
        print("ls(m+1):",ls[m+1],"ls[m]",ls[m])
        m -= 1
    ls[m +1] = element

print(ls)