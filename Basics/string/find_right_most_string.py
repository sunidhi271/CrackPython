# your task is to create a function that returns the right-most digit found in a given string.

import string

def find_right_most_digit(text):
    size = len(str(text))
    
    for char in reversed(text):
        if char.isdigit():
            return int(char)
    return -1

# OR
# def find_right_most_digit(text):
#    size = len(str(text))
#    if text[size - 1].isdigit() == True:
#        return text[size - 1]
#    else:
#        return -1

print(find_right_most_digit('The value is here 234.0'))
