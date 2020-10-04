#!/usr/bin/python

def igpay(word):
    if word[0] in ['a', 'e', 'i', 'o', 'u']:
        print word + "way"
    else:
        print word[1:] + word[0] + "ay"


igpay("dog")
igpay("pig")
igpay("apple")
