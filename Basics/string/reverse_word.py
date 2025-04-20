# Word Reverser using For Loop
# Do NOT use the reversed function!

def reverse_word(word):
    length = len(word)
    reverse = ''
    for char in word:
        reverse = char + reverse
    return reverse
    
print(reverse_word("OpenAI"))
        
        
