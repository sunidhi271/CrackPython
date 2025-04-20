# Calculate the Sum of Squares of First n Even Numbers

def sum_of_squares(n):
    val=0
    sum=0
    for i in range(n):     
        val += 2               #2, 4, 6
        sum += (val*val)       #4, 20, 56
    
    return(sum)

n=3
print(sum_of_squares(n))
