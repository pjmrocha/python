#!/usr/bin/python

import json
from math import floor
from geopy.distance import geodesic

with open("gh4g-9sfh.json") as nasa_file:
    nasa = json.loads(nasa_file.read())

#print type(nasa)

# somewhere in Ireland
lat1 = 52.8408
long1 = -6.9261

lat2 = float(nasa[0]["geolocation"]["latitude"])
long2 = float(nasa[0]["geolocation"]["longitude"])

distKm = geodesic((lat1, long1), (lat2, long2)).kilometers
distMl = geodesic((lat1, long1), (lat2, long2)).miles

print "Distance from {0},{1} to {2},{3}: {4}Km".format(lat1, long1, lat2, long2, floor(distKm))
print "Distance from {0},{1} to {2},{3}: {4}m".format(lat1, long1, lat2, long2, floor(distMl))
