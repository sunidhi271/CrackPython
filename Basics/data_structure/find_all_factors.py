# Create a Python function named find_factors that determines all the factors of a given integer.
# Output should be a list of integers which are factors of the given number.

def find_factors(n):
    list = []          #This is how we declare a list
    i = 1
    while i <= n:
        if n % i == 0:
            list += [i] 
            # list.append(i)  #This is another way to add values to the list
        i += 1 
    return(list)
    
print(find_factors(0))   #Prints: []
print(find_factors(12))  # Output: [1, 2, 3, 4, 6, 12]
    
