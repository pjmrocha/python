#!/usr/bin/python

def numerus(roman):
    num = 0
    idx = 0
    while idx < len(roman):
        n = roman[idx]
        if n == 'i': num+=1
        if n == 'v':
            if idx>0 and roman[idx-1] == 'i': num+=3
            else: num+=5
        if n == 'x':
            if idx>0 and roman[idx-1] == 'i': num+=8
            else: num+=10
        if n == 'l':
            if idx>0 and roman[idx-1] == 'x': num+=30
            else: num+=50
        if n == 'c':
            if idx>0 and roman[idx-1] == 'x': num+=80
            else: num+=100
        if n == 'd':
            if idx>0 and roman[idx-1] == 'c': num+=300
            else: num+=500
        if n == 'm':
            if idx>0 and roman[idx-1] == 'c': num+=800
            else: num+=1000

        idx+=1

    print "{0} - {1}".format(roman, str(num))


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
