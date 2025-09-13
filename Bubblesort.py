#Bubble sort is a comparison-based algorithm in which each pair of adjacent elements is compared and swapped, if they are not in order. 

random_list = [25,5,10,95,75,55,15,65,12,24,16]
r = len(random_list)

for i in range(r-1):
    for j in range(r-i-1):
        if(random_list[j]) > (random_list[j+1]):
            random_list[j], random_list[j+1] = random_list[j+1], random_list[j]

print(random_list)
 

 
 
