# Finding the Next Fibonacci Number Exceeding a Threshold
# You are tasked with creating a Python function that identifies the first Fibonacci number that exceeds a given threshold number, using a while loop.
# So, if input threshold is 10, then its next fibbonacci number is 13.
# If input is -10, its next fibbonacci number is 0.

def next_fibonacci(threshold):
    a, b = 0, 1
    
    if threshold < 0:
        return(0)
    elif threshold == 0:
        return(1)
    elif threshold == 1:
        return(2)
    else:
        while a < threshold:
            print(a, end=" ")
            a, b = b, (a + b)
        return(a)
      
        
print(f"Next: {next_fibonacci(10)}")
