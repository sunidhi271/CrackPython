# Calculate the Sum of Squares Up to a Limit
# Description: Your goal is to compute the sum of squares of numbers up to a specified limit.

def sum_of_squares_upto_limit(limit):
    i = 1
    sum = 0
    
    while i*i <= limit:
        sum += i * i
        i += 1 

    return sum
    
print(sum_of_squares_upto_limit(30))
