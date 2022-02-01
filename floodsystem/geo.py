# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
from haversine import haversine

p = (0.,0.)
def stations_by_distance(stations, p):
    stationanddistance = []
    for station in stations: 
        distance = float(haversine(p,station.coordinate))
        stationanddistance.append(station.name,distance)
    utils.sort_by_key(stationanddistance)
    return stationanddistance

def rivers_with_station(stations):
    riverandstation = []
    for station in stations:
        if station.river == True and station.river in riverandstation == False:
            riverandstation.append(station.river)
        else:
            continue
    return riverandstation

def stations_by_river(stations):
    print("Hello")