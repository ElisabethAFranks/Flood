import datetime
import numpy as np
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list
import floodsystem.flood as flood
import floodsystem.plot as plot

import matplotlib.pyplot as plt

def run():
    """Task 2E"""
    print("run starts")
    # Build list of stations
    stations = build_station_list()
    # Station name to find
    station_names = flood.stations_highest_rel_level(stations, 5)
    
    station_list = []
    for station in stations:
        for i in range(len(station_names)):
            if station.name == station_names[i][0]:
                station_list.append(station)
                

    
    # Fetch data over past 2 days
    dt = 10
    dates = np.empty(6, dtype=object)
    levels = [None, None ,None ,None ,None,None, None ,None ,None ,None]
    for i in range(len(station_list)):
        dates[i], levels[i] = fetch_measure_levels(
            station_list[i].measure_id, dt=datetime.timedelta(days=dt))

        plot.plot_water_levels(station_list[i], dates[i], levels[i])
    

if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()