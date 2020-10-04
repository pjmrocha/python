# generator function
def firstn(n):
    num = 0
    while num < n:
        yield num
        num += 1

print firstn(5)

for n in firstn(2):
    print n

# generator expression
items = (s for s in [10, 12, 14, 20])
print items
print next(items) # prints 10
print next(items) # prints 12
