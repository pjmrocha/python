#!/usr/bin/python

def intersect(list1, list2):
    result = []
    for l1 in list1:
        for l2 in list2:
            if l1 == l2 and l1 not in result: result.append(l1)

    return result



list1 = ['apple', 'tomato', 'pear', 'grapes', 'watermelon']

list2 = ['apple', 'strawberry', 'tomato', 'apple']

list3 = ['pear', 'strawberry', 'carrot', 'cucumber', 'grapes', 'lettuce']

# using intersection
print set(list1).intersection(list2)
# using custom function
print intersect(list1, list2)

# using intersection
print set(list1).intersection(list3)
# using custom function
print intersect(list1, list3)
