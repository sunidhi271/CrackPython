# Check Consecutive Identical Characters in a string
# Here we use len() function to get the length of a string

def has_consecutive_identical_characters(text):
    
    total_ch = len(text)
    i = 0
    count = 0
    for i in range(0, total_ch - 2):
        if text[i] == text[i + 1]:
            return True
        else:
            i += 1 
    return False
    
        
print(has_consecutive_identical_characters('Helllo World!'))
        
        
        
        
        
    
    
    
    
