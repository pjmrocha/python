#!/usr/bin/python

def repeat(n):
  res = []
  for i in range(1, n+1):
    res = res + [i]*2

  return res


print repeat(3)    # [1,1,2,2,3,3]
print repeat(5)    # [1,1,2,2,3,3,4,4,5,5]
