# LIST is a type od datastructure which makes storing data very easy and using this calculations also becomes very easy.
# List is defined like this - marks = [99, 95, 100 ,85, 92]
# pre-defined functions that can be used with LIST
# print(sum(marks))
# print(len(marks))
# print(max.marks))
# print(min.marks))
# print(marks.index(85))
# To add a new value to the list - append.marks(97)
# To append value to a specific index - insert.marks(0,75)
# To see marks of a specfic index - print(marks[0])


#Q: your task is to create a Python function named has_greater_element that checks whether there is any number greater than a given value in a list of numbers.

def has_greater_element(numbers, value):
    if len(numbers) == 0:
        return False
    else:
        for num in numbers:
            if num > value:
                return True
                break
        return False


list_of_numbers1 = [10,30,55,6,99]
list_of_numbers2 = [10,30,55,6,199]
list_of_numbers3 = []
value = 100

print(has_greater_element(list_of_numbers3, value))

            
    
    
