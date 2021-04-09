# given a specific dictionary, determine if a list of string elements is sorted
#
# dict = ["c", "b", "a"]
#
# list = ["bb", "ab", "cb"]

#!/usr/bin/python

mydict = ["c", "b", "a"]
mylist = ["bb", "ba", "cb"]       # not sorted
#mylist = ["cb", "bb", "ba"]       # sorted

def isSorted(myMapDict, mylist):

     # parse the whole list comparing each element
     for w1 in range(len(mylist)-1):
         for w2 in range(w1+1, len(mylist)):
             if not isWordSorted(myMapDict, mylist[w1], mylist[w2]):
                 return False

     return True


def isWordSorted(myMapDict, word1, word2):
    # considering words in dictionary have the same length
    for i in range(len(word1)):
        if (myMapDict[word1[i]] > myMapDict[word2[i]]):
            return False;

    return True;


# convert the dictionay to a map, so each letter/item as an integer which will used to rank the position in the dictionary
def mapDict(mydict):
    myMap = {}
    pos = 0
    for d in mydict:
        myMap[d] = pos
        pos = pos+1

    return myMap

# entry point
if __name__ == '__main__':
    myMapDict = mapDict(mydict)
    isSort = isSorted(myMapDict, mylist)
    if (isSort): print("Sorted")
    else: print("Not sorted")
