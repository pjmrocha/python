#!/usr/bin/python

s1 = "250"
s2 = "3"
res = 0
carry = 0

i = len(s1)-1
while i >= 0:
  j = len(s2)-1
  while j >= 0:
    n = ( int(s1[i]) * int(s2[j]) ) + carry

    if ( n >= 10 ):
      n = n - 10     # if number is bigger than 10, we just want the right most digit
      carry = 1      # flag we have an added value to carry to next operation
    else:
      carry = 0

    res = res + n * (pow(10, len(s1)-i-1))
    j = j - 1

  i = i - 1


print res
