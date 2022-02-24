import datetime

from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list
from floodsystem.plot import plot_water_levels

def run():
    stations = build_station_list()
    update_water_levels(stations)
    

    # Fetch data over past 2 days
    dt = 10
    dates, levels = fetch_measure_levels(
        station_cam.measure_id, dt=datetime.timedelta(days=dt))

    # Print level history

    for date, level in zip(dates, levels):
        plot_water_levels(station, dates, levels):


if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()
