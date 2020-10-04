#!/usr/bin/python

import json
from math import floor
import haversine

with open("gh4g-9sfh.json") as nasa_file:
    meteors = json.loads(nasa_file.read())

lat1 = 52.8408       # somewhere in Ireland
long1 = -6.9261
closest_dist = 9999  # default distance
the_one = None

for meteor in meteors:
    try:
        lat2 = float(meteor["geolocation"]["latitude"])
        long2 = float(meteor["geolocation"]["longitude"])
        dist = haversine.haversine((lat1, long1), (lat2, long2))

        if dist < closest_dist:
            the_one = meteor
            closest_dist = dist

    except:
        continue

print "The closest meteor from {0},{1} was {2}\n".format(lat1, long1, the_one)
print "It fell at distance of {0}Km".format(closest_dist)
