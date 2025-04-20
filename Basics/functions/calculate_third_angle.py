#  Calculate the Third Angle of a Triangle

def calculate_third_angle(a,b):
    first_angle = a
    second_angle = b
    third_angle = 180 - (first_angle + second_angle)
    return(third_angle)
    
print(f"Third angle is: {calculate_third_angle(30,90)}")
