# Calculate Simple Interest
# To calculate the total amount with simple interest over a specific duration, we use the formula:
# total = principal + (principal * interest * 0.01 * duration)

def calculate_simple_interest(principal,duration,interest):
    total = principal + (principal * interest * 0.01 * duration)
    return total
    
print(calculate_simple_interest(1000,5,5))
