import datetime
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.plot import plot_water_levels
from floodsystem.flood import stations_highest_rel_level
import numpy as np

def run():
    stations = build_station_list()
    station_names = stations_highest_rel_level(stations, 5)
    station_list = []
    for station in stations:
        for i in range(len(station_names)):
            if station.name == station_names[i][0]:
                station_list.append(station)
    dt = 10
    dates = np.empty(6, dtype=object)
    levels = [None, None ,None ,None ,None,None, None ,None ,None ,None]
    for i in range(len(station_list)):
        dates[i], levels[i] = fetch_measure_levels(station_list[i].measure_id, dt=datetime.timedelta(days=dt))
        plot_water_levels(station_list[i], dates[i], levels[i])
    plt.title("station.name")
    plt.legend(loc="upper left")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()
