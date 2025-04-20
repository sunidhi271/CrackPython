# Print Factorial Of a number 
# Description: The factorial of a non-negative integer n is the product of all positive integers less than or equal to n. 
# It is represented by n!. 
# For instance, the factorial of 3 (denoted as 3!) is 3*2*1 = 6 and the factorial of 5 (denoted as 5!) is 5*4*3*2*1 = 120.

num=6
factorial=1

for i in range(num,0,-1):
    print(f"factorial = {factorial} * {i}")
    factorial *= i
    
print(f"Factorial of {num} = {factorial}")
