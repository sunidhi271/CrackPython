# Check if a Year is a Leap Year
# Description: A year is a leap year in the Gregorian calendar if:
# - It is divisible by 4 (AND)
# - It is NOT divisible by 100 (except when it is divisible by 400)
# means, If divisible by 4 and divisible by 100 and divisible by 400 - Leap Year
# If divisible by 4 and not divisible by 100, - Leap Year

def is_leap_year(year):
    if (year % 4) == 0:
        print("condition 1")
        if (year % 100) == 0:
            print("condition 2")
            if (year % 400) == 0:
                print("condition 3")
                return True
            else:
                print("condition 4")
                return False
        else:
            print("condition 5")
            return True
    else:
        print("condition 6")
        return False
        
print(is_leap_year(2300))
