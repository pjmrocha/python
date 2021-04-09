mydict = {'car': 'ford', 'fruit': 'apple', 'country': 'Japan'}

print(mydict)

print("--1--")
for d in mydict:
    print("key .{0}. - value .{1}.".format(d, mydict[d]))
