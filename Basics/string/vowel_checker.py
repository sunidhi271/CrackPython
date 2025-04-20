# Task is to create a function that determines whether a given character is a vowel or not.

def is_vowel(char):
    vowel = 'aeiouAEIOU'
    if char in vowel:
        return(True)
    else:
        return(False)
        
print(is_vowel('z'))
