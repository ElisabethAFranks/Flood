import datetime
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.plot import plot_water_levels
from floodsystem.flood import stations_highest_rel_level
import numpy as np

def run():
    stations = build_station_list()
    update_water_levels(stations)
    high_stations = stations_highest_rel_level(stations,5)
    list_of_stations = []
    for station in stations:
        for i in range(len(high_stations)):
            if station.name == high_stations[i][0]:
                list_of_stations.append(station)
    dt = 10
    for i in range(len(list_of_stations)):
        dates = np.empty(6, dtype = object)
        levels = [None, None, None, None, None, None, None, None, None, None]
        dates[i], levels[i] = fetch_measure_levels(list_of_stations[i].measure_id, dt=datetime.timedelta(days=dt))
        plot_water_levels(list_of_stations[i],dates[i], levels[i])


if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()
