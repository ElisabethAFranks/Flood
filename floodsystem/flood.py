from station import MonitoringStation

def stations_level_over_threshold(stations,tol):
    list_of_stations_over_tol = []
    for station in stations:
        if station.typical_range_consistent() and station.relative_water_level() != None:
            if station.relative_water_level() > tol:
                list_of_stations_over_tol.append((station, station.relative_water_level()))
    else:
        pass
    list_of_stations_over_tol = sorted(list_of_stations_over_tol, key = lambda x:-x[1])
    return list_of_stations_over_tol