from .station import MonitoringStation
import string
from turtle import st
from unittest import skip
import numpy as np
from .geo import stations_by_river
from .utils import sorted_by_key  # noqa
from .stationdata import update_water_levels, build_station_list

def stations_level_over_threshold(stations,tol):
    list_of_stations_over_tol = []
    for i in stations:
        if MonitoringStation.typical_range_consistent(i) and MonitoringStation.relative_water_level(i) != None:
            if MonitoringStation.relative_water_level(i) > tol:
                list_of_stations_over_tol.append((i, MonitoringStation.relative_water_level()))
    else:
        pass
    list_of_stations_over_tol = sorted(list_of_stations_over_tol, key = lambda x:-x[1])
    return list_of_stations_over_tol

#2C
def stations_highest_rel_level(stations, N):
    """stations_highest_rel_level(stations, N) returns a list of N stations in which the water level is closest to the maximum"""
    difference = []
    if stations[0].latest_level == None:
        update_water_levels(stations)

    for station in stations:
        if station.typical_range_consistent():
            try:
                if (station.latest_level - station.typical_range[1]) < 50:
                    difference.append((station.name, (station.latest_level - station.typical_range[1])))

            except Exception:
                difference.append((station.name, -5000))
                # if station.latest_level == None
        else:
            difference.append((station.name, -5000))

    difference = sorted(difference, key=lambda x: -x[1])
    #print(difference)
    return difference[:N]
