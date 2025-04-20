# Your task is to create function that checks whether a given string consists solely of valid hexadecimal characters. 
# An empty string should not be considered as a valid hex string.
# The standard numeral system is called decimal and is made up of 10 symbols: 0,1,2,3,4,5,6,7,8,9.
# The hexadecimal numeral system, often shortened to "hex", is a numeral system made up of 16 symbols.
# Hexadecimal uses the decimal numbers and six extra symbols. 
# There are no numerical symbols that represent values greater than nine, so letters taken from the English alphabet are used, namely: A (value 10), B (value 11), C (value 12), D (value 13), E (value 14), and F (value 15).
# In this exercise, both lowercase and uppercase representations are considered valid. However, an empty string is not considered a valid hex string.

import string

def is_hex_string(text):
    hex_digits = '0123456789abcdefABCDEF'
    count = 0
    length = len(text)
    if length == 0:
        return False
    else:
        for i in text:
            if i in hex_digits:
                count += 1
        
        if length == count:
            return True
        else:
            return False

print(is_hex_string('')) 
