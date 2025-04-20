# Find the Number of Digits in a Number

def get_number_of_digits(number):
    number_of_digits=0
    if number == 0:
        return 1 
    if number < 0:
        return -1
    
    while number > 0:
        number = number // 10   # gets the remainder
        number_of_digits +=1 
    
    return(number_of_digits)

print(get_number_of_digits(123))    
    
