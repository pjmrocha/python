#!/usr/bin/python

from zipfile import ZipFile

# read the whole file
with open("./file_test.txt") as myfile:
    f = myfile.read()     # returns the whole content as a string
    print f

print "-----"

# read all lines and return as a list
with open("./file_test.txt") as myfile:
    f = myfile.readlines()     # returns a list with each line as an item
    print f

print "-----"

# read the first byes of a file
with open("./file_test.txt") as myfile:
    f = myfile.read(10)     # reads the first 10 bytes of the file
    print f
    f = myfile.read(25)     # reads the following 25 bytes of the file
    print f

print "-----"

# read file line by line
with open("./file_test.txt") as myfile:
   for f in myfile:
       print f.strip()       # remove end of line characher from the read line as the print command will add one in stdout
       #print f              # version with end of line character included

print "-----"

# other way to read line by line
myfile = open("./file_test.txt")
f = myfile.readline()
while (f):
    print f.strip()
    f = myfile.readline()

print "-----"

# read a zip file
with ZipFile("./file_test_zip.zip") as myzip:
    myzip.printdir()
