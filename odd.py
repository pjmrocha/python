import math

def isOdd(n):
    if math.floor(n/2.0) == n/2.0:
        return 0
    else:
        return 1

print isOdd(6)
print isOdd(3)
