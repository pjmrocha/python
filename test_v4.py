#!/usr/bin/python

print "Hello hello"

l1 = [5, 3, 2, 1]

print l1
for l in l1:
    print l

n = l1[0]
for l in range(0, len(l1)-1):
    for k in range(l+1, len(l1)):
        if l1[l] > l1[k]:
            n = l1[l]
            l1[l] = l1[k]
            l1[k] = n
        else:
            break

print l1
