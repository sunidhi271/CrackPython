# construct a Python function titled reverse_list that inverts a given list of integers without resorting to any built-in Python functions.

def reverse_list(list):
    start=0
    end=len(list) - 1
    
    while start < end:
        list[start], list[end] = list[end], list[start]    #This is called as teo pointer method. 
        start += 1 
        end -= 1 
    return list
        
#print(reverse_list([10, 20, 30]))
print(reverse_list([5, 15, 25, 35]))
#print(reverse_list([1]))
