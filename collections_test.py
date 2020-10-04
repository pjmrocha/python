
lst = [1,2,3]
dic = {'1': 'x1', '2': 'y2', '3': 'z3'}
tpl = ("a2b", "c3c", "b5c")

# 1
print lst
print lst[-1]

# 2
lst.append(5)
print lst

# 3
print dic
for d in dic:
    print "dic k{0}-v{1}".format(d, dic[d])

i = "Fox jumps over the fence".find("over")
print "Find " + str(i)

lst.insert(2,99)
print lst
lst.remove(99)
print lst
lst.pop()
print lst

l1 = list(lst)
l2 = list(lst)
print l1
print l2
print l1 + l2

print tpl[0]
#tpl[1] = "f4f"
print type(tpl)
