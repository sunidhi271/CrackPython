# In this exercise, you are tasked with creating a function that determines whether a given integer is a prime number or not. 
# A prime number is only divisible by 1 and itself.
# 0 and 1 are not prime numbers.

def is_prime(number):
    div=0
    
    if number < 2:
        return False
    
    for i in range(2,number):
        if number % i == 0:
            return False
    return True


print(is_prime(0))
            
