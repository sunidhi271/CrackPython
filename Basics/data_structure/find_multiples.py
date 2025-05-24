# Given a number and a limit, find all the mutiples of a number which are less than the limit, and print them in a list.

def find_multiples(num, limit):
    list = [] 
    multiple = num
    i = 1
    while multiple < limit:
        list.append(multiple)
        multiple += num
    
    return(list)
    

print(find_multiples(5, 22))

#For find_multiples(5, 22), the result should be [5, 10, 15, 20]
