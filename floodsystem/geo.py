# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
import haversine
from floodsystem.utils import sorted_by_key
from floodsystem.station import MonitoringStation

def stations_by_distance(stations, p):
    """function which returns a tuple of the station's name and the station's distance from point p"""
    station_and_distance = []
    for station in stations: 
        distance = float(haversine(p,station.coord))
        station_and_distance.append(station.name,distance)
    station_and_distance = sorted([(station.name, station.town, distance[i]) for i, station in enumerate(stations)], key = lambda x:x[2])
    return station_and_distance

def rivers_with_station(stations):
    """function which returns a list of rivers which have a monitoring station"""
    river_and_station = []
    for station in stations:
        if station.river == True and station.river in riverandstation == False:
            river_and_station.append(station.river)
        else:
            continue
    river_and_station = sorted(river_and_station)
    return river_and_station

def stations_by_river(stations):
    """function which returns a dictionary of rivers and a list of the stations on the river"""
    station_and_river = {}
    for station in stations:
        if not station.river in station_and_river:
            station_and_river.update({station.river: list([station.name])})
        else:
            station_and_river[station.river] = list(station_and_river[station.river]) + [station.name]
    for station in station_and_river:
        station_and_river[station] = sorted(station_and_river[station])
        river_and_station = rivers_with_station(stations)
    return river_and_station
