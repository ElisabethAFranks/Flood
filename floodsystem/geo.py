# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
from haversine import haversine
from utils import sorted_by_key
from station import MonitoringStation

def stations_by_distance(stations, p):
    """function which returns a tuple of the station's name and the station's distance from point p"""
    stationanddistance = []
    for station in stations: 
        distance = float(haversine(p,station.coordinate))
        stationanddistance.append(station.name,distance)
    stationanddistance = sorted([(station.name, station.town, distance[i]) for i, station in enumerate(stations)], key = lambda x:x[2])
    return stationanddistance

def rivers_with_station(stations):
    """function which returns a list of rivers which have a monitoring station"""
    riverandstation = []
    for station in stations:
        if station.river == True and station.river in riverandstation == False:
            riverandstation.append(station.river)
        else:
            continue
    riverandstation = sorted(riverandstation)
    return riverandstation

def stations_by_river(stations):
    """function which returns a dictionary of rivers and a list of the stations on the river"""
    stationandriver = {}
    for station in stations:
        if not station.river in stationandriver:
            stationandriver.update({station.river: list([station.name])})
        else:
            stationandriver[station.river] = list(stationandriver[station.river]) + [station.name]
    for station in stationandriver:
        stationandriver[station] = sorted(stationandriver[station])
        riverandstation = rivers_with_station(stations)
    return riverandstation
