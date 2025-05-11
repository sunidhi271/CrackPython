def is_list_sorted(list1):
    if len(list1) == 0:
        return True
    
    if list1 == sorted(list1):
        return True
    else:
        return False

# Another Way:   
#    if not list:
#        return True
#    for i in range(len(list) - 1):
#        if list[i] > list[i + 1]:
#            return False
#    return True
        
        
print(is_list_sorted([]))                   #O/P: True
#print(is_list_sorted([10, 20, 30]))        #O/P: True
#print(is_list_sorted([10, 30, 20]))        #O/P: False
