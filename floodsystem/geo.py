# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
from haversine import haversine, Unit
p = (0.,0.)
stationanddistance = []
def stations_by_distance(stations, p):
    for station in stations: 
        distance = float(haversine(p,station.coordinate, unit=Unit.km))
        stationanddistance.append(station.name,distance)
    return stationanddistance