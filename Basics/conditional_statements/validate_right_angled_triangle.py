# your task is to create a Python function that determines whether the given lengths of three sides form a right-angled triangle or not.
# As per the Pythagorean theorem, in a right-angled triangle, the square of the length of the hypotenuse (the side opposite the right angle) is equal to the sum of the squares of the lengths of the other two sides.
# If any side has a non-positive length, it's not considered a valid triangle.


def is_right_angled_triangle(side1,side2,side3):
    if (side1 < 0) or (side2 < 0) or (side3 < 0):
        print("Invalid Entry")
        return False
    if (side1*side1 + side2*side2) == (side3*side3):
        return True
    if (side2*side2 + side3*side3) == (side1*side1):
        return True
    if (side3*side3 + side1*side1) == (side2*side2):
        return True
    else:
        return False

print(is_right_angled_triangle(3,4,5))
