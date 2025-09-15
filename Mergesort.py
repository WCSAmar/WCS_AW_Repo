#Merge-sort first divides the array into equal halves, then combines them in a sorted manner. Write a program that sorts the array using merge-sort algorithm.
ls = [25,5,10,95,75,55,15,12,24]

def msort(ls):
    if len(ls) > 1: 
        mid = len(ls)//2
        #Diving array into equal halves
        left_half = ls[:mid]
        right_half = ls[mid:]
                
        msort(left_half)        
        msort(right_half)

        #Intializing counters for merging
        i = j = k = 0
 
        while i < len(left_half) and j < len(right_half):
            
            if left_half[i] < right_half[j]:
                ls[k] = left_half[i] 
                i += 1
            else:
                ls[k] = right_half[j]
                j += 1
            k += 1
        
        while i < len(left_half):
            ls[k] = left_half[i]
            i += 1
            k += 1
 
        while j < len(right_half):
            ls[k] = right_half[j]
            j += 1
            k += 1
    return ls

msort(ls)
print("Sorted List:",ls)

     

    

