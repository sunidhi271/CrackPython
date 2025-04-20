# Count Uppercase Letters
# Your task is to create a function that counts the number of uppercase letters in a given string.
# Here we use built in function - isupper()

def count_uppercase_letters(text):
    i = 0
    count = 0
    for ch in text:
        if ch.isupper() == True:    
            count += 1
    return count
    
print(count_uppercase_letters("Hello World! My Name is xyZ."))
            
