#!/usr/bin/python

import json

myfile = "./movies.json"

class movie:
    def __init__(self, title):
        self.title = title

# load json
def getMyJson(file):
    with open(file) as jfile:
        movies = json.load(jfile)

    # list all movies
    for m in movies["items"]:
        print(m)

    # for Movie, create a object of class movie
    for t in movies["items"]:
        print(t["name"])
        if (t["name"] == "Movie3"):
            m3 = movie(t["name"])
            print(m3.title)

# main
if __name__ == "__main__":
  getMyJson(myfile)
