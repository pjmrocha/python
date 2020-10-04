#!/usr/bin/python

def to_val(letter):
    dict = {'i': 1, 'v': 5, 'x': 10, 'l': 50, 'c': 100, 'd': 500, 'm': 1000}
    return dict[letter]

def numerus(roman):
    total = 0
    prev = 0
    for l in roman:
        n = to_val(l)
        if n > prev:
            total -= prev
            n -= prev
        total += n
        prev = n

    print "{0} - {1}".format(roman, str(total))


numerus("ii")       #2
numerus("iv")       #6
numerus("vi")       #6
numerus("ix")       #6
numerus("x")        #10
numerus("xiv")      #14
numerus("xxiii")    #23
numerus("xxix")     #29
numerus("xlvii")    #47
numerus("cccxxvii") #327
numerus("cdxlix")   #449
numerus("mmxlix")   #2049
