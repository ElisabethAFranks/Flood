from floodsystem.stationdata import build_station_list, update_water_levels
import floodsystem.geo as geo

def run():
    """Requirements for Task 1E"""

    # Build list of stations build them properly
    stations = build_station_list()

    print(geo.rivers_by_station_number(stations, 10))


if __name__ == "__main__":
    print("*** Task 1E CUED Part IA Flood Warning System ***")
    run()