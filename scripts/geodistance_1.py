#!/usr/bin/python

import json
from math import floor
import haversine

with open("gh4g-9sfh.json") as nasa_file:
    nasa = json.loads(nasa_file.read())

#print type(nasa)

lat1 = 52.8408
long1 = -6.9261

lat2 = float(nasa[0]["geolocation"]["latitude"])
long2 = float(nasa[0]["geolocation"]["longitude"])

dist = haversine.haversine((lat1, long1), (lat2, long2))

print "Distance from {0},{1} to {2},{3}: {4}Km".format(lat1, long1, lat2, long2, floor(dist))
