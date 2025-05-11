# easy
# Check if sum of all integers in list1 is same as sum of all integers in list2

def are_sums_equal(list1, list2):
#    sum1=0 
#    sum2=0 
#    for i in list1:
#        sum1 += i
#    for j in list2:
#        sum2 += j 
#    if sum1 == sum2:
#        return True
#    else:
#        return False
    if sum(list1) == sum(list2):
        return True
    else:
        return False

list1=[1, 10, 34, 56]
list2=[2, 9, 40, 50]

print(are_sums_equal(list1, list2))

#O/P: True
