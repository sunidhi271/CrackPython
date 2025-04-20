# your task is to create a function that checks whether two given strings are anagrams of each other. 
# An anagram is a word or phrase formed by rearranging the letters of a different word or phrase.
# You can assume that the input strings only contain lowercase alphabets.

import string

def is_anagram(string1,string2):
    if sorted(string1) == sorted(string2):
        return True
    else:
        return False

print(is_anagram('hello', 'world'))
            

