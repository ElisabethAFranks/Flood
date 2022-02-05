from floodsystem.stationdata import build_station_list
import floodsystem.geo as geo


def run():
    """Requirements for Task 1B"""

    # Build list of stations
    stations = build_station_list()
    p = (52.2053,0.1218)
    
     # Returns list of closest ten stations
    print(geo.stations_by_distance(stations[:10]))

     # Returns list of furthest ten stations
    print(geo.stations_by_distance(stations[-10:]))

if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()