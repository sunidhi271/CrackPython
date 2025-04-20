#  Find the Longest Word in a given sentence.

def find_longest_word(text):
    i = 0
    largest = 0
    length = len(text)
    if length == 0:
        return ''
    else:
        words = text.split()
        for word in words:
            word_size = len(word)
            if word_size > largest:
                largest = len(word)
                largest_word = word
        return (largest_word)
        
print(find_longest_word('The quick brown fox jumps over the lazy dog'))
            
