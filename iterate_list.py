mylist = [1,2,3]
mylist_mix = [1,True,"A"]

mylist_tupple = [(1,2), (3,4)]
mylist_tupple_mix = [(1,True), ("B",4)]

print(mylist)
print(mylist_mix)

print(mylist_tupple)
print(mylist_tupple_mix)

print("--mylist--")
for l in mylist:
    print("item {0}".format(l))
print("--mylist_mix--")
for l in mylist_mix:
    print("item {0}".format(l))

print("--mylist_tupple--")
for l in mylist_tupple:
    print("item {0}".format(*l))
print("--mylist_tupple_mix--")
for l in mylist_tupple_mix:
    print("item {0}".format(*l))
