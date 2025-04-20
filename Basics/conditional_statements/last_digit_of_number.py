# Find Last Digit of a Number

def get_last_digit(n):
    last = n % 10
    return(last)
  
num=1056
print(f"Last digit of {num} is {get_last_digit(num)}")
