# Check if a Number is a Perfect Number
# Description: A perfect number is a positive integer that is equal to the sum of its positive divisors, excluding itself.

def is_perfect_number(number):
    sum = 0
    if number <= 0:
        return False
    else:
        for i in range(1,number):
            if number % i == 0:
                sum += i
        if sum == number:
            return True
        else:
            return False

num = 6 
if is_perfect_number(num):
    print(f"{num} is a Perfect Number !")
else:
    print(f"{num} is Not a Perfect Number")
