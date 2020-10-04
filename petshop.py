#!/usr/bin/python

pets = {'cat': 10.5, 'dog': 9.9, 'canary': 2.0, 'hamster': 21.0}

while True:
    pet = raw_input("What pet do you want to buy?")
    if not pet: break   # exit on empty input
    try:
        print "You can buy a {0} for {1}".format(pet, pets[pet])
    except:
        print "Sorry, we don't have {0}".format(pet)
