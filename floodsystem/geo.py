# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
from floodsystem.utils import sorted_by_key
from floodsystem.station import MonitoringStation
import numpy as np

def stations_by_distance(stations, p):
    """function which returns a tuple of the station's name and the station's distance from point p"""
    positions = np.array([station.coord for station in stations])
    distanceToP = 2 * 6371 * np.arcsin(np.sqrt((np.sin((np.deg2rad(p[0] - positions[:,0]))/2))**2 + np.cos(np.deg2rad(positions[:,0])) * np.cos(np.deg2rad(p[0])) * (np.sin((np.deg2rad(p[1] - positions[:,1]))/2))**2))
    stationanddistance = sorted([(station, distanceToP[i]) for i, station in enumerate(stations)], key = lambda x:x[1])
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


def stations_within_radius(stations, centre, r):
    """stations_within_radius(stations, centre, r) returns an alphabetical list of the stations within radius r of the coordinate, centre"""
    # Calls stations from previous function
    stations_distance = stations_by_distance(stations, centre)

    #create list of stations in radius
    stations_in_r = []

    #adds stations to stations_in_r
    for i, stations in enumerate(stations):
        if stations_distance[i][2] < r:
            stations_in_r.append(stations_distance[i][0])
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
