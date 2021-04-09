#!/usr/bin/python

def calculator(math_operation):
    res = None
    try:
        items = math_operation.split(" ")
        n1 = int(items[0])
        n2 = int(items[2])
        op = items[1]
        if op == "+": res = n1 + n2
        elif op == "-": res = n1 - n2
        elif op == "*": res = n1 * n2
        elif op == "/": res = n1 / n2
        else: raise
    except ValueError:
        print "Error: values not supported"
    except:
        print "Error: operation not supported"

    return res



#while True:
#    calc = input("Enter your math operation: ")

print calculator("2 + 3")
print calculator("15 - 9")
print calculator("5 * 10")
print calculator("100 / 5")
print calculator("-4 / 2")
print calculator("3 ! 6")
print calculator("four * two")
