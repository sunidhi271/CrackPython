# Calculate the Sum of Divisors
# Description: your task is to create a Python function that calculates the sum of all divisors of a given integer number.

def calculate_sum_of_divisors(number):
    sum=0
    if number <= 0:
        return sum
    else:
        for i in range(1, number+1):
            if number % i == 0:
                sum += i
        return sum
                

print(f"Sum of devisors of number: {calculate_sum_of_divisors(2)}")
