import datetime
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list
from floodsystem.plot import plot_water_levels

def run():
    stations = build_station_list()
    update_water_levels(stations)
    high_stations = flood.stations_highest_rel_level(stations,5)
    list_of_stations = []
    for station in stations:
        for i in range(len(high_stations)):
            if station.name == high_stations[i][0]:
                list_of_stations.append(station)
    dt = 10
    dates, levels = fetch_measure_levels(
        station_cam.measure_id, dt=datetime.timedelta(days=dt))

    # Print level history

    for i in range(len(list_of_stations)):
        dates[i], levels[i] = fetch_measure_levels(list_of_stations[i].measure_id, dt=datetime.timedelta(days=dt)
        plot.plot_water_levels(list_of_stations[i],dates[i], levels[i])


if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()
