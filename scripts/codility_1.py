import math

def solution(a):
    a.sort()
    res = a[0]+1
    if res == 0:
        return 1

    for i in a:
        if i < res:
            return res
        else
            res = i
        
print solution([6, 3, 1, 2, 9])
b = [-3, -5, -1, -2]
print b
print solution(b)
print b
