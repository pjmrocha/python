#!/usr/bin/python

def pair(list1, list2):
    result = []
    l = 0
    lmax = min(len(list1), len(list2))
    while (l < lmax):
        result.append("{0} - {1}".format(list1[l], list2[l]))
        l+=1

    return result


list1 = ['apple', 'orange', 'banana', 'grapes']

list2 = ['tomato', 'lettuce', 'cucumber', 'onion', 'garlic', 'potato']

# using zip
for (a, b) in zip(list1, list2): print "{0} - {1}".format(a, b)
# using custom function
print pair(list1, list2)

print "  Hello  \n"
print "Hello2"
