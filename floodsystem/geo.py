# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
from .utils import sorted_by_key
from .station import MonitoringStation
import numpy as np

def stations_by_distance(stations, p):
    """function which returns a tuple of the station's name and the station's distance from point p"""
    positions = np.array([station.coord for station in stations])
    distanceToP = 2 * 6371 * np.arcsin(np.sqrt((np.sin((np.deg2rad(p[0] - positions[:,0]))/2))**2 + np.cos(np.deg2rad(positions[:,0])) * np.cos(np.deg2rad(p[0])) * (np.sin((np.deg2rad(p[1] - positions[:,1]))/2))**2))
    stationanddistance = sorted([(station, distanceToP[i]) for i,station in enumerate(stations)], key = lambda x:x[1])
    return stationanddistance

def rivers_with_station(stations):
    """function which returns a list of rivers which have a monitoring station"""
    riverandstation = set()
    for station in stations:
        riverandstation.add(station.river)
    riverandstation = sorted(riverandstation)
    return riverandstation

def stations_by_river(stations):
    """function which returns a dictionary of rivers and a list of the stations on the river"""
    riverandstation = set(rivers_with_station(stations))
    stationandriver = {}
    for station in stations:
        if not station.river in stationandriver:
            stationandriver.update({station.river: list([station.name])})
        else:
            stationandriver[station.river] = list(stationandriver[station.river]) + [station.name]
    for station in stationandriver:
        stationandriver[station] = sorted(stationandriver[station])
    return stationandriver


def stations_within_radius(stations, centre, r):
    """stations_within_radius(stations, centre, r) returns an alphabetical list of the stations within radius r of the coordinate, centre"""
    # Calls stations from previous function
    stations_dist = stations_by_distance(stations, centre)

    #create list of stations in radius
    stations_in_r = []

    #adds stations to stations_in_r
    for i, stations in enumerate(stations):
        if stations_dist[i][1] < r:
            stations_in_r.append(stations_dist[i][0].name)
        else:
            break
    
    #sort stations_in_r alphabetically
    stations_in_r.sort()
    
    return stations_in_r


def rivers_by_station_number(stations, N):
    """rivers_by_station_number returns a list of tuples(river name, number of stations) sorted by number of stations for the first N rivers"""
    #use dictionary from stations_by_river(stations)
    stations_by_riv = stations_by_river(stations) 

    #create empty list of rivers
    rivers_stations = []

    #add number of stations to list
    for key, value in stations_by_riv.items():
        rivers_stations.append((key, len(value)))

    #sort list by number of stations
    rivers_stations = sorted(rivers_stations, key = lambda x:-x[1])  

    output = rivers_stations[:N]

    #sort what happens if nth entry has equal sumber of stations
    list_complete = False
    while list_complete == False:
        if rivers_stations[-N][1] == rivers_stations[-(N+1)]:
            output.append(rivers_stations[-(N+1)])
            
        else:
            list_complete = True

    return output




