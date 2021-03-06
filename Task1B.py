from floodsystem.stationdata import build_station_list
import floodsystem.geo as geo
from floodsystem.stationdata import MonitoringStation


def run():
    """Requirements for Task 1B"""

    # Build list of stations
    stations = build_station_list()
    
    # Returns list of closest ten stations
    print("The closest ten stations are:")
    output = geo.stations_by_distance(stations, (52.2053, 0.1218))[:10]
    #print(geo.stations_by_distance(stations, (52.2053, 0.1218))[:10])
    for i in range(len(output)):
        print(output[i][0].name, output[i][1])

     # Returns list of furthest ten stations
    #print("The furthest ten stations are:")
    #print(geo.stations_by_distance(stations, (52.2053, 0.1218))[-10:])

if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()