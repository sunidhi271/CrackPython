# Check for a Valid Triangle
# Description: your task is to create a Python function that checks if the three given angles can form a valid triangle.
# An angle cannot be less than or equal to 0.

def is_valid_triangle(a,b,c):
    angle1=a
    angle2=b
    angle3=c
    
    if angle1>0 or angle2>0 or angle3>0:
        sum=angle1+angle2+angle3
        if sum == 180:
            return True
        else:
            return False
    else:
        return False
     
is_valid_triangle(100,50,30)   
        
