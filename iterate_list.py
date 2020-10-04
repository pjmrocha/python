mylist = [1,2,3]
mylist_tupple = [(1,2), (3,4)]

print(mylist)
print(mylist_tupple)

print("--First--")
for l in mylist:
    print("item {0}".format(l))

print("--Second--")
for l in mylist_tupple:
    print("item {0}".format(*l))
